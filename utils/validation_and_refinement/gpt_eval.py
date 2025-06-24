"""
GPT evaluator for API responses.
Uses GPT to determine if an API response is information or an error message.
"""

# from langchain.pydantic_v1 import BaseModel, Field
from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
import json
import os


# Define the model for classification output
class Classification(BaseModel):
    """Classification output model."""
    response_type: str = Field(..., enum=['information', 'code_error', 'server_error', 'request_error'])


class DocCompleteness(BaseModel):
    """Documentation completeness classification model."""
    is_complete: bool = Field(..., description="Whether the documentation is complete")
    reason: str = Field(..., description="Reason for the completeness decision")


def initialize_gpt_evaluator(temperature=0, model="gpt-4o"):
    """
    Initialize the GPT evaluator.
    
    Args:
        temperature: Temperature parameter for the model
        model: The model name to use
        
    Returns:
        llm: The initialized LLM
        tagging_prompt: The prompt template
    """
    # Create prompt template
    tagging_prompt = ChatPromptTemplate.from_template(
        """
Given an API description, response, and Python code, classify the response type:

- information: Valid response containing useful data as expected
- code_error: Error due to bugs in the Python code (syntax, logic, url path doesn't match, etc.)
- server_error: Server-side error (500, service unavailable, authentication error, etc.)
- request_error: Invalid operation due to bad parameters or unsupported operation (only choose this when other errors are not applicable and you think the code is correct but the response is an error)

API Description: {description}
API Response: {response}
Code: {code}
        """
    )
    
    # Initialize LLM
    llm = ChatOpenAI(temperature=temperature, model=model).with_structured_output(Classification)
    return llm, tagging_prompt


def evaluate_doc_completeness(llm, api_doc, function_name, locator_path):
    """
    Use GPT to evaluate if the API documentation is complete for a given function.
    Results are cached in locator.json to avoid repeated evaluations.
    
    Args:
        llm: The LLM to use
        api_doc: The API documentation to evaluate
        function_name: The name of the function being documented
        locator_path: Path to the locator.json file
        
    Returns:
        tuple: (is_complete, reason)
    """
    print(f"\nEvaluating documentation completeness for {function_name}")
    print(f"Locator path: {locator_path}")
    
    # Load existing locator.json if it exists
    locator_data = {}
    if os.path.exists(locator_path):
        try:
            with open(locator_path, 'r', encoding='utf-8') as f:
                locator_data = json.load(f)
                print(f"Loaded existing locator.json with {len(locator_data)} entries")
        except Exception as e:
            print(f"Error reading locator.json: {str(e)}")
    
    # Check if this function has already been evaluated
    if function_name in locator_data:
        print(f"Found existing entry for {function_name}")
        if isinstance(locator_data[function_name], dict):
            cached_result = locator_data[function_name]
            if 'is_complete' in cached_result and 'doc' in cached_result:
                print(f"Using cached completeness evaluation for {function_name}")
                return cached_result['is_complete'], cached_result.get('reason', '')
            else:
                print(f"Found entry but missing required fields: {cached_result}")
        else:
            print(f"Found entry but not in expected format: {locator_data[function_name]}")
    
    print("No valid cache found, evaluating documentation...")
    
    # Create prompt template for documentation completeness
    doc_prompt = ChatPromptTemplate.from_template(
        """
You are an expert API documentation evaluator. Your task is to determine if the provided API documentation is complete and sufficient for implementing the given function.

Function Name: {function_name}

API Documentation:
{doc}

Please evaluate if this documentation is complete enough to implement the function. Consider:
1. Does it describe all required parameters?
2. Does it explain the expected response format?
3. Does it provide enough context about the API's purpose and behavior?
4. Are there any missing details that would be crucial for implementation?

Respond with a structured evaluation of the documentation's completeness.
        """
    )
    
    # Initialize LLM for documentation evaluation
    doc_llm = ChatOpenAI(temperature=0, model="gpt-4o-mini").with_structured_output(DocCompleteness)
    
    # Invoke the prompt
    prompt = doc_prompt.invoke({
        "function_name": function_name,
        "doc": api_doc
    })
    
    # Get the response from GPT
    gpt_response = doc_llm.invoke(prompt)
    
    # Cache the result in locator.json
    locator_data[function_name] = {
        'is_complete': gpt_response.is_complete,
        'reason': gpt_response.reason,
        'doc': api_doc
    }
    
    print(f"Caching evaluation result for {function_name}")
    print(f"Result: {locator_data[function_name]}")
    
    try:
        with open(locator_path, 'w', encoding='utf-8') as f:
            json.dump(locator_data, f, indent=2)
        print(f"Successfully wrote to {locator_path}")
    except Exception as e:
        print(f"Error writing to locator.json: {str(e)}")
    
    return gpt_response.is_complete, gpt_response.reason


def gpt_evaluate(llm, prompt_template, api_description, api_response, code):
    """
    Use GPT to decide if the API response is a piece of information or an error message.
    
    Args:
        llm: The LLM to use
        prompt_template: The prompt template
        api_description: Description of the API
        api_response: The API response to evaluate
        
    Returns:
        response_type: 'information' or 'error'
    """
    # Truncate the response to avoid token limit issues
    if isinstance(api_response, str):
        api_response = api_response[:500] if len(api_response) > 500 else api_response
    
    # Invoke the prompt
    prompt = prompt_template.invoke({
        "description": api_description, 
        "response": api_response,
        "code": code
    })
    
    # Get the response from GPT
    gpt_response = llm.invoke(prompt)
    
    return gpt_response.response_type

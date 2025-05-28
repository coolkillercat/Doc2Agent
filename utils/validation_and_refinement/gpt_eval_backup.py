"""
GPT evaluator for API responses.
Uses GPT to determine if an API response is information or an error message.
"""

# from langchain.pydantic_v1 import BaseModel, Field
from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate


# Define the model for classification output
class Classification(BaseModel):
    """Classification output model."""
    response_type: str = Field(..., enum=['information', 'code_error', 'server_error'])


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
You will be given:
1. API Json Documentation: It includes all endpoints information. Please refer to the API description of the most relevent one based on the similarity of the Python function name and the endpoint's name.
2. An API response.
3. A Python code snippet that calls the API.

Your task is to decide if the following API response is an useful information as the API description suggests, an error caused by the code (code_error), or an error caused by the server side (server error).

API Description:
{description}

API Response:
{response}

Code:
{code}
        """
    )
    
    # Initialize LLM

    llm = ChatOpenAI(temperature=temperature, model=model).with_structured_output(Classification)
    return llm, tagging_prompt


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

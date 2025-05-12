from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.pydantic_v1 import BaseModel, Field, validator
from typing import Optional, Any, Union, List
from bs4 import BeautifulSoup


class Parameters(BaseModel):
    name: str = Field(description="Name of the parameter")
    type: Optional[str] = Field(description="Type of the parameter")
    description: Optional[str] = Field(description="Description of the parameter. If the parameter is categorical, please list all possible values.")
    default: Optional[Any] = Field(
        description="Default value of the parameter")
    example: Optional[Any] = Field(
        description="Example value of the parameter")


class Endpoint(BaseModel):
    name: str = Field(description="Name of the endpoint")
    description: Optional[str] = Field(
        description="Description of the endpoint")
    method: str = Field(description="Method of the endpoint")
    url: Union[str, List[str]] = Field(description="URL of the endpoint, start with http:// or https://")
    headers: Optional[List] = Field(
        default=[], description="Headers of the endpoint")
    required_parameters: Optional[List[Parameters]]
    optional_parameters: Optional[List[Parameters]]


class Api_json(BaseModel):
    title: Optional[str] = Field(description="Title of the API")
    endpoints: List[Endpoint]

def html_file_parser(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()
    soup = BeautifulSoup(html_content, 'html.parser')
    text_content = soup.get_text(separator=' ', strip=True)
    return text_content

class Extractor():
    def __init__(self):
        self.llm = ChatOpenAI(model='gpt-4o', temperature=0)

    def extract_api_json(self, file_path, file_parser=html_file_parser):
        # Gets the text content from the HTML file
        text_content = file_parser(file_path)
        
        # Split the content into chunks for processing
        # Make chunks extremely small to avoid any token limit issues
        chunk_size = 8000  # characters, roughly 2000 tokens to stay well below limits
        content_chunks = self._split_content_into_chunks(text_content, chunk_size)
        
        # Process each chunk and merge results
        all_endpoints = []
        title = "API Documentation"
        
        for i, chunk in enumerate(content_chunks):
            print(f"Processing chunk {i+1}/{len(content_chunks)}...")

            # Query GPT to extract API JSON for this chunk
        template = '''
            You will be provided with a piece of API documentation text. Your target is to extract the well-structured API JSON form from the given text.
        The API JSON form should include the endpoints with name, description, method, url, headers, and required_parameters/optional_parameters with descriptions and types.
        Required parameters, optional parameters, and url must be inside a list. If you cannot find API url or there are just endpoints without base url, please only put a 'missing' string in the url field.
        Additionally, if a parameter has an example value mentioned in the text, include it as the example. If not, generate a sensible example value based on the parameter description.
            
            This is part {chunk_num} of {total_chunks} of the API documentation, so only extract the endpoints described in this specific part.
        
        API JSON form example:
                    {{{{
                    "title": "Example API Documentation",
                    "endpoints": [
                            {{{{
                        "name": "Get User",
                        "description": "Retrieves a user by ID.",
                        "method": "GET",
                        "url": "https://api.example.com/users/userId",
                        "headers": [],
                        "required_parameters": [
                                {{{{
                            "name": "userId",
                            "type": "string",
                            "description": "The ID of the user",
                            "default": null,
                            "example": "123"
                                }}}}
                        ],
                        "optional_parameters": []
                            }}}}
                    ]
                    }}}}
        '''
            template = template.format(chunk_num=i+1, total_chunks=len(content_chunks))
            
        human_template = "{text}"
        prompt = ChatPromptTemplate.from_messages([
            ("system", template),
            ("human", human_template),
        ])
            
            try:
                chain = prompt | self.llm.with_structured_output(Api_json, method="json_mode")
                result = chain.invoke({"text": chunk})
                
                # Extract the API title from the first chunk if available
                if i == 0 and result.title:
                    title = result.title
                
                # Add endpoints from this chunk to our collection
                all_endpoints.extend(result.endpoints)
                
                # Wait a bit to avoid rate limiting
                if i < len(content_chunks) - 1:
                    import time
                    time.sleep(2)  # Wait 2 seconds between chunks
                    
            except Exception as e:
                print(f"Error processing chunk {i+1}: {str(e)}")
                continue
        
        # Combine all endpoints into a single API JSON
        combined_api = Api_json(title=title, endpoints=all_endpoints)
        json = combined_api.json(indent=4)
        return json
    
    def _split_content_into_chunks(self, text, chunk_size):
        """Split content into chunks at appropriate boundaries."""
        if len(text) <= chunk_size:
            return [text]
        
        chunks = []
        current_position = 0
        
        while current_position < len(text):
            # Find a good boundary to split (paragraph or line break)
            end_position = min(current_position + chunk_size, len(text))
            
            # Try to find paragraph break
            if end_position < len(text):
                # Look for paragraph breaks (double newline)
                paragraph_break = text.rfind('\n\n', current_position, end_position)
                if paragraph_break != -1 and paragraph_break > current_position + chunk_size // 2:
                    end_position = paragraph_break + 2
                else:
                    # Look for single newline
                    line_break = text.rfind('\n', current_position, end_position)
                    if line_break != -1 and line_break > current_position + chunk_size // 2:
                        end_position = line_break + 1
                    else:
                        # If no good break found, try to break at a sentence
                        sentence_break = text.rfind('. ', current_position, end_position)
                        if sentence_break != -1 and sentence_break > current_position + chunk_size // 2:
                            end_position = sentence_break + 2
            
            # Add chunk
            chunks.append(text[current_position:end_position])
            current_position = end_position
        
        return chunks

if __name__=="__main__":
    from langchain_core.utils.function_calling import convert_to_openai_tool
    temp=convert_to_openai_tool(Api_json)
    print(temp)

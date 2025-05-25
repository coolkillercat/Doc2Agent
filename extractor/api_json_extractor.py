from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
# from langchain_core.pydantic_v1 import BaseModel, Field, validator
from pydantic import BaseModel, Field, validator
from typing import Optional, Any, Union, List
from bs4 import BeautifulSoup


class Parameters(BaseModel):
    name: str = Field(description="Name of the parameter")
    type: Optional[str] = Field(description="Type of the parameter")
    description: Optional[str] = Field(description="Description of the parameter. If the parameter is categorical, please list all possible values.")
    default: Optional[Any] = Field(
        None,
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
        # Limit the number of tokens for llm
        tokens = text_content.split()
        token_limit = 117500
        limited_tokens = tokens[:token_limit]
        text_content = ' '.join(limited_tokens)

        # Query GPT to extract API JSON
        template = '''
        You will be provided with a long text. It is extracted from one or several HTML files. Your target is to extract the well-structured API JSON form from the given text.
        The API JSON form should include the endpoints with name, description, method, url, headers, and required_parameters/optional_parameters with descriptions and types.
        Required parameters, optional parameters, and url must be inside a list. If you cannot find API url or there are just endpoints without base url, please only put a 'missing' string in the url field.
        Additionally, if a parameter has an example value mentioned in the text, include it as the example. If not, generate a sensible example value based on the parameter description.
        
        API JSON form example:
                {{
                    "title": "Example API Documentation",
                    "endpoints": [
                        {{
                        "name": "Get User",
                        "description": "Retrieves a user by ID.",
                        "method": "GET",
                        "url": "https://api.example.com/users/userId",
                        "headers": [],
                        "required_parameters": [
                            {{
                            "name": "userId",
                            "type": "string",
                            "description": "The ID of the user",
                            "default": null,
                            "example": "123"
                            }}
                        ],
                        "optional_parameters": []
                        }}
                    ]
                }}
        '''
        human_template = "{text}"
        prompt = ChatPromptTemplate.from_messages([
            ("system", template),
            ("human", human_template),
        ])
        chain = prompt | self.llm.with_structured_output(
            Api_json, method="json_mode")
        result = chain.invoke({"text": text_content})
        # json = result.json(indent=4)
        json = result.model_dump_json(indent=4)
        return json

if __name__=="__main__":
    from langchain_core.utils.function_calling import convert_to_openai_tool
    temp=convert_to_openai_tool(Api_json)
    print(temp)

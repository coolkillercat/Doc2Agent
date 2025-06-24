# code agent

import anthropic  


def initialize_claude():
    """Initialize the Claude API client"""
    # $env:ANTHROPIC_API_KEY='your-key-here'
    client = anthropic.Anthropic()
    return client

def fix_code(client, code: str, error: str, api_doc: str, params: dict, config: dict = None) -> str:
    """Fix code using Claude API with structured instructions"""
    
    with open("./template/fix_code_prompt_template.txt", "r") as f:
        template = f.read()

    # Format config as a string for the template
    config_str = ""
    if config:
        if 'base_url' in config:
            config_str += f"Base URL: {config['base_url']}\n"
        if 'headers' in config:
            config_str += f"Headers: {config['headers']}\n"
        if 'info' in config:
            config_str += f"Testing Info: {config['info']}\n"
        
        # Add remaining config items that aren't base_url, headers, or info
        additional_config = {k: v for k, v in config.items() if k not in ['base_url', 'headers', 'info']}
        if additional_config:
            config_str += f"Additional Config: {additional_config}"
    else:
        config_str = "No configuration provided"

    if isinstance(error, str) and len(error) > 1000:
        error = error[:1000]
    prompt = template.format(client=client, code=code, error=error, api_doc=api_doc, params=str(params), config=config_str)

    chat = client.messages.create(
        model="claude-3-7-sonnet-20250219",
        max_tokens=16384,
        temperature=0,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    
    try:
        return chat.content[0].text.strip()
    except (AttributeError, IndexError) as e:
        raise RuntimeError("Failed to process API response") from e
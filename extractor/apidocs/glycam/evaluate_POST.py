import requests
import json
from urllib.parse import quote

def evaluate(sequence=None, base_url="https://glycam.org"):
    """
    Evaluate a glycan sequence to determine if it can be built and what options are available.
    
    This function sends a request to the GEMS API to evaluate a glycan sequence.
    It returns information about whether the sequence is valid, available build options,
    and if a default structure is created.
    
    Args:
        sequence (str): The glycan sequence to evaluate (e.g., "DManpa1-6DManpa1-OH")
        base_url (str, optional): The base URL for the API. Defaults to "https://glycam.org".
    
    Returns:
        requests.Response: The response object from the API request
    
    Example:
        >>> response = evaluate(sequence="DManpa1-6DManpa1-OH")
        >>> response_json = response.json()
    """
    api_url = f"{base_url}/json/evaluate/sequence/"
    payload = {
        "entity": {
            "sequence": sequence,
            "services": ["evaluate"]
        }
    }
    headers = {
        "Content-Type": "application/json"
    }
    
    assert sequence is not None, 'Missing required parameter: sequence'
    
    response = requests.post(url=api_url, json=payload, headers=headers, timeout=50)
    return response

if __name__ == '__main__':
    r = evaluate(sequence='''DManpa1-6DManpa1-OH''')
    r_json = None
    try:
        r_json = r.json()
    except:
        pass
    import json
    result_dict = dict()
    result_dict['status_code'] = r.status_code
    result_dict['text'] = r.text
    result_dict['json'] = r_json
    result_dict['content'] = r.content.decode("utf-8")
    print(json.dumps(result_dict, indent=4))
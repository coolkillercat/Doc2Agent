import requests
import json
from urllib.parse import quote

def convert_composition_to_wurcs(composition=None):
    """
    Convert glycan composition text to WURCS format.
    
    Args:
        composition (str or list): Composition text in format like "Hex:3|HexNAc:2" or a list of dictionaries
            with composition details like [{"hex":"1", "hexnac":"2", ...}]
    
    Returns:
        Returns the WURCS format representation of a glycan composition specified as either a formatted string or a list of composition dictionaries.
    Examples:
        >>> convert_composition_to_wurcs("Hex:3|HexNAc:2")
        >>> convert_composition_to_wurcs([{"hex":"1", "hexnac":"2", "dhex":"3", "neu5ac":"1", "neu5gc":"0", "P":"1", "S":"1", "Ac":"1"}])
    """
    api_url = "https://api.glycosmos.org/glycancompositionconverter/1.0.0/composition2wurcs"
    headers = {'Content-Type': 'application/json'}
    assert composition is not None, 'Missing required parameter: composition'
    
    if isinstance(composition, str):
        # If composition is a string like "Hex:3|HexNAc:2", use it in the URL
        api_url = f"{api_url}/{quote(composition)}"
        response = requests.get(url=api_url, headers=headers, timeout=50)
    else:
        # If composition is a list of dictionaries, send it as JSON in the request body
        response = requests.post(url=api_url, json=composition, headers=headers, timeout=50)
    
    return response

if __name__ == '__main__':
    r = convert_composition_to_wurcs(composition='Hex:3|HexNAc:2')
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
import requests
import json
from urllib.parse import quote

def convert_composition_text_to_wurcs_format(text=None):
    """
    Convert glycan composition text to WURCS format.
    
    Args:
        text (str): Composition text of the glycan (e.g., "Hex(3)HexNAc(2)")
    
    Returns:
        dict: A dictionary containing the WURCS format representation and ID for the given glycan composition text.
        
    Example:
        >>> result = convert_composition_text_to_wurcs_format("Hex(3)HexNAc(2)")
        >>> print(result["id"])
        G14669DU
        >>> print(result["wurcs"])
        WURCS=2.0/2,5,4/[axxxxh-1x_1-5_2*NCC/3=O][axxxxh-1x_1-5]/1-1-2-2-2/a?|b?|c?|d?|e?}-{a?|b?|c?|d?|e?_a?|b?|c?|d?|e?}-{a?|b?|c?|d?|e?_a?|b?|c?|d?|e?}-{a?|b?|c?|d?|e?_a?|b?|c?|d?|e?}-{a?|b?|c?|d?|e?
    """
    api_url = "https://api.glycosmos.org/composition2wurcs"
    
    assert text is not None, 'Missing required parameter: text'
    
    querystring = {'text': text}
    headers = {}
    
    response = requests.get(url=api_url, params=querystring, headers=headers, timeout=50)
    
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

if __name__ == '__main__':
    r = convert_composition_text_to_wurcs_format(text='Hex(3)HexNAc(2)')
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
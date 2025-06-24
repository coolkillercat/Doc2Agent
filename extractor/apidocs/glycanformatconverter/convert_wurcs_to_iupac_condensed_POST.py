import requests, json
from urllib.parse import quote

def convert_wurcs_to_iupac_condensed(wurcs=None):
    """
    Convert WURCS format to IUPAC Condensed format using the GlycanFormatConverter API.
    
    Args:
        wurcs (str): The WURCS format text to convert.
            Example: "WURCS=2.0/3,5,4/[a2122h-1b_1-5_2*NCC/3=O][a1122h-1b_1-5][a1122h-1a_1-5]/1-1-2-3-3/a4-b1_b4-c1_c3-d1_c6-e1"
    
    Returns:
        dict: A dictionary containing the conversion result with keys:
            - input: The input WURCS string
            - IUPACcondensed: The converted IUPAC condensed format
    
    Raises:
        AssertionError: If the wurcs parameter is None
        requests.exceptions.RequestException: If there's an issue with the API request
    """
    api_url = "https://api.glycosmos.org/glycanformatconverter/2.10.0/wurcs2iupaccondensed"
    assert wurcs is not None, 'Missing required parameter: wurcs'
    
    payload = [wurcs]
    headers = {'Content-Type': 'application/json'}
    
    response = requests.post(url=api_url, json=payload, headers=headers, timeout=50)
    return response.json()[0]

if __name__ == '__main__':
    r = convert_wurcs_to_iupac_condensed(wurcs='WURCS=2.0/3,5,4/[a2122h-1b_1-5_2*NCC/3=O][a1122h-1b_1-5][a1122h-1a_1-5]/1-1-2-3-3/a4-b1_b4-c1_c3-d1_c6-e1')
    result_dict = dict()
    result_dict['status_code'] = 200
    result_dict['text'] = json.dumps(r)
    result_dict['json'] = r
    result_dict['content'] = json.dumps(r)
    print(json.dumps(result_dict, indent=4))
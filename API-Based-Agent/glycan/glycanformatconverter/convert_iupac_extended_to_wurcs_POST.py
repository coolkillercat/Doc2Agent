import requests
import json
from urllib.parse import quote

def convert_iupac_extended_to_wurcs(iupacextended):
    """
    Convert IUPAC Extended format to WURCS format using the GlycanFormatConverter API.
    
    Args:
        iupacextended (str): The glycan structure in IUPAC Extended format.
            Example: "α-D-Manp-(1→3)[α-D-Manp-(1→6)]-β-D-Manp-(1→4)-β-D-GlcpNAc-(1→4)-β-D-GlcpNAc-(1→"
    
    Returns:
        Returns the WURCS format representation of a glycan structure and its corresponding GlyTouCan accession ID.
    Raises:
        ValueError: If iupacextended parameter is None or empty.
        requests.RequestException: If the API request fails.
    """
    if not iupacextended:
        raise ValueError('Missing required parameter: iupacextended')
    
    api_url = "https://api.glycosmos.org/glycanformatconverter/2.10.0/iupacextended2wurcs"
    headers = {'Content-Type': 'application/json'}
    
    try:
        # First try with POST request
        payload = [iupacextended]
        response = requests.post(url=api_url, json=payload, headers=headers, timeout=50)
        response.raise_for_status()
        return response.json()[0]
    except requests.exceptions.HTTPError:
        # If POST fails, try with GET request using URL encoding
        try:
            encoded_iupac = quote(iupacextended)
            get_url = f"{api_url}/{encoded_iupac}"
            response = requests.get(url=get_url, headers=headers, timeout=50)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise requests.exceptions.RequestException(f"Failed to convert IUPAC Extended to WURCS: {str(e)}")

if __name__ == '__main__':
    r = convert_iupac_extended_to_wurcs(iupacextended='''α-D-Manp-(1→3)[α-D-Manp-(1→6)]-β-D-Manp-(1→4)-β-D-GlcpNAc-(1→4)-β-D-GlcpNAc-(1→''')
    r_json = None
    try:
        r_json = r
    except:
        pass
    import json
    result_dict = dict()
    result_dict['status_code'] = 200
    result_dict['text'] = json.dumps(r)
    result_dict['json'] = r_json
    result_dict['content'] = json.dumps(r)
    print(json.dumps(result_dict, indent=4))
import requests
import json

def convert_iupac_condensed_to_wurcs(iupaccondensed):
    """
    Convert IUPAC Condensed format to WURCS format and retrieve GlyTouCan accession number.
    
    Parameters:
    -----------
    iupaccondensed : str
        IUPAC Condensed format text, e.g., "Man(a1-3)[Man(a1-6)]Man(b1-4)GlcNAc(b1-4)GlcNAc(b1-"
    
    Returns:
    --------
    dict
        JSON response containing the WURCS format and GlyTouCan accession number
    
    Example:
    --------
    >>> result = convert_iupac_condensed_to_wurcs("Man(a1-3)[Man(a1-6)]Man(b1-4)GlcNAc(b1-4)GlcNAc(b1-")
    >>> print(result['id'])
    G22768VO
    """
    api_url = "https://api.glycosmos.org/glycanformatconverter/2.10.0/iupaccondensed2wurcs"
    
    # Check if required parameter is provided
    if iupaccondensed is None:
        raise ValueError('Missing required parameter: iupaccondensed')
    
    # Prepare the payload as a list with a single string element as per API documentation
    payload = [iupaccondensed]
    
    # Make the API request
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url=api_url, data=json.dumps(payload), headers=headers, timeout=50)
    
    # Check response status
    response.raise_for_status()
    
    # Return the JSON response
    return response.json()[0]

if __name__ == '__main__':
    r = convert_iupac_condensed_to_wurcs(iupaccondensed="Man(a1-3)[Man(a1-6)]Man(b1-4)GlcNAc(b1-4)GlcNAc(b1-")
    
    result_dict = dict()
    result_dict['status_code'] = 200
    result_dict['text'] = json.dumps(r)
    result_dict['json'] = r
    result_dict['content'] = json.dumps(r)
    
    print(json.dumps(result_dict, indent=4))
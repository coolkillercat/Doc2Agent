import requests

def convert_linearcode_to_wurcs(linearcode=None):
    """
    Convert a LinearCode format to WURCS format and retrieve GlyTouCan accession number.
    
    Parameters:
    -----------
    linearcode : str, required
        LinearCode format text, e.g., "Ma3(Ma6)Mb4GNb4GN"
    
    Returns:
    --------
    dict
        Dictionary containing the conversion result with fields:
        - id: GlyTouCan accession number
        - wurcs: WURCS format of the input
        - WURCS: Same as wurcs
        - input: The original LinearCode input
    
    Example:
    --------
    >>> result = convert_linearcode_to_wurcs(linearcode="Ma3(Ma6)Mb4GNb4GN")
    >>> print(result["id"])  # Prints the GlyTouCan accession number
    >>> print(result["wurcs"])  # Prints the WURCS format
    """
    api_url = "https://api.glycosmos.org/glycanformatconverter/2.10.0/linearcode2wurcs"
    
    if linearcode is None:
        raise ValueError('Missing required parameter: linearcode')
    
    # The API expects a JSON array with the linearcode as a string
    payload = [linearcode]
    headers = {'Content-Type': 'application/json'}
    
    try:
        response = requests.post(url=api_url, json=payload, headers=headers)
        
        # Check if the request was successful
        response.raise_for_status()
        
        # Return the first item in the response array
        return response.json()[0]
    except requests.exceptions.RequestException as e:
        raise Exception(f"API request failed: {str(e)}")

if __name__ == '__main__':
    try:
        result = convert_linearcode_to_wurcs(linearcode='Ma3(Ma6)Mb4GNb4GN')
        import json
        result_dict = dict()
        result_dict['status_code'] = 200
        result_dict['text'] = json.dumps(result)
        result_dict['json'] = result
        result_dict['content'] = json.dumps(result)
        print(json.dumps(result_dict, indent=4))
    except Exception as e:
        print(f"Error: {e}")
import requests
from urllib.parse import quote
import xml.etree.ElementTree as ET

def structure_search_substructure(smiles, MatchIsotopes=False, MatchCharges=False, RingsNotEmbedded=False, 
                                 SingleDoubleBondsMatch=True, ChainsMatchRings=True, StripHydrogen=False, 
                                 Stereo="ignore", MaxSeconds=None, MaxRecords=2000000, output_format="XML"):
    """
    Perform a substructure search in PubChem using the PUG REST API.
    
    Parameters:
    -----------
    smiles : str
        SMILES string representing the substructure to search for.
    MatchIsotopes : bool, optional
        If True, atoms must be of the specified isotope. Default is False.
    MatchCharges : bool, optional
        If True, atoms must match the specified charge. Default is False.
    RingsNotEmbedded : bool, optional
        If True, rings may not be embedded in a larger system. Default is False.
    SingleDoubleBondsMatch : bool, optional
        If True, single or double bonds match aromatic bonds. Default is True.
    ChainsMatchRings : bool, optional
        If True, chain bonds in the query may match rings in hits. Default is True.
    StripHydrogen : bool, optional
        If True, remove any explicit hydrogens before searching. Default is False.
    Stereo : str, optional
        How to handle stereo; one of "ignore", "exact", "relative", "nonconflicting". Default is "ignore".
    MaxSeconds : int, optional
        Maximum search time in seconds. Default is None (unlimited).
    MaxRecords : int, optional
        Maximum number of hits to return. Default is 2000000.
    output_format : str, optional
        Output format: "XML", "JSON", "JSONP", "ASNT", "ASNB", "TXT". Default is "XML".
    
    Returns:
    --------
    requests.Response
        The response object from the API request.
    
    Examples:
    ---------
    >>> response = structure_search_substructure(smiles="C3=NC1=C(C=NC2=C1C=NC=C2)[N]3", MatchIsotopes=True, MaxRecords=100)
    >>> cids = parse_cids_from_response(response)
    """
    # Validate output format
    valid_formats = ["XML", "JSON", "JSONP", "ASNT", "ASNB", "TXT"]
    if output_format.upper() not in valid_formats:
        raise ValueError(f"Invalid output format. Must be one of {valid_formats}")
    
    # Build the URL
    api_url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/fastsubstructure/smiles/{quote(smiles, safe='')}/cids/{output_format}"
    
    # Build query parameters
    querystring = {}
    if MatchIsotopes:
        querystring['MatchIsotopes'] = 'true'
    if MatchCharges:
        querystring['MatchCharges'] = 'true'
    if RingsNotEmbedded:
        querystring['RingsNotEmbedded'] = 'true'
    if not SingleDoubleBondsMatch:
        querystring['SingleDoubleBondsMatch'] = 'false'
    if not ChainsMatchRings:
        querystring['ChainsMatchRings'] = 'false'
    if StripHydrogen:
        querystring['StripHydrogen'] = 'true'
    if Stereo != "ignore":
        querystring['Stereo'] = Stereo
    if MaxSeconds is not None:
        querystring['MaxSeconds'] = str(MaxSeconds)
    if MaxRecords != 2000000:
        querystring['MaxRecords'] = str(MaxRecords)
    
    # Set appropriate headers based on output format
    headers = {}
    if output_format.upper() == "XML":
        headers['Accept'] = 'application/xml'
    elif output_format.upper() == "JSON":
        headers['Accept'] = 'application/json'
    elif output_format.upper() == "JSONP":
        headers['Accept'] = 'application/javascript'
    elif output_format.upper() == "ASNT":
        headers['Accept'] = 'text/plain'
    elif output_format.upper() == "ASNB":
        headers['Accept'] = 'application/ber-encoded'
    elif output_format.upper() == "TXT":
        headers['Accept'] = 'text/plain'
    
    # Make the request
    response = requests.get(url=api_url, params=querystring, headers=headers, timeout=50)
    return response

def parse_cids_from_response(response):
    """
    Parse CIDs from the XML response.
    
    Parameters:
    -----------
    response : requests.Response
        The response from the structure_search_substructure function.
    
    Returns:
        Returns a list of PubChem compound IDs (CIDs) extracted from a PubChem API response.
    --------
    list
        List of CIDs as integers.
    """
    if response.status_code != 200:
        return []
    
    try:
        root = ET.fromstring(response.content)
        cids = []
        for cid in root.findall(".//CID"):
            cids.append(int(cid.text))
        return cids
    except ET.ParseError:
        return []

if __name__ == '__main__':
    r = structure_search_substructure(smiles='C3=NC1=C(C=NC2=C1C=NC=C2)[N]3', MatchIsotopes=True, MaxRecords=100)
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
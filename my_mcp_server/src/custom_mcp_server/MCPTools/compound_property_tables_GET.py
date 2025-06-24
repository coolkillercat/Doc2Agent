import requests
from urllib.parse import quote

def compound_property_tables(cid=None, property_tags=None):
    """
    Retrieve chemical property data for specified compounds in CSV format.
    
    Args:
        cid (str): Comma-separated list of PubChem compound IDs.
        property_tags (str): Comma-separated list of property tags to retrieve.
            Available properties include: MolecularFormula, MolecularWeight, 
            InChIKey, CanonicalSMILES, IsomericSMILES, etc.
    
    Returns:
        Returns chemical property data for specified compounds in CSV format based on requested property tags.
    Example:
        >>> response = compound_property_tables(cid="1,2,3", property_tags="MolecularFormula,MolecularWeight")
        >>> print(response.text)
    """
    assert cid is not None, 'Missing required parameter: cid'
    assert property_tags is not None, 'Missing required parameter: property_tags'
    
    api_url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/{quote(cid, safe='')}/property/{quote(property_tags, safe='')}/CSV"
    
    response = requests.get(url=api_url, timeout=50)
    return response

if __name__ == '__main__':
    r = compound_property_tables(cid='1,2,3,4,5', property_tags='MolecularFormula,MolecularWeight,InChIKey')
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
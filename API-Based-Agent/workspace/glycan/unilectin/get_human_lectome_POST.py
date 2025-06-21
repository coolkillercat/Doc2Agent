import requests
import json
from urllib.parse import quote

def get_human_lectome(getcolumns="RefSeqID,UniProt_ID", wherecolumn="lectinStatus", isvalue="Curated", limit=1000):
    """
    Retrieve human lectome data from the UniLectin database.
    
    This function queries the UniLectin API to get information about human lectins
    based on specified filtering criteria.
    
    Parameters:
        getcolumns (str): Comma-separated list of columns to retrieve (e.g., "RefSeqID,UniProt_ID")
        wherecolumn (str): Column to filter on (e.g., "lectinStatus", "common_protein_name")
        isvalue (str): Value to match in the wherecolumn (supports wildcards like "%SIGLEC%")
        limit (int): Maximum number of results to return (default: 1000, use -1 for all)
    
    Returns:
        Returns information about human lectins from the UniLectin database based on specified filtering criteria.
    Example:
        # Get all human lectins with curated status
        response = get_human_lectome(
            getcolumns="RefSeqID,UniProt_ID",
            wherecolumn="lectinStatus",
            isvalue="Curated",
            limit=1000
        )
        
        # Get all SIGLEC lectins
        response = get_human_lectome(
            getcolumns="RefSeqID,UniProt_ID",
            wherecolumn="common_protein_name",
            isvalue="%SIGLEC%",
            limit=1000
        )
    """
    api_url = "https://unilectin.unige.ch/api/gethumanlectome"
    payload = {
        'getcolumns': getcolumns,
        'wherecolumn': wherecolumn,
        'isvalue': isvalue,
        'limit': limit
    }
    headers = {'Content-Type': 'application/json'}
    
    assert getcolumns is not None, 'Missing required parameter: getcolumns'
    assert wherecolumn is not None, 'Missing required parameter: wherecolumn'
    assert isvalue is not None, 'Missing required parameter: isvalue'
    
    response = requests.post(url=api_url, json=payload, headers=headers, timeout=50)
    return response

if __name__ == '__main__':
    r = get_human_lectome(getcolumns="RefSeqID,UniProt_ID", wherecolumn="lectinStatus", isvalue="Curated", limit=1000)
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
import requests
import json
import csv
from io import StringIO

def get_ligands(getcolumns="ligand_id,iupac", wherecolumn="iupac", isvalue="%Gal%", limit=1000):
    """
    Retrieve ligand information from the UniLectin database.
    
    This function queries the UniLectin API to get ligand data based on specified criteria.
    
    Args:
        getcolumns (str): Columns to retrieve, comma-separated (e.g., "ligand_id,iupac")
        wherecolumn (str): Column to filter on (e.g., "iupac", "ligand_id")
        isvalue (str): Value to match in the wherecolumn (supports wildcards like "%Gal%")
        limit (int): Maximum number of results to return (default: 1000, use -1 for all)
    
    Returns:
        Returns ligand information from the UniLectin database, including requested fields like ligand IDs and IUPAC names based on specified filter criteria.
    Example:
        >>> get_ligands(getcolumns="ligand_id,iupac", wherecolumn="iupac", isvalue="%Gal%")
        [{'ligand_id': '1', 'iupac': 'Gal(b1-4)GlcNAc'}, {'ligand_id': '2', 'iupac': 'Gal'}, ...]
    """
    api_url = "https://unilectin.unige.ch/api/getligands"
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
    
    if response.status_code == 200:
        # Parse CSV-like response
        csv_data = StringIO(response.text)
        reader = csv.reader(csv_data)
        rows = list(reader)
        
        if len(rows) > 1:  # Check if there's at least a header row and one data row
            headers = rows[0]
            result = []
            for row in rows[1:]:
                result.append(dict(zip(headers, row)))
            return result
        return []
    else:
        response.raise_for_status()

if __name__ == '__main__':
    r = get_ligands(getcolumns="ligand_id,iupac", wherecolumn="iupac", isvalue="%Gal%", limit=1000)
    r_json = None
    try:
        r_json = r
    except:
        pass
    
    result_dict = dict()
    result_dict['status_code'] = 200
    result_dict['text'] = r
    result_dict['json'] = r_json
    result_dict['content'] = str(r)
    print(json.dumps(result_dict, indent=4))
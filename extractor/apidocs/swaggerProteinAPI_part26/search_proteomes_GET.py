import requests
from urllib.parse import quote

def search_proteomes(offset=0, size=100, upid=None, name=None, taxid=None, keyword=None, xref=None, genome_acc=None, is_ref_proteome=None, is_redundant=None):
    """
    Search proteomes in UniProt.
    
    Args:
        offset (int, optional): Off set, page starting point. Default is 0.
        size (int, optional): Page size. Default is 100. When -1, returns all records.
        upid (str, optional): UniProt proteome UPID(s). Comma separated values accepted up to 100.
        name (str, optional): Search proteome name.
        taxid (str, optional): Organism taxon ID. Comma separated values accepted up to 20.
        keyword (str, optional): Terms the proteome contains.
        xref (str, optional): Proteome cross references such as Genome assembly ID or Biosample ID.
        genome_acc (str, optional): Genome accession. Comma separated values accepted up to 20.
        is_ref_proteome (str, optional): Reference Proteome(true) or not reference proteome (false).
        is_redundant (str, optional): Redundant Proteome(true) or non redundant proteome (false).
    
    Returns:
        Returns proteome information from UniProt based on search criteria such as proteome ID, organism name, taxonomy ID, and other filters.
    Examples:
        >>> search_proteomes(upid="UP000005640")
        >>> search_proteomes(name="Homo sapiens", taxid="9606")
        >>> search_proteomes(offset=0, size=100, upid="UP000005640", name="Homo sapiens", 
                            taxid="9606", keyword="kinase", xref="GCA_000001405.28", 
                            genome_acc="GCA_000001405.28", is_ref_proteome="true", 
                            is_redundant="false")
    """
    api_url = "https://www.ebi.ac.uk/proteins/api/proteomes"
    querystring = {
        'offset': offset, 
        'size': size, 
        'upid': upid, 
        'name': name, 
        'taxid': taxid, 
        'keyword': keyword, 
        'xref': xref, 
        'genome_acc': genome_acc, 
        'is_ref_proteome': is_ref_proteome, 
        'is_redundant': is_redundant
    }
    
    # Remove None values
    querystring = {k: v for k, v in querystring.items() if v is not None}
    
    headers = {'Content-Type': 'application/json'}
    
    response = requests.get(url=api_url, params=querystring, headers=headers, timeout=50)
    return response

if __name__ == '__main__':
    r = search_proteomes(offset=0, size=100, upid='UP000005640', name='Homo sapiens', taxid='9606', keyword='kinase', xref='GCA_000001405.28', genome_acc='GCA_000001405.28', is_ref_proteome='true', is_redundant='false')
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
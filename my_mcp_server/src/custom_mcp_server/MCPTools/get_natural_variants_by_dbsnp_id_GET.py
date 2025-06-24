import requests
from urllib.parse import quote

def get_natural_variants_by_dbsnp_id(dbid, offset=0, size=100, sourcetype=None, consequencetype=None, wildtype=None, alternativesequence=None, location=None):
    """
    Get natural variants in UniProt by NIH-NCBI SNP database identifier.
    
    Parameters:
    -----------
    dbid : str
        Cross-reference NIH-NCBI SNP database identifier, e.g. rs121918508
    offset : int, optional
        Off set, page starting point, with default value 0
    size : int, optional
        Page size with default value 100. When page size is -1, it returns all records and offset will be ignored
    sourcetype : str, optional
        Filter by the sourceType for variants: uniprot, large scale study, mixed, clinvar, nci-tcga, cosmic curated, ensembl, gnomad, topmed and exac. Comma separated values accepted up to 2.
    consequencetype : str, optional
        Filter by consequenceType for variants: missense, stop gained or stop lost. Comma separated values accepted up to 2.
    wildtype : str, optional
        Search by specific wildType amino acid. Options: Any single letter amino acid and * for stop codon. Comma separated values accepted up to 20.
    alternativesequence : str, optional
        Filter by the alternativeSequence amino acid. Any single letter amino acid and * for stopcodon and - for deletions. Comma separated values accepted up to 20.
    location : str, optional
        Filter by the amino acid range position in the sequence(s). Any valid amino acid range position within the length of the protein sequence such as 10-60 (start position to end position)
    
    Returns:
        Returns natural variants in UniProt proteins associated with a specific NIH-NCBI SNP database identifier.
    --------
    requests.Response
        Response object from the API request
    
    Examples:
    ---------
    >>> get_natural_variants_by_dbsnp_id(dbid='rs121918508')
    >>> get_natural_variants_by_dbsnp_id(dbid='rs121918508', sourcetype='uniprot,clinvar', consequencetype='missense,stop gained')
    >>> get_natural_variants_by_dbsnp_id(dbid='rs121918508', wildtype='A', alternativesequence='V', location='10-60')
    """
    base_url = "https://www.ebi.ac.uk"
    api_url = f"{base_url}/proteins/api/variation/dbsnp/{quote(str(dbid))}"
    
    headers = {'Content-Type': 'application/json'}
    
    params = {}
    if offset is not None:
        params['offset'] = offset
    if size is not None:
        params['size'] = size
    if sourcetype is not None:
        params['sourcetype'] = sourcetype
    if consequencetype is not None:
        params['consequencetype'] = consequencetype
    if wildtype is not None:
        params['wildtype'] = wildtype
    if alternativesequence is not None:
        params['alternativesequence'] = alternativesequence
    if location is not None:
        params['location'] = location
    
    response = requests.get(url=api_url, params=params, headers=headers, timeout=50)
    return response

if __name__ == '__main__':
    r = get_natural_variants_by_dbsnp_id(dbid='rs121918508', offset=0, size=100, sourcetype='uniprot,clinvar', consequencetype='missense,stop gained', wildtype='A', alternativesequence='V,-', location='10-60')
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
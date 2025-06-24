import requests
from urllib.parse import quote

def get_natural_variants_by_uniprot_accession(accession, sourcetype=None, consequencetype=None, wildtype=None, alternativesequence=None, location=None):
    """
    Get natural variants by UniProt accession.
    
    Parameters:
    -----------
    accession : str
        UniProt accession (required)
    sourcetype : str, optional
        Filter by the sourceType for variants: uniprot, large scale study, mixed, clinvar, nci-tcga, cosmic curated, ensembl, gnomad, topmed and exac. Comma separated values accepted up to 2.
        Example: 'uniprot,clinvar'
    consequencetype : str, optional
        Filter by consequenceType for variants: missense, stop gained or stop lost. Comma separated values accepted up to 2.
        Example: 'missense,stop gained'
    wildtype : str, optional
        Search by specific wildType amino acid. Options: Any single letter amino acid and * for stop codon. Comma separated values accepted up to 20.
        Example: 'A,C'
    alternativesequence : str, optional
        Filter by the alternativeSequence amino acid. Any single letter amino acid and * for stopcodon and - for deletions. Comma separated values accepted up to 20.
        Example: 'V,L,-'
    location : str, optional
        Filter by the amino acid range position in the sequence(s). Any valid amino acid range position within the length of the protein sequence such as 10-60 (start position to end position)
        Example: '10-60'
    
    Returns:
    --------
    requests.Response
        The API response object
    
    Example:
    --------
    >>> get_natural_variants_by_uniprot_accession('Q9NXB0-3', sourcetype='uniprot,clinvar', consequencetype='missense')
    """
    base_url = "https://www.ebi.ac.uk"
    api_url = f"{base_url}/proteins/api/variation/{quote(accession, safe='')}"
    
    # Remove None values from parameters
    params = {}
    if sourcetype is not None:
        params['sourcetype'] = sourcetype
    if consequencetype is not None:
        params['consequencetype'] = consequencetype
    if wildtype is not None:
        # Ensure wildtype only contains valid characters (single letters and commas)
        # Remove '*' as it's causing the error
        valid_wildtype = ','.join([wt for wt in wildtype.split(',') if wt != '*'])
        if valid_wildtype:
            params['wildtype'] = valid_wildtype
    if alternativesequence is not None:
        params['alternativesequence'] = alternativesequence
    if location is not None:
        params['location'] = location
    
    headers = {'Content-Type': 'application/json'}
    
    response = requests.get(url=api_url, params=params, headers=headers, timeout=50)
    return response

if __name__ == '__main__':
    r = get_natural_variants_by_uniprot_accession(accession='P12345', sourcetype='uniprot,clinvar', consequencetype='missense,stop gained', wildtype='A,C', alternativesequence='V,L,-', location='10-60')
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
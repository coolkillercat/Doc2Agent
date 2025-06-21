import requests
from typing import Optional, Union, List


def search_proteomics_peptides(
    offset: Optional[int] = 0,
    size: Optional[int] = 100,
    accession: Optional[Union[str, List[str]]] = None,
    taxid: Optional[Union[str, List[str]]] = None,
    upid: Optional[Union[str, List[str]]] = None,
    datasource: Optional[Union[str, List[str]]] = None,
    peptide: Optional[Union[str, List[str]]] = None,
    unique: Optional[str] = None
) -> requests.Response:
    """
    Search proteomics peptides in UniProt.
    
    Args:
        offset (int, optional): Off set, page starting point. Defaults to 0.
        size (int, optional): Page size. When page size is -1, it returns all records and offset will be ignored. Defaults to 100.
        accession (str or list, optional): UniProt accession(s). Comma separated values accepted up to 100.
        taxid (str or list, optional): Organism taxon ID. Comma separated values accepted up to 20.
        upid (str or list, optional): UniProt proteome UPID(s). Comma separated values accepted up to 100.
        datasource (str or list, optional): Proteomics data source(s): MaxQB, PeptideAtlas, EPD or ProteomicsDB. Comma separated values accepted up to 2.
        peptide (str or list, optional): Peptide sequence. Comma separated values accepted up to 20.
        unique (str, optional): Peptide uniqueness (unique peptides map to one gene group only). Values can be true or false.
    
    Returns:
        Returns proteomics peptide data from UniProt matching the specified search criteria such as accession numbers, taxon IDs, and peptide sequences.
    Examples:
        >>> response = search_proteomics_peptides(accession="Q9NXB0-3")
        >>> response = search_proteomics_peptides(
        ...     offset=0,
        ...     size=100,
        ...     accession="P12345,Q67890",
        ...     taxid="9606,10090",
        ...     upid="UP000005640,UP000002311",
        ...     datasource="MaxQB,PeptideAtlas",
        ...     peptide="PEPTIDE1,PEPTIDE2",
        ...     unique="true"
        ... )
    """
    api_url = "https://www.ebi.ac.uk/proteins/api/proteomics"
    
    # Create a dictionary for parameters
    params = {
        'offset': offset,
        'size': size
    }
    
    # Process list parameters
    if accession:
        params['accession'] = ','.join(accession) if isinstance(accession, list) else accession
    if taxid:
        params['taxid'] = ','.join(map(str, taxid)) if isinstance(taxid, list) else taxid
    if upid:
        params['upid'] = ','.join(upid) if isinstance(upid, list) else upid
    if datasource:
        params['datasource'] = ','.join(datasource) if isinstance(datasource, list) else datasource
    if peptide:
        params['peptide'] = ','.join(peptide) if isinstance(peptide, list) else peptide
    if unique:
        params['unique'] = unique
    
    headers = {'Content-Type': 'application/json'}
    
    response = requests.get(
        url=api_url,
        params=params,
        headers=headers,
        timeout=50
    )
    
    return response


if __name__ == '__main__':
    r = search_proteomics_peptides(
        offset=0,
        size=100,
        accession='P12345,Q67890',
        taxid='9606,10090',
        upid='UP000005640,UP000002311',
        datasource='MaxQB,PeptideAtlas',
        peptide='PEPTIDE1,PEPTIDE2',
        unique='true'
    )
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
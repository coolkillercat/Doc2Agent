import requests
from typing import List, Optional


def get_uniprot_protein_sequence_features_by_accession(
    accession: str,
    categories: Optional[List[str]] = None,
    types: Optional[List[str]] = None,
    location: Optional[str] = None
) -> requests.Response:
    """
    Get UniProt protein sequence features by accession.
    
    Args:
        accession (str): UniProt accession (required)
        categories (List[str], optional): Category type(s): MOLECULE_PROCESSING, TOPOLOGY, 
            SEQUENCE_INFORMATION, STRUCTURAL, DOMAINS_AND_SITES, PTM, VARIANTS, MUTAGENESIS.
            Comma separated values accepted up to 20.
        types (List[str], optional): Feature type(s): INIT_MET, SIGNAL, PROPEP, TRANSIT, CHAIN, 
            PEPTIDE, TOPO_DOM, TRANSMEM, DOMAIN, REPEAT, ZN_FING, DNA_BIND, REGION, COILED, 
            MOTIF, COMPBIAS, ACT_SITE, BINDING, SITE, NON_STD, MOD_RES, LIPID, CARBOHYD, 
            DISULFID, CROSSLNK, VAR_SEQ, VARIANT, MUTAGEN, UNSURE, CONFLICT, NON_CONS, 
            NON_TER, HELIX, TURN, STRAND, INTRAMEM.
            Comma separated values accepted up to 20.
        location (str, optional): Filter by the amino acid range position in the sequence(s).
            Any valid amino acid range position within the length of the protein sequence 
            such as 10-60 (start position to end position).
    
    Returns:
        Returns protein sequence features for a specified UniProt accession, including sequence information, structural elements, domains, and modifications.
    Examples:
        >>> response = get_uniprot_protein_sequence_features_by_accession(
        ...     accession="P12345",
        ...     categories=["MOLECULE_PROCESSING", "TOPOLOGY"],
        ...     types=["INIT_MET", "SIGNAL"],
        ...     location="10-60"
        ... )
        >>> response.status_code
        200
    """
    base_url = "https://www.ebi.ac.uk"
    api_url = f"{base_url}/proteins/api/features/{accession}"
    
    headers = {'Content-Type': 'application/json'}
    
    # Prepare query parameters
    params = {}
    if categories:
        params['categories'] = ','.join(categories)
    if types:
        params['types'] = ','.join(types)
    if location:
        params['location'] = location
    
    response = requests.get(url=api_url, params=params, headers=headers, timeout=50)
    return response


if __name__ == '__main__':
    r = get_uniprot_protein_sequence_features_by_accession(
        accession='P12345',
        categories=['MOLECULE_PROCESSING', 'TOPOLOGY'],
        types=['INIT_MET', 'SIGNAL'],
        location='10-60'
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
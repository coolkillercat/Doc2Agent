import requests
from urllib.parse import quote

def search_natural_variants(offset=0, size=100, sourcetype=None, consequencetype=None, wildtype=None, alternativesequence=None, location=None, accession=None, disease=None, omim=None, evidence=None, taxid=None, dbtype=None, dbid=None):
    """
    Search natural variants in UniProt.
    
    Parameters:
    -----------
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
    accession : str, optional
        UniProt accession(s). Comma separated values accepted up to 100.
    disease : str, optional
        Search by disease name/ acronym for associated variants , e.g. alzheimer disease 1 or AD1. Partial names allowed.
    omim : str, optional
        Search by MIM ID, e.g. 104300. Comma separated values accepted up to 20.
    evidence : str, optional
        Search by PubMed ID, e.g. 22472873. Comma separated values accepted up to 20.
    taxid : str, optional
        Organism taxon ID. Comma separated values accepted up to 20.
    dbtype : str, optional
        Cross reference database type, e.g, dbSNP, cosmic curate or ClinVar. Comma separated values accepted up to 2.
    dbid : str, optional
        Cross-reference database ID, e.g. rs121918508 for dbSNP, COSM29836 for cosmic curated, rcv61200 for ClinVar. Comma separated values accepted up to 20.
    
    Returns:
        Returns natural protein variants from UniProt with filtering options for source type, consequence type, amino acid changes, disease associations, and other variant properties.
    --------
    requests.Response
        The API response object
    
    Examples:
    ---------
    >>> search_natural_variants(accession="Q9NXB0-3")
    >>> search_natural_variants(offset=0, size=100, sourcetype="uniprot,clinvar", consequencetype="missense,stop gained", wildtype="A", alternativesequence="V,-", location="10-60", accession="P12345,Q67890", disease="alzheimer disease 1", omim="104300", evidence="22472873", taxid="9606", dbtype="dbSNP,ClinVar", dbid="rs121918508")
    """
    api_url = "https://www.ebi.ac.uk/proteins/api/variation"
    querystring = {}
    
    if offset is not None:
        querystring['offset'] = offset
    if size is not None:
        querystring['size'] = size
    if sourcetype is not None:
        querystring['sourcetype'] = sourcetype
    if consequencetype is not None:
        querystring['consequencetype'] = consequencetype
    if wildtype is not None:
        querystring['wildtype'] = wildtype
    if alternativesequence is not None:
        querystring['alternativesequence'] = alternativesequence
    if location is not None:
        querystring['location'] = location
    if accession is not None:
        querystring['accession'] = accession
    if disease is not None:
        querystring['disease'] = disease
    if omim is not None:
        querystring['omim'] = omim
    if evidence is not None:
        querystring['evidence'] = evidence
    if taxid is not None:
        querystring['taxid'] = taxid
    if dbtype is not None:
        querystring['dbtype'] = dbtype
    if dbid is not None:
        querystring['dbid'] = dbid
    
    headers = {'Content-Type': 'application/json'}
    
    response = requests.get(url=api_url, params=querystring, headers=headers, timeout=50)
    return response

if __name__ == '__main__':
    r = search_natural_variants(offset=0, size=100, sourcetype='uniprot,clinvar', consequencetype='missense,stop gained', wildtype='A', alternativesequence='V,-', location='10-60', accession='P12345,Q67890', disease='alzheimer disease 1', omim='104300', evidence='22472873', taxid='9606', dbtype='dbSNP,ClinVar', dbid='rs121918508')
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
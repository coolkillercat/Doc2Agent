PUG REST - PubChem

ResetSubmit search

# PUG REST

This document describes the REST-style version of PUG (Power User
Gateway), a web interface for accessing PubChem data and services. It
details both the syntax of the HTTP requests, and the available
functions. This is more of a specification document; a less formal, [tutorial-style PUG REST document](https://pubchem.ncbi.nlm.nih.gov/docs/pug-rest-tutorial) is now available. For comments, help, or to suggest new functionality, please contact [pubchem-help@ncbi.nlm.nih.gov](mailto:pubchem-help@ncbi.nlm.nih.gov).

Additional information of PUG REST can also be found in the following papers:

> > - Kim S, Thiessen PA, Cheng T, Yu B, Bolton EE. **An update on PUG-REST: RESTful interface for programmatic access to PubChem**. Nucleic Acids Res. 2018 July 2; 46(W1):W563-570. doi:10.1093/nar/gky294.
> >   [[PubMed PMID: 29718389]](https://www.ncbi.nlm.nih.gov/pubmed/29718389) [[PubMed Central ID: PMC6030920]](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6030920/) [[Free Full Text]](https://doi.org/10.1093/nar/gky294)
> > - Kim S, Thiessen PA, Bolton EE, Bryant SH. **PUG-SOAP and PUG-REST: web services for programmatic access to chemical information in PubChem**. Nucleic Acids Res. 2015 Jul 1; 43(W1):W605-W611. doi: 10.1093/nar/gkv396.
> >   [[PubMed PMID: 25934803]](https://www.ncbi.nlm.nih.gov/pubmed/25934803) [[PubMed Central PMCID: PMC4489244]](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4489244/) [[Free Full Text]](http://doi.org/10.1093/nar/gkv396)
> > - Kim S, Thiessen PA, Bolton EE. **Programmatic Retrieval of Small Molecule Information from PubChem Using PUG-REST**.
> >   In Kutchukian PS, ed. Chemical Biology Informatics and Modeling.
> >   Methods in Pharmacology and Toxicology. New York, NY: Humana Press,
> >   2018, pp. 1-24. doi:10.1007/7653\_2018\_30.
> >   [[Full Text]](https://doi.org/10.1007/7653_2018_30)

> > **USAGE POLICY**: Please note that PUG REST is not
> > designed for very large volumes (millions) of requests. We ask that any
> > script or application not make more than 5 requests per second, in order
> > to avoid overloading the PubChem servers. To check additional request
> > volume limitations, please read [this document](https://pubchem.ncbi.nlm.nih.gov/docs/programmatic-access#section=Request-Volume-Limitations).
> > If you have a large data set that you need to compute with, please
> > contact us for help on optimizing your task, as there are likely more
> > efficient ways to approach such bulk queries.

> > **503 HTTP STATUS CODE**: Please note that this status
> > code may be returned when the server is temporarily unable to service
> > your request due to maintenance downtime or capacity problems. (Please
> > try again later.) Please also note that an HTML document may be
> > returned.

> > **Example Perl scripts** demonstrating how to access PubChem data through PUG-REST are available [here](https://pubchem.ncbi.nlm.nih.gov/docs/pug-rest#section=Example-Scripts).

## URL-based API

### The URL Path

Most – if not all – of the information the service needs to produce
its results is encoded into the URL. The general form of the URL has
three parts – input, operation, and output – after the common prefix,
followed by operation options as URL arguments (after the ‘?’):

`https://pubchem.ncbi.nlm.nih.gov/rest/pug/<input
specification>/<operation specification>/[<output
specification>][?<operation_options>]`

#### Input

The input portion of the URL tells the service which records to use
as the subject of the query. This is further subdivided into two or more
locations in the URL “path” as follows:

`<input specification> = <domain>/<namespace>/<identifiers>`

`<domain> = substance | compound | assay | gene | protein | pathway | taxonomy | cell | <other inputs>`

`compound domain <namespace> = cid | name | smiles | inchi
| sdf | inchikey | formula | <structure search> | <xref> |
listkey | <fast search>`

`<structure search> = {substructure | superstructure | similarity | identity}/{smiles | inchi | sdf | cid}`

`<fast search> = {fastidentity | fastsimilarity_2d |
fastsimilarity_3d | fastsubstructure | fastsuperstructure}/{smiles |
smarts | inchi | sdf | cid} | fastformula`

`<xref> = xref / {RegistryID | RN | PubMedID | MMDBID |
ProteinGI | NucleotideGI | TaxonomyID | MIMID | GeneID | ProbeID |
PatentID}`

`substance domain <namespace> = sid | sourceid/<source
id> | sourceall/<source name> | name | <xref> | listkey`

`<source name> = any valid PubChem depositor name`

`assay domain <namespace> = aid | listkey | type/<assay
type> | sourceall/<source name> | target/<assay target> |
activity/<activity column name>`

`<assay type> = all | confirmatory | doseresponse | onhold
| panel | rnai | screening | summary | cellbased | biochemical | invivo
| invitro | activeconcentrationspecified`

`<assay target> = gi | proteinname | geneid | genesymbol | accession`

`gene domain <namespace> = geneid | genesymbol | synonym`

`protein domain <namespace> = accession | gi | synonym`

`pathway domain <namespace> = pwacc`

`taxonomy domain <namespace> = taxid | synonym`

`cell domain <namespace> = cellacc | synonym`

`<other inputs> = sources / [substance, assay] |
sourcetable | conformers | annotations/[sourcename/<source name> |
heading/<heading>] | classification | standardize | periodictable`

`<identifiers> = comma-separated list of positive integers
(e.g. cid, sid, aid) or identifier strings (source, inchikey, formula);
in some cases only a single identifier string (name, smiles, xref;
inchi, sdf by POST only)`

For example, to access CID 2244 (aspirin), one would construct the first part of the URL this way:

`https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/2244/<operation specification>/[<output specification>]`

Some source names contain the ‘/’ (forward slash) character, which is
incompatible with the URL syntax; for these, replace the ‘/’ with a ‘.’
(period) in the URL. Other special characters may need to be escaped,
such as ‘&’ should be replaced by ‘%26’. For example:

`https://pubchem.ncbi.nlm.nih.gov/rest/pug/substance/sourceid/
DTP.NCI/<operation specification>/[<output specification>]`

#### Operation

The operation part of the URL tells the service what to do with the
input records – such as to retrieve whole record data blobs or specific
properties of a compound, etc. The construction of this part of the
“path” will depend on what the operation is. Currently, if no operation
is specified at all, the default is to retrieve the entire record. What
operations are available are, of course, dependent on the input domain –
that is, certain operations are applicable only to compounds and not
assays, for example.

`compound domain <operation specification> = record |
<compound property> | synonyms | sids | cids | aids | assaysummary
| classification | <xrefs> | description | conformers`

`<compound property> = property / [comma-separated list of property tags]`

`substance domain <operation specification> = record |
synonyms | sids | cids | aids | assaysummary | classification |
<xrefs> | description`

`<xrefs> = xrefs / [comma-separated list of xrefs tags]`

`assay domain <operation specification> = record | concise
| aids | sids | cids | description | targets/<target type> |
<doseresponse> | summary | classification`

`<target_type> = {ProteinGI, ProteinName, GeneID, GeneSymbol}`

`<doseresponse> = doseresponse/sid`

`gene domain <operation specification> = summary | aids | concise | pwaccs`

`protein domain <operation specification> = summary | aids | concise | pwaccs`

`pathway domain <operation specification> = summary | cids | geneids | accessions`

`taxonomy domain <operation specification> = summary | aids`

`cell domain <operation specification> = summary | aids`

For example, to access the molecular formula and InChI key for CID 2244, one would use a URL like:

`https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/2244/property/MolecularFormula,InChIKey/[<output specification>]`

#### Output

The final portion of the URL tells the service what output format is
desired. Note that this is formally optional, as output format can also
be specified in the HTTP Accept field of the request header – see below
for more detail.

`<output specification> = XML | ASNT | ASNB | JSON | JSONP [ ?callback=<callback name> ] | SDF | CSV | PNG | TXT`

ASNT is NCBI’s text (human-readable) variant of ASN.1; ASNB is
standard binary ASN.1 and is currently returned as Base64-encoded ascii
text. Note that not all formats are applicable to the results of all
operations; one cannot, for example, retrieve a whole compound record as
CSV or a property table as SDF. TXT output is only available in a
restricted set of cases where all the information is the same – for
example, synonyms for a single CID where there is one synonym per line.

For example, to access the molecular formula for CID 2244 in JSON format, one would use the (now complete) URL:

<https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/2244/property/MolecularFormula/JSON>

JSONP takes an optional callback function name (which defaults to “callback” if not specified). For example:

<https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/2244/property/MolecularFormula/JSONP?callback=my_callback>

## HTTP Interface Details

### Request Header

The HTTP request header may be used to supply some types of information to this service.

The value of “Accept” may be a MIME type that will tell the service
what output format is accepted by the client, and hence what format is
returned by the server. The allowed values are:

| Accept value | Output Format |
| --- | --- |
| application/xml | XML |
| application/json | JSON |
| application/javascript | JSONP |
| application/ber-encoded | ASNB |
| chemical/x-mdl-sdfile | SDF |
| text/csv | CSV |
| image/png | PNG |
| text/plain | TXT |

The Content-Type in the HTTP response header will also be set by the
reverse of the above table, e.g. XML data will have “Content-Type:
application/xml”.

For example, the URL:

<https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/2244>

with “Accept: chemical/x-mdl-sdfile” in the request header will return CID 2244 in SDF format.

For proper transmission of certain special characters, strings passed
e.g. for SMILES input may need to be URL encoded; for example,
“smiles=C1C[CH+]1” should be encoded as “smiles=C1C%5BCH%2B%5D1”. For
correct parsing of any POST body, the proper content type header must be
included in the request header (see below).

### Request (POST) Body

Some parts of the URL may be moved to the body of a POST request,
rather than being part of the URL path. For example, a list of CID
integers – which may be too long to fit within the size limitations of a
GET request URL – may be moved to the POST body:

<https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/property/MolecularFormula,MolecularWeight/CSV>

with “cid=1,2,3,4,5” in the POST body, would retrieve a CSV-formatted
table of results for these CIDs. Note that for the service to parse
such POST information correctly, the “Content-Type:
application/x-www-form-urlencoded” value must be included in the request
header. One may also use “Content-Type: multipart/form-data” with the
POST body formatted accordingly. See [here](http://www.w3.org/TR/html4/interact/forms.html#h-17.13.4) for more information on content type encoding.

### Status Codes

If the operation was successful, the HTTP status code will be 200
(OK). If the server encounters an error, it will return an HTTP status
code that gives some indication of what went wrong; possibly along with,
depending on the output format (such as in a tag in XML), some
additional more human-readable detail message(s). The codes in the
400-range are errors on the client side, and those in the 500 range
indicate a problem on the server side; the codes currently in use are:

| HTTP Status | Error Code | General Error Category |
| --- | --- | --- |
| 200 | (none) | Success |
| 202 | (none) | Accepted (asynchronous operation pending) |
| 400 | PUGREST.BadRequest | Request is improperly formed (syntax error in the URL, POST body, etc.) |
| 404 | PUGREST.NotFound | The input record was not found (e.g. invalid CID) |
| 405 | PUGREST.NotAllowed | Request not allowed (such as invalid MIME type in the HTTP Accept header) |
| 500 | PUGREST.Unknown | An unknown error occurred |
| 500 | PUGREST.ServerError | Some problem on the server side (such as a database server down, etc.) |
| 501 | PUGREST.Unimplemented | The requested operation has not (yet) been implemented by the server |
| 503 | PUGREST.ServerBusy | Too many requests or server is busy, retry later |
| 504 | PUGREST.Timeout | The request timed out, from server overload or too broad a request |

### HTTPS

NCBI now requires HTTPS (URLs beginning with https://) for web service access.

## Schemas

A schema for the XML data returned by PUG REST may be found at:

<https://pubchem.ncbi.nlm.nih.gov/pug_rest/pug_rest.xsd>

Some operations (such as full record retrieval) may use the standard PubChem schema at:

<https://ftp.ncbi.nlm.nih.gov/pubchem/specifications/pubchem.xsd>

Classification data is returned with this schema:

<https://pubchem.ncbi.nlm.nih.gov/pug_rest/hierarchy_data.xsd>

## Operations

### Full-record Retrieval

Returns full records for PubChem substances, compounds, and assays.

Valid output formats for substances and compounds are XML, JSON(P),
ASNT/B, SDF, and PNG. A compound record may optionally be either 2D or
3D; substances are always given with coordinates as deposited. For PNG
output, only the first SID or CID is used if the input is a list.

| Option | Allowed Values (default in bold) | Meaning |
| --- | --- | --- |
| record\_type | **2d**, 3d | Type of conformer for compounds |
| image\_size | **large**, small, <width>x<height> | Image size: large (300x300), small (100x100), or arbitrary (e.g. 320x240) |

Valid output formats for assays are XML, JSON(P), ASNT/B, and CSV.
Assay record retrieval is limited to a single AID with 10000 SIDs at a
time; a subset of the SIDs of an assay may be specified as options:

| Option | Allowed Values | Meaning |
| --- | --- | --- |
| sid | listkey, or comma-separated integers | SID rows to retrieve for an assay |
| listkey | valid SID listkey | listkey containing SIDs, if using sid=listkey |

Examples:

<https://pubchem.ncbi.nlm.nih.gov/rest/pug/substance/sourceid/IBM/5F1CA2B314D35F28C7F94168627B29E3/ASNT>

<https://pubchem.ncbi.nlm.nih.gov/rest/pug/substance/sourceid/DTP.NCI/747285/SDF>

<https://pubchem.ncbi.nlm.nih.gov/rest/pug/substance/sourceid/DTP.NCI/747285/PNG>

<https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/2244/SDF>

<https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/2244/PNG>

<https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/2244/SDF?record_type=3d>

<https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/2244/PNG?record_type=3d&image_size=small>

<https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/aspirin/SDF>

<https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/inchikey/BPGDAMSIGCZZLK-UHFFFAOYSA-N/SDF>

<https://pubchem.ncbi.nlm.nih.gov/rest/pug/assay/aid/1000/XML>

<https://pubchem.ncbi.nlm.nih.gov/rest/pug/assay/aid/1000/ASNT?version=1.1> (for old-version)

<https://pubchem.ncbi.nlm.nih.gov/rest/pug/assay/aid/1000/CSV?sid=26736081,26736082,26736083>

<https://pubchem.ncbi.nlm.nih.gov/rest/pug/assay/aid/1000/concise/CSV>

### Compound Property Tables

Returns a table of compound properties. More than one property may be
requested, in a comma-separated list of property tags in the request
URL. Valid output formats for the property table are: XML, ASNT/B,
JSON(P), CSV, and TXT (limited to a single property). Available
properties are:

| Property | Notes |
| --- | --- |
| MolecularFormula | [Molecular formula](#Molecular%20Formula). |
| MolecularWeight | The molecular weight is the sum of all atomic weights of the constituent atoms in a compound, measured in g/mol. In the absence of explicit isotope labelling, averaged natural abundance is assumed. If an atom bears an explicit isotope label, 100% isotopic purity is assumed at this location. |
| CanonicalSMILES | Canonical SMILES (Simplified Molecular Input Line Entry System) string. It is a unique SMILES string of a compound, generated by a “canonicalization” algorithm. |
| IsomericSMILES | Isomeric SMILES string. It is a SMILES string with stereochemical and isotopic specifications. |
| InChI | Standard IUPAC International Chemical Identifier (InChI). It does not allow for user selectable options in dealing with the stereochemistry and tautomer layers of the InChI string. |
| InChIKey | Hashed version of the full standard InChI, consisting of 27 characters. |
| IUPACName | Chemical name systematically determined according to the IUPAC nomenclatures. |
| Title | The title used for the compound summary page. |
| XLogP | Computationally generated octanol-water partition coefficient or distribution coefficient. XLogP is used as a measure of hydrophilicity or hydrophobicity of a molecule. |
| ExactMass | The mass of the most likely isotopic composition for a single molecule, corresponding to the most intense ion/molecule peak in a mass spectrum. |
| MonoisotopicMass | The mass of a molecule, calculated using the mass of the most abundant isotope of each element. |
| TPSA | [Topological polar surface area](#TPSA), computed by the algorithm described in [the paper by Ertl et al](https://doi.org/10.1021/jm000942e). |
| Complexity | The [molecular complexity](#Complexity) rating of a compound, computed using the Bertz/Hendrickson/Ihlenfeldt formula. |
| Charge | The total (or net) charge of a molecule. |
| HBondDonorCount | Number of hydrogen-bond donors in the structure. |
| HBondAcceptorCount | Number of hydrogen-bond acceptors in the structure. |
| RotatableBondCount | Number of rotatable bonds. |
| HeavyAtomCount | Number of non-hydrogen atoms. |
| IsotopeAtomCount | Number of atoms with enriched isotope(s) |
| AtomStereoCount | Total number of atoms with tetrahedral (sp3) stereo [e.g., (R)- or (S)-configuration] |
| DefinedAtomStereoCount | Number of atoms with defined tetrahedral (sp3) stereo. |
| UndefinedAtomStereoCount | Number of atoms with undefined tetrahedral (sp3) stereo. |
| BondStereoCount | Total number of bonds with planar (sp2) stereo [e.g., (E)- or (Z)-configuration]. |
| DefinedBondStereoCount | Number of atoms with defined planar (sp2) stereo. |
| UndefinedBondStereoCount | Number of atoms with undefined planar (sp2) stereo. |
| CovalentUnitCount | Number of covalently bound units. |
| PatentCount | Number of patent documents linked to this compound. |
| PatentFamilyCount | Number of unique patent families linked to this compound (e.g. patent documents grouped by family). |
| LiteratureCount | Number of articles linked to this compound (by PubChem's consolidated literature analysis). |
| Volume3D | Analytic volume of the first diverse conformer (default conformer) for a compound. |
| XStericQuadrupole3D | The x component of the quadrupole moment (Qx) of the first diverse conformer (default conformer) for a compound. |
| YStericQuadrupole3D | The y component of the quadrupole moment (Qy) of the first diverse conformer (default conformer) for a compound. |
| ZStericQuadrupole3D | The z component of the quadrupole moment (Qz) of the first diverse conformer (default conformer) for a compound. |
| FeatureCount3D | Total number of 3D features (the sum of FeatureAcceptorCount3D, FeatureDonorCount3D, FeatureAnionCount3D, FeatureCationCount3D, FeatureRingCount3D and FeatureHydrophobeCount3D) |
| FeatureAcceptorCount3D | Number of hydrogen-bond acceptors of a conformer. |
| FeatureDonorCount3D | Number of hydrogen-bond donors of a conformer. |
| FeatureAnionCount3D | Number of anionic centers (at pH 7) of a conformer. |
| FeatureCationCount3D | Number of cationic centers (at pH 7) of a conformer. |
| FeatureRingCount3D | Number of rings of a conformer. |
| FeatureHydrophobeCount3D | Number of hydrophobes of a conformer. |
| ConformerModelRMSD3D | Conformer sampling RMSD in Å. |
| EffectiveRotorCount3D | Total number of 3D features (the sum of FeatureAcceptorCount3D, FeatureDonorCount3D, FeatureAnionCount3D, FeatureCationCount3D, FeatureRingCount3D and FeatureHydrophobeCount3D) |
| ConformerCount3D | The number of conformers in the conformer model for a compound. |
| Fingerprint2D | Base64-encoded PubChem Substructure Fingerprint of a molecule. |

Example:

<https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/1,2,3,4,5/property/MolecularFormula,MolecularWeight,InChIKey/CSV>

### Synonyms

Returns a list of substance or compound synonyms. Valid output formats for synonyms are XML, JSON(P), ASNT/B, and TXT (limited).

Examples:

<https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/aspirin/synonyms/XML>

<https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/smiles/CCCC/synonyms/XML>

<https://pubchem.ncbi.nlm.nih.gov/rest/pug/substance/sid/53789435/synonyms/TXT>

### Description

Returns the title and description for an S/CID, the same as used in
the web summary pages for these records. Valid output formats are XML,
JSON(P) , and ASNT/B.

<https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/1983/description/XML>

### SIDS / CIDS / AIDS

Returns a list of SIDs, CIDs, or AIDs. Possibly interconverts record
identifiers, with options in the table below; these options, if present,
must be specified as standard URL arguments (e.g. after the ‘?’). The
list of identifiers may be grouped by input (e.g. when converting from
one type to another); flattened to a unique target set (implied for TXT
output); or stored on the server (which also implies flat), in which
case a list key is returned. Valid output formats are XML, JSON(P),
ASNT/B, and TXT.

| Option | Allowed Values (default in bold) | Meaning |
| --- | --- | --- |
| aids\_type | **all**, active, inactive | Type of AIDs to return, given SIDs or CIDs |
| sids\_type | **all**, active, inactive, doseresponse | Type of SIDs to return, given AIDs |
| sids\_type | all, **standardized**, component | Type of SIDs to return, given CIDs |
| sids\_type | **original** | Type of SIDs to return, given SIDs |
| cids\_type | **all**, active, inactive | Type of CIDs to return, given AIDs |
| cids\_type | all, **standardized**, component | Type of CIDs to return, given SIDs |
| cids\_type | **original**, parent, component, preferred, similar\_2d, similar\_3d,same\_stereo, same\_isotopes,same\_connectivity, same\_tautomer,same\_parent, same\_parent\_stereo, same\_parent\_isotopes,same\_parent\_connectivity, same\_parent\_tautomer | Type of CIDs to return, given CIDs |
| list\_return | grouped, flat, listkey | Type of identifier list to return |
| sourcename | (any substance source) | For SIDs by name only, restrict to source |

Examples:

<https://pubchem.ncbi.nlm.nih.gov/rest/pug/substance/name/glucose/sids/XML>

<https://pubchem.ncbi.nlm.nih.gov/rest/pug/substance/name/glucose/sids/XML?list_return=listkey>

<https://pubchem.ncbi.nlm.nih.gov/rest/pug/substance/name/aspirin/sids/JSON?sourcename=ChemIDplus>

<https://pubchem.ncbi.nlm.nih.gov/rest/pug/substance/name/aspirin/sids/JSON?sourcename=ChemIDplus&name_type=word>

<https://pubchem.ncbi.nlm.nih.gov/rest/pug/substance/listkey/xxxxxx/sids/XML> (where ‘xxxxxx’ is the listkey from the above URL)

<https://pubchem.ncbi.nlm.nih.gov/rest/pug/substance/name/glucose/cids/XML?list_return=grouped>

<https://pubchem.ncbi.nlm.nih.gov/rest/pug/substance/name/glucose/cids/XML?list_return=flat>

<https://pubchem.ncbi.nlm.nih.gov/rest/pug/substance/sourceall/MLSMR/sids/JSON?list_return=listkey>

<https://pubchem.ncbi.nlm.nih.gov/rest/pug/substance/sourceall/R%26D%20Chemicals/sids/XML?list_return=listkey>

<https://pubchem.ncbi.nlm.nih.gov/rest/pug/substance/sid/123061,123079/cids/XML?cids_type=all>

<https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/2244/sids/JSON>

<https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/inchi/cids/JSON> (where the POST body contains “inchi=InChI=1S/C3H8/c1-3-2/h3H2,1-2H3”)

<https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/192180/cids/TXT?cids_type=component>

<https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/2244/aids/JSON?aids_type=active>

<https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/2244/sids/JSON?sids_type=component>

<https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/2244/cids/TXT?cids_type=same_connectivity>

<https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/21145249/cids/XML?cids_type=parent>

<https://pubchem.ncbi.nlm.nih.gov/rest/pug/assay/aid/1000/sids/XML?sids_type=inactive>

<https://pubchem.ncbi.nlm.nih.gov/rest/pug/assay/aid/504526/sids/JSON?sids_type=doseresponse>

<https://pubchem.ncbi.nlm.nih.gov/rest/pug/assay/type/doseresponse/aids/JSON>

<https://pubchem.ncbi.nlm.nih.gov/rest/pug/assay/sourceall/DTP.NCI/aids/XML>

<https://pubchem.ncbi.nlm.nih.gov/rest/pug/substance/xref/PatentID/EP0711162A1/sids/XML>

<https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/aspirin/cids/XML?name_type=word>

<https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/aspirin/cids/XML?name_type=complete>

<https://pubchem.ncbi.nlm.nih.gov/rest/pug/assay/target/genesymbol/USP2/aids/TXT>

<https://pubchem.ncbi.nlm.nih.gov/rest/pug/assay/target/gi/116516899/aids/JSON>

<https://pubchem.ncbi.nlm.nih.gov/rest/pug/assay/activity/EC50/aids/TXT> (where EC50 is case-sensitive)

### Assay Description

Returns assay descriptions. Valid output formats are XML, JSON(P), and ASNT/B.

Example:

<https://pubchem.ncbi.nlm.nih.gov/rest/pug/assay/aid/450/description/XML>

### Assay Targets

Return assay target information. Valid output formats are XML, JSON(P), ASNT/B, and TXT. Available target types are:

| Target Type | Notes |
| --- | --- |
| ProteinGI | NCBI GI of a protein sequence |
| ProteinName | protein name |
| GeneID | NCBI Gene database identifier |
| GeneSymbol | gene symbol |

Example:

<https://pubchem.ncbi.nlm.nih.gov/rest/pug/assay/aid/490,1000/targets/ProteinGI,ProteinName,GeneID,GeneSymbol/XML>

### Assay Summary

Returns a summary of biological test results for the given SID(s) or
CID(s), including assay experiment information, bioactivity, and target.
Valid output formats are XML, JSON(P), ASNT/B, and CSV.

Examples:

<https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/1000,1001/assaysummary/CSV>

<https://pubchem.ncbi.nlm.nih.gov/rest/pug/substance/sid/104234342/assaysummary/XML>

There is also a per-AID assay summary available in a simplified format. Valid output formats are XML, JSON(P), and ASNT/B.

Example:

<https://pubchem.ncbi.nlm.nih.gov/rest/pug/assay/aid/1000/summary/XML>

### Assay Dose-Response

Returns assay dose-response data for a single AID with up to 1000
SID(s). Valid output formats are XML, JSON(P), ASNT/B, and CSV. A subset
of the SIDs of an assay may be specified as options:

| Option | Allowed Values | Meaning |
| --- | --- | --- |
| sid | listkey, or comma-separated integers | SID rows to retrieve for an assay |
| listkey | valid SID listkey | listkey containing SIDs, if using sid=listkey |

Examples:

<https://pubchem.ncbi.nlm.nih.gov/rest/pug/assay/aid/504526/doseresponse/XML>

<https://pubchem.ncbi.nlm.nih.gov/rest/pug/assay/aid/504526/doseresponse/CSV?sid=104169547,109967232>

<https://pubchem.ncbi.nlm.nih.gov/rest/pug/assay/aid/doseresponse/XML> (with “aid=504526&sid=104169547,109967232” in the POST body)

<https://pubchem.ncbi.nlm.nih.gov/rest/pug/assay/aid/602332/sids/XML?sids_type=doseresponse&list_return=listkey>

followed by

<https://pubchem.ncbi.nlm.nih.gov/rest/pug/assay/aid/602332/doseresponse/CSV?sid=listkey&listkey=xxxxxx&listkey_count=100> (where ‘xxxxxx’ is the listkey returned by the previous URL)

### Gene Summary

Returns a summary of gene: GeneID, Symbol, Name, TaxonomyID,
Taxonomy, Description, and a list of Synonyms. Valid output formats are
XML, JSON(P), and ASNT/B.

Examples:

<https://pubchem.ncbi.nlm.nih.gov/rest/pug/gene/geneid/1956,13649/summary/JSON> (by GeneID)

<https://pubchem.ncbi.nlm.nih.gov/rest/pug/gene/genesymbol/EGFR/summary/XML> (by genesymbol, case-insensitive and default to human)

<https://pubchem.ncbi.nlm.nih.gov/rest/pug/gene/genesymbol/EGFR/10090/summary/JSON> (mouse with NCBI TaxonomyID 9606)

<https://pubchem.ncbi.nlm.nih.gov/rest/pug/gene/genesymbol/EGFR/Rattus%20norvegicus/summary/JSON> (mouse with scientific taxonomy name)

<https://pubchem.ncbi.nlm.nih.gov/rest/pug/gene/genesymbol/EGFR/Norway%20rat/summary/JSON> (mouse with common taxonomy name)

<https://pubchem.ncbi.nlm.nih.gov/rest/pug/gene/synonym/EGFR/summary/JSON> (by synonym, note that one synonym may map to multiple GeneIDs)

Please check [PUG REST Tutorial](https://pubchem.ncbi.nlm.nih.gov/docs/pug-rest-tutorial#section=Access-to-PubChem-Genes) for a complete list of available data and more examples.

### Protein Summary

Returns a summary of protein: ProteinAccession, Name, TaxonomyID,
Taxonomy, and a list of Synonyms. Valid output formats are XML, JSON(P),
and ASNT/B.

Examples:

<https://pubchem.ncbi.nlm.nih.gov/rest/pug/protein/accession/P00533,P01422/summary/JSON>

Please check [PUG REST Tutorial](https://pubchem.ncbi.nlm.nih.gov/docs/pug-rest-tutorial#section=Access-to-PubChem-Proteins) for a complete list of available data and more examples.

### Pathway Summary

Returns a summary of pathway: PathwayAccession, SourceName, SourceID,
SourceURL, Name, Type, Category, Description, TaxonomyID, and Taxonomy.
Valid output formats are XML, JSON(P), and ASNT/B.

Examples:

<https://pubchem.ncbi.nlm.nih.gov/rest/pug/pathway/pwacc/Reactome:R-HSA-70171,BioCyc:HUMAN_PWY-4983/summary/JSON>

Please check [PUG REST Tutorial](https://pubchem.ncbi.nlm.nih.gov/docs/pug-rest-tutorial#section=Access-to-PubChem-Pathways) for a complete list of available data and more examples.

### Taxonomy Summary

Returns a summary of taxonomy: TaxonomyID, ScientificName,
CommonName, Rank, RankedLineage, and a list of Synonyms. Valid output
formats are XML, JSON(P), and ASNT/B.

Examples:

<https://pubchem.ncbi.nlm.nih.gov/rest/pug/taxonomy/taxid/9606,10090,10116/summary/JSON>

Please check [PUG REST Tutorial](https://pubchem.ncbi.nlm.nih.gov/docs/pug-rest-tutorial#section=Access-to-PubChem-Taxonomies) for a complete list of available data and more examples.

### Cell Line Summary

Returns a summary of taxonomy: CellAccession, Name, Sex, Category,
SourceTissue, SourceTaxonomyID, SourceOrganism, and a list of Synonyms.
Valid output formats are XML, JSON(P), and ASNT/B.

Examples:

<https://pubchem.ncbi.nlm.nih.gov/rest/pug/cell/cellacc/CVCL_0030,CVCL_0045/summary/JSON> (by [Cellosaurus](https://web.expasy.org/cellosaurus/) cell line accession)

<https://pubchem.ncbi.nlm.nih.gov/rest/pug/cell/synonym/HeLa/summary/JSON> (by synonym)

Please check [PUG REST Tutorial](https://pubchem.ncbi.nlm.nih.gov/docs/pug-rest-tutorial#section=Access-to-PubChem-Cell-Lines) for a complete list of available data and more examples.

### Classification

Returns the nodes in the classification tree for a single SID, CID, or AID. Valid output formats are XML, JSON(P), and ASNT/B.

Example:

<https://pubchem.ncbi.nlm.nih.gov/rest/pug/substance/sid/1917/classification/XML>

### Dates

Returns dates associated with PubChem identifiers; note that not all
date types are relevant to all identifier types – see the table below.
Multiple date types may be requested. Valid output formats are XML,
JSON(P), and ASNT/B. Options are:

| Option | Allowed Values (default in bold) | Meaning |
| --- | --- | --- |
| dates\_type | **deposition** | when an SID or AID first appeared |
| modification | when an SID or AID was last modified |  |
| hold | when an SID or AID will be released |  |
| **creation** | when a CID first appeared |  |

Examples:

<https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/2244/dates/JSON>

<https://pubchem.ncbi.nlm.nih.gov/rest/pug/substance/sid/1,2,3,135653256/dates/XML?dates_type=modification,deposition,hold>

<https://pubchem.ncbi.nlm.nih.gov/rest/pug/assay/aid/1,624113/dates/XML?dates_type=deposition,hold>

### XRefs

Returns cross-references associated with PubChem SIDs or CIDs.
Multiple types may be requested in a comma-separated list in the URL
path. Valid output formats are XML, JSON(P), ASNT/B, and TXT (limited to
a single type). Available cross-references are:

| Cross-reference | Meaning |
| --- | --- |
| RegistryID | external registry identifier |
| RN | registry number |
| PubMedID | NCBI PubMed identifier |
| MMDBID | NCBI MMDB identifier |
| DBURL | external database home page URL |
| SBURL | external database substance URL |
| ProteinGI | NCBI protein GI |
| NucleotideGI | NCBI nucleotide GI |
| TaxonomyID | NCBI taxonomy identifier |
| MIMID | NCBI MIM identifier |
| GeneID | NCBI gene identifier |
| ProbeID | NCBI probe identifier |
| PatentID | patent identifier |
| SourceName | external depositor name |
| SourceCategory | depositor category(ies) |

Examples:

<https://pubchem.ncbi.nlm.nih.gov/rest/pug/substance/sid/127378063/xrefs/PatentID/XML>

<https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/vioxx/xrefs/RegistryID,RN,PubMedID/JSONP>

<https://pubchem.ncbi.nlm.nih.gov/rest/pug/substance/sourceall/ChEBI/xrefs/RegistryID/JSON>

### Conformers

A list of diverse order conformer IDs can be obtained from CID. Valid
output formats are XML, JSON(P), ASNT/B, and TXT (limited to a single
CID):

<https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/2244/conformers/XML>

Individual conformer records – either computed 3D coordinates for
compounds or deposited/experimental 3D coordinates for some substances –
can be retrieved by conformer ID:

<https://pubchem.ncbi.nlm.nih.gov/rest/pug/conformers/000008C400000001/SDF>

## Structure Search Operations

### Substructure / Superstructure

This is a special type of compound namespace input that retrieves
CIDs by substructure or superstructure search. It requires a CID, or a
SMILES, InChI, or SDF string in the URL path or POST body (InChI and SDF
by POST only). Valid output formats are XML, JSON(P), and ASNT/B.

Example:

[https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/fastsubstructure/smiles/C3=NC1=C(C=NC2=C1C=NC=C2)[N]3/cids/XML](https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/fastsubstructure/smiles/C3=NC1=C(C=NC2=C1C=NC=C2)%5BN%5D3/cids/XML)

`https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/
fastsubstructure/inchi/cids/XML (where the POST body contains
“inchi=InChI=1S/C9H6N4/c1-2-10-3-6-7(1)11-4-8-9(6)13-5-12-8/h1-5H,
(H,12,13)”)`

<https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/fastsuperstructure/cid/2244/cids/XML>

Structure search options are specified via URL arguments:

| Option | Type | Meaning | Default |
| --- | --- | --- | --- |
| MatchIsotopes | boolean | atoms must be of the specified isotope | false |
| MatchCharges | boolean | atoms must match the specified charge | false |
| MatchTautomers | boolean | allow match to tautomers of the given structure (no longer supported) | false |
| RingsNotEmbedded | boolean | rings may not be embedded in a larger system | false |
| SingleDoubleBondsMatch | boolean | single or double bonds match aromatic bonds | true |
| ChainsMatchRings | boolean | chain bonds in the query may match rings in hits | true |
| StripHydrogen | boolean | remove any explicit hydrogens before searching | false |
| Stereo | enum | how to handle stereo; one of ignore, exact, relative, nonconflicting | ignore |
| MaxSeconds | integer | maximum search time in seconds | unlimited |
| MaxRecords | integer | maximum number of hits | 2M |
| listkey | string | restrict to matches within hits from a prior search | none |

Example:

[https://
pubchem.ncbi.nlm.nih.gov/rest/pug/compound/fastsubstructure/smiles/
C1=NC2=C(N1)C(=O)N=C(N2)N/cids/XML?MatchIsotopes=true&MaxRecords=100](https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/fastsubstructure/smiles/C1=NC2=C(N1)C(=O)N=C(N2)N/cids/XML?MatchIsotopes=true&MaxRecords=100)

### Similarity

This is a special type of compound namespace input that retrieves
CIDs by 2D similarity search. It requires a CID, or a SMILES, InChI, or
SDF string in the URL path or POST body (InChI and SDF by POST only).
Valid output formats are XML, JSON(P), and ASNT/B.

Example:

<https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/fastsimilarity_2d/cid/2244/cids/XML>

Similarity search options are specified via URL arguments:

| Option | Type | Meaning | Default |
| --- | --- | --- | --- |
| Threshold | integer | minimum Tanimoto score for a hit | 90 |
| MaxSeconds | integer | maximum search time in seconds | unlimited |
| MaxRecords | integer | maximum number of hits | 2M |
| listkey | string | restrict to matches within hits from a prior search | none |

Example:

[https://
pubchem.ncbi.nlm.nih.gov/rest/pug/compound/fastsimilarity\_2d/smiles/
C1=NC2=C(N1)C(=O)N=C(N2)N/cids/XML?Threshold=95&MaxRecords=100](https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/fastsimilarity_2d/smiles/C1=NC2=C(N1)C(=O)N=C(N2)N/cids/XML?Threshold=95&MaxRecords=100)

### Identity

This is a special type of compound namespace input that retrieves
CIDs by identity search. It requires a CID, or a SMILES, InChI, or SDF
string in the URL path or POST body (InChI and SDF by POST only). Valid
output formats are XML, JSON(P), and ASNT/B.

Example:

<https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/fastidentity/smiles/CCCCC/cids/XML>

Identity search options are specified via URL arguments:

| Option | Type | Values / Meaning | Default |
| --- | --- | --- | --- |
| identity\_type | string | same\_connectivity, same\_tautomer, same\_stereo, same\_isotope, same\_stereo\_isotope, nonconflicting\_stereo, same\_isotope\_nonconflicting\_stereo | same\_stereo\_isotope |
| MaxSeconds | integer | maximum search time in seconds | unlimited |
| MaxRecords | integer | maximum number of hits | 2M |
| listkey | string | restrict to matches within hits from a prior search | none |

Example:

[https://
pubchem.ncbi.nlm.nih.gov/rest/pug/compound/fastidentity/smiles/
C1=NC2=C(N1)C(=O)N=C(N2)N/cids/XML?identity\_type=same\_isotope](https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/fastidentity/smiles/C1=NC2=C(N1)C(=O)N=C(N2)N/cids/XML?identity_type=same_isotope)

### Molecular Formula

This is a special type of compound namespace input that retrieves
CIDs by molecular formula search. It requires a formula string in the
URL path. Valid output formats are XML, JSON(P), and ASNT/B.

Example:

<https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/fastformula/C10H21N/cids/XML>

Search options are specified via URL arguments:

| Option | Type | Meaning | Default |
| --- | --- | --- | --- |
| AllowOtherElements | boolean | Allow other elements to be present in addition to those specified | false |
| MaxSeconds | integer | maximum search time in seconds | unlimited |
| MaxRecords | integer | maximum number of hits | 2M |
| listkey | string | restrict to matches within hits from a prior search | none |

Example:

<https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/fastformula/C10H21N/cids/JSON?AllowOtherElements=true&MaxRecords=10>

### Search Within a Search

The synchronous ("fast...") searches can use a prior result set to
restrict results, using "cachekey" (a hit list storage system on the
server side). For example, if you want to look for compounds that have
the formula C6H12O and contain a six-membered carbon ring, first do the
formula search with cachekey result:

<https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/fastformula/C6H12O/cids/JSON?list_return=cachekey>

This will produce something like:

```
{

"IdentifierList": {

"Size": 692,

"CacheKey": "is0tv08FKrkdkyiKqvJhpCDDO6PtouNSmXf4HoJm6h-Cf9Y"

}

}

```

Use that cache key string as input to a substructure search this way:

[https://
pubchem.ncbi.nlm.nih.gov/rest/pug/compound/fastsubstructure/smiles/
C1CCCCC1/cids/JSON?cachekey=is0tv08FKrkdkyiKqvJhpCDDO6PtouNSmXf4HoJm6h-
Cf9Y](https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/fastsubstructure/smiles/C1CCCCC1/cids/JSON?cachekey=is0tv08FKrkdkyiKqvJhpCDDO6PtouNSmXf4HoJm6h-Cf9Y)

This will limit the substructure search to just those compounds found
by the formula search. Note that it is important to do the more
restrictive search first; a search that is too broad (like looking for
substructure C1CCCCC1 across all compounds), and that results in many
millions of hits, will take too long to process and will time out.

### Asynchronous (polled) Search Inputs

While these are deprecated and use of these operations is not
recommended, historically, PubChem used queued services for structure
searches, which involved an initial request that returns a "listkey",
which should followed by another request with that listkey that may
return a waiting message, or the final result, for example:

<https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/listkey/xxxxx/cids/XML> (where ‘xxxxx’ is the ListKey returned in the prior search request)

Examples:

<https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/substructure/cid/2244/cids/XML?StripHydrogen=true>

<https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/identity/cid/5793/cids/TXT?identity_type=same_connectivity>

<https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/similarity_2d/cid/2244/cids/XML?Threshold=99>

<https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/similarity_3d/cid/2244/cids/JSON>

<https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/formula/C6H12O/cids/XML>

## Other Inputs

These are special input domains that do not deal with lists of
PubChem record identifiers; regular operations are not possible with
these inputs.

### Source Names

Returns a list of all current depositors (sources) of substances or assays. Valid output formats are XML, JSON(P), and ASNT/B.

Examples:

<https://pubchem.ncbi.nlm.nih.gov/rest/pug/sources/substance/XML>

<https://pubchem.ncbi.nlm.nih.gov/rest/pug/sources/assay/JSONP>

### Source Table

A more complete table of source information, including organization
names and record counts is available for both substances and assays.
Valid output formats are CSV, XML, JSON(P), and ASNT/B.

<https://pubchem.ncbi.nlm.nih.gov/rest/pug/sourcetable/substance/JSON>

<https://pubchem.ncbi.nlm.nih.gov/rest/pug/sourcetable/assay/CSV>

### Classification Nodes

This is a simplified interface to retrieve lists of identifiers from classification nodes. It uses the general syntax:

`https://pubchem.ncbi.nlm.nih.gov/rest/pug/classification/hnid/<integer>/<id type>/<format>`

The HNID integer can be obtained from the classification browser, and
is the identifier for a specific classification node. The output
identifier type is case-insensitive and must be one of: cid, compound;
sid, substance; aid, bioassay; patent; pmid, pubmedid; doi; gene,
geneid; protein; taxonomy, taxonomyid; pathway, pathwayid; disease,
diseaseid; or cell, cellid. Note that the plural form is also accepted,
e.g. "cid" or "cids". The list can also be retrieved as a cache key
(but, note, not as a list key). Valid formats are TXT, XML, JSON(P), and
ASNT/B.

For example:

<https://pubchem.ncbi.nlm.nih.gov/rest/pug/classification/hnid/1857282/cids/TXT>

<https://pubchem.ncbi.nlm.nih.gov/rest/pug/classification/hnid/1857282/cids/XML?list_return=cachekey>

<https://pubchem.ncbi.nlm.nih.gov/rest/pug/classification/hnid/4501233/patents/JSON>

### Periodic Table

A summary of the data used to populate [PubChem's periodic table page](https://pubchem.ncbi.nlm.nih.gov/periodic-table/) can be retrieved through PUG REST:

<https://pubchem.ncbi.nlm.nih.gov/rest/pug/periodictable/JSON>

### Standardize

This will return the standardized form of the user input, which can
be SMILES, InChI, or SDF. Components and neutralized forms are included
by default, unless "include\_component=false" is specified.
Valid output formats are SDF, XML, JSON(P), and ASNT/B.

For example:

<https://pubchem.ncbi.nlm.nih.gov/rest/pug/standardize/smiles/CCCC/SDF>

[https://pubchem.ncbi.nlm.nih.gov/rest/pug/standardize/smiles/CC(=O)[O-]/SDF](https://pubchem.ncbi.nlm.nih.gov/rest/pug/standardize/smiles/CC(=O)%5BO-%5D/SDF)

[https://pubchem.ncbi.nlm.nih.gov/rest/pug/standardize/smiles/CC(=O)[O-]/SDF?include\_components=false](https://pubchem.ncbi.nlm.nih.gov/rest/pug/standardize/smiles/CC(=O)%5BO-%5D/SDF?include_components=false)

## Other Options

### Pagination

When retrieving identifiers by listkey, the listkey\_start and
listkey\_count options indicate at what index (zero-based) in the list to
begin retrieval, and how many identifiers to return, respectively.

Example:

<https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/1,2,3,4,5/cids/XML?list_return=listkey>

followed by:

`https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/listkey/
xxxxxx/cids/XML?listkey_start=2&listkey_count=2 where ‘xxxxxx’ is
the listkey returned by the first URL, will return a list containing
(only) CIDs 3 and 4.`

## Example Scripts

The following zip file contains example perl scripts demonstrating how to access PubChem data through PUG-REST.

[pug\_rest\_scripts\_nar\_2018.zip](https://ftp.ncbi.nlm.nih.gov/pubchem/publications/pug_rest_scripts_nar_2018.zip)

These scripts were prepared as a supplementary material of the following paper:

> > Kim S, Thiessen PA, Cheng T, Yu B, and Bolton EE. An Update on
> > PUG-REST: RESTful Interface for programmatic access to PubChem. Nucleic
> > Acids Res 2018; gky294. Epub 2018 Apr 30. doi: [10.1093/nar/gky294](https://dx.doi.org/10.1093/nar/gky294).
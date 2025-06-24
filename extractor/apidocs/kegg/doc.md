KEGG API Manual

## [kegg3 logo](https://www.kegg.jp/kegg/rest/)  KEGG API Manual

[KEGG API](https://www.kegg.jp/kegg/rest/) is a REST-style Application Programming Interface to the KEGG database resource.

---

#### General form

**URL form**

```
https://rest.kegg.jp/<operation>/<argument>[/<argument2[/<argument3> ...]]

<operation> = info | list | find | get | conv | link | ddi
```

**Database name**

```
<database> = KEGG databases (Table 1) and Outside databases integrated in KEGG (Table 2)

= pathway | brite | module | ko | <org> | vg | vp | ag | genome | compound |
drug | dgroup | disease_ja | drug_ja | dgroup_ja | compound_ja |
genes | ligand | kegg | <outside_db>

<org> = KEGG organism code

<outside_db> = pubmed | ncbi-geneid | ncbi-proteinid | uniprot | pubchem | chebi |
atc | jtc | ndc | yj
```

**Database entry identifier**

```
<dbentry> = <kid> | <org>:<gene> | <database>:<entry>

<kid> = KEGG identifier
<gene> = Gene entry name or accession
<entry> = Database entry name or accession

<dbentries> = <dbentry>1[+<dbentry>2...]

```

#### Naming conventions

KEGG is an integrated database consisting of sixteen databases
(including four Japanese versions) shown in Table 1. Except for "genes",
"enzyme" and "variant", each database entry is identified by the KEGG
identifier <kid> consisting of a database-dependent prefix
followed by a five-digit number (see [KEGG Objects](https://www.kegg.jp/kegg/kegg3.html)
for more details), such as K number, C number and D numbers as
identifiers of "ko", "compound" and "drug" databases, respectively.

A "genes" entry is identified by

<org>:<gene>

where <org> is the three- or four-letter KEGG organism code or the
T number genome identifier and <gene> is the gene identifier,
usually NCBI GeneID or INSDC Locus\_tag (see [KEGG GENES](https://www.kegg.jp/kegg/genes.html)).

An "enzyme" entry, a "variant" entry or an entry of any outside database is identified by

<database>:<entry>

where <database> is the database name or its abbreviation defined
in Tables 1-2 and <entry> is the entry name or the accession
number given by the database.

Table 1. KEGG databases

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  |  |  |  | | --- | --- | --- | --- | --- | | DB name | Abbrev | Content | Web page | kid prefix | | --- | | | | | | pathway | path | KEGG pathway maps | [KEGG PATHWAY](https://www.kegg.jp/kegg/pathway.html) | map, ko, ec, rn, <org> | | brite | br | BRITE functional hierarchies | [KEGG BRITE](https://www.kegg.jp/kegg/brite.html) | br, jp, ko, <org> | | module | md | KEGG modules | [KEGG MODULE](https://www.kegg.jp/kegg/module.html) | M, <org>\_M | | orthology | ko | KO functional orthologs | [KEGG ORTHOLOGY](https://www.kegg.jp/kegg/ko.html) | K | | genes | <org> vg vp ag | Genes in KEGG organisms Genes in viruses category Mature peptides in viruses Genes in addendum category | [KEGG GENES](https://www.kegg.jp/kegg/genes.html) | - | | genome | gn | KEGG organisms | [KEGG GENOME](https://www.kegg.jp/kegg/genome.html) | T | | compound | cpd | Small molecules | [KEGG COMPOUND](https://www.kegg.jp/kegg/compound/) | C | | glycan | gl | Glycans | [KEGG GLYCAN](https://www.kegg.jp/kegg/glycan/) | G | | reaction | rn | Biochemical reactions | [KEGG REACTION](https://www.kegg.jp/kegg/reaction/) | R | | rclass | rc | Reaction class |  | RC | | enzyme | ec | Enzyme nomenclature | [KEGG ENZYME](https://www.kegg.jp/kegg/annotation/enzyme.html) | - | | network | ne | Network elements | [KEGG NETWORK](https://www.kegg.jp/kegg/network.html) | N | | variant | hsa\_var | Human gene variants |  | - | | disease | ds | Human diseases | [KEGG DISEASE](https://www.kegg.jp/kegg/disease/) | H | | drug | dr | Drugs | [KEGG DRUG](https://www.kegg.jp/kegg/drug/) | D | | dgroup | dg | Drug groups |  | DG | | --- | | | | | | disease\_ja | ds\_ja | H number | [KEGG DISEASE](https://www.kegg.jp/kegg/disease/disease_ja.html) (in Japanese) | | | drug\_ja | dr\_ja | D number | [KEGG DRUG](https://www.kegg.jp/kegg/drug/drug_ja.html) (in Japanese) | | | dgroup\_ja | dg\_ja | DG number |  | | | compound\_ja | cpd\_ja | C number |  | | |

- "genes" is a composite database consisting of KEGG organisms with
three- or four-letter <org> codes, and viruses (vg, vp) and
addendum (ag) categories (see [KEGG GENES](https://www.kegg.jp/kegg/genes.html)).
- "pathway", "brite" and "module" consist of manually created
reference datasets and computationally generated organism-specific
datasets (see [KEGG Pathway Maps](https://www.kegg.jp/kegg/kegg3a.html)).
- "kegg" stands for the collection of all databases shown above.
- "ligand" stands for the collection of chemical databases: compound, glycan, reaction and enzyme.

In addition to these databases, the NCBI PubMed database shown in Table 2
is tightly integrated in KEGG. Table 2 also contains databases used
only for ID conversion (conv operation) or links (link operation).

Table 2. Outside databases integrated in KEGG

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  |  |  |  | | --- | --- | --- | --- | --- | | DB name | Abbrev | Entry ID | Web page | Remark | | --- | | | | | | pubmed | pmid | PubMed ID | [NCBI PubMed](https://pubmed.ncbi.nlm.nih.gov/) |  | | ncbi-geneid |  | Gene ID | [NCBI Gene](https://www.ncbi.nlm.nih.gov/gene/) | conv only | | ncbi-proteinid |  | Protein ID | [NCBI Protein](https://www.ncbi.nlm.nih.gov/protein/) | conv only | | uniprot | up | UniProt Accession | [UniProt](https://www.uniprot.org/) | conv only | | pubchem |  | PubChem SID | [NCBI PubChem](https://www.ncbi.nlm.nih.gov/pubchem/) | conv only | | chebi |  | ChEBI ID | [ChEBI](https://www.ebi.ac.uk/chebi/) | conv only | |  | atc | 7-letter ATC code | [ATC classification](https://www.kegg.jp/brite/br08303) | link only | |  | jtc | Therapeutic category code | [Therapeutic category in Japan](https://www.kegg.jp/brite/br08301) | link only | |  | ndc | National Drug Code | Drug products in the USA | ddi only | |  | yj | YJ code | Drug products in Japan | ddi only | |

#### Output

**Output format**

The output of all operations is in a text format:

- tab-delimited text returned from list, find, conv and link
- [flat file database format](https://www.kegg.jp/kegg/docs/dbentry.html) returned from get
- text message returned from info

**Status code**

The HTTP status code can be used to check if the operation was successful.

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| | Code | Meaning | | --- | --- | | 200 | Success | | 400 | Bad request (syntax error, wrong database name, etc.) | | 404 | Not found (e.g., requesting amino acid sequence for RNA) | |

---

## KEGG API Operations

#### INFO

**Name**

info – display database release information and linked db information

**URL form**

```
https://rest.kegg.jp/info/<database>

<database> = kegg | pathway | brite | module | ko | genes | <org> | vg | vp | ag |
network | variant | disease | drug | dgroup
```

**Description**

This operation displays the database release information with statistics
for the databases shown in Table 1. Except for kegg, genes and ligand,
this operation also displays the list of linked databases that can be
used in the link operation.

**Examples**

|  |  |  |
| --- | --- | --- |
| [/info/kegg](https://rest.kegg.jp/info/kegg) |  | displays the current statistics of the KEGG database |
| [/info/pathway](https://rest.kegg.jp/info/pathway) |  | displays the number of pathway entries including both the reference and organism-specific pathways |
| [/info/hsa](https://rest.kegg.jp/info/hsa) |  | displays the number of gene entries for the KEGG organism *Homo sapiens* |

**See also**

[Current statistics](https://www.kegg.jp/kegg/docs/statistics.html) in the KEGG website.

---

#### LIST

**Name**

list – obtain a list of entry identifiers and associated names

**URL form**

```
https://rest.kegg.jp/list/<database>

<database> = pathway | brite | module | ko | <org> | vg | vp | ag | genome | compound |
drug | dgroup | organism
```

```
https://rest.kegg.jp/list/pathway/<org>
```

```
https://rest.kegg.jp/list/brite/<option>

<option> = br | jp | ko | <org>
```

```
https://rest.kegg.jp/list/<dbentries>

<dbentries> = Entries of the following <database>
<database> = pathway | brite | module | ko | <org> | vg | vp | ag | genome | compound |
drug | dgroup
```

**Description**

This operation can be used to obtain a list of all entries in each
database. The database names shown in Tables 1 and 2, excluding the
composite database names of genes, ligand and kegg, may be given. The
special database name "organism" is allowed only in this operation,
which may be used to obtain a list of KEGG organisms with the three- or
four-letter organism codes.

When the organism code is known, the second form can be used to obtain a list of organism-specific pathways.

The third form is a similar option for brite hierarchies.

The fourth form may be used to obtain a list of definitions for a given
set of database entry identifiers. The maximum number of identifiers
that can be given is 10.

**Examples**

|  |  |  |
| --- | --- | --- |
| [/list/pathway](https://rest.kegg.jp/list/pathway) |  | returns the list of reference pathways |
| [/list/pathway/hsa](https://rest.kegg.jp/list/pathway/hsa) |  | returns the list of human pathways |
| [/list/organism](https://rest.kegg.jp/list/organism) |  | returns the list of KEGG organisms with taxonomic classification |
| [/list/hsa](https://rest.kegg.jp/list/hsa) |  | returns the entire list of human genes with gene types and chromosomal positions |
| [/list/T01001](https://rest.kegg.jp/list/T01001) |  | same as above |
| [/list/hsa:10458+ece:Z5100](https://rest.kegg.jp/list/hsa:10458+ece:Z5100) |  | returns the list of a human gene and an E.coli O157 gene |
| [/list/C01290+G00092](https://rest.kegg.jp/list/C01290+G00092) |  | returns the list of a compound entry and a glycan entry |

---

#### FIND

**Name**

find – find entries with matching query keyword or other query data

**URL form**

```
https://rest.kegg.jp/find/<database>/<query>

<database> = pathway | brite | module | ko | genes | <org> | vg | vp | ag | genome |
variant | disease | drug | dgroup
```

```
https://rest.kegg.jp/find/<database>/<query>/<option>

<database> = compound | drug
<option> = formula | exact_mass | mol_weight | nop
```

**Description**

This is a search operation. The first form searches entry identifier and associated fields shown below for matching keywords.

| Database | Text search fields (see [flat file format](https://www.kegg.jp/kegg/rest/dbentry.html)) |
| --- | --- |
| pathway | ENTRY and NAME |
| brite | ENTRY and NAME |
| module | ENTRY and NAME |
| ko | ENTRY, SYMBOL and NAME |
| genes (<org>, vg, vp, ag) | ENTRY, SYMBOL, NAME and KO |
| genome | ENTRY, ORG\_CODE and NAME |
| compound | ENTRY and NAME |
| glycan | ENTRY, NAME and COMPOSITION |
| reaction | ENTRY, NAME and DEFINITION |
| enzyme | ENTRY and NAME |
| network | ENTRY and NAME |
| variant | ENTRY and NAME |
| disease | ENTRY and NAME |
| drug | ENTRY and NAME |
| dgroup | ENTRY and NAME |

In the second form the chemical formula search is a partial match
irrespective of the order of atoms given. The exact mass (or molecular
weight) is checked by rounding off to the same decimal place as the
query data. A range of values may also be specified with the minus(-)
sign.

**Examples**

|  |  |  |
| --- | --- | --- |
| [/find/genes/shiga+toxin](https://rest.kegg.jp/find/genes/shiga+toxin) |  | for keywords "shiga" and "toxin" (use nop option to disable this processing) |
| [/find/genes/"shiga toxin"](https://rest.kegg.jp/find/genes/shiga%20toxin) |  | for keywords "shiga toxin" |

|  |  |  |
| --- | --- | --- |
| [/find/compound/C7H10O5/formula](https://rest.kegg.jp/find/compound/C7H10O5/formula) |  | for chemical formula "C7H10O5" |
| [/find/compound/O5C7/formula](https://rest.kegg.jp/find/compound/O5C7/formula) |  | for chemical formula containing "O5" and "C7" |
| [/find/compound/174.05/exact\_mass](https://rest.kegg.jp/find/compound/174.05/exact_mass) |  | for 174.045 =< exact mass < 174.055 |
| [/find/compound/300-310/mol\_weight](https://rest.kegg.jp/find/compound/300-310/mol_weight) |  | for 300 =< molecular weight =< 310 |

**See also**

DBGET search interface such as in the [KEGG Table of Contents](https://www.kegg.jp/kegg/kegg2.html) page.

---

#### GET

**Name**

get – retrieve given database entries

**URL form**

```
https://rest.kegg.jp/get/<dbentries>[/<option>]

<dbentries> = KEGG database entries of the following <database>
<database> = pathway | brite | module | ko | <org> | vg | vp | ag | genome | compound |
drug | dgroup | disease_ja | drug_ja | dgroup_ja | compound_ja

<option> = aaseq | ntseq | mol | kcf | image | conf | kgml | json
```

**Description**

This operation retrieves given database entries in a flat file format or
in other formats with options. Flat file formats are available for all
KEGG databases except brite. The input is limited up to 10 entries.

Options allow retrieval of selected fields, including sequence data from
genes entries, chemical structure data or gif image files from
compound, glycan and drug entries, png image files or kgml files from
pathway entries. The input is limited to one compound/glycan/drug entry
with the image option, and to one pathway entry with the image or kgml
option.

**Examples**

|  |  |  |
| --- | --- | --- |
| [/get/C01290+G00092](https://rest.kegg.jp/get/C01290+G00092) |  | retrieves a compound entry and a glycan entry |
| [/get/hsa:10458+ece:Z5100](https://rest.kegg.jp/get/hsa:10458+ece:Z5100) |  | retrieves a human gene entry and an E.coli O157 gene entry |
| [/get/hsa:10458+ece:Z5100/aaseq](https://rest.kegg.jp/get/hsa:10458+ece:Z5100/aaseq) |  | retrieves amino acid sequences of a human gene and an E.coli O157 gene |
| [/get/C00002/image](https://rest.kegg.jp/get/C00002/image) |  | retrieves the gif image file of a compound |
| [/get/hsa00600/image](https://rest.kegg.jp/get/hsa00600/image) |  | retrieves the png image file of a pathway map |
| [/get/map00600/image2x](https://rest.kegg.jp/get/map00600/image2x) |  | retrieves the doubled-sized png image file of a reference pathway map New! |
| [/get/hsa00600/conf](https://rest.kegg.jp/get/hsa00600/conf) |  | retrieves the conf file of a pathway map |
| [/get/hsa00600/kgml](https://rest.kegg.jp/get/hsa00600/kgml) |  | retrieves the kgml file of a pathway map |
| [/get/br:br08301](https://rest.kegg.jp/get/br:br08301) |  | retrieves the htext file of a brite hierarchy |
| [/get/br:br08301/json](https://rest.kegg.jp/get/br:br08301/json) |  | retrieves the json file of a brite hierarchy |

**See also**

[KEGG WebLinks](https://www.kegg.jp/kegg/rest/weblink.html) to retrieve entries in HTML.

---

#### CONV

**Name**

conv – convert KEGG identifiers to/from outside identifiers

**URL form**

```
https://rest.kegg.jp/conv/<target_db>/<source_db>

(<target_db> <source_db>) = (<kegg_db> <outside_db>) | (<outside_db> <kegg_db>)

For gene identifiers:
<kegg_db> = <org>
<org> = KEGG organism code or T number
<outside_db> = ncbi-geneid | ncbi-proteinid | uniprot

For chemical substance identifiers:
<kegg_db> = compound | glycan | drug
<outside_db> = pubchem | chebi
```

```
https://rest.kegg.jp/conv/<target_db>/<dbentries>

For gene identifiers:
<dbentries> = database entries of the following <database>
<database> = <org> | genes | ncbi-geneid | ncbi-proteinid | uniprot
<org> = KEGG organism code or T number

For chemical substance identifiers:
<dbentries> = database entries of the following <database>
<database> = compound | glycan | drug | pubchem | chebi
```

**Description**

This operation can be used to convert entry identifiers (accession
numbers) of outside databases to KEGG identifiers, and vice versa. The
first form allows database to database mapping, while the second form
allows conversion of a selected number of entries. The database name
"genes" may be used only in the second form.

**Examples**

|  |  |  |
| --- | --- | --- |
| [/conv/eco/ncbi-geneid](https://rest.kegg.jp/conv/eco/ncbi-geneid) |  | conversion from NCBI GeneID to KEGG ID for E. coli genes |
| [/conv/ncbi-geneid/eco](https://rest.kegg.jp/conv/ncbi-geneid/eco) |  | opposite direction |
| [/conv/ncbi-proteinid/hsa:10458+ece:Z5100](https://rest.kegg.jp/conv/ncbi-proteinid/hsa:10458+ece:Z5100) |  | conversion from KEGG ID to NCBI ProteinID |
| [/conv/genes/ncbi-geneid:948364](https://rest.kegg.jp/conv/genes/ncbi-geneid:948364) |  | conversion from NCBI GeneID to KEGG ID when the organism code is not known |

**See also**

[Convert ID](https://www.kegg.jp/kegg/tool/conv_id.html) tool in [KEGG Mapper](https://www.kegg.jp/kegg/mapper.html).

---

#### LINK

**Name**

link – find related entries by using database cross-references

**URL form**

```
https://rest.kegg.jp/link/<target_db>/<source_db>

<target_db> = <database>
<source_db> = <database>

<database> = pathway | brite | module | ko | <org> | vg | vp | ag | genome | compound |
drug | dgroup | <outside_db>
<outside_db> = pubmed | atc | jtc
```

```
https://rest.kegg.jp/link/<target_db>/<dbentries>

<dbentries> = KEGG database entries of the following <database>
<database> = pathway | brite | module | ko | <org> | vg | vp | ag | genome | compound |
drug | dgroup | <outside_db>
<outside_db> = pubmed | atc | jtc
```

**Description**

This operation allows retrieval of cross-references within all KEGG
databases, as well as between KEGG databases and outside databases. It
is useful for finding various relationships, such as relationships
between genes and pathways. The first form allows retrieval of database
to database cross-references, while the second form allows retrieval for
a selected number of entries. The database name "genes" may be used
only for "ko" entries in the second form.

**Examples**

|  |  |  |
| --- | --- | --- |
| [/link/pathway/hsa](https://rest.kegg.jp/link/pathway/hsa) |  | KEGG pathways linked from each of the human genes |
| [/link/hsa/pathway](https://rest.kegg.jp/link/hsa/pathway) |  | human genes linked from each of the KEGG pathways |
| [/link/pathway/hsa:10458+ece:Z5100](https://rest.kegg.jp/link/pathway/hsa:10458+ece:Z5100) |  | KEGG pathways linked from a human gene and an E. coli O157 gene |
| [/link/genes/K00500](https://rest.kegg.jp/link/genes/K00500) |  | List of genes with the KO assignment of K00500 |
| [/link/hsa/hsa00010](https://rest.kegg.jp/link/hsa/hsa00010) |  | List of human genes in pathway hsa00010 |
| [/link/ko/map00010](https://rest.kegg.jp/link/ko/map00010) or [/link/ko/ko00010](https://rest.kegg.jp/link/ko/ko00010) |  | List of KO entries in pathway map00010 or ko00010 |
| [/link/rn/map00010](https://rest.kegg.jp/link/rn/map00010) or [/link/rn/rn00010](https://rest.kegg.jp/link/rn/rn00010) |  | List of reaction entries in pathway map00010 or rn00010 |
| [/link/ec/map00010](https://rest.kegg.jp/link/ec/map00010) or [/link/ec/ec00010](https://rest.kegg.jp/link/ec/ec00010) |  | List of EC number entries in pathway map00010 or ec00010 |
| [/link/cpd/map00010](https://rest.kegg.jp/link/cpd/map00010) |  | List of compound entries in pathway map00010 |

---

#### DDI

**Name**

ddi – find adverse drug-drug interactions

**URL form**

```
https://rest.kegg.jp/ddi/<dbentry>

<dbentry> = Single entry of the following <database>
<database> = drug | ndc | yj
```

```
https://rest.kegg.jp/ddi/<dbentries>

<dbentries> = Multiple entries in one of the following <database>
<database> = drug | ndc | yj
```

**Description**

This operation searches against the KEGG drug interaction database,
where drug-drug interactions designated as contraindication (CI) and
precaution (P) in Japanese drug labels are extracted, standardized by
KEGG identifiers and annotated with any possible molecular mechanims.
The first form reports all known interactions, while the second form can
be used to check if any drug pair in a given set of drugs is CI or P.

**Examples**

|  |  |  |
| --- | --- | --- |
| [/ddi/D00564](https://rest.kegg.jp/ddi/D00564) |  | drugs that are known to interact with a given drug |
| [/ddi/D00564+D00100+D00109](https://rest.kegg.jp/ddi/D00564+D00100+D00109) |  | check if drug-drug interactions are present among given drugs |
| [/ddi/ndc:0078-0401](https://rest.kegg.jp/ddi/ndc:0078-0401) |  | drug products that are known to interact with Gleevec |

**See also**

[Drug Interaction Checker](https://www.kegg.jp/medicus-bin/select_drug?lang=en) tool in [KEGG MEDICUS](https://www.kegg.jp/kegg/medicus.html).

---

---

#### LINK (with RDF option)

**Name**

link – find related entries by using database cross-references

**URL form**

```
https://rest.kegg.jp/link/<target_db>/<source_db>[/<option>]

<target_db> = <database>
<source_db> = <database>

<database> = drug | atc | jtc

<option> = turtle | n-triple
```

```
https://rest.kegg.jp/link/<target_db>/<dbentries>[/<option>]

<dbentries> = KEGG database entries of the following <database>
<database> = drug | atc | jtc

<option> = turtle | n-triple
```

**Description**

This operation allows retrieval of cross-references within a few
selected databases. The first form allows retrieval of database to
database cross-references, while the second form allows retrieval for a
selected number of entries.

**Examples**

|  |  |  |
| --- | --- | --- |
| [/link/atc/D01441/n-triple](https://rest.kegg.jp/link/atc/D01441/n-triple) |  | ATC code of a given KEGG DRUG entry in N-Triples format |
| [/link/jtc/D01441/turtle](https://rest.kegg.jp/link/jtc/D01441/turtle) |  | Japanese therapeutic category of a given KEGG DRUG entry in Turtle format |

---

*Last updated: May 26, 2023*

[« Back](javascript:history.back())
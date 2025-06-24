UniLectin interactive lectin database

# UniLectin exploration platform and database for curated and predicted lectin carbohydrate binding proteins

Unilectin-API
The present page lists the endpoints available for UniLectin API.
Click on any of the links to show the documentation of the concerned endpoint and some usage examples.

api/getlectins

Description

This endpoint enables to perform queries on UniLectin3D's **lectin** table.
It retrieves the content of the specified column(s) (**getcolumns**) where another column (**wherecolumn**) has a specific value (**isvalue**).

The available columns for this table are:

- **lectin.lectin\_id**: UniLectin3D's lectin ID, e.g. 1000
- **pdb**: PDB ID, e.g. 2CY6
- **fold**: Lectin fold, e.g. b-sandwich / ConA-like
- **class**: Lectin class, e.g. L-type (legume lectin)
- **family**: Lectin family, e.g. ConA and related
- **origin**: Lectin origin, e.g. Plant lectins
- **species**: lectin species
- **species\_id**: e.g. 380
- **resolution**: Structure resolution, e.g. 2
- **uniprot**: UniProt ID, e.g. P81460
- **protein\_name**: Common protein name, e.g. Concanavalin-A (Con A)
- **ligand**: Trehalose
- **monosac**: Monosaccharide, e.g. D-Glcp
- **iupac**: Ligand's IUPAC, e.g. Glc(a1-1)Glc
- **glycoct**: Ligand's GlycoCT
- **glytoucan\_id**: Ligand's GlyTouCan ID, e.g. G10543DQ

Parameters

- **getcolumn**: string of the column(s) to be fetched (one or multiple columns, separated by comma)
- **wherecolumn**: string of the conditional column
- **isvalue**: string of the value to be matched in **wherecolumn** (here, wildcards are also accepted such as "Rattus%" to match everything starting with ",Rattus",)
- **limit**: (optional) integer of the number of results to be returned (default: 1000, -1 for all)

Examples

- Get all the binding domain IDs (PDB) and their UniProt IDs:

Try this query
{ "getcolumns": "pdb,uniprot", "wherecolumn": "pdb", "isvalue": "%%" , "limit": "1000"}
- Get the whole predicted lectome of a specific species:

Try this query
{ "getcolumns": "iupac,species", "wherecolumn": "species", "isvalue": "Rattus norvegicus", "limit": "1000"}
- Get all the lectins that have a ligand:

Try this query
{ "getcolumns": "pdb,uniprot", "wherecolumn": "iupac", "isvalue": "VALUE\_NOT\_EMPTY", "limit": "1000"}

Query content

{ "getcolumns": "iupac,species", "wherecolumn": "species", "isvalue": "Rattus norvegicus" }

curl
-X POST "https://unilectin.unige.ch/api/getlectins" -H "accept:
text/plain" -H "Content-Type: application/json" -d " { \"getcolumns\":
\"iupac,species\", \"wherecolumn\": \"species\", \"isvalue\": \"Rattus
norvegicus\" } "

Show raw results

|  |  |
| --- | --- |
|  |  |

api/getlectinspredicted

Description

This endpoint enables to perform queries on the **predicted lectin** table.
It retrieves the content of the specified column(s) (**getcolumns**) where another column (**wherecolumn**) has a specific value (**isvalue**).

The available columns for this table are:

- **uniprot**: Uniprot ID, e.g. P36307
- **protein.protein\_id**: e.g. 6
- **protein.name**: e.g. Outer capsid protein VP4
- **fold**: e.g. b-sandwich ConA-like
- **domains.domains\_id**: e.g. 787209
- **length**: e.g. 772
- **genus**: e.g. Rotavirus
- **gene**: e.g. PYEQ01000096.1
- **gene\_begin**: e.g. 6118
- **gene\_end**: e.g. 11124
- **cluster**: e.g. P35746
- **strain**: e.g. CCP5
- **species**: e.g. Rotavirus A
- **superkingdom**: e.g. Viruses
- **kingdom** e.g. Orthornavirae
- **phylum**: e.g. Duplornaviricota
- **domain**: Lectin class, e.g. Rotavirus spike protein
- **score**: Score of prediction similarity to the reference, from 0 to 1, e.g. 0.539
- **ref\_seq**: Reference protein sequence
- **match\_seq**: Protein sequence of the predicted lectin

Parameters

- **getcolumn**: string of the column(s) to be fetched (one or multiple columns, separated by comma)
- **wherecolumn**: string of the conditional column
- **isvalue**: string of the value to be matched in **wherecolumn** (wildcards are also accepted such as "Rattus%" to match everything starting with "Rattus")
- **limit**: (optional) integer of the number of results to be returned (default: 1000, -1 for all)

Examples

- Get the predicted lectome from all the proteins of the bacteria superkingdom:

Try this query
{ "getcolumns": "fold,domain,uniprot,superkingdom", "wherecolumn": "superkingdom", "isvalue": "Bacteria%" , "limit": "2000"}
- Get all predicted lectins:

Try this query
{ "getcolumns": "uniprot,domain", "wherecolumn": "uniprot", "isvalue": "%%", "limit": "2000"}

Query content

{ "getcolumns": "protein.name,uniprot,fold,domain,superkingdom",
"wherecolumn": "superkingdom", "isvalue": "Bacteria%", "limit": "2000"}

Show raw results

|  |  |
| --- | --- |
|  |  |

api/getligands

Description

This endpoint enables to perform queries on the **ligand** table.
It retrieves the content of the specified columns (**getcolumns**) where another column (**wherecolumn**) has a specific value (**isvalue**).

The available columns for this table are:

- **ligand\_id**
- **iupac**
- **glycoct**
- **glytoucan\_id**

Parameters

- **getcolumn**: string of the column(s) to be fetched (one or multiple columns, separated by comma)
- **wherecolumn**: string of the conditional column
- **isvalue**: string of the value to be matched in **wherecolumn** (wildcards are also accepted such as "Rattus%" to match everything starting with "Rattus")
- **limit**: (optional) integer of the number of results to be returned (default: 1000, -1 for all)

Examples

- Get ALL the columns and rows of the ligand table:

Try this query
{ "getcolumns": "ligand\_id,iupac,glycoct,glytoucan\_id", "wherecolumn": "ligand\_id", "isvalue": "%%" , "limit": "-1"}
- Get the ligands whose iupac contain a NAc:

Try this query
{ "getcolumns": "iupac", "wherecolumn": "iupac", "isvalue": "%NAc%", "limit": "1000"}

Query content

{ "getcolumns": "ligand\_id,iupac", "wherecolumn": "iupac", "isvalue": "%Gal%", "limit": "1000" }

Show raw results

|  |  |
| --- | --- |
|  |  |

api/gethumanlectome

Description

This endpoint enables to perform queries on the **Human Lectome** table.
It retrieves the content of the specified columns (**getcolumns**) where another column (**wherecolumn**) has a specific value (**isvalue**).

The available columns for this table are:

- **UniProt\_ID**: UniProt ID, e.g. Q13438
- **RefSeqID**: NCBI ID, e.g. NP\_006803
- **GeneID**: e.g. 10956
- **lectomeXplore\_score**: Score of prediction similarity to the reference, from 0 to 1, e.g. 1.0
- **infer\_class**: Lectin class, e.g. P-type lectin-like
- **infer\_fold**: Lectin fold, e.g. b-barrel
- **PDB\_ID**: e.g. 3AIH
- **family**: Protein family, e.g. MRH
- **common\_protein\_name** e.g. MRH - mannose-6-phosphate receptor homology domain
- **lectinStatus**: Curated, Low evidence or Very low evidence
- **glycanStatus**: Specific or Uncharacterised
- **Chromosome**: e.g. 12
- **iupac**: IUPAC of the ligand(s) that bind(s) the concerned lectin, e.g. Man(a1-6)Man(a1-6)Man
- **lectomexplore\_id**: Lectin ID in LectomeXplore (if any), e.g. 553088

Parameters

- **getcolumn**: string of the column to be fetched (one or multiple columns, separated by comma)
- **wherecolumn**: string of the conditional column
- **isvalue**: string of the value to be matched in **wherecolumn** (wildcards are also accepted as e.g. "Rattus%" to match everything starting with "Rattus")
- **limit**: (optional) integer of the number of results to be returned (default: 1000, -1 for all)

Examples

- Get all the human lectins with a curated status:

Try this query
{ "getcolumns": "RefSeqID,UniProt\_ID", "wherecolumn": "lectinStatus", "isvalue": "Curated" , "limit": "1000"}
- Get all the SIGLEC lectins:

Try this query
{ "getcolumns": "RefSeqID,UniProt\_ID", "wherecolumn": "common\_protein\_name", "isvalue": "%SIGLEC%" , "limit": "1000"}

Query content

{ "getcolumns":
"RefSeqID,UniProt\_ID,GeneID,common\_protein\_name,infer\_class,infer\_fold",
"wherecolumn": "lectinStatus", "isvalue": "Curated", "limit": "1000"}

Show raw results

|  |  |
| --- | --- |
|  |  |

api/getbiotechlectins

Description

This endpoint enables to perform queries in **BiotechLec**'s dataset.
It retrieves the content of the specified columns (**getcolumns**) where another column (**wherecolumn**) has a specific value (**isvalue**).

The available columns for this dataset are:

- **Lectin**: Commercial name of the lectin, e.g. MPA
- **Organism**: Species name, e.g. Maclura pomifera
- **Preferred glycan**: IUPAC of the lectin's preferred glycan, e.g. Gal(b1-3)GalNAc
- **Origin**: e.g. Plant
- **uniprot**: UniProt ID, e.g. P18674
- **protein name**: Common protein name, e.g. Agglutinin alpha chain
- **Length**: Protein sequence length, e.g. 133
- **PDB**: PDB ID, e.g. 3LLZ
- **Fold** Lectin fold, e.g. b-prism I
- **Class** Lectin class, e.g. Jacalin-like
- **InterPro family** InterPro family ID, e.g. IPR001229

Parameters

- **getcolumn**: string of the column to be fetched (one or multiple columns, separated by comma)
- **wherecolumn**: string of the conditional column
- **isvalue**: string of the value to be matched in **wherecolumn** (wildcards are also accepted as e.g. "Rattus%" to match everything starting with "Rattus")
- **limit**: (optional) integer of the number of results to be returned (default: 1000, -1 for all)

Examples

- Get all BiotechLec's lectins from plants:

Try this query
{
"getcolumns": "Lectin,Preferred glycan,uniprot,protein
name,Length,PDB", "wherecolumn": "Origin", "isvalue": "Plant",
"exactmatch": "True"}

Try this query
{
"getcolumns": "Lectin,Preferred glycan,uniprot,protein
name,Length,PDB", "wherecolumn": "Class", "isvalue": "Jacalin",
"exactmatch": "False"}

Query content

{ "getcolumns": "Lectin,Preferred glycan,uniprot,protein
name,Length,PDB", "wherecolumn": "Organism", "isvalue": "Escherichia
coli", "exactmatch": "True"}

Show raw results

|  |  |
| --- | --- |
|  |  |

api/getproplec

Description

This endpoint enables to perform queries on the **predicted propeller lectin** table.
It retrieves the content of the specified column(s) (**getcolumns**) where another column (**wherecolumn**) has a specific value (**isvalue**).

The available columns for this table are:

- **ncbi**: RefSeq ID, e.g. ABB17278
- **uniprot**: UniProt ID, e.g. Q309D1
- **protein.protein\_id**: PropLec lectin ID, e.g. 17491
- **protein.name**: e.g. Lectin PVL (Fragment)
- **domain**: Lectin family, e.g. PropLec7B\_PVL
- **domains.domains\_id**: PropLec domain ID, e.g. 31702
- **length**: Lectin length, e.g. 395
- **genus**: e.g. Lacrymaria
- **gene**: e.g. DQ232759.1
- **gene\_begin**: e.g. 1
- **gene\_end**: e.g. 1188
- **cluster**: e.g. Q309D1
- **species**: e.g. Lacrymaria velutina
- **superkingdom**: e.g. Eukaryota
- **kingdom**: e.g. Fungi
- **phylum**: e.g. Basidiomycota
- **score**: Score of prediction similarity to the reference, from 0 to 1, e.g. 0.871
- **nbdomain**: Number of lectin domains, e.g. 8

Parameters

- **getcolumn**: string of the column(s) to be fetched (one or multiple columns, separated by comma)
- **wherecolumn**: string of the conditional column
- **isvalue**: string of the value to be matched in **wherecolumn** (wildcards are also accepted such as "Rattus%" to match everything starting with "Rattus")
- **limit**: (optional) integer of the number of results to be returned (default: 1000, -1 for all)

Examples

- Get the propeller lectome from all the proteins of the bacteria superkingdom:

Try this query
{ "getcolumns": "domain,uniprot,superkingdom", "wherecolumn": "superkingdom", "isvalue": "Bacteria%" , "limit": "2000"}
- Get all predicted propeller lectins:

Try this query
{ "getcolumns": "uniprot,domain", "wherecolumn": "uniprot", "isvalue": "%%", "limit": "2000"}

Query content

{ "getcolumns": "protein.name,uniprot,ncbi,domain,superkingdom",
"wherecolumn": "superkingdom", "isvalue": "Bacteria%", "limit": "2000"}

Show raw results

|  |  |
| --- | --- |
|  |  |

api/getmycolec

Description

This endpoint enables to perform queries on the **predicted fungal lectin** table.
It retrieves the content of the specified column(s) (**getcolumns**) where another column (**wherecolumn**) has a specific value (**isvalue**).

The available columns for this table are:

- **protein\_id**: MycoLec lectin ID, e.g. 14183377
- **protein**: e.g. %SS1G\_09838T0%
- **fold**: Lectin fold, e.g. b-trefoil
- **domain**: Lectin class, e.g. Sclerotinia lectin-like
- **domains.domains\_id**: MycoLec domain ID, e.g. 30121
- **length**: Lectin length, e.g. 153
- **genus**: e.g. Sclerotinia
- **ref\_seq**: Reference protein sequence, e.g. MGFKGVGTYEIVPYQ%
- **match\_seq**: Protein sequence of the predicted lectin, e.g. MGFKGVGTYEIVPYQ%
- **species**: e.g. Sclerotinia sclerotiorum
- **phylum**: e.g. Ascomycota
- **class**: e.g. Leotiomycetes
- **family**: e.g. Sclerotiniaceae
- **score**: Score of prediction similarity to the reference, from 0 to 1, e.g. 1

Parameters

- **getcolumn**: string of the column(s) to be fetched (one or multiple columns, separated by comma)
- **wherecolumn**: string of the conditional column
- **isvalue**: string of the value to be matched in **wherecolumn** (wildcards are also accepted such as "Rattus%" to match everything starting with "Rattus")
- **limit**: (optional) integer of the number of results to be returned (default: 1000, -1 for all)

Examples

- Get the lectome from all the proteins of the species Sclerotinia sclerotiorum:

Try this query
{ "getcolumns": "fold,domain,species", "wherecolumn": "species", "isvalue": "Sclerotinia sclerotiorum" , "limit": "2000"}
- Get all predicted fungal lectins:

Try this query
{ "getcolumns": "protein,fold,domain", "wherecolumn": "protein", "isvalue": "%%", "limit": "2000"}

Query content

{ "getcolumns": "protein,fold,domain,species", "wherecolumn":
"species", "isvalue": "Sclerotinia sclerotiorum", "limit": "2000"}

Show raw results

|  |  |
| --- | --- |
|  |  |

api/gettreflec

Description

This endpoint enables to perform queries on the **predicted trefoil lectin** table.
It retrieves the content of the specified column(s) (**getcolumns**) where another column (**wherecolumn**) has a specific value (**isvalue**).

The available columns for this table are:

- **ncbi**: RefSeq ID, e.g. QBM06340
- **uniprot**: UniProt ID, e.g. A0A646QV53
- **protein.protein\_id**: TrefLec lectin ID, e.g. 25617
- **protein.name**: e.g. R-type lectin 1
- **domain**: Lectin family, e.g. Sevil-like
- **domains.domains\_id**: TrefLec domain ID, e.g. 18336
- **length**: Lectin length, e.g. 129
- **genus**: e.g. Mytilisepta
- **gene**: e.g. MK434191.1
- **gene\_begin**: e.g. 130
- **gene\_end**: e.g. 519
- **cluster**: e.g. Q309D1
- **species**: e.g. Mytilisepta virgata
- **superkingdom**: e.g. Eukaryota
- **kingdom**: e.g. Metazoa
- **phylum**: e.g. Mollusca
- **score**: Score of prediction similarity to the reference, from 0 to 1, e.g. 0.685
- **nbdomain**: Number of lectin domains, e.g. 3

Parameters

- **getcolumn**: string of the column(s) to be fetched (one or multiple columns, separated by comma)
- **wherecolumn**: string of the conditional column
- **isvalue**: string of the value to be matched in **wherecolumn** (wildcards are also accepted such as "Rattus%" to match everything starting with "Rattus")
- **limit**: (optional) integer of the number of results to be returned (default: 1000, -1 for all)

Examples

- Get the trefoil lectome from all the proteins of the bacteria superkingdom:

Try this query
{ "getcolumns": "domain,uniprot,superkingdom", "wherecolumn": "superkingdom", "isvalue": "Bacteria%" , "limit": "2000"}
- Get all predicted trefoil lectins:

Try this query
{ "getcolumns": "uniprot,domain", "wherecolumn": "uniprot", "isvalue": "%%", "limit": "2000"}

Query content

{ "getcolumns": "protein.name,uniprot,ncbi,domain,superkingdom",
"wherecolumn": "superkingdom", "isvalue": "Bacteria%", "limit": "2000"}

Show raw results

|  |  |
| --- | --- |
|  |  |
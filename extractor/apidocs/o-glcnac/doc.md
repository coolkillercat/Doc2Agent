API - Documentation

# Get started

```
API Endpoint

https://oglcnac.mcw.edu/api/v1/

```

The *O*-GlcNAc Database REST API provides programmatic access to read protein *O*-GlcNAcylation data.

This API is public but limits the number of requests to 60/m. Please download datasets in JSON format [here](https://www.oglcnac.mcw.edu/download) to overcome those limitations.

This is a Beta version. If you wish new API endpoints or filters to be added, please email to [admin@oglcnac.com](mailto:admin@oglcnac.com).

## get proteins

```

Proteins API Endpoint

https://oglcnac.mcw.edu/api/v1/proteins/

```

```

# Here is a curl example
curl \
https://oglcnac.mcw.edu/api/v1/proteins/?query_protein=P08047

```

To get proteins you need to make a GET call to the following url :
`https://oglcnac.mcw.edu/api/v1/proteins/`

```

Result example :

{
"_id": "P08047-0",
"PTM": {
"INIT_MET": [
{
"M1": {
"nature": "Removed",
"type": "M",
"isoform_id": "P08047-0",
"monoisotopic_mass_free": null,
"average_mass_free": null,
"monoisotopic_mass_ptm": null,
"average_mass_ptm": null,
"sequence": [
"",
"M",
""
],
"numbers": [
"",
"1",
""
]
}
}
],
"MOD_RES": [
{
"S2": {
"nature": "phosphorylation",
"type": "S",
"isoform_id": "P08047-0",
"monoisotopic_mass_free": null,
"average_mass_free": null,
"monoisotopic_mass_ptm": null,
"average_mass_ptm": null,
"sequence": [
"",
"S",
""
],
"numbers": [
"",
"2",
""
]
}
},
{
"S7": {
"nature": "phosphorylation",
"type": "S",
"isoform_id": "P08047-0",
"monoisotopic_mass_free": null,
"average_mass_free": null,
"monoisotopic_mass_ptm": null,
"average_mass_ptm": null,
"sequence": [
"",
"S",
""
],
"numbers": [
"",
"7",
""
]
}
},
{
"S59": {
"nature": "phosphorylation",
"type": "S",
"isoform_id": "P08047-0",
"monoisotopic_mass_free": null,
"average_mass_free": null,
"monoisotopic_mass_ptm": null,
"average_mass_ptm": null,
"sequence": [
"",
"S",
""
],
"numbers": [
"",
"59",
""
]
}
},
{
"S101": {
"nature": "phosphorylation",
"type": "S",
"isoform_id": "P08047-0",
"monoisotopic_mass_free": null,
"average_mass_free": null,
"monoisotopic_mass_ptm": null,
"average_mass_ptm": null,
"sequence": [
"",
"S",
""
],
"numbers": [
"",
"101",
""
]
}
},
{
"T278": {
"nature": "phosphorylation",
"type": "T",
"isoform_id": "P08047-0",
"monoisotopic_mass_free": null,
"average_mass_free": null,
"monoisotopic_mass_ptm": null,
"average_mass_ptm": null,
"sequence": [
"",
"T",
""
],
"numbers": [
"",
"278",
""
]
}
},
{
"T453": {
"nature": "phosphorylation",
"type": "T",
"isoform_id": "P08047-0",
"monoisotopic_mass_free": null,
"average_mass_free": null,
"monoisotopic_mass_ptm": null,
"average_mass_ptm": null,
"sequence": [
"",
"T",
""
],
"numbers": [
"",
"453",
""
]
}
},
{
"S612": {
"nature": "phosphorylation",
"type": "S",
"isoform_id": "P08047-0",
"monoisotopic_mass_free": null,
"average_mass_free": null,
"monoisotopic_mass_ptm": null,
"average_mass_ptm": null,
"sequence": [
"",
"S",
""
],
"numbers": [
"",
"612",
""
]
}
},
{
"T640": {
"nature": "phosphorylation",
"type": "T",
"isoform_id": "P08047-0",
"monoisotopic_mass_free": null,
"average_mass_free": null,
"monoisotopic_mass_ptm": null,
"average_mass_ptm": null,
"sequence": [
"",
"T",
""
],
"numbers": [
"",
"640",
""
]
}
},
{
"S641": {
"nature": "phosphorylation",
"type": "S",
"isoform_id": "P08047-0",
"monoisotopic_mass_free": null,
"average_mass_free": null,
"monoisotopic_mass_ptm": null,
"average_mass_ptm": null,
"sequence": [
"",
"S",
""
],
"numbers": [
"",
"641",
""
]
}
},
{
"T651": {
"nature": "phosphorylation",
"type": "T",
"isoform_id": "P08047-0",
"monoisotopic_mass_free": null,
"average_mass_free": null,
"monoisotopic_mass_ptm": null,
"average_mass_ptm": null,
"sequence": [
"",
"T",
""
],
"numbers": [
"",
"651",
""
]
}
},
{
"T668": {
"nature": "phosphorylation",
"type": "T",
"isoform_id": "P08047-0",
"monoisotopic_mass_free": null,
"average_mass_free": null,
"monoisotopic_mass_ptm": null,
"average_mass_ptm": null,
"sequence": [
"",
"T",
""
],
"numbers": [
"",
"668",
""
]
}
},
{
"S670": {
"nature": "phosphorylation",
"type": "S",
"isoform_id": "P08047-0",
"monoisotopic_mass_free": null,
"average_mass_free": null,
"monoisotopic_mass_ptm": null,
"average_mass_ptm": null,
"sequence": [
"",
"S",
""
],
"numbers": [
"",
"670",
""
]
}
},
{
"T681": {
"nature": "phosphorylation",
"type": "T",
"isoform_id": "P08047-0",
"monoisotopic_mass_free": null,
"average_mass_free": null,
"monoisotopic_mass_ptm": null,
"average_mass_ptm": null,
"sequence": [
"",
"T",
""
],
"numbers": [
"",
"681",
""
]
}
},
{
"S698": {
"nature": "phosphorylation",
"type": "S",
"isoform_id": "P08047-0",
"monoisotopic_mass_free": null,
"average_mass_free": null,
"monoisotopic_mass_ptm": null,
"average_mass_ptm": null,
"sequence": [
"",
"S",
""
],
"numbers": [
"",
"698",
""
]
}
},
{
"S702": {
"nature": "phosphorylation",
"type": "S",
"isoform_id": "P08047-0",
"monoisotopic_mass_free": null,
"average_mass_free": null,
"monoisotopic_mass_ptm": null,
"average_mass_ptm": null,
"sequence": [
"",
"S",
""
],
"numbers": [
"",
"702",
""
]
}
},
{
"T739": {
"nature": "phosphorylation",
"type": "T",
"isoform_id": "P08047-0",
"monoisotopic_mass_free": null,
"average_mass_free": null,
"monoisotopic_mass_ptm": null,
"average_mass_ptm": null,
"sequence": [
"",
"T",
""
],
"numbers": [
"",
"739",
""
]
}
}
],
"CARBOHYD": [
{
"S491": {
"nature": "oglcnacylation",
"type": "S",
"isoform_id": "P08047-0",
"monoisotopic_mass_free": null,
"average_mass_free": null,
"monoisotopic_mass_ptm": null,
"average_mass_ptm": null,
"sequence": [
"",
"S",
""
],
"numbers": [
"",
"491",
""
]
}
},
{
"S612": {
"nature": "oglcnacylation",
"type": "S",
"isoform_id": "P08047-0",
"monoisotopic_mass_free": null,
"average_mass_free": null,
"monoisotopic_mass_ptm": null,
"average_mass_ptm": null,
"sequence": [
"",
"S",
""
],
"numbers": [
"",
"612",
""
]
}
},
{
"T640": {
"nature": "oglcnacylation",
"type": "T",
"isoform_id": "P08047-0",
"monoisotopic_mass_free": null,
"average_mass_free": null,
"monoisotopic_mass_ptm": null,
"average_mass_ptm": null,
"sequence": [
"",
"T",
""
],
"numbers": [
"",
"640",
""
]
}
},
{
"S641": {
"nature": "oglcnacylation",
"type": "S",
"isoform_id": "P08047-0",
"monoisotopic_mass_free": null,
"average_mass_free": null,
"monoisotopic_mass_ptm": null,
"average_mass_ptm": null,
"sequence": [
"",
"S",
""
],
"numbers": [
"",
"641",
""
]
}
},
{
"S698": {
"nature": "oglcnacylation",
"type": "S",
"isoform_id": "P08047-0",
"monoisotopic_mass_free": null,
"average_mass_free": null,
"monoisotopic_mass_ptm": null,
"average_mass_ptm": null,
"sequence": [
"",
"S",
""
],
"numbers": [
"",
"698",
""
]
}
},
{
"S702": {
"nature": "oglcnacylation",
"type": "S",
"isoform_id": "P08047-0",
"monoisotopic_mass_free": null,
"average_mass_free": null,
"monoisotopic_mass_ptm": null,
"average_mass_ptm": null,
"sequence": [
"",
"S",
""
],
"numbers": [
"",
"702",
""
]
}
}
]
},
"code": 1,
"desactivated_sites": [],
"gene_names": [
"SP1",
"TSFP1"
],
"isoform_ids": [
"P08047-0",
"P08047-2",
"P08047-3"
],
"length": 785,
"length_pmids": 35,
"lineage": [
"Eukaryota",
"Metazoa",
"Chordata",
"Craniata",
"Vertebrata",
"Euteleostomi",
"Mammalia",
"Eutheria",
"Euarchontoglires",
"Primates",
"Haplorrhini",
"Catarrhini",
"Hominidae",
"Homo"
],
"main_id": "P08047",
"main_name": "SP1",
"mass": 80693,
"organism_name": "HUMAN",
"organism_sci": "Homo sapiens",
"pmid_list": [
"20699577",
"17049555",
"9452489",
"28510447",
"19302979",
"9079710",
"16408927",
"24129563",
"9111324",
"16027160",
"27655845",
"17614351",
"24995865",
"16332679",
"31847126",
"24553187",
"21740066",
"26499076",
"23013401",
"29351928",
"31866443",
"28054006",
"11371615",
"24802710",
"25352121",
"21105874",
"20305658",
"30397120",
"21795679",
"33214551",
"33686291",
"19193796",
"20657584",
"9343410",
"23301498"
],
"protein_altFullName": [],
"protein_altShortName": [],
"protein_recFullName": [
"Transcription factor Sp1"
],
"protein_recShortName": [],
"reload": false,
"score": 100.0,
"sequence": "MSDQDHSMDEMTAVVKIEKGVGGNNGGNGNGGGAFSQARSSSTGSSSSTGGGGQESQPSPLALLAATCSRIESPNENSNNSQGPSQSGGTGELDLTATQLSQGANGWQIISSSSGATPTSKEQSGSSTNGSNGSESSKNRTVSGGQYVVAAAPNLQNQQVLTGLPGVMPNIQYQVIPQFQTVDGQQLQFAATGAQVQQDGSGQIQIIPGANQQIITNRGSGGNIIAAMPNLLQQAVPLQGLANNVLSGQTQYVTNVPVALNGNITLLPVNSVSAATLTPSSQAVTISSSGSQESGSQPVTSGTTISSASLVSSQASSSSFFTNANSYSTTTTTSNMGIMNFTTSGSSGTNSQGQTPQRVSGLQGSDALNIQQNQTSGGSLQAGQQKEGEQNQQTQQQQILIQPQLVQGGQALQALQAAPLSGQTFTTQAISQETLQNLQLQAVPNSGPIIIRTPTVGPNGQVSWQTLQLQNLQVQNPQAQTITLAPMQGVSLGQTSSSNTTLTPIASAASIPAGTVTVNAAQLSSMPGLQTINLSALGTSGIQVHPIQGLPLAIANAPGDHGAQLGLHGAGGDGIHDDTAGGEEGENSPDAQPQAGRRTRREACTCPYCKDSEGRGSGDPGKKKQHICHIQGCGKVYGKTSHLRAHLRWHTGERPFMCTWSYCGKRFTRSDELQRHKRTHTGEKKFACPECPKRFMRSDHLSKHIKTHQNKKGGPGVALSVGTLPLDSGAGSEGSGTATPSALITTNMVAMEAICPEGIARLANSGINVMQVADLQSINISGNGF",
"sites": [
[
"S120",
"P08047-0"
],
[
"S126",
"P08047-0"
],
[
"T128",
"P08047-0"
],
[
"S134",
"P08047-0"
],
[
"T254",
"P08047-0"
],
[
"T265",
"P08047-0"
],
[
"S271",
"P08047-0"
],
[
"S273",
"P08047-0"
],
[
"T276",
"P08047-0"
],
[
"S312",
"P08047-0"
],
[
"T394",
"P08047-0"
],
[
"S421",
"P08047-0"
],
[
"T424",
"P08047-0"
],
[
"S446",
"P08047-0"
],
[
"T453",
"P08047-0"
],
[
"T455",
"P08047-0"
],
[
"S491",
"P08047-0"
],
[
"S507",
"P08047-0"
],
[
"S510",
"P08047-0"
],
[
"T517",
"P08047-0"
],
[
"S612",
"P08047-0"
],
[
"T640",
"P08047-0"
],
[
"S641",
"P08047-0"
],
[
"S698",
"P08047-0"
],
[
"S702",
"P08047-0"
]
],
"species_links": [
[
"P08047-0",
"SP1_HUMAN"
],
[
"O89090-0",
"SP1_MOUSE"
],
[
"Q01714-0",
"SP1_RAT"
]
],
"status": true,
"ts": 0,
"uniprot_name": "SP1_HUMAN",
"untested_sites": [],
"validated_sites": [
{
"position": "640",
"status": true,
"result": [
"T640",
"P08047-0"
],
"submitted": [
[
"T640"
],
[
true,
false,
false
],
[
"P08047-0",
"P08047-2",
"P08047-3"
]
],
"comment": null,
"alternative": []
},
{
"position": "446",
"status": true,
"result": [
"S446",
"P08047-0"
],
"submitted": [
[
"S446"
],
[
true,
false,
false
],
[
"P08047-0",
"P08047-2",
"P08047-3"
]
],
"comment": null,
"alternative": []
},
{
"position": "702",
"status": true,
"result": [
"S702",
"P08047-0"
],
"submitted": [
[
"S702"
],
[
true,
false,
false
],
[
"P08047-0",
"P08047-2",
"P08047-3"
]
],
"comment": null,
"alternative": []
},
{
"position": "641",
"status": true,
"result": [
"S641",
"P08047-0"
],
"submitted": [
[
"S641"
],
[
true,
false,
false
],
[
"P08047-0",
"P08047-2",
"P08047-3"
]
],
"comment": null,
"alternative": []
},
{
"position": "128",
"status": true,
"result": [
"T128",
"P08047-0"
],
"submitted": [
[
"T128"
],
[
true,
false,
false
],
[
"P08047-0",
"P08047-2",
"P08047-3"
]
],
"comment": null,
"alternative": []
},
{
"position": "421",
"status": true,
"result": [
"S421",
"P08047-0"
],
"submitted": [
[
"S421"
],
[
true,
false,
false
],
[
"P08047-0",
"P08047-2",
"P08047-3"
]
],
"comment": null,
"alternative": []
},
{
"position": "698",
"status": true,
"result": [
"S698",
"P08047-0"
],
"submitted": [
[
"S698"
],
[
true,
false,
false
],
[
"P08047-0",
"P08047-2",
"P08047-3"
]
],
"comment": null,
"alternative": []
},
{
"position": "276",
"status": true,
"result": [
"T276",
"P08047-0"
],
"submitted": [
[
"T276"
],
[
true,
false,
false
],
[
"P08047-0",
"P08047-2",
"P08047-3"
]
],
"comment": null,
"alternative": []
},
{
"position": "134",
"status": true,
"result": [
"S134",
"P08047-0"
],
"submitted": [
[
"S134"
],
[
true,
false,
false
],
[
"P08047-0",
"P08047-2",
"P08047-3"
]
],
"comment": null,
"alternative": []
},
{
"position": "120",
"status": true,
"result": [
"S120",
"P08047-0"
],
"submitted": [
[
"S120"
],
[
true,
false,
false
],
[
"P08047-0",
"P08047-2",
"P08047-3"
]
],
"comment": null,
"alternative": []
},
{
"position": "424",
"status": true,
"result": [
"T424",
"P08047-0"
],
"submitted": [
[
"T424"
],
[
true,
false,
false
],
[
"P08047-0",
"P08047-2",
"P08047-3"
]
],
"comment": null,
"alternative": []
},
{
"position": "271",
"status": true,
"result": [
"S271",
"P08047-0"
],
"submitted": [
[
"S271"
],
[
true,
false,
false
],
[
"P08047-0",
"P08047-2",
"P08047-3"
]
],
"comment": null,
"alternative": []
},
{
"position": "612",
"status": true,
"result": [
"S612",
"P08047-0"
],
"submitted": [
[
"S612"
],
[
true,
false,
false
],
[
"P08047-0",
"P08047-2",
"P08047-3"
]
],
"comment": null,
"alternative": []
},
{
"position": "507",
"status": true,
"result": [
"S507",
"P08047-0"
],
"submitted": [
[
"S507"
],
[
true,
false,
false
],
[
"P08047-0",
"P08047-2",
"P08047-3"
]
],
"comment": null,
"alternative": []
},
{
"position": "394",
"status": true,
"result": [
"T394",
"P08047-0"
],
"submitted": [
[
"T394"
],
[
true,
false,
false
],
[
"P08047-0",
"P08047-2",
"P08047-3"
]
],
"comment": null,
"alternative": []
},
{
"position": "265",
"status": true,
"result": [
"T265",
"P08047-0"
],
"submitted": [
[
"T265"
],
[
true,
false,
false
],
[
"P08047-0",
"P08047-2",
"P08047-3"
]
],
"comment": null,
"alternative": []
},
{
"position": "312",
"status": true,
"result": [
"S312",
"P08047-0"
],
"submitted": [
[
"S312"
],
[
true,
false,
false
],
[
"P08047-0",
"P08047-2",
"P08047-3"
]
],
"comment": null,
"alternative": []
},
{
"position": "517",
"status": true,
"result": [
"T517",
"P08047-0"
],
"submitted": [
[
"T517"
],
[
true,
false,
false
],
[
"P08047-0",
"P08047-2",
"P08047-3"
]
],
"comment": null,
"alternative": []
},
{
"position": "126",
"status": true,
"result": [
"S126",
"P08047-0"
],
"submitted": [
[
"S126"
],
[
true,
false,
false
],
[
"P08047-0",
"P08047-2",
"P08047-3"
]
],
"comment": null,
"alternative": []
},
{
"position": "510",
"status": true,
"result": [
"S510",
"P08047-0"
],
"submitted": [
[
"S510"
],
[
true,
false,
false
],
[
"P08047-0",
"P08047-2",
"P08047-3"
]
],
"comment": null,
"alternative": []
},
{
"position": "455",
"status": true,
"result": [
"T455",
"P08047-0"
],
"submitted": [
[
"T455"
],
[
true,
false,
false
],
[
"P08047-0",
"P08047-2",
"P08047-3"
]
],
"comment": null,
"alternative": []
},
{
"position": "453",
"status": true,
"result": [
"T453",
"P08047-0"
],
"submitted": [
[
"T453"
],
[
true,
false,
false
],
[
"P08047-0",
"P08047-2",
"P08047-3"
]
],
"comment": null,
"alternative": []
},
{
"position": "254",
"status": true,
"result": [
"T254",
"P08047-0"
],
"submitted": [
[
"T254"
],
[
true,
false,
false
],
[
"P08047-0",
"P08047-2",
"P08047-3"
]
],
"comment": null,
"alternative": []
},
{
"position": "491",
"status": true,
"result": [
"S491",
"P08047-0"
],
"submitted": [
[
"S491"
],
[
true,
false,
false
],
[
"P08047-0",
"P08047-2",
"P08047-3"
]
],
"comment": null,
"alternative": []
},
{
"position": "273",
"status": true,
"result": [
"S273",
"P08047-0"
],
"submitted": [
[
"S273"
],
[
true,
false,
false
],
[
"P08047-0",
"P08047-2",
"P08047-3"
]
],
"comment": null,
"alternative": []
}
],
"species_colors": [
"#ACD2EC",
"#5E7585"
],
"full_name": [
"Transcription factor Sp1"
],
"length_sites": 25,
"COMPUTED": {
"OGLCNAC": [
{
"S120": {
"nature": "oglcnac",
"type": "S",
"organism_sci": "Homo sapiens",
"isoform_id": "P08047-0",
"monoisotopic_maso_free": 1061.4989,
"average_maso_free": 1062.1014400000001,
"monoisotopic_maso_ptm": 1264.5783000000001,
"average_maso_ptm": 1265.29644,
"sequence": [
"GATPT",
"S",
"KEQSG"
],
"numbers": [
115,
"120",
125
]
}
},
{
"S126": {
"nature": "oglcnac",
"type": "S",
"organism_sci": "Homo sapiens",
"isoform_id": "P08047-0",
"monoisotopic_maso_free": 1080.46834,
"average_maso_free": 1081.06104,
"monoisotopic_maso_ptm": 1283.54774,
"average_maso_ptm": 1284.25604,
"sequence": [
"KEQSG",
"S",
"STNGS"
],
"numbers": [
121,
"126",
131
]
}
},
{
"T128": {
"nature": "oglcnac",
"type": "T",
"organism_sci": "Homo sapiens",
"isoform_id": "P08047-0",
"monoisotopic_maso_free": 994.39518,
"average_maso_free": 994.92714,
"monoisotopic_maso_ptm": 1197.47458,
"average_maso_ptm": 1198.12214,
"sequence": [
"QSGSS",
"T",
"NGSNG"
],
"numbers": [
123,
"128",
133
]
}
},
{
"S134": {
"nature": "oglcnac",
"type": "S",
"organism_sci": "Homo sapiens",
"isoform_id": "P08047-0",
"monoisotopic_maso_free": 1079.44794,
"average_maso_free": 1080.03284,
"monoisotopic_maso_ptm": 1282.52734,
"average_maso_ptm": 1283.22784,
"sequence": [
"NGSNG",
"S",
"ESSKN"
],
"numbers": [
129,
"134",
139
]
}
},
{
"T254": {
"nature": "oglcnac",
"type": "T",
"organism_sci": "Homo sapiens",
"isoform_id": "P08047-0",
"monoisotopic_maso_free": 1218.62444,
"average_maso_free": 1219.3599399999998,
"monoisotopic_maso_ptm": 1421.7038400000001,
"average_maso_ptm": 1422.5549399999998,
"sequence": [
"QTQYV",
"T",
"NVPVA"
],
"numbers": [
249,
"254",
259
]
}
},
{
"T265": {
"nature": "oglcnac",
"type": "T",
"organism_sci": "Homo sapiens",
"isoform_id": "P08047-0",
"monoisotopic_maso_free": 1166.6659000000002,
"average_maso_free": 1167.3705400000001,
"monoisotopic_maso_ptm": 1369.7453000000003,
"average_maso_ptm": 1370.56554,
"sequence": [
"LNGNI",
"T",
"LLPVN"
],
"numbers": [
260,
"265",
270
]
}
},
{
"S271": {
"nature": "oglcnac",
"type": "S",
"organism_sci": "Homo sapiens",
"isoform_id": "P08047-0",
"monoisotopic_maso_free": 1070.5971499999998,
"average_maso_free": 1071.23884,
"monoisotopic_maso_ptm": 1273.67655,
"average_maso_ptm": 1274.43384,
"sequence": [
"LLPVN",
"S",
"VSAAT"
],
"numbers": [
266,
"271",
276
]
}
},
{
"S273": {
"nature": "oglcnac",
"type": "S",
"organism_sci": "Homo sapiens",
"isoform_id": "P08047-0",
"monoisotopic_maso_free": 1058.56077,
"average_maso_free": 1059.18454,
"monoisotopic_maso_ptm": 1261.6401700000001,
"average_maso_ptm": 1262.37954,
"sequence": [
"PVNSV",
"S",
"AATLT"
],
"numbers": [
268,
"273",
278
]
}
},
{
"T276": {
"nature": "oglcnac",
"type": "T",
"organism_sci": "Homo sapiens",
"isoform_id": "P08047-0",
"monoisotopic_maso_free": 1019.5134899999999,
"average_maso_free": 1020.10454,
"monoisotopic_maso_ptm": 1222.59289,
"average_maso_ptm": 1223.29954,
"sequence": [
"SVSAA",
"T",
"LTPSS"
],
"numbers": [
271,
"276",
281
]
}
},
{
"S312": {
"nature": "oglcnac",
"type": "S",
"organism_sci": "Homo sapiens",
"isoform_id": "P08047-0",
"monoisotopic_maso_free": 1022.4880099999998,
"average_maso_free": 1023.06474,
"monoisotopic_maso_ptm": 1225.5674099999999,
"average_maso_ptm": 1226.25974,
"sequence": [
"SASLV",
"S",
"SQASS"
],
"numbers": [
307,
"312",
317
]
}
},
{
"T394": {
"nature": "oglcnac",
"type": "T",
"organism_sci": "Homo sapiens",
"isoform_id": "P08047-0",
"monoisotopic_maso_free": 1371.63788,
"average_maso_free": 1372.4139399999997,
"monoisotopic_maso_ptm": 1574.71728,
"average_maso_ptm": 1575.6089399999996,
"sequence": [
"EQNQQ",
"T",
"QQQQI"
],
"numbers": [
389,
"394",
399
]
}
},
{
"S421": {
"nature": "oglcnac",
"type": "S",
"organism_sci": "Homo sapiens",
"isoform_id": "P08047-0",
"monoisotopic_maso_free": 1119.55602,
"average_maso_free": 1120.22724,
"monoisotopic_maso_ptm": 1322.63542,
"average_maso_ptm": 1323.4222399999999,
"sequence": [
"QAAPL",
"S",
"GQTFT"
],
"numbers": [
416,
"421",
426
]
}
},
{
"T424": {
"nature": "oglcnac",
"type": "T",
"organism_sci": "Homo sapiens",
"isoform_id": "P08047-0",
"monoisotopic_maso_free": 1149.5665900000001,
"average_maso_free": 1150.25354,
"monoisotopic_maso_ptm": 1352.6459900000002,
"average_maso_ptm": 1353.4485399999999,
"sequence": [
"PLSGQ",
"T",
"FTTQA"
],
"numbers": [
419,
"424",
429
]
}
},
{
"S446": {
"nature": "oglcnac",
"type": "S",
"organism_sci": "Homo sapiens",
"isoform_id": "P08047-0",
"monoisotopic_maso_free": 1107.62878,
"average_maso_free": 1108.3028400000003,
"monoisotopic_maso_ptm": 1310.70818,
"average_maso_ptm": 1311.4978400000002,
"sequence": [
"QAVPN",
"S",
"GPIII"
],
"numbers": [
441,
"446",
451
]
}
},
{
"T453": {
"nature": "oglcnac",
"type": "T",
"organism_sci": "Homo sapiens",
"isoform_id": "P08047-0",
"monoisotopic_maso_free": 1162.70736,
"average_maso_free": 1163.4257400000001,
"monoisotopic_maso_ptm": 1365.7867600000002,
"average_maso_ptm": 1366.62074,
"sequence": [
"PIIIR",
"T",
"PTVGP"
],
"numbers": [
448,
"453",
458
]
}
},
{
"T455": {
"nature": "oglcnac",
"type": "T",
"organism_sci": "Homo sapiens",
"isoform_id": "P08047-0",
"monoisotopic_maso_free": 1123.63493,
"average_maso_free": 1124.3053400000001,
"monoisotopic_maso_ptm": 1326.71433,
"average_maso_ptm": 1327.50034,
"sequence": [
"IIRTP",
"T",
"VGPNG"
],
"numbers": [
450,
"455",
460
]
}
},
{
"S491": {
"nature": "oglcnac",
"type": "S",
"organism_sci": "Homo sapiens",
"isoform_id": "P08047-0",
"monoisotopic_maso_free": 1103.5281,
"average_maso_free": 1104.24324,
"monoisotopic_maso_ptm": 1306.6075,
"average_maso_ptm": 1307.43824,
"sequence": [
"PMQGV",
"S",
"LGQTS"
],
"numbers": [
486,
"491",
496
]
}
},
{
"S507": {
"nature": "oglcnac",
"type": "S",
"organism_sci": "Homo sapiens",
"isoform_id": "P08047-0",
"monoisotopic_maso_free": 1039.59133,
"average_maso_free": 1040.22474,
"monoisotopic_maso_ptm": 1242.67073,
"average_maso_ptm": 1243.41974,
"sequence": [
"LTPIA",
"S",
"AASIP"
],
"numbers": [
502,
"507",
512
]
}
},
{
"S510": {
"nature": "oglcnac",
"type": "S",
"organism_sci": "Homo sapiens",
"isoform_id": "P08047-0",
"monoisotopic_maso_free": 957.5130800000001,
"average_maso_free": 958.0793400000001,
"monoisotopic_maso_ptm": 1160.59248,
"average_maso_ptm": 1161.2743400000002,
"sequence": [
"IASAA",
"S",
"IPAGT"
],
"numbers": [
505,
"510",
515
]
}
},
{
"T517": {
"nature": "oglcnac",
"type": "T",
"organism_sci": "Homo sapiens",
"isoform_id": "P08047-0",
"monoisotopic_maso_free": 1027.5297999999998,
"average_maso_free": 1028.13014,
"monoisotopic_maso_ptm": 1230.6091999999999,
"average_maso_ptm": 1231.32514,
"sequence": [
"PAGTV",
"T",
"VNAAQ"
],
"numbers": [
512,
"517",
522
]
}
},
{
"S612": {
"nature": "oglcnac",
"type": "S",
"organism_sci": "Homo sapiens",
"isoform_id": "P08047-0",
"monoisotopic_maso_free": 1197.5084200000001,
"average_maso_free": 1198.27264,
"monoisotopic_maso_ptm": 1400.5878200000002,
"average_maso_ptm": 1401.4676399999998,
"sequence": [
"PYCKD",
"S",
"EGRGS"
],
"numbers": [
607,
"612",
617
]
}
},
{
"T640": {
"nature": "oglcnac",
"type": "T",
"organism_sci": "Homo sapiens",
"isoform_id": "P08047-0",
"monoisotopic_maso_free": 1258.7145799999998,
"average_maso_free": 1259.47404,
"monoisotopic_maso_ptm": 1461.79398,
"average_maso_ptm": 1462.66904,
"sequence": [
"KVYGK",
"T",
"SHLRA"
],
"numbers": [
635,
"640",
645
]
}
},
{
"S641": {
"nature": "oglcnac",
"type": "S",
"organism_sci": "Homo sapiens",
"isoform_id": "P08047-0",
"monoisotopic_maso_free": 1267.67853,
"average_maso_free": 1268.4410400000002,
"monoisotopic_maso_ptm": 1470.75793,
"average_maso_ptm": 1471.63604,
"sequence": [
"VYGKT",
"S",
"HLRAH"
],
"numbers": [
636,
"641",
646
]
}
},
{
"S698": {
"nature": "oglcnac",
"type": "S",
"organism_sci": "Homo sapiens",
"isoform_id": "P08047-0",
"monoisotopic_maso_free": 1403.7455699999998,
"average_maso_free": 1404.65314,
"monoisotopic_maso_ptm": 1606.82497,
"average_maso_ptm": 1607.8481399999998,
"sequence": [
"KRFMR",
"S",
"DHLSK"
],
"numbers": [
693,
"698",
703
]
}
},
{
"S702": {
"nature": "oglcnac",
"type": "S",
"organism_sci": "Homo sapiens",
"isoform_id": "P08047-0",
"monoisotopic_maso_free": 1320.7262099999998,
"average_maso_free": 1321.50204,
"monoisotopic_maso_ptm": 1523.80561,
"average_maso_ptm": 1524.69704,
"sequence": [
"RSDHL",
"S",
"KHIKT"
],
"numbers": [
697,
"702",
707
]
}
}
]
}
}

```

#### QUERY PARAMETERS

| Field | Type | Description |
| --- | --- | --- |
| query\_protein | String | UniProtKB ID |

## Errors

The *O*-GlcNAc Database API uses the following error codes:

| Error Code | Meaning |
| --- | --- |
| {} | No result found for the requested UniProtKB ID |
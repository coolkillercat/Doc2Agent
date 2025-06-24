WURCS-RDF API | Wiki.js

---

---

Page Contents

Talk

View Discussion

Last edited by

Masaaki Shiota

08/14/2023

- [WURCS-RDF](https://gitlab.com/glycoinfo/wurcsrdf) 1.2.6
- [WURCSFramework](https://gitlab.com/glycoinfo/wurcsframework) 1.2.5

Generate the WURCS-RDF from WURCS.

- Parameters
- **gtcid**: string (required) - GlyTouCan ID.
- **wurcs**: string (required) - WURCS format text.
- [Example](https://api.glycosmos.org/wurcsrdf/1.2.6/wurcs2wurcsrdf/G22768VO/WURCS%3D2.0%2F3%2C5%2C4%2F%5Ba2122h-1b_1-5_2%2ANCC%2F3%3DO%5D%5Ba1122h-1b_1-5%5D%5Ba1122h-1a_1-5%5D%2F1-1-2-3-3%2Fa4-b1_b4-c1_c3-d1_c6-e1)

- Example

```
curl -d '{"gtcid": "G22768VO", "wurcs": "WURCS=2.0/3,5,4/[a2122h-1b_1-5_2*NCC/3=O][a1122h-1b_1-5][a1122h-1a_1-5]/1-1-2-3-3/a4-b1_b4-c1_c3-d1_c6-e1"}' https://api.glycosmos.org/wurcsrdf/1.2.6/wurcs2wurcsrdf
```

Copy

- Request
- Body

```
{
"gtcid": "G22768VO",
"wurcs": "WURCS=2.0/3,5,4/[a2122h-1b_1-5_2*NCC/3=O][a1122h-1b_1-5][a1122h-1a_1-5]/1-1-2-3-3/a4-b1_b4-c1_c3-d1_c6-e1"
}
```

Copy

Get SPARQL query for substructure search from WURCS.

- Parameters
- **wurcs**: string (required) - WURCS format text.
- [Example](https://api.glycosmos.org/wurcsrdf/1.2.6/wurcs2sparql/WURCS%3D2.0%2F3%2C5%2C4%2F%5Ba2122h-1b_1-5_2%2ANCC%2F3%3DO%5D%5Ba1122h-1b_1-5%5D%5Ba1122h-1a_1-5%5D%2F1-1-2-3-3%2Fa4-b1_b4-c1_c3-d1_c6-e1)

- Example

```
curl -d '{"wurcs": "WURCS=2.0/3,5,4/[a2122h-1b_1-5_2*NCC/3=O][a1122h-1b_1-5][a1122h-1a_1-5]/1-1-2-3-3/a4-b1_b4-c1_c3-d1_c6-e1", "rootnode": "true"}' https://api.glycosmos.org/wurcsrdf/1.2.6/wurcs2sparql
```

Copy

- Request
- Body

```
{
"wurcs": "WURCS=2.0/3,5,4/[a2122h-1b_1-5_2*NCC/3=O][a1122h-1b_1-5][a1122h-1a_1-5]/1-1-2-3-3/a4-b1_b4-c1_c3-d1_c6-e1",
"rootnode": "true"
}
```

Copy

<https://api.glycosmos.org/index.html#wurcs-rdf-api>

Please contact the server administrator with any questions or problems, [support@glycosmos.org](mailto:support@glycosmos.org).

No comments yet.
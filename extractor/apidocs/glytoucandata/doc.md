GlyTouCan Data API | Wiki.js

---

---

Page Contents

Talk

View Discussion

Last edited by

Masaaki Shiota

08/14/2023

- [GlyTouCan Endpoint](https://ts.glytoucan.org/sparql)

Obtain all accession numbers and WURCS format text from GlyTouCan.

- Example

```
wget https://api.glycosmos.org/sparqlist/Glytoucan-list
```

Copy

Obtain the GlyTouCan ID from WURCS.

- Parameters
- **wurcs**: string (required) - WURCS format text.
- [Example](https://api.glycosmos.org/sparqlist/wurcs2gtcids?wurcs=WURCS%3D2.0%2F3%2C5%2C4%2F%5Ba2122h-1b_1-5_2%2ANCC%2F3%3DO%5D%5Ba1122h-1b_1-5%5D%5Ba1122h-1a_1-5%5D%2F1-1-2-3-3%2Fa4-b1_b4-c1_c3-d1_c6-e1)
- Response
- Body

```
[
{
"id": "G22768VO",
"wurcs": "WURCS=2.0/3,5,4/[a2122h-1b_1-5_2*NCC/3=O][a1122h-1b_1-5][a1122h-1a_1-5]/1-1-2-3-3/a4-b1_b4-c1_c3-d1_c6-e1"
}
]
```

Copy

- Example

```
curl -d wurcs='WURCS=2.0/3,5,4/[a2122h-1b_1-5_2*NCC/3=O][a1122h-1b_1-5][a1122h-1a_1-5]/1-1-2-3-3/a4-b1_b4-c1_c3-d1_c6-e1' https://api.glycosmos.org/sparqlist/wurcs2gtcids
```

Copy

- Request
- Parameters
- `wurcs`

```
WURCS=2.0/3,5,4/[a2122h-1b_1-5_2*NCC/3=O][a1122h-1b_1-5][a1122h-1a_1-5]/1-1-2-3-3/a4-b1_b4-c1_c3-d1_c6-e1
```

Copy

- Response
- Body

```
[
{
"id": "G22768VO",
"wurcs": "WURCS=2.0/3,5,4/[a2122h-1b_1-5_2*NCC/3=O][a1122h-1b_1-5][a1122h-1a_1-5]/1-1-2-3-3/a4-b1_b4-c1_c3-d1_c6-e1"
}
]
```

Copy

Obtain the WURCS [& GlycoCT] from GlyTouCan ID.

- Parameters
- **gtcid**: string (required) - GlyTouCan ID.
- [Example](https://api.glycosmos.org/sparqlist/gtcid2seqs?gtcid=G22768VO)
- Response
- Body

```
[
{
"id": "G22768VO",
"wurcs": "WURCS=2.0/3,5,4/[a2122h-1b_1-5_2*NCC/3=O][a1122h-1b_1-5][a1122h-1a_1-5]/1-1-2-3-3/a4-b1_b4-c1_c3-d1_c6-e1"
},
{
"id": "G22768VO",
"glycoct": "RES\n1b:b-dglc-HEX-1:5\n2s:n-acetyl\n3b:b-dglc-HEX-1:5\n4s:n-acetyl\n5b:b-dman-HEX-1:5\n6b:a-dman-HEX-1:5\n7b:a-dman-HEX-1:5\nLIN\n1:1d(2+1)2n\n2:1o(4+1)3d\n3:3d(2+1)4n\n4:3o(4+1)5d\n5:5o(3+1)6d\n6:5o(6+1)7d"
}
]
```

Copy

- Example

```
curl -d gtcid=G22768VO https://api.glycosmos.org/sparqlist/gtcid2seqs
```

Copy

- Request
- Parameters
- `gtcid`

```
G22768VO
```

Copy

- Response
- Body

```
[
{
"id": "G22768VO",
"wurcs": "WURCS=2.0/3,5,4/[a2122h-1b_1-5_2*NCC/3=O][a1122h-1b_1-5][a1122h-1a_1-5]/1-1-2-3-3/a4-b1_b4-c1_c3-d1_c6-e1"
},
{
"id": "G22768VO",
"glycoct": "RES\n1b:b-dglc-HEX-1:5\n2s:n-acetyl\n3b:b-dglc-HEX-1:5\n4s:n-acetyl\n5b:b-dman-HEX-1:5\n6b:a-dman-HEX-1:5\n7b:a-dman-HEX-1:5\nLIN\n1:1d(2+1)2n\n2:1o(4+1)3d\n3:3d(2+1)4n\n4:3o(4+1)5d\n5:5o(3+1)6d\n6:5o(6+1)7d"
}
]
```

Copy

*Loading comments...*
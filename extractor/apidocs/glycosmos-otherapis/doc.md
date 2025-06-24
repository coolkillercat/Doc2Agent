Other APIs | Wiki.js

---

---

Page Contents

Talk

View Discussion

Last edited by

Masaaki Shiota

08/14/2023

Convert composition text to WURCS format.

- Parameters
- **text**: string (required) - composition text.
- [Example](https://api.glycosmos.org/composition2wurcs?text=Hex%283%29HexNAc%282%29)
- Response
- Body

```
{
"id": "G14669DU",
"wurcs": "WURCS=2.0/2,5,4/[axxxxh-1x_1-5_2*NCC/3=O][axxxxh-1x_1-5]/1-1-2-2-2/a?|b?|c?|d?|e?}-{a?|b?|c?|d?|e?_a?|b?|c?|d?|e?}-{a?|b?|c?|d?|e?_a?|b?|c?|d?|e?}-{a?|b?|c?|d?|e?_a?|b?|c?|d?|e?}-{a?|b?|c?|d?|e?"
}
```

Copy

- Parameters
- **wurcs**: string (required) - WURCS format text.
- [Example](https://api.glycosmos.org/partialmatch/wurcsrdf?wurcs=WURCS%3D2.0%2F5%2C5%2C4%2F%5Ba2122h-1x_1-5%5D%5Ba2112h-1b_1-5%5D%5Ba2112h-1a_1-5%5D%5Ba2112h-1b_1-5_2%2ANCC%2F3%3DO%5D%5Ba2112h-1a_1-5_2%2ANCC%2F3%3DO%5D%2F1-2-3-4-5%2Fa4-b1_b3-c1_c3-d1_d3-e1)
- Response
- Body

```
[
{
"id": "G48061MK",
"wurcs": "WURCS=2.0/5,5,4/[a2122h-1x_1-5][a2112h-1b_1-5][a2112h-1a_1-5][a2112h-1b_1-5_2*NCC/3=O][a2112h-1a_1-5_2*NCC/3=O]/1-2-3-4-5/a4-b1_b3-c1_c3-d1_d3-e1"
},
{
"id": "G51197ZR",
"wurcs": "WURCS=2.0/5,5,4/[a2122h-1b_1-5][a2112h-1b_1-5][a2112h-1a_1-5][a2112h-1b_1-5_2*NCC/3=O][a2112h-1a_1-5_2*NCC/3=O]/1-2-3-4-5/a4-b1_b3-c1_c3-d1_d3-e1"
},
{
"id": "G44161QY",
"wurcs": "WURCS=2.0/7,9,8/[a2122h-1b_1-5][a2112h-1b_1-5][a2112h-1a_1-5][a2112h-1b_1-5_2*NCC/3=O][a2112h-1a_1-5_2*NCC/3=O][a2122h-1b_1-5_2*NCC/3=O][Aad21122h-2a_2-6_5*NCC/3=O]/1-2-3-4-5-6-2-7-4/a4-b1_b3-c1_b6-f1_c3-d1_d3-e1_f4-g1_g3-h2_g4-i1"
}
]
```

Copy

- Parameters
- **glycoct**: string - GlycoCT format text.
- **wurcs**: string - WURCS format text.
- [Example](https://api.glycosmos.org/partialmatch/glycoql?glycoct=RES%0A1b%3Ax-dglc-HEX-1%3A5%0A2b%3Ab-dgal-HEX-1%3A5%0A3b%3Aa-dgal-HEX-1%3A5%0A4b%3Ab-dgal-HEX-1%3A5%0A5s%3An-acetyl%0A6b%3Aa-dgal-HEX-1%3A5%0A7s%3An-acetyl%0ALIN%0A1%3A1o%284%2B1%292d%0A2%3A2o%283%2B1%293d%0A3%3A3o%283%2B1%294d%0A4%3A4d%282%2B1%295n%0A5%3A4o%283%2B1%296d%0A6%3A6d%282%2B1%297n)
- Response
- Body

```
[
{
"id": "G51197ZR",
"res_num": "5"
},
{
"id": "G44161QY",
"res_num": "9"
},
{
"id": "G48061MK",
"res_num": "5"
}
]
```

Copy

Convert GWS format to WURCS format.

- Parameters
- **gws**: string (required) - GWS format text.
- [Example](https://api.glycosmos.org/gws2wurcs?gws=freeEnd--%3Fb1D-GlcNAc%2Cp--4b1D-GlcNAc%2Cp--4b1D-Man%2Cp--%3Fa1D-Man%2Cp%24MONO%2CUnd%2C0%2C0%2CfreeEnd)
- Response
- Body

```
{
"id": "G03717EM",
"wurcs": "WURCS=2.0/3,4,3/[a2122h-1b_1-5_2*NCC/3=O][a1122h-1b_1-5][a1122h-1a_1-5]/1-1-2-3/a4-b1_b4-c1_c?-d1",
"WURCS": "WURCS=2.0/3,4,3/[a2122h-1b_1-5_2*NCC/3=O][a1122h-1b_1-5][a1122h-1a_1-5]/1-1-2-3/a4-b1_b4-c1_c?-d1",
"input": "freeEnd--?b1D-GlcNAc,p--4b1D-GlcNAc,p--4b1D-Man,p--?a1D-Man,p$MONO,Und,0,0,freeEnd",
"GlycoCT": "RES\n1b:b-dglc-HEX-1:5\n2s:n-acetyl\n3b:b-dglc-HEX-1:5\n4s:n-acetyl\n5b:b-dman-HEX-1:5\n6b:a-dman-HEX-1:5\nLIN\n1:1d(2+1)2n\n2:1o(4+1)3d\n3:3d(2+1)4n\n4:3o(4+1)5d\n5:5o(-1+1)6d"
}
```

Copy

- Example

```
curl -d '["freeEnd--?b1D-GlcNAc,p--4b1D-GlcNAc,p--4b1D-Man,p--?a1D-Man,p$MONO,Und,0,0,freeEnd"]' https://api.glycosmos.org/gws2wurcs
```

Copy

- Request
- Body

```
["freeEnd--?b1D-GlcNAc,p--4b1D-GlcNAc,p--4b1D-Man,p--?a1D-Man,p$MONO,Und,0,0,freeEnd"]
```

Copy

- Response
- Body

```
[
{
"id": "G03717EM",
"wurcs": "WURCS=2.0/3,4,3/[a2122h-1b_1-5_2*NCC/3=O][a1122h-1b_1-5][a1122h-1a_1-5]/1-1-2-3/a4-b1_b4-c1_c?-d1",
"WURCS": "WURCS=2.0/3,4,3/[a2122h-1b_1-5_2*NCC/3=O][a1122h-1b_1-5][a1122h-1a_1-5]/1-1-2-3/a4-b1_b4-c1_c?-d1",
"input": "freeEnd--?b1D-GlcNAc,p--4b1D-GlcNAc,p--4b1D-Man,p--?a1D-Man,p$MONO,Und,0,0,freeEnd",
"GlycoCT": "RES\n1b:b-dglc-HEX-1:5\n2s:n-acetyl\n3b:b-dglc-HEX-1:5\n4s:n-acetyl\n5b:b-dman-HEX-1:5\n6b:a-dman-HEX-1:5\nLIN\n1:1d(2+1)2n\n2:1o(4+1)3d\n3:3d(2+1)4n\n4:3o(4+1)5d\n5:5o(-1+1)6d"
}
]
```

Copy

Please contact the server administrator with any questions or problems, [support@glycosmos.org](mailto:support@glycosmos.org).

No comments yet.
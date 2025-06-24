GlycanFormatConverter API | Wiki.js

---

---

Page Contents

Talk

View Discussion

Last edited by

Masaaki Shiota

12/18/2023

- [GlycanFormatConverter](https://gitlab.com/glycoinfo/glycanformatconverter) 2.10.0
- [WURCSFramework](https://gitlab.com/glycoinfo/wurcsframework) 1.2.14

Convert GlycoCT format to WURCS format and retrieve GlyTouCan accession number. Line breaks and plus signs (+) must be encoded.

- Parameters
- **glycoct**: string (required) - GlycoCT format text.
- [Example](https://api.glycosmos.org/glycanformatconverter/2.10.0/glycoct2wurcs/RES%0D%0A1b%3Ax-dglc-HEX-1%3A5%0D%0A2s%3An-acetyl%0D%0A3b%3Ab-dglc-HEX-1%3A5%0D%0A4s%3An-acetyl%0D%0A5b%3Ab-dman-HEX-1%3A5%0D%0A6b%3Aa-dman-HEX-1%3A5%0D%0A7b%3Aa-dman-HEX-1%3A5%0D%0ALIN%0D%0A1%3A1d%282%2B1%292n%0D%0A2%3A1o%284%2B1%293d%0D%0A3%3A3d%282%2B1%294n%0D%0A4%3A3o%284%2B1%295d%0D%0A5%3A5o%283%2B1%296d%0D%0A6%3A5o%286%2B1%297d)
- Response
- Body

```
{
"id": "G20624LQ",
"wurcs": "WURCS=2.0/4,5,4/[a2122h-1x_1-5_2*NCC/3=O][a2122h-1b_1-5_2*NCC/3=O][a1122h-1b_1-5][a1122h-1a_1-5]/1-2-3-4-4/a4-b1_b4-c1_c3-d1_c6-e1",
"WURCS": "WURCS=2.0/4,5,4/[a2122h-1x_1-5_2*NCC/3=O][a2122h-1b_1-5_2*NCC/3=O][a1122h-1b_1-5][a1122h-1a_1-5]/1-2-3-4-4/a4-b1_b4-c1_c3-d1_c6-e1",
"input": "RES\r\n1b:x-dglc-HEX-1:5\r\n2s:n-acetyl\r\n3b:b-dglc-HEX-1:5\r\n4s:n-acetyl\r\n5b:b-dman-HEX-1:5\r\n6b:a-dman-HEX-1:5\r\n7b:a-dman-HEX-1:5\r\nLIN\r\n1:1d(2+1)2n\r\n2:1o(4+1)3d\r\n3:3d(2+1)4n\r\n4:3o(4+1)5d\r\n5:5o(3+1)6d\r\n6:5o(6+1)7d"
}
```

Copy

- Example

```
curl -d '["RES\n1b:x-dglc-HEX-1:5\n2s:n-acetyl\n3b:b-dglc-HEX-1:5\n4s:n-acetyl\n5b:b-dman-HEX-1:5\n6b:a-dman-HEX-1:5\n7b:a-dman-HEX-1:5\nLIN\n1:1d(2+1)2n\n2:1o(4+1)3d\n3:3d(2+1)4n\n4:3o(4+1)5d\n5:5o(3+1)6d\n6:5o(6+1)7d"]' https://api.glycosmos.org/glycanformatconverter/2.10.0/glycoct2wurcs
```

Copy

- Request
- Body

```
["RES\n1b:x-dglc-HEX-1:5\n2s:n-acetyl\n3b:b-dglc-HEX-1:5\n4s:n-acetyl\n5b:b-dman-HEX-1:5\n6b:a-dman-HEX-1:5\n7b:a-dman-HEX-1:5\nLIN\n1:1d(2+1)2n\n2:1o(4+1)3d\n3:3d(2+1)4n\n4:3o(4+1)5d\n5:5o(3+1)6d\n6:5o(6+1)7d"]
```

Copy

- Response
- Body

```
[
{
"id": "G20624LQ",
"wurcs": "WURCS=2.0/4,5,4/[a2122h-1x_1-5_2*NCC/3=O][a2122h-1b_1-5_2*NCC/3=O][a1122h-1b_1-5][a1122h-1a_1-5]/1-2-3-4-4/a4-b1_b4-c1_c3-d1_c6-e1",
"WURCS": "WURCS=2.0/4,5,4/[a2122h-1x_1-5_2*NCC/3=O][a2122h-1b_1-5_2*NCC/3=O][a1122h-1b_1-5][a1122h-1a_1-5]/1-2-3-4-4/a4-b1_b4-c1_c3-d1_c6-e1",
"input": "RES\n1b:x-dglc-HEX-1:5\n2s:n-acetyl\n3b:b-dglc-HEX-1:5\n4s:n-acetyl\n5b:b-dman-HEX-1:5\n6b:a-dman-HEX-1:5\n7b:a-dman-HEX-1:5\nLIN\n1:1d(2+1)2n\n2:1o(4+1)3d\n3:3d(2+1)4n\n4:3o(4+1)5d\n5:5o(3+1)6d\n6:5o(6+1)7d"
}
]
```

Copy

Convert IUPAC Extended format to WURCS format and retrieve GlyTouCan accession number.

- Parameters
- **iupacextended**: string (required) - IUPAC Extended format text.
- [Example](https://api.glycosmos.org/glycanformatconverter/2.10.0/iupacextended2wurcs/%CE%B1-D-Manp-%281%E2%86%923%29%5B%CE%B1-D-Manp-%281%E2%86%926%29%5D-%CE%B2-D-Manp-%281%E2%86%924%29-%CE%B2-D-GlcpNAc-%281%E2%86%924%29-%CE%B2-D-GlcpNAc-%281%E2%86%92)
- Response
- Body

```
{
"id": "G22768VO",
"wurcs": "WURCS=2.0/3,5,4/[a2122h-1b_1-5_2*NCC/3=O][a1122h-1b_1-5][a1122h-1a_1-5]/1-1-2-3-3/a4-b1_b4-c1_c3-d1_c6-e1",
"WURCS": "WURCS=2.0/3,5,4/[a2122h-1b_1-5_2*NCC/3=O][a1122h-1b_1-5][a1122h-1a_1-5]/1-1-2-3-3/a4-b1_b4-c1_c3-d1_c6-e1",
"input": "α-D-Manp-(1→3)[α-D-Manp-(1→6)]-β-D-Manp-(1→4)-β-D-GlcpNAc-(1→4)-β-D-GlcpNAc-(1→"
}
```

Copy

- Example

```
curl -d '["α-D-Manp-(1→3)[α-D-Manp-(1→6)]-β-D-Manp-(1→4)-β-D-GlcpNAc-(1→4)-β-D-GlcpNAc-(1→"]' https://api.glycosmos.org/glycanformatconverter/2.10.0/iupacextended2wurcs
```

Copy

- Request
- Body

```
["α-D-Manp-(1→3)[α-D-Manp-(1→6)]-β-D-Manp-(1→4)-β-D-GlcpNAc-(1→4)-β-D-GlcpNAc-(1→"]
```

Copy

- Response
- Body

```
[
{
"id": "G22768VO",
"wurcs": "WURCS=2.0/3,5,4/[a2122h-1b_1-5_2*NCC/3=O][a1122h-1b_1-5][a1122h-1a_1-5]/1-1-2-3-3/a4-b1_b4-c1_c3-d1_c6-e1",
"WURCS": "WURCS=2.0/3,5,4/[a2122h-1b_1-5_2*NCC/3=O][a1122h-1b_1-5][a1122h-1a_1-5]/1-1-2-3-3/a4-b1_b4-c1_c3-d1_c6-e1",
"input": "α-D-Manp-(1→3)[α-D-Manp-(1→6)]-β-D-Manp-(1→4)-β-D-GlcpNAc-(1→4)-β-D-GlcpNAc-(1→"
}
]
```

Copy

Convert IUPAC Condensed format to WURCS format and retrieve GlyTouCan accession number.

- Parameters
- **iupaccondensed**: string (required) - IUPAC Condensed format text.
- [Example](https://api.glycosmos.org/glycanformatconverter/2.10.0/iupaccondensed2wurcs/Man%28a1-3%29%5BMan%28a1-6%29%5DMan%28b1-4%29GlcNAc%28b1-4%29GlcNAc%28b1-)
- Response
- Body

```
{
"id": "G22768VO",
"wurcs": "WURCS=2.0/3,5,4/[a2122h-1b_1-5_2*NCC/3=O][a1122h-1b_1-5][a1122h-1a_1-5]/1-1-2-3-3/a4-b1_b4-c1_c3-d1_c6-e1",
"WURCS": "WURCS=2.0/3,5,4/[a2122h-1b_1-5_2*NCC/3=O][a1122h-1b_1-5][a1122h-1a_1-5]/1-1-2-3-3/a4-b1_b4-c1_c3-d1_c6-e1",
"input": "Man(a1-3)[Man(a1-6)]Man(b1-4)GlcNAc(b1-4)GlcNAc(b1-"
}
```

Copy

- Example

```
curl -d '["Man(a1-3)[Man(a1-6)]Man(b1-4)GlcNAc(b1-4)GlcNAc(b1-"]' https://api.glycosmos.org/glycanformatconverter/2.10.0/iupaccondensed2wurcs
```

Copy

- Request
- Body

```
["Man(a1-3)[Man(a1-6)]Man(b1-4)GlcNAc(b1-4)GlcNAc(b1-"]
```

Copy

- Response
- Body

```
[
{
"id": "G22768VO",
"wurcs": "WURCS=2.0/3,5,4/[a2122h-1b_1-5_2*NCC/3=O][a1122h-1b_1-5][a1122h-1a_1-5]/1-1-2-3-3/a4-b1_b4-c1_c3-d1_c6-e1",
"WURCS": "WURCS=2.0/3,5,4/[a2122h-1b_1-5_2*NCC/3=O][a1122h-1b_1-5][a1122h-1a_1-5]/1-1-2-3-3/a4-b1_b4-c1_c3-d1_c6-e1",
"input": "Man(a1-3)[Man(a1-6)]Man(b1-4)GlcNAc(b1-4)GlcNAc(b1-"
}
]
```

Copy

Convert LinearCode format to WURCS format and retrieve GlyTouCan accession number.

- Parameters
- **linearcode**: string (required) - LinearCode format text.
- [Example](https://api.glycosmos.org/glycanformatconverter/2.10.0/linearcode2wurcs/Ma3%28Ma6%29Mb4GNb4GN)
- Response
- Body

```
{
"id": "G20624LQ",
"wurcs": "WURCS=2.0/4,5,4/[a2122h-1x_1-5_2*NCC/3=O][a2122h-1b_1-5_2*NCC/3=O][a1122h-1b_1-5][a1122h-1a_1-5]/1-2-3-4-4/a4-b1_b4-c1_c3-d1_c6-e1",
"WURCS": "WURCS=2.0/4,5,4/[a2122h-1x_1-5_2*NCC/3=O][a2122h-1b_1-5_2*NCC/3=O][a1122h-1b_1-5][a1122h-1a_1-5]/1-2-3-4-4/a4-b1_b4-c1_c3-d1_c6-e1",
"input": "Ma3(Ma6)Mb4GNb4GN"
}
```

Copy

- Example

```
curl -d '["Ma3(Ma6)Mb4GNb4GN"]' https://api.glycosmos.org/glycanformatconverter/2.10.0/linearcode2wurcs
```

Copy

- Request
- Body

```
["Ma3(Ma6)Mb4GNb4GN"]
```

Copy

- Response
- Body

```
[
{
"id": "G20624LQ",
"wurcs": "WURCS=2.0/4,5,4/[a2122h-1x_1-5_2*NCC/3=O][a2122h-1b_1-5_2*NCC/3=O][a1122h-1b_1-5][a1122h-1a_1-5]/1-2-3-4-4/a4-b1_b4-c1_c3-d1_c6-e1",
"WURCS": "WURCS=2.0/4,5,4/[a2122h-1x_1-5_2*NCC/3=O][a2122h-1b_1-5_2*NCC/3=O][a1122h-1b_1-5][a1122h-1a_1-5]/1-2-3-4-4/a4-b1_b4-c1_c3-d1_c6-e1",
"input": "Ma3(Ma6)Mb4GNb4GN"
}
]
```

Copy

Convert KCF format to WURCS format and retrieve GlyTouCan accession number. Spaces and line breaks must be encoded.

- Parameters
- **kcf**: string (required) - KCF format text.
- [Example](https://api.glycosmos.org/glycanformatconverter/2.10.0/kcf2wurcs/ENTRY%20%20%20%20%20XYZ%20%20%20%20%20%20%20%20%20%20Glycan%0ANODE%20%20%20%20%20%205%0A1%20%20%20%20%20GlcNAc%20%20%20%20%2015.0%20%20%20%20%207.0%0A2%20%20%20%20%20GlcNAc%20%20%20%20%20%208.0%20%20%20%20%207.0%0A3%20%20%20%20%20Man%20%20%20%20%20%20%20%20%201.0%20%20%20%20%207.0%0A4%20%20%20%20%20Man%20%20%20%20%20%20%20%20-6.0%20%20%20%2012.0%0A5%20%20%20%20%20Man%20%20%20%20%20%20%20%20-6.0%20%20%20%20%202.0%0AEDGE%20%20%20%20%20%204%0A1%20%20%20%20%202%3Ab1%20%20%20%20%20%20%201%3A4%0A2%20%20%20%20%203%3Ab1%20%20%20%20%20%20%202%3A4%0A3%20%20%20%20%205%3Aa1%20%20%20%20%20%20%203%3A3%0A4%20%20%20%20%204%3Aa1%20%20%20%20%20%20%203%3A6%0A%2F%2F%2F)
- Response
- Body

```
{
"id": "G20624LQ",
"wurcs": "WURCS=2.0/4,5,4/[a2122h-1x_1-5_2*NCC/3=O][a2122h-1b_1-5_2*NCC/3=O][a1122h-1b_1-5][a1122h-1a_1-5]/1-2-3-4-4/a4-b1_b4-c1_c3-d1_c6-e1",
"WURCS": "WURCS=2.0/4,5,4/[a2122h-1x_1-5_2*NCC/3=O][a2122h-1b_1-5_2*NCC/3=O][a1122h-1b_1-5][a1122h-1a_1-5]/1-2-3-4-4/a4-b1_b4-c1_c3-d1_c6-e1",
"input": "ENTRY     XYZ          Glycan\nNODE      5\n1     GlcNAc     15.0     7.0\n2     GlcNAc      8.0     7.0\n3     Man         1.0     7.0\n4     Man        -6.0    12.0\n5     Man        -6.0     2.0\nEDGE      4\n1     2:b1       1:4\n2     3:b1       2:4\n3     5:a1       3:3\n4     4:a1       3:6\n///"
}
```

Copy

- Example

```
curl -d '["ENTRY     XYZ          Glycan\nNODE      5\n1     GlcNAc     15.0     7.0\n2     GlcNAc      8.0     7.0\n3     Man         1.0     7.0\n4     Man        -6.0    12.0\n5     Man        -6.0     2.0\nEDGE      4\n1     2:b1       1:4\n2     3:b1       2:4\n3     5:a1       3:3\n4     4:a1       3:6\n///"]' https://api.glycosmos.org/glycanformatconverter/2.10.0/kcf2wurcs
```

Copy

- Request
- Body

```
["ENTRY     XYZ          Glycan\nNODE      5\n1     GlcNAc     15.0     7.0\n2     GlcNAc      8.0     7.0\n3     Man         1.0     7.0\n4     Man        -6.0    12.0\n5     Man        -6.0     2.0\nEDGE      4\n1     2:b1       1:4\n2     3:b1       2:4\n3     5:a1       3:3\n4     4:a1       3:6\n///"]
```

Copy

- Response
- Body

```
[
{
"id": "G20624LQ",
"wurcs": "WURCS=2.0/4,5,4/[a2122h-1x_1-5_2*NCC/3=O][a2122h-1b_1-5_2*NCC/3=O][a1122h-1b_1-5][a1122h-1a_1-5]/1-2-3-4-4/a4-b1_b4-c1_c3-d1_c6-e1",
"WURCS": "WURCS=2.0/4,5,4/[a2122h-1x_1-5_2*NCC/3=O][a2122h-1b_1-5_2*NCC/3=O][a1122h-1b_1-5][a1122h-1a_1-5]/1-2-3-4-4/a4-b1_b4-c1_c3-d1_c6-e1",
"input": "ENTRY     XYZ          Glycan\nNODE      5\n1     GlcNAc     15.0     7.0\n2     GlcNAc      8.0     7.0\n3     Man         1.0     7.0\n4     Man        -6.0    12.0\n5     Man        -6.0     2.0\nEDGE      4\n1     2:b1       1:4\n2     3:b1       2:4\n3     5:a1       3:3\n4     4:a1       3:6\n///"
}
]
```

Copy

Convert WURCS-JSON format to WURCS format.

- Parameters
- **wurcsjson**: string (required) - WURCS-JSON format text.
- [Example](https://api.glycosmos.org/glycanformatconverter/2.10.0/wurcsjson2wurcs/%7B%22Composition%22%3A%7B%7D%2C%22WURCS%22%3A%22%22%2C%22Aglycone%22%3A%22%22%2C%22Fragments%22%3A%7B%7D%2C%22Repeat%22%3A%7B%7D%2C%22Edges%22%3A%7B%22e0%22%3A%7B%22Acceptor%22%3A%7B%22Position%22%3A%5B4%5D%2C%22Node%22%3A%22m0%22%2C%22LinkageType%22%3A%22H_AT_OH%22%7D%2C%22Donor%22%3A%7B%22Position%22%3A%5B1%5D%2C%22Node%22%3A%22m1%22%2C%22LinkageType%22%3A%22DEOXY%22%7D%2C%22Probability%22%3A%7B%22High%22%3A1%2C%22Low%22%3A1%7D%7D%2C%22e1%22%3A%7B%22Acceptor%22%3A%7B%22Position%22%3A%5B4%5D%2C%22Node%22%3A%22m1%22%2C%22LinkageType%22%3A%22H_AT_OH%22%7D%2C%22Donor%22%3A%7B%22Position%22%3A%5B1%5D%2C%22Node%22%3A%22m2%22%2C%22LinkageType%22%3A%22DEOXY%22%7D%2C%22Probability%22%3A%7B%22High%22%3A1%2C%22Low%22%3A1%7D%7D%2C%22e2%22%3A%7B%22Acceptor%22%3A%7B%22Position%22%3A%5B3%5D%2C%22Node%22%3A%22m2%22%2C%22LinkageType%22%3A%22H_AT_OH%22%7D%2C%22Donor%22%3A%7B%22Position%22%3A%5B1%5D%2C%22Node%22%3A%22m3%22%2C%22LinkageType%22%3A%22DEOXY%22%7D%2C%22Probability%22%3A%7B%22High%22%3A1%2C%22Low%22%3A1%7D%7D%2C%22e3%22%3A%7B%22Acceptor%22%3A%7B%22Position%22%3A%5B6%5D%2C%22Node%22%3A%22m2%22%2C%22LinkageType%22%3A%22H_AT_OH%22%7D%2C%22Donor%22%3A%7B%22Position%22%3A%5B1%5D%2C%22Node%22%3A%22m4%22%2C%22LinkageType%22%3A%22DEOXY%22%7D%2C%22Probability%22%3A%7B%22High%22%3A1%2C%22Low%22%3A1%7D%7D%7D%2C%22AN%22%3A%22%22%2C%22Bridge%22%3A%7B%7D%2C%22Monosaccharides%22%3A%7B%22m0%22%3A%7B%22Modifications%22%3A%5B%5D%2C%22TrivialName%22%3A%5B%22glc%22%5D%2C%22Substituents%22%3A%5B%7B%22Status%22%3A%22simple%22%2C%22Acceptor%22%3A%7B%22Position%22%3A%5B2%5D%2C%22LinkageType%22%3A%22DEOXY%22%7D%2C%22Donor%22%3A%7B%22Position%22%3A%5B0%5D%2C%22LinkageType%22%3A%22NONMONOSACCHARIDE%22%7D%2C%22Probability%22%3A%7B%22High%22%3A1%2C%22Low%22%3A1%7D%2C%22Notation%22%3A%22NAc%22%7D%5D%2C%22Configuration%22%3A%5B%22d%22%5D%2C%22SuperClass%22%3A%22HEX%22%2C%22RingSize%22%3A%22p%22%2C%22AnomState%22%3A%22x%22%2C%22AnomPosition%22%3A1%2C%22Notation%22%3A%22GlcNAc%22%7D%2C%22m1%22%3A%7B%22Modifications%22%3A%5B%5D%2C%22TrivialName%22%3A%5B%22glc%22%5D%2C%22Substituents%22%3A%5B%7B%22Status%22%3A%22simple%22%2C%22Acceptor%22%3A%7B%22Position%22%3A%5B2%5D%2C%22LinkageType%22%3A%22DEOXY%22%7D%2C%22Donor%22%3A%7B%22Position%22%3A%5B0%5D%2C%22LinkageType%22%3A%22NONMONOSACCHARIDE%22%7D%2C%22Probability%22%3A%7B%22High%22%3A1%2C%22Low%22%3A1%7D%2C%22Notation%22%3A%22NAc%22%7D%5D%2C%22Configuration%22%3A%5B%22d%22%5D%2C%22SuperClass%22%3A%22HEX%22%2C%22RingSize%22%3A%22p%22%2C%22AnomState%22%3A%22b%22%2C%22AnomPosition%22%3A1%2C%22Notation%22%3A%22GlcNAc%22%7D%2C%22m2%22%3A%7B%22Modifications%22%3A%5B%5D%2C%22TrivialName%22%3A%5B%22man%22%5D%2C%22Substituents%22%3A%5B%5D%2C%22Configuration%22%3A%5B%22d%22%5D%2C%22SuperClass%22%3A%22HEX%22%2C%22RingSize%22%3A%22p%22%2C%22AnomState%22%3A%22b%22%2C%22AnomPosition%22%3A1%2C%22Notation%22%3A%22Man%22%7D%2C%22m3%22%3A%7B%22Modifications%22%3A%5B%5D%2C%22TrivialName%22%3A%5B%22man%22%5D%2C%22Substituents%22%3A%5B%5D%2C%22Configuration%22%3A%5B%22d%22%5D%2C%22SuperClass%22%3A%22HEX%22%2C%22RingSize%22%3A%22p%22%2C%22AnomState%22%3A%22a%22%2C%22AnomPosition%22%3A1%2C%22Notation%22%3A%22Man%22%7D%2C%22m4%22%3A%7B%22Modifications%22%3A%5B%5D%2C%22TrivialName%22%3A%5B%22man%22%5D%2C%22Substituents%22%3A%5B%5D%2C%22Configuration%22%3A%5B%22d%22%5D%2C%22SuperClass%22%3A%22HEX%22%2C%22RingSize%22%3A%22p%22%2C%22AnomState%22%3A%22a%22%2C%22AnomPosition%22%3A1%2C%22Notation%22%3A%22Man%22%7D%7D%7D)
- Response
- Body

```
{
"id": "G20624LQ",
"wurcs": "WURCS=2.0/4,5,4/[a2122h-1x_1-5_2*NCC/3=O][a2122h-1b_1-5_2*NCC/3=O][a1122h-1b_1-5][a1122h-1a_1-5]/1-2-3-4-4/a4-b1_b4-c1_c3-d1_c6-e1",
"WURCS": "WURCS=2.0/4,5,4/[a2122h-1x_1-5_2*NCC/3=O][a2122h-1b_1-5_2*NCC/3=O][a1122h-1b_1-5][a1122h-1a_1-5]/1-2-3-4-4/a4-b1_b4-c1_c3-d1_c6-e1"
}
```

Copy

- Example

```
curl -d '["{\"Composition\":{},\"WURCS\":\"\",\"Aglycone\":\"\",\"Fragments\":{},\"Repeat\":{},\"Edges\":{\"e0\":{\"Acceptor\":{\"Position\":[4],\"Node\":\"m0\",\"LinkageType\":\"H_AT_OH\"},\"Donor\":{\"Position\":[1],\"Node\":\"m1\",\"LinkageType\":\"DEOXY\"},\"Probability\":{\"High\":1,\"Low\":1}},\"e1\":{\"Acceptor\":{\"Position\":[4],\"Node\":\"m1\",\"LinkageType\":\"H_AT_OH\"},\"Donor\":{\"Position\":[1],\"Node\":\"m2\",\"LinkageType\":\"DEOXY\"},\"Probability\":{\"High\":1,\"Low\":1}},\"e2\":{\"Acceptor\":{\"Position\":[3],\"Node\":\"m2\",\"LinkageType\":\"H_AT_OH\"},\"Donor\":{\"Position\":[1],\"Node\":\"m3\",\"LinkageType\":\"DEOXY\"},\"Probability\":{\"High\":1,\"Low\":1}},\"e3\":{\"Acceptor\":{\"Position\":[6],\"Node\":\"m2\",\"LinkageType\":\"H_AT_OH\"},\"Donor\":{\"Position\":[1],\"Node\":\"m4\",\"LinkageType\":\"DEOXY\"},\"Probability\":{\"High\":1,\"Low\":1}}},\"AN\":\"\",\"Bridge\":{},\"Monosaccharides\":{\"m0\":{\"Modifications\":[],\"TrivialName\":[\"glc\"],\"Substituents\":[{\"Status\":\"simple\",\"Acceptor\":{\"Position\":[2],\"LinkageType\":\"DEOXY\"},\"Donor\":{\"Position\":[0],\"LinkageType\":\"NONMONOSACCHARIDE\"},\"Probability\":{\"High\":1,\"Low\":1},\"Notation\":\"NAc\"}],\"Configuration\":[\"d\"],\"SuperClass\":\"HEX\",\"RingSize\":\"p\",\"AnomState\":\"x\",\"AnomPosition\":1,\"Notation\":\"GlcNAc\"},\"m1\":{\"Modifications\":[],\"TrivialName\":[\"glc\"],\"Substituents\":[{\"Status\":\"simple\",\"Acceptor\":{\"Position\":[2],\"LinkageType\":\"DEOXY\"},\"Donor\":{\"Position\":[0],\"LinkageType\":\"NONMONOSACCHARIDE\"},\"Probability\":{\"High\":1,\"Low\":1},\"Notation\":\"NAc\"}],\"Configuration\":[\"d\"],\"SuperClass\":\"HEX\",\"RingSize\":\"p\",\"AnomState\":\"b\",\"AnomPosition\":1,\"Notation\":\"GlcNAc\"},\"m2\":{\"Modifications\":[],\"TrivialName\":[\"man\"],\"Substituents\":[],\"Configuration\":[\"d\"],\"SuperClass\":\"HEX\",\"RingSize\":\"p\",\"AnomState\":\"b\",\"AnomPosition\":1,\"Notation\":\"Man\"},\"m3\":{\"Modifications\":[],\"TrivialName\":[\"man\"],\"Substituents\":[],\"Configuration\":[\"d\"],\"SuperClass\":\"HEX\",\"RingSize\":\"p\",\"AnomState\":\"a\",\"AnomPosition\":1,\"Notation\":\"Man\"},\"m4\":{\"Modifications\":[],\"TrivialName\":[\"man\"],\"Substituents\":[],\"Configuration\":[\"d\"],\"SuperClass\":\"HEX\",\"RingSize\":\"p\",\"AnomState\":\"a\",\"AnomPosition\":1,\"Notation\":\"Man\"}}}"]' https://api.glycosmos.org/glycanformatconverter/2.10.0/wurcsjson2wurcs
```

Copy

- Request
- Body

```
["{\"Composition\":{},\"WURCS\":\"\",\"Aglycone\":\"\",\"Fragments\":{},\"Repeat\":{},\"Edges\":{\"e0\":{\"Acceptor\":{\"Position\":[4],\"Node\":\"m0\",\"LinkageType\":\"H_AT_OH\"},\"Donor\":{\"Position\":[1],\"Node\":\"m1\",\"LinkageType\":\"DEOXY\"},\"Probability\":{\"High\":1,\"Low\":1}},\"e1\":{\"Acceptor\":{\"Position\":[4],\"Node\":\"m1\",\"LinkageType\":\"H_AT_OH\"},\"Donor\":{\"Position\":[1],\"Node\":\"m2\",\"LinkageType\":\"DEOXY\"},\"Probability\":{\"High\":1,\"Low\":1}},\"e2\":{\"Acceptor\":{\"Position\":[3],\"Node\":\"m2\",\"LinkageType\":\"H_AT_OH\"},\"Donor\":{\"Position\":[1],\"Node\":\"m3\",\"LinkageType\":\"DEOXY\"},\"Probability\":{\"High\":1,\"Low\":1}},\"e3\":{\"Acceptor\":{\"Position\":[6],\"Node\":\"m2\",\"LinkageType\":\"H_AT_OH\"},\"Donor\":{\"Position\":[1],\"Node\":\"m4\",\"LinkageType\":\"DEOXY\"},\"Probability\":{\"High\":1,\"Low\":1}}},\"AN\":\"\",\"Bridge\":{},\"Monosaccharides\":{\"m0\":{\"Modifications\":[],\"TrivialName\":[\"glc\"],\"Substituents\":[{\"Status\":\"simple\",\"Acceptor\":{\"Position\":[2],\"LinkageType\":\"DEOXY\"},\"Donor\":{\"Position\":[0],\"LinkageType\":\"NONMONOSACCHARIDE\"},\"Probability\":{\"High\":1,\"Low\":1},\"Notation\":\"NAc\"}],\"Configuration\":[\"d\"],\"SuperClass\":\"HEX\",\"RingSize\":\"p\",\"AnomState\":\"x\",\"AnomPosition\":1,\"Notation\":\"GlcNAc\"},\"m1\":{\"Modifications\":[],\"TrivialName\":[\"glc\"],\"Substituents\":[{\"Status\":\"simple\",\"Acceptor\":{\"Position\":[2],\"LinkageType\":\"DEOXY\"},\"Donor\":{\"Position\":[0],\"LinkageType\":\"NONMONOSACCHARIDE\"},\"Probability\":{\"High\":1,\"Low\":1},\"Notation\":\"NAc\"}],\"Configuration\":[\"d\"],\"SuperClass\":\"HEX\",\"RingSize\":\"p\",\"AnomState\":\"b\",\"AnomPosition\":1,\"Notation\":\"GlcNAc\"},\"m2\":{\"Modifications\":[],\"TrivialName\":[\"man\"],\"Substituents\":[],\"Configuration\":[\"d\"],\"SuperClass\":\"HEX\",\"RingSize\":\"p\",\"AnomState\":\"b\",\"AnomPosition\":1,\"Notation\":\"Man\"},\"m3\":{\"Modifications\":[],\"TrivialName\":[\"man\"],\"Substituents\":[],\"Configuration\":[\"d\"],\"SuperClass\":\"HEX\",\"RingSize\":\"p\",\"AnomState\":\"a\",\"AnomPosition\":1,\"Notation\":\"Man\"},\"m4\":{\"Modifications\":[],\"TrivialName\":[\"man\"],\"Substituents\":[],\"Configuration\":[\"d\"],\"SuperClass\":\"HEX\",\"RingSize\":\"p\",\"AnomState\":\"a\",\"AnomPosition\":1,\"Notation\":\"Man\"}}}"]
```

Copy

- Response
- Body

```
[
{
"id": "G20624LQ",
"wurcs": "WURCS=2.0/4,5,4/[a2122h-1x_1-5_2*NCC/3=O][a2122h-1b_1-5_2*NCC/3=O][a1122h-1b_1-5][a1122h-1a_1-5]/1-2-3-4-4/a4-b1_b4-c1_c3-d1_c6-e1",
"WURCS": "WURCS=2.0/4,5,4/[a2122h-1x_1-5_2*NCC/3=O][a2122h-1b_1-5_2*NCC/3=O][a1122h-1b_1-5][a1122h-1a_1-5]/1-2-3-4-4/a4-b1_b4-c1_c3-d1_c6-e1"
}
]
```

Copy

Convert WURCS format to GlycoCT format.

- Parameters
- **wurcs**: string (required) - WURCS format text.
- [Example](https://api.glycosmos.org/glycanformatconverter/2.10.0/wurcs2glycoct/WURCS%3D2.0%2F3%2C5%2C4%2F%5Ba2122h-1b_1-5_2%2ANCC%2F3%3DO%5D%5Ba1122h-1b_1-5%5D%5Ba1122h-1a_1-5%5D%2F1-1-2-3-3%2Fa4-b1_b4-c1_c3-d1_c6-e1)
- Response
- Body

```
{
"input": "WURCS=2.0/3,5,4/[a2122h-1b_1-5_2*NCC/3=O][a1122h-1b_1-5][a1122h-1a_1-5]/1-1-2-3-3/a4-b1_b4-c1_c3-d1_c6-e1",
"GlycoCT": "RES\n1b:b-dglc-HEX-1:5\n2s:n-acetyl\n3b:b-dglc-HEX-1:5\n4s:n-acetyl\n5b:b-dman-HEX-1:5\n6b:a-dman-HEX-1:5\n7b:a-dman-HEX-1:5\nLIN\n1:1d(2+1)2n\n2:1o(4+1)3d\n3:3d(2+1)4n\n4:3o(4+1)5d\n5:5o(3+1)6d\n6:5o(6+1)7d\n"
}
```

Copy

- Example

```
curl -d '["WURCS=2.0/3,5,4/[a2122h-1b_1-5_2*NCC/3=O][a1122h-1b_1-5][a1122h-1a_1-5]/1-1-2-3-3/a4-b1_b4-c1_c3-d1_c6-e1"]' https://api.glycosmos.org/glycanformatconverter/2.10.0/wurcs2glycoct
```

Copy

- Request
- Body

```
["WURCS=2.0/3,5,4/[a2122h-1b_1-5_2*NCC/3=O][a1122h-1b_1-5][a1122h-1a_1-5]/1-1-2-3-3/a4-b1_b4-c1_c3-d1_c6-e1"]
```

Copy

- Response
- Body

```
[
{
"input": "WURCS=2.0/3,5,4/[a2122h-1b_1-5_2*NCC/3=O][a1122h-1b_1-5][a1122h-1a_1-5]/1-1-2-3-3/a4-b1_b4-c1_c3-d1_c6-e1",
"GlycoCT": "RES\n1b:b-dglc-HEX-1:5\n2s:n-acetyl\n3b:b-dglc-HEX-1:5\n4s:n-acetyl\n5b:b-dman-HEX-1:5\n6b:a-dman-HEX-1:5\n7b:a-dman-HEX-1:5\nLIN\n1:1d(2+1)2n\n2:1o(4+1)3d\n3:3d(2+1)4n\n4:3o(4+1)5d\n5:5o(3+1)6d\n6:5o(6+1)7d\n"
}
]
```

Copy

Convert WURCS format to IUPAC Extended format.

- Parameters
- **wurcs**: string (required) - WURCS format text.
- [Example](https://api.glycosmos.org/glycanformatconverter/2.10.0/wurcs2iupacextended/WURCS%3D2.0%2F3%2C5%2C4%2F%5Ba2122h-1b_1-5_2%2ANCC%2F3%3DO%5D%5Ba1122h-1b_1-5%5D%5Ba1122h-1a_1-5%5D%2F1-1-2-3-3%2Fa4-b1_b4-c1_c3-d1_c6-e1)
- Response
- Body

```
{
"input": "WURCS=2.0/3,5,4/[a2122h-1b_1-5_2*NCC/3=O][a1122h-1b_1-5][a1122h-1a_1-5]/1-1-2-3-3/a4-b1_b4-c1_c3-d1_c6-e1",
"IUPACextended": "α-D-Manp-(1→3)[α-D-Manp-(1→6)]-β-D-Manp-(1→4)-β-D-GlcpNAc-(1→4)-β-D-GlcpNAc-(1→"
}
```

Copy

- Example

```
curl -d '["WURCS=2.0/3,5,4/[a2122h-1b_1-5_2*NCC/3=O][a1122h-1b_1-5][a1122h-1a_1-5]/1-1-2-3-3/a4-b1_b4-c1_c3-d1_c6-e1"]' https://api.glycosmos.org/glycanformatconverter/2.10.0/wurcs2iupacextended
```

Copy

- Request
- Body

```
["WURCS=2.0/3,5,4/[a2122h-1b_1-5_2*NCC/3=O][a1122h-1b_1-5][a1122h-1a_1-5]/1-1-2-3-3/a4-b1_b4-c1_c3-d1_c6-e1"]
```

Copy

- Response
- Body

```
[
{
"input": "WURCS=2.0/3,5,4/[a2122h-1b_1-5_2*NCC/3=O][a1122h-1b_1-5][a1122h-1a_1-5]/1-1-2-3-3/a4-b1_b4-c1_c3-d1_c6-e1",
"IUPACextended": "α-D-Manp-(1→3)[α-D-Manp-(1→6)]-β-D-Manp-(1→4)-β-D-GlcpNAc-(1→4)-β-D-GlcpNAc-(1→"
}
]
```

Copy

Convert WURCS format to IUPAC Condensed format.

- Parameters
- **wurcs**: string (required) - WURCS format text.
- [Example](https://api.glycosmos.org/glycanformatconverter/2.10.0/wurcs2iupaccondensed/WURCS%3D2.0%2F3%2C5%2C4%2F%5Ba2122h-1b_1-5_2%2ANCC%2F3%3DO%5D%5Ba1122h-1b_1-5%5D%5Ba1122h-1a_1-5%5D%2F1-1-2-3-3%2Fa4-b1_b4-c1_c3-d1_c6-e1)
- Response
- Body

```
{
"input": "WURCS=2.0/3,5,4/[a2122h-1b_1-5_2*NCC/3=O][a1122h-1b_1-5][a1122h-1a_1-5]/1-1-2-3-3/a4-b1_b4-c1_c3-d1_c6-e1",
"IUPACcondensed": "Man(a1-3)[Man(a1-6)]Man(b1-4)GlcNAc(b1-4)GlcNAc(b1-"
}
```

Copy

- Example

```
curl -d '["WURCS=2.0/3,5,4/[a2122h-1b_1-5_2*NCC/3=O][a1122h-1b_1-5][a1122h-1a_1-5]/1-1-2-3-3/a4-b1_b4-c1_c3-d1_c6-e1"]' https://api.glycosmos.org/glycanformatconverter/2.10.0/wurcs2iupaccondensed
```

Copy

- Request
- Body

```
["WURCS=2.0/3,5,4/[a2122h-1b_1-5_2*NCC/3=O][a1122h-1b_1-5][a1122h-1a_1-5]/1-1-2-3-3/a4-b1_b4-c1_c3-d1_c6-e1"]
```

Copy

- Response
- Body

```
[
{
"input": "WURCS=2.0/3,5,4/[a2122h-1b_1-5_2*NCC/3=O][a1122h-1b_1-5][a1122h-1a_1-5]/1-1-2-3-3/a4-b1_b4-c1_c3-d1_c6-e1",
"IUPACcondensed": "Man(a1-3)[Man(a1-6)]Man(b1-4)GlcNAc(b1-4)GlcNAc(b1-"
}
]
```

Copy

Convert WURCS format to GLYCAM sequence.

- Parameters
- **wurcs**: string (required) - WURCS format text.
- [Example](https://api.glycosmos.org/glycanformatconverter/2.10.0/wurcs2glycam/WURCS%3D2.0%2F3%2C5%2C4%2F%5Ba2122h-1b_1-5_2%2ANCC%2F3%3DO%5D%5Ba1122h-1b_1-5%5D%5Ba1122h-1a_1-5%5D%2F1-1-2-3-3%2Fa4-b1_b4-c1_c3-d1_c6-e1)
- Response
- Body

```
{
"input": "WURCS=2.0/3,5,4/[a2122h-1b_1-5_2*NCC/3=O][a1122h-1b_1-5][a1122h-1a_1-5]/1-1-2-3-3/a4-b1_b4-c1_c3-d1_c6-e1",
"GLYCAM": "DManpa1-3[DManpa1-6]DManpb1-4DGlcpNAcb1-4DGlcpNAcb1-OH"
}
```

Copy

- Example

```
curl -d '["WURCS=2.0/3,5,4/[a2122h-1b_1-5_2*NCC/3=O][a1122h-1b_1-5][a1122h-1a_1-5]/1-1-2-3-3/a4-b1_b4-c1_c3-d1_c6-e1"]' https://api.glycosmos.org/glycanformatconverter/2.10.0/wurcs2glycam
```

Copy

- Request
- Body

```
["WURCS=2.0/3,5,4/[a2122h-1b_1-5_2*NCC/3=O][a1122h-1b_1-5][a1122h-1a_1-5]/1-1-2-3-3/a4-b1_b4-c1_c3-d1_c6-e1"]
```

Copy

- Response
- Body

```
[
{
"input": "WURCS=2.0/3,5,4/[a2122h-1b_1-5_2*NCC/3=O][a1122h-1b_1-5][a1122h-1a_1-5]/1-1-2-3-3/a4-b1_b4-c1_c3-d1_c6-e1",
"GLYCAM": "DManpa1-3[DManpa1-6]DManpb1-4DGlcpNAcb1-4DGlcpNAcb1-OH"
}
]
```

Copy

Convert WURCS format to WURCS-JSON format.

- Parameters
- **wurcs**: string (required) - WURCS format text.
- [Example](https://api.glycosmos.org/glycanformatconverter/2.10.0/wurcs2wurcsjson/WURCS%3D2.0%2F4%2C5%2C4%2F%5Ba2122h-1x_1-5_2%2ANCC%2F3%3DO%5D%5Ba2122h-1b_1-5_2%2ANCC%2F3%3DO%5D%5Ba1122h-1b_1-5%5D%5Ba1122h-1a_1-5%5D%2F1-2-3-4-4%2Fa4-b1_b4-c1_c3-d1_c6-e1)
- Response
- Body

```
{
"Composition": {},
"WURCS": "",
"Aglycone": "",
"Fragments": {},
"Repeat": {},
"Edges": {
"e0": {
"Acceptor": {
"Position": [
4
],
"Node": "m0",
"LinkageType": "H_AT_OH"
},
"Donor": {
"Position": [
1
],
"Node": "m1",
"LinkageType": "DEOXY"
},
"Probability": {
"High": 1,
"Low": 1
}
},
"e1": {
"Acceptor": {
"Position": [
4
],
"Node": "m1",
"LinkageType": "H_AT_OH"
},
"Donor": {
"Position": [
1
],
"Node": "m2",
"LinkageType": "DEOXY"
},
"Probability": {
"High": 1,
"Low": 1
}
},
"e2": {
"Acceptor": {
"Position": [
3
],
"Node": "m2",
"LinkageType": "H_AT_OH"
},
"Donor": {
"Position": [
1
],
"Node": "m3",
"LinkageType": "DEOXY"
},
"Probability": {
"High": 1,
"Low": 1
}
},
"e3": {
"Acceptor": {
"Position": [
6
],
"Node": "m2",
"LinkageType": "H_AT_OH"
},
"Donor": {
"Position": [
1
],
"Node": "m4",
"LinkageType": "DEOXY"
},
"Probability": {
"High": 1,
"Low": 1
}
}
},
"AN": "",
"Bridge": {},
"Monosaccharides": {
"m0": {
"Modifications": [],
"TrivialName": [
"glc"
],
"Substituents": [
{
"Status": "simple",
"Acceptor": {
"Position": [
2
],
"LinkageType": "DEOXY"
},
"Donor": {
"Position": [
0
],
"LinkageType": "NONMONOSACCHARIDE"
},
"Probability": {
"High": 1,
"Low": 1
},
"Notation": "NAc"
}
],
"Configuration": [
"d"
],
"SuperClass": "HEX",
"RingSize": "p",
"AnomState": "x",
"AnomPosition": 1,
"Notation": "GlcNAc"
},
"m1": {
"Modifications": [],
"TrivialName": [
"glc"
],
"Substituents": [
{
"Status": "simple",
"Acceptor": {
"Position": [
2
],
"LinkageType": "DEOXY"
},
"Donor": {
"Position": [
0
],
"LinkageType": "NONMONOSACCHARIDE"
},
"Probability": {
"High": 1,
"Low": 1
},
"Notation": "NAc"
}
],
"Configuration": [
"d"
],
"SuperClass": "HEX",
"RingSize": "p",
"AnomState": "b",
"AnomPosition": 1,
"Notation": "GlcNAc"
},
"m2": {
"Modifications": [],
"TrivialName": [
"man"
],
"Substituents": [],
"Configuration": [
"d"
],
"SuperClass": "HEX",
"RingSize": "p",
"AnomState": "b",
"AnomPosition": 1,
"Notation": "Man"
},
"m3": {
"Modifications": [],
"TrivialName": [
"man"
],
"Substituents": [],
"Configuration": [
"d"
],
"SuperClass": "HEX",
"RingSize": "p",
"AnomState": "a",
"AnomPosition": 1,
"Notation": "Man"
},
"m4": {
"Modifications": [],
"TrivialName": [
"man"
],
"Substituents": [],
"Configuration": [
"d"
],
"SuperClass": "HEX",
"RingSize": "p",
"AnomState": "a",
"AnomPosition": 1,
"Notation": "Man"
}
}
}
```

Copy

- Example

```
curl -d '["WURCS=2.0/4,5,4/[a2122h-1x_1-5_2*NCC/3=O][a2122h-1b_1-5_2*NCC/3=O][a1122h-1b_1-5][a1122h-1a_1-5]/1-2-3-4-4/a4-b1_b4-c1_c3-d1_c6-e1"]' https://api.glycosmos.org/glycanformatconverter/2.10.0/wurcs2wurcsjson
```

Copy

- Request
- Body

```
["WURCS=2.0/4,5,4/[a2122h-1x_1-5_2*NCC/3=O][a2122h-1b_1-5_2*NCC/3=O][a1122h-1b_1-5][a1122h-1a_1-5]/1-2-3-4-4/a4-b1_b4-c1_c3-d1_c6-e1"]
```

Copy

- Response
- Body

```
[
{
"Composition": {},
"WURCS": "",
"Aglycone": "",
"Fragments": {},
"Repeat": {},
"Edges": {
"e0": {
"Acceptor": {
"Position": [
4
],
"Node": "m0",
"LinkageType": "H_AT_OH"
},
"Donor": {
"Position": [
1
],
"Node": "m1",
"LinkageType": "DEOXY"
},
"Probability": {
"High": 1,
"Low": 1
}
},
"e1": {
"Acceptor": {
"Position": [
4
],
"Node": "m1",
"LinkageType": "H_AT_OH"
},
"Donor": {
"Position": [
1
],
"Node": "m2",
"LinkageType": "DEOXY"
},
"Probability": {
"High": 1,
"Low": 1
}
},
"e2": {
"Acceptor": {
"Position": [
3
],
"Node": "m2",
"LinkageType": "H_AT_OH"
},
"Donor": {
"Position": [
1
],
"Node": "m3",
"LinkageType": "DEOXY"
},
"Probability": {
"High": 1,
"Low": 1
}
},
"e3": {
"Acceptor": {
"Position": [
6
],
"Node": "m2",
"LinkageType": "H_AT_OH"
},
"Donor": {
"Position": [
1
],
"Node": "m4",
"LinkageType": "DEOXY"
},
"Probability": {
"High": 1,
"Low": 1
}
}
},
"AN": "",
"Bridge": {},
"Monosaccharides": {
"m0": {
"Modifications": [],
"TrivialName": [
"glc"
],
"Substituents": [
{
"Status": "simple",
"Acceptor": {
"Position": [
2
],
"LinkageType": "DEOXY"
},
"Donor": {
"Position": [
0
],
"LinkageType": "NONMONOSACCHARIDE"
},
"Probability": {
"High": 1,
"Low": 1
},
"Notation": "NAc"
}
],
"Configuration": [
"d"
],
"SuperClass": "HEX",
"RingSize": "p",
"AnomState": "x",
"AnomPosition": 1,
"Notation": "GlcNAc"
},
"m1": {
"Modifications": [],
"TrivialName": [
"glc"
],
"Substituents": [
{
"Status": "simple",
"Acceptor": {
"Position": [
2
],
"LinkageType": "DEOXY"
},
"Donor": {
"Position": [
0
],
"LinkageType": "NONMONOSACCHARIDE"
},
"Probability": {
"High": 1,
"Low": 1
},
"Notation": "NAc"
}
],
"Configuration": [
"d"
],
"SuperClass": "HEX",
"RingSize": "p",
"AnomState": "b",
"AnomPosition": 1,
"Notation": "GlcNAc"
},
"m2": {
"Modifications": [],
"TrivialName": [
"man"
],
"Substituents": [],
"Configuration": [
"d"
],
"SuperClass": "HEX",
"RingSize": "p",
"AnomState": "b",
"AnomPosition": 1,
"Notation": "Man"
},
"m3": {
"Modifications": [],
"TrivialName": [
"man"
],
"Substituents": [],
"Configuration": [
"d"
],
"SuperClass": "HEX",
"RingSize": "p",
"AnomState": "a",
"AnomPosition": 1,
"Notation": "Man"
},
"m4": {
"Modifications": [],
"TrivialName": [
"man"
],
"Substituents": [],
"Configuration": [
"d"
],
"SuperClass": "HEX",
"RingSize": "p",
"AnomState": "a",
"AnomPosition": 1,
"Notation": "Man"
}
}
}
]
```

Copy

Normalize WURCS format and retrieve GlyTouCan accession number.

- Parameters
- **wurcs**: string (required) - WURCS format text.
- [Example](https://api.beta.glycosmos.org/glycanformatconverter/2.10.0/wurcs2wurcs/WURCS%3D2.0%2F3%2C5%2C4%2F%5Ba2122h-1b_1-5_2%2ANCC%2F3%3DO%5D%5Ba1122h-1b_1-5%5D%5Ba1122h-1a_1-5%5D%2F1-1-2-3-3%2Fa4-b1_b4-c1_c3-d1_c6-e1)
- Response
- Body

```
{
"id": "G22768VO",
"wurcs": "WURCS=2.0/3,5,4/[a2122h-1b_1-5_2*NCC/3=O][a1122h-1b_1-5][a1122h-1a_1-5]/1-1-2-3-3/a4-b1_b4-c1_c3-d1_c6-e1",
"WURCS": "WURCS=2.0/3,5,4/[a2122h-1b_1-5_2*NCC/3=O][a1122h-1b_1-5][a1122h-1a_1-5]/1-1-2-3-3/a4-b1_b4-c1_c3-d1_c6-e1"
}
```

Copy

- Example

```
curl -d '["WURCS=2.0/3,5,4/[a2122h-1b_1-5_2*NCC/3=O][a1122h-1b_1-5][a1122h-1a_1-5]/1-1-2-3-3/a4-b1_b4-c1_c3-d1_c6-e1"]' https://api.glycosmos.org/glycanformatconverter/2.10.0/wurcs2wurcs
```

Copy

- Request
- Body

```
["WURCS=2.0/3,5,4/[a2122h-1b_1-5_2*NCC/3=O][a1122h-1b_1-5][a1122h-1a_1-5]/1-1-2-3-3/a4-b1_b4-c1_c3-d1_c6-e1"]
```

Copy

- Response
- Body

```
[
{
"id": "G22768VO",
"wurcs": "WURCS=2.0/3,5,4/[a2122h-1b_1-5_2*NCC/3=O][a1122h-1b_1-5][a1122h-1a_1-5]/1-1-2-3-3/a4-b1_b4-c1_c3-d1_c6-e1",
"WURCS": "WURCS=2.0/3,5,4/[a2122h-1b_1-5_2*NCC/3=O][a1122h-1b_1-5][a1122h-1a_1-5]/1-1-2-3-3/a4-b1_b4-c1_c3-d1_c6-e1"
}
]
```

Copy

Normalize GlycoCT format (GlycoCT to GlycoCT) convert an incorrect GlycoCT into a normalized one.

- Parameters
- **glycoct**: string (required) - GlycoCT format text.
- [Example](https://api.glycosmos.org/glycanformatconverter/2.10.0/glycoct2glycoct/RES%0D%0A1b%3Ax-dglc-HEX-1%3A5%0D%0A2s%3An-acetyl%0D%0A3b%3Ab-dglc-HEX-1%3A5%0D%0A4s%3An-acetyl%0D%0A5b%3Ab-dman-HEX-1%3A5%0D%0A6b%3Aa-dman-HEX-1%3A5%0D%0A7b%3Aa-dman-HEX-1%3A5%0D%0ALIN%0D%0A1%3A1d%282%2B1%292n%0D%0A2%3A1o%284%2B1%293d%0D%0A3%3A3d%282%2B1%294n%0D%0A4%3A3o%284%2B1%295d%0D%0A5%3A5o%283%2B1%296d%0D%0A6%3A5o%286%2B1%297d)
- Response
- Body

```
{
"input": "RES\r\n1b:x-dglc-HEX-1:5\r\n2s:n-acetyl\r\n3b:b-dglc-HEX-1:5\r\n4s:n-acetyl\r\n5b:b-dman-HEX-1:5\r\n6b:a-dman-HEX-1:5\r\n7b:a-dman-HEX-1:5\r\nLIN\r\n1:1d(2+1)2n\r\n2:1o(4+1)3d\r\n3:3d(2+1)4n\r\n4:3o(4+1)5d\r\n5:5o(3+1)6d\r\n6:5o(6+1)7d",
"GlycoCT": "RES\n1b:x-dglc-HEX-1:5\n2s:n-acetyl\n3b:b-dglc-HEX-1:5\n4s:n-acetyl\n5b:b-dman-HEX-1:5\n6b:a-dman-HEX-1:5\n7b:a-dman-HEX-1:5\nLIN\n1:1d(2+1)2n\n2:1o(4+1)3d\n3:3d(2+1)4n\n4:3o(4+1)5d\n5:5o(3+1)6d\n6:5o(6+1)7d\n"
}
```

Copy

- Example

```
curl -d '["RES\n1b:x-dglc-HEX-1:5\n2s:n-acetyl\n3b:b-dglc-HEX-1:5\n4s:n-acetyl\n5b:b-dman-HEX-1:5\n6b:a-dman-HEX-1:5\n7b:a-dman-HEX-1:5\nLIN\n1:1d(2+1)2n\n2:1o(4+1)3d\n3:3d(2+1)4n\n4:3o(4+1)5d\n5:5o(3+1)6d\n6:5o(6+1)7d"]' https://api.glycosmos.org/glycanformatconverter/2.10.0/glycoct2glycoct
```

Copy

- Request
- Body

```
["RES\n1b:x-dglc-HEX-1:5\n2s:n-acetyl\n3b:b-dglc-HEX-1:5\n4s:n-acetyl\n5b:b-dman-HEX-1:5\n6b:a-dman-HEX-1:5\n7b:a-dman-HEX-1:5\nLIN\n1:1d(2+1)2n\n2:1o(4+1)3d\n3:3d(2+1)4n\n4:3o(4+1)5d\n5:5o(3+1)6d\n6:5o(6+1)7d"]
```

Copy

- Response
- Body

```
[
{
"input": "RES\n1b:x-dglc-HEX-1:5\n2s:n-acetyl\n3b:b-dglc-HEX-1:5\n4s:n-acetyl\n5b:b-dman-HEX-1:5\n6b:a-dman-HEX-1:5\n7b:a-dman-HEX-1:5\nLIN\n1:1d(2+1)2n\n2:1o(4+1)3d\n3:3d(2+1)4n\n4:3o(4+1)5d\n5:5o(3+1)6d\n6:5o(6+1)7d",
"GlycoCT": "RES\n1b:x-dglc-HEX-1:5\n2s:n-acetyl\n3b:b-dglc-HEX-1:5\n4s:n-acetyl\n5b:b-dman-HEX-1:5\n6b:a-dman-HEX-1:5\n7b:a-dman-HEX-1:5\nLIN\n1:1d(2+1)2n\n2:1o(4+1)3d\n3:3d(2+1)4n\n4:3o(4+1)5d\n5:5o(3+1)6d\n6:5o(6+1)7d\n"
}
]
```

Copy

GlycanFormatConverter API is available in the following versions. Each version is supported for a limited time.

- [Version 2.5.2](https://api.glycosmos.org/glycanformatconverter/#version-2.5.2) (through December 2023)
- [Version 2.7.0](https://api.glycosmos.org/glycanformatconverter/#version-2.7.0) (through December 2024)
- [Version 2.8.2](https://api.glycosmos.org/glycanformatconverter/#version-2.8.2) (through December 2025)

Please contact the server administrator with any questions or problems, [support@glycosmos.org](mailto:support@glycosmos.org).

*Loading comments...*
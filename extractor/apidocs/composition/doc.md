Composition API | Wiki.js

---

---

Page Contents

Talk

View Discussion

Last edited by

Masaaki Shiota

12/20/2023

- [GlycanCompositionConverter](https://gitlab.com/glycosmos/glycompconverter) 1.0.0
- [WURCSFramework](https://gitlab.com/glycoinfo/wurcsframework) 1.2.14

Convert composition text to WURCS format.

- Parameters
- **composition**: string (required) - composition text.
- [Example](https://api.glycosmos.org/glycancompositionconverter/1.0.0/composition2wurcs/Hex:3%7CHexNAc:2)
- Response
- Body

```
WURCS=2.0/2,5,4/[axxxxh-1x_1-5_2*NCC/3=O][axxxxh-1x_1-5]/1-1-2-2-2/a?|b?|c?|d?|e?}-{a?|b?|c?|d?|e?_a?|b?|c?|d?|e?}-{a?|b?|c?|d?|e?_a?|b?|c?|d?|e?}-{a?|b?|c?|d?|e?_a?|b?|c?|d?|e?}-{a?|b?|c?|d?|e?
```

Copy

- Example

```
curl -d '[{"hex":"1","hexnac":"2","dhex":"3","neu5ac":"1","neu5gc":"0","P":"1","S":"1","Ac":"1"},{"hex":"1","hexnac":"2","dhex":"3","neu5ac":"1","neu5gc":"0","P":"0","S":"0","Ac":"0"},{"hex":"2","hexnac":"1","dhex":"0","neu5ac":"0","neu5gc":"0","P":"1","S":"0","Ac":"0"},{"hex":"2","hexnac":"1","dhex":"1","neu5ac":"2","neu5gc":"1","P":"0","S":"1","Ac":"0"},{"hex":"2","hexnac":"1","dhex":"1","neu5ac":"2","neu5gc":"1","P":"0","S":"0","Ac":"1"}]' https://api.glycosmos.org/glycancompositionconverter/1.0.0/composition2wurcs
```

Copy

- Request
- Body

```
[
{
"hex": "1",
"hexnac": "2",
"dhex": "3",
"neu5ac": "1",
"neu5gc": "0",
"P": "1",
"S": "1",
"Ac": "1"
},
{
"hex": "1",
"hexnac": "2",
"dhex": "3",
"neu5ac": "1",
"neu5gc": "0",
"P": "0",
"S": "0",
"Ac": "0"
},
{
"hex": "2",
"hexnac": "1",
"dhex": "0",
"neu5ac": "0",
"neu5gc": "0",
"P": "1",
"S": "0",
"Ac": "0"
},
{
"hex": "2",
"hexnac": "1",
"dhex": "1",
"neu5ac": "2",
"neu5gc": "1",
"P": "0",
"S": "1",
"Ac": "0"
},
{
"hex": "2",
"hexnac": "1",
"dhex": "1",
"neu5ac": "2",
"neu5gc": "1",
"P": "0",
"S": "0",
"Ac": "1"
}
]
```

Copy

- Response
- Body

```
{
"data": [
{
"P": "1",
"Ac": "1",
"neu5ac": "1",
"S": "1",
"wurcs": "WURCS=2.0/4,7,9/[Aad21122h-2x_2-6_5*NCC/3=O][axxxxm-1x_1-5][axxxxh-1x_1-5_2*NCC/3=O][axxxxh-1x_1-5]/1-2-2-2-3-3-4/a?|b?|c?|d?|e?|f?|g?}*OCC/3=O_a?|b?|c?|d?|e?|f?|g?}*OPO/3O/3=O_a?|b?|c?|d?|e?|f?|g?}*OSO/3=O/3=O_a?|b?|c?|d?|e?|f?|g?}-{a?|b?|c?|d?|e?|f?|g?_a?|b?|c?|d?|e?|f?|g?}-{a?|b?|c?|d?|e?|f?|g?_a?|b?|c?|d?|e?|f?|g?}-{a?|b?|c?|d?|e?|f?|g?_a?|b?|c?|d?|e?|f?|g?}-{a?|b?|c?|d?|e?|f?|g?_a?|b?|c?|d?|e?|f?|g?}-{a?|b?|c?|d?|e?|f?|g?_a?|b?|c?|d?|e?|f?|g?}-{a?|b?|c?|d?|e?|f?|g?",
"dhex": "3",
"hex": "1",
"hexnac": "2",
"id": "G42666LT"
},
{
"neu5ac": "1",
"wurcs": "WURCS=2.0/4,7,6/[Aad21122h-2x_2-6_5*NCC/3=O][axxxxm-1x_1-5][axxxxh-1x_1-5_2*NCC/3=O][axxxxh-1x_1-5]/1-2-2-2-3-3-4/a?|b?|c?|d?|e?|f?|g?}-{a?|b?|c?|d?|e?|f?|g?_a?|b?|c?|d?|e?|f?|g?}-{a?|b?|c?|d?|e?|f?|g?_a?|b?|c?|d?|e?|f?|g?}-{a?|b?|c?|d?|e?|f?|g?_a?|b?|c?|d?|e?|f?|g?}-{a?|b?|c?|d?|e?|f?|g?_a?|b?|c?|d?|e?|f?|g?}-{a?|b?|c?|d?|e?|f?|g?_a?|b?|c?|d?|e?|f?|g?}-{a?|b?|c?|d?|e?|f?|g?",
"dhex": "3",
"hex": "1",
"hexnac": "2",
"id": "G75682RP"
},
{
"P": "1",
"wurcs": "WURCS=2.0/2,3,3/[axxxxh-1x_1-5_2*NCC/3=O][axxxxh-1x_1-5]/1-2-2/a?|b?|c?}*OPO/3O/3=O_a?|b?|c?}-{a?|b?|c?_a?|b?|c?}-{a?|b?|c?",
"hex": "2",
"hexnac": "1",
"id": "G20620DF"
},
{
"neu5ac": "2",
"S": "1",
"wurcs": "WURCS=2.0/5,7,7/[Aad21122h-2x_2-6_5*NCC/3=O][Aad21122h-2x_2-6_5*NCCO/3=O][axxxxm-1x_1-5][axxxxh-1x_1-5_2*NCC/3=O][axxxxh-1x_1-5]/1-1-2-3-4-5-5/a?|b?|c?|d?|e?|f?|g?}*OSO/3=O/3=O_a?|b?|c?|d?|e?|f?|g?}-{a?|b?|c?|d?|e?|f?|g?_a?|b?|c?|d?|e?|f?|g?}-{a?|b?|c?|d?|e?|f?|g?_a?|b?|c?|d?|e?|f?|g?}-{a?|b?|c?|d?|e?|f?|g?_a?|b?|c?|d?|e?|f?|g?}-{a?|b?|c?|d?|e?|f?|g?_a?|b?|c?|d?|e?|f?|g?}-{a?|b?|c?|d?|e?|f?|g?_a?|b?|c?|d?|e?|f?|g?}-{a?|b?|c?|d?|e?|f?|g?",
"dhex": "1",
"neu5gc": "1",
"hex": "2",
"hexnac": "1",
"id": "G84440AS"
},
{
"Ac": "1",
"neu5ac": "2",
"wurcs": "WURCS=2.0/5,7,7/[Aad21122h-2x_2-6_5*NCC/3=O][Aad21122h-2x_2-6_5*NCCO/3=O][axxxxm-1x_1-5][axxxxh-1x_1-5_2*NCC/3=O][axxxxh-1x_1-5]/1-1-2-3-4-5-5/a?|b?|c?|d?|e?|f?|g?}*OCC/3=O_a?|b?|c?|d?|e?|f?|g?}-{a?|b?|c?|d?|e?|f?|g?_a?|b?|c?|d?|e?|f?|g?}-{a?|b?|c?|d?|e?|f?|g?_a?|b?|c?|d?|e?|f?|g?}-{a?|b?|c?|d?|e?|f?|g?_a?|b?|c?|d?|e?|f?|g?}-{a?|b?|c?|d?|e?|f?|g?_a?|b?|c?|d?|e?|f?|g?}-{a?|b?|c?|d?|e?|f?|g?_a?|b?|c?|d?|e?|f?|g?}-{a?|b?|c?|d?|e?|f?|g?",
"dhex": "1",
"neu5gc": "1",
"hex": "2",
"hexnac": "1",
"id": ""
}
],
"keys": [
"hex",
"hexnac",
"dhex",
"neu5ac",
"P",
"S",
"Ac",
"neu5gc",
"wurcs",
"id"
]
}
```

Copy

<https://api.glycosmos.org/index.html#composition-api>

Please contact the server administrator with any questions or problems, [support@glycosmos.org](mailto:support@glycosmos.org).

*Loading comments...*
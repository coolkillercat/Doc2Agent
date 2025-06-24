WURCSFramework API | Wiki.js

---

---

Page Contents

Talk

View Discussion

Last edited by

Masaaki Shiota

12/18/2023

- [WURCSFramework](https://gitlab.com/glycoinfo/wurcsframework) 1.2.14

Validate WURCS to find errors and warnings.

- Parameters
- **wurcs**: string (required) - WURCS format text.
- [Example](https://api.glycosmos.org/wurcsframework/1.2.14/wurcsvalidator/WURCS%3D2.0%2F3%2C5%2C4%2F%5Ba2122h-1b_1-5_2%2ANCC%2F3%3DO%5D%5Ba1122h-1b_1-5%5D%5Ba1122h-1a_1-5%5D%2F1-1-2-3-3%2Fa4-b1_b4-c1_c3-d1_c6-e1)
- Response
- Body

```
{
"m_sStandardString": "WURCS=2.0/3,5,4/[a2122h-1b_1-5_2*NCC/3=O][a1122h-1b_1-5][a1122h-1a_1-5]/1-1-2-3-3/a4-b1_b4-c1_c3-d1_c6-e1",
"m_sInputString": "WURCS=2.0/3,5,4/[a2122h-1b_1-5_2*NCC/3=O][a1122h-1b_1-5][a1122h-1a_1-5]/1-1-2-3-3/a4-b1_b4-c1_c3-d1_c6-e1",
"m_mapTypeToReports": {
"ERROR": [],
"UNVERIFIABLE": [],
"WARNING": []
}
}
```

Copy

- Example

```
curl -d '["WURCS=2.0/3,5,4/[a2122h-1b_1-5_2*NCC/3=O][a1122h-1b_1-5][a1122h-1a_1-5]/1-1-2-3-3/a4-b1_b4-c1_c3-d1_c6-e1"]' https://api.glycosmos.org/wurcsframework/1.2.14/wurcsvalidator
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
"m_sStandardString": "WURCS=2.0/3,5,4/[a2122h-1b_1-5_2*NCC/3=O][a1122h-1b_1-5][a1122h-1a_1-5]/1-1-2-3-3/a4-b1_b4-c1_c3-d1_c6-e1",
"m_sInputString": "WURCS=2.0/3,5,4/[a2122h-1b_1-5_2*NCC/3=O][a1122h-1b_1-5][a1122h-1a_1-5]/1-1-2-3-3/a4-b1_b4-c1_c3-d1_c6-e1",
"m_mapTypeToReports": {
"ERROR": [],
"UNVERIFIABLE": [],
"WARNING": []
}
}
]
```

Copy

Calculate the mass from WURCS.

- Parameters
- **wurcs**: string (required) - WURCS format text.
- [Example](https://api.glycosmos.org/wurcsframework/1.2.14/wurcs2mass/WURCS%3D2.0%2F3%2C5%2C4%2F%5Ba2122h-1b_1-5_2%2ANCC%2F3%3DO%5D%5Ba1122h-1b_1-5%5D%5Ba1122h-1a_1-5%5D%2F1-1-2-3-3%2Fa4-b1_b4-c1_c3-d1_c6-e1)
- Response
- Body

```
{
"input": "WURCS=2.0/3,5,4/[a2122h-1b_1-5_2*NCC/3=O][a1122h-1b_1-5][a1122h-1a_1-5]/1-1-2-3-3/a4-b1_b4-c1_c3-d1_c6-e1",
"mass": 910.32778
}
```

Copy

- Example

```
curl -d '["WURCS=2.0/3,5,4/[a2122h-1b_1-5_2*NCC/3=O][a1122h-1b_1-5][a1122h-1a_1-5]/1-1-2-3-3/a4-b1_b4-c1_c3-d1_c6-e1"]' https://api.glycosmos.org/wurcsframework/1.2.14/wurcs2mass
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
"mass": 910.32778
}
]
```

Copy

Retrieve the anomeric symbol of the reducing end from WURCS.

- Parameters
- **wurcs**: string (required) - WURCS format text.
- [Example](https://api.glycosmos.org/wurcsframework/1.2.14/wurcs2anomer/WURCS%3D2.0%2F3%2C5%2C4%2F%5Ba2122h-1b_1-5_2%2ANCC%2F3%3DO%5D%5Ba1122h-1b_1-5%5D%5Ba1122h-1a_1-5%5D%2F1-1-2-3-3%2Fa4-b1_b4-c1_c3-d1_c6-e1)
- Response
- Body

```
{
"anomer": "b",
"input": "WURCS=2.0/3,5,4/[a2122h-1b_1-5_2*NCC/3=O][a1122h-1b_1-5][a1122h-1a_1-5]/1-1-2-3-3/a4-b1_b4-c1_c3-d1_c6-e1"
}
```

Copy

- Example

```
curl -d '["WURCS=2.0/3,5,4/[a2122h-1b_1-5_2*NCC/3=O][a1122h-1b_1-5][a1122h-1a_1-5]/1-1-2-3-3/a4-b1_b4-c1_c3-d1_c6-e1"]' https://api.glycosmos.org/wurcsframework/1.2.14/wurcs2anomer
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
"anomer": "b",
"input": "WURCS=2.0/3,5,4/[a2122h-1b_1-5_2*NCC/3=O][a1122h-1b_1-5][a1122h-1a_1-5]/1-1-2-3-3/a4-b1_b4-c1_c3-d1_c6-e1"
}
]
```

Copy

Determine if the composition WURCS is valid for glycosylation.

- Parameters
- **wurcs**: string (required) - WURCS format text.
- [Example](https://api.glycosmos.org/wurcsframework/1.2.14/compositionvalidator/WURCS%3D2.0%2F3%2C5%2C4%2F%5Ba2122h-1b_1-5_2%2ANCC%2F3%3DO%5D%5Ba1122h-1b_1-5%5D%5Ba1122h-1a_1-5%5D%2F1-1-2-3-3%2Fa4-b1_b4-c1_c3-d1_c6-e1)
- Response
- Body

```
{
"valid": true,
"input": "WURCS=2.0/3,5,4/[a2122h-1b_1-5_2*NCC/3=O][a1122h-1b_1-5][a1122h-1a_1-5]/1-1-2-3-3/a4-b1_b4-c1_c3-d1_c6-e1"
}
```

Copy

- Example

```
curl -d '["WURCS=2.0/3,5,4/[a2122h-1b_1-5_2*NCC/3=O][a1122h-1b_1-5][a1122h-1a_1-5]/1-1-2-3-3/a4-b1_b4-c1_c3-d1_c6-e1"]' https://api.glycosmos.org/wurcsframework/1.2.14/compositionvalidator
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
"valid": true,
"input": "WURCS=2.0/3,5,4/[a2122h-1b_1-5_2*NCC/3=O][a1122h-1b_1-5][a1122h-1a_1-5]/1-1-2-3-3/a4-b1_b4-c1_c3-d1_c6-e1"
}
]
```

Copy

<https://api.glycosmos.org/wurcsframework/>

Please contact the server administrator with any questions or problems, [support@glycosmos.org](mailto:support@glycosmos.org).

*Loading comments...*
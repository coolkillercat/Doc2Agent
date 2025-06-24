## Add a GPG key for a given user

DETAILS:
**Tier:** Free, Premium, Ultimate
**Offering:** Self-managed, GitLab Dedicated

Create new GPG key owned by the specified user. Available only for administrator.

```plaintext
POST /users/:id/gpg_keys
```

Parameters:

| Attribute | Type    | Required | Description           |
| --------- | ------- | -------- | --------------------- |
| `id`      | integer | yes      | ID of the user    |
| `key_id`  | integer | yes      | ID of the GPG key |

```shell
curl --data-urlencode "key=-----BEGIN PGP PUBLIC KEY BLOCK-----
> xsBNBFVjnlIBCACibzXOLCiZiL2oyzYUaTOCkYnSUhymg3pdbfKtd4mpBa58xKBj
> t1pTHVpw3Sk03wmzhM/Ndlt1AV2YhLv++83WKr+gAHFYFiCV/tnY8bx3HqvVoy8O
> CfxWhw4QZK7+oYzVmJj8ZJm3ZjOC4pzuegNWlNLCUdZDx9OKlHVXLCX1iUbjdYWa
> qKV6tdV8hZolkbyjedQgrpvoWyeSHHpwHF7yk4gNJWMMI5rpcssL7i6mMXb/sDzO
> VaAtU5wiVducsOa01InRFf7QSTxoAm6Xy0PGv/k48M6xCALa9nY+BzlOv47jUT57
> vilf4Szy9dKD0v9S0mQ+IHB+gNukWrnwtXx5ABEBAAHNFm5hbWUgKGNvbW1lbnQp
> IDxlbUBpbD7CwHUEEwECACkFAlVjnlIJEINgJNgv009/AhsDAhkBBgsJCAcDAgYV
> CAIJCgsEFgIDAQAAxqMIAFBHuBA8P1v8DtHonIK8Lx2qU23t8Mh68HBIkSjk2H7/
> oO2cDWCw50jZ9D91PXOOyMPvBWV2IE3tARzCvnNGtzEFRtpIEtZ0cuctxeIF1id5
> crfzdMDsmZyRHAOoZ9VtuD6mzj0ybQWMACb7eIHjZDCee3Slh3TVrLy06YRdq2I4
> bjMOPePtK5xnIpHGpAXkB3IONxyITpSLKsA4hCeP7gVvm7r7TuQg1ygiUBlWbBYn
> iE5ROzqZjG1s7dQNZK/riiU2umGqGuwAb2IPvNiyuGR3cIgRE4llXH/rLuUlspAp
> o4nlxaz65VucmNbN1aMbDXLJVSqR1DuE00vEsL1AItI=
> =XQoy
> -----END PGP PUBLIC KEY BLOCK-----" \
     --header "PRIVATE-TOKEN: <your_access_token>" "https://gitlab.example.com/api/v4/users/2/gpg_keys"
```

Example response:

```json
[
    {
        "id": 1,
        "key": "-----BEGIN PGP PUBLIC KEY BLOCK-----\nxsBNBFVjnlIBCACibzXOLCiZiL2oyzYUaTOCkYnSUhymg3pdbfKtd4mpBa58xKBj\nt1pTHVpw3Sk03wmzhM/Ndlt1AV2YhLv++83WKr+gAHFYFiCV/tnY8bx3HqvVoy8O\nCfxWhw4QZK7+oYzVmJj8ZJm3ZjOC4pzuegNWlNLCUdZDx9OKlHVXLCX1iUbjdYWa\nqKV6tdV8hZolkbyjedQgrpvoWyeSHHpwHF7yk4gNJWMMI5rpcssL7i6mMXb/sDzO\nVaAtU5wiVducsOa01InRFf7QSTxoAm6Xy0PGv/k48M6xCALa9nY+BzlOv47jUT57\nvilf4Szy9dKD0v9S0mQ+IHB+gNukWrnwtXx5ABEBAAHNFm5hbWUgKGNvbW1lbnQp\nIDxlbUBpbD7CwHUEEwECACkFAlVjnlIJEINgJNgv009/AhsDAhkBBgsJCAcDAgYV\nCAIJCgsEFgIDAQAAxqMIAFBHuBA8P1v8DtHonIK8Lx2qU23t8Mh68HBIkSjk2H7/\noO2cDWCw50jZ9D91PXOOyMPvBWV2IE3tARzCvnNGtzEFRtpIEtZ0cuctxeIF1id5\ncrfzdMDsmZyRHAOoZ9VtuD6mzj0ybQWMACb7eIHjZDCee3Slh3TVrLy06YRdq2I4\nbjMOPePtK5xnIpHGpAXkB3IONxyITpSLKsA4hCeP7gVvm7r7TuQg1ygiUBlWbBYn\niE5ROzqZjG1s7dQNZK/riiU2umGqGuwAb2IPvNiyuGR3cIgRE4llXH/rLuUlspAp\no4nlxaz65VucmNbN1aMbDXLJVSqR1DuE00vEsL1AItI=\n=XQoy\n-----END PGP PUBLIC KEY BLOCK-----",
        "created_at": "2017-09-05T09:17:46.264Z"
    }
]
```


## Get signature of a commit

Get the [signature from a commit](../user/project/repository/signed_commits),
if it is signed. For unsigned commits, it results in a 404 response.

```plaintext
GET /projects/:id/repository/commits/:sha/signature
```

Parameters:

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `id`      | integer/string | yes | The ID or [URL-encoded path of the project](rest/index.md#namespaced-path-encoding) owned by the authenticated user |
| `sha` | string | yes | The commit hash or name of a repository branch or tag |

```shell
curl --header "PRIVATE-TOKEN: <your_access_token>" \
  --url "https://gitlab.example.com/api/v4/projects/1/repository/commits/da738facbc19eb2fc2cef57c49be0e6038570352/signature"
```

Example response if commit is GPG signed:

```json
{
  "signature_type": "PGP",
  "verification_status": "verified",
  "gpg_key_id": 1,
  "gpg_key_primary_keyid": "8254AAB3FBD54AC9",
  "gpg_key_user_name": "John Doe",
  "gpg_key_user_email": "johndoe@example.com",
  "gpg_key_subkey_id": null,
  "commit_source": "gitaly"
}
```

Example response if commit is signed with SSH:

```json
{
  "signature_type": "SSH",
  "verification_status": "verified",
  "key": {
    "id": 11,
    "title": "Key",
    "created_at": "2023-05-08T09:12:38.503Z",
    "expires_at": "2024-05-07T00:00:00.000Z",
    "key": "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAILZzYDq6DhLp3aX84DGIV3F6Vf+Ae4yCTTz7RnqMJOlR MyKey)",
    "usage_type": "auth_and_signing"
  },
  "commit_source": "gitaly"
}
```

Example response if commit is X.509 signed:

```json
{
  "signature_type": "X509",
  "verification_status": "unverified",
  "x509_certificate": {
    "id": 1,
    "subject": "CN=gitlab@example.org,OU=Example,O=World",
    "subject_key_identifier": "BC:BC:BC:BC:BC:BC:BC:BC:BC:BC:BC:BC:BC:BC:BC:BC:BC:BC:BC:BC",
    "email": "gitlab@example.org",
    "serial_number": 278969561018901340486471282831158785578,
    "certificate_status": "good",
    "x509_issuer": {
      "id": 1,
      "subject": "CN=PKI,OU=Example,O=World",
      "subject_key_identifier": "AB:AB:AB:AB:AB:AB:AB:AB:AB:AB:AB:AB:AB:AB:AB:AB:AB:AB:AB:AB",
      "crl_url": "http://example.com/pki.crl"
    }
  },
  "commit_source": "gitaly"
}
```

Example response if commit is unsigned:

```json
{
  "message": "404 GPG Signature Not Found"
}
```

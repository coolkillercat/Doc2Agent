## Single SSH key for given user

> - [Introduced](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/81790) in GitLab 14.9.

Get a single key for a given user.

```plaintext
GET /users/:id/keys/:key_id
```

Parameters:

| Attribute | Type    | Required | Description          |
|-----------|---------|----------|----------------------|
| `id`      | integer | yes      | ID of specified user |
| `key_id`  | integer | yes      | SSH key ID           |

```json
{
  "id": 1,
  "title": "Public key",
  "key": "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAIEAiPWx6WM4lhHNedGfBpPJNPpZ7yKu+dnn1SJejgt4596k6YjzGGphH2TUxwKzxcKDKKezwkpfnxPkSMkuEspGRt/aZZ9wa++Oi7Qkr8prgHc4soW6NUlfDzpvZK2H5E7eQaSeP3SAwGmQKUFHCddNaP0L+hM7zhFNzjFvpaMgJw0=",
  "created_at": "2014-08-01T14:47:39.080Z"
}
```


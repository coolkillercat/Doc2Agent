## Add SSH key

> - The `usage_type` parameter was [introduced](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/105551) in GitLab 15.7.

Creates a new key owned by the authenticated user.

```plaintext
POST /user/keys
```

Parameters:

| Attribute    | Type   | Required | Description                                                                    |
|--------------|--------|----------|--------------------------------------------------------------------------------|
| `title`      | string | yes      | New SSH key's title                                                            |
| `key`        | string | yes      | New SSH key                                                                    |
| `expires_at` | string | no       | Expiration date of the SSH key in ISO 8601 format (`YYYY-MM-DDTHH:MM:SSZ`) |
| `usage_type` | string | no       | Scope of usage for the SSH key: `auth`, `signing` or `auth_and_signing`. Default: `auth_and_signing` |

```json
{
  "title": "ABC",
  "key": "ssh-dss AAAAB3NzaC1kc3MAAACBAMLrhYgI3atfrSD6KDas1b/3n6R/HP+bLaHHX6oh+L1vg31mdUqK0Ac/NjZoQunavoyzqdPYhFz9zzOezCrZKjuJDS3NRK9rspvjgM0xYR4d47oNZbdZbwkI4cTv/gcMlquRy0OvpfIvJtjtaJWMwTLtM5VhRusRuUlpH99UUVeXAAAAFQCVyX+92hBEjInEKL0v13c/egDCTQAAAIEAvFdWGq0ccOPbw4f/F8LpZqvWDydAcpXHV3thwb7WkFfppvm4SZte0zds1FJ+Hr8Xzzc5zMHe6J4Nlay/rP4ewmIW7iFKNBEYb/yWa+ceLrs+TfR672TaAgO6o7iSRofEq5YLdwgrwkMmIawa21FrZ2D9SPao/IwvENzk/xcHu7YAAACAQFXQH6HQnxOrw4dqf0NqeKy1tfIPxYYUZhPJfo9O0AmBW2S36pD2l14kS89fvz6Y1g8gN/FwFnRncMzlLY/hX70FSc/3hKBSbH6C6j8hwlgFKfizav21eS358JJz93leOakJZnGb8XlWvz1UJbwCsnR2VEY8Dz90uIk1l/UqHkA= loic@call",
  "expires_at": "2016-01-21T00:00:00.000Z",
  "usage_type": "auth"
}
```

Returns a created key with status `201 Created` on success. If an
error occurs a `400 Bad Request` is returned with a message explaining the error:

```json
{
  "message": {
    "fingerprint": [
      "has already been taken"
    ],
    "key": [
      "has already been taken"
    ]
  }
}
```


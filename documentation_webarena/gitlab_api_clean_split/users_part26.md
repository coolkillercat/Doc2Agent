## Delete SSH key for given user

DETAILS:
**Tier:** Free, Premium, Ultimate
**Offering:** Self-managed, GitLab Dedicated

Deletes key owned by a specified user. Available only for administrator.

```plaintext
DELETE /users/:id/keys/:key_id
```

Parameters:

| Attribute | Type    | Required | Description          |
|-----------|---------|----------|----------------------|
| `id`      | integer | yes      | ID of specified user |
| `key_id`  | integer | yes      | SSH key ID           |


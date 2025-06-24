## Delete authentication identity from user

DETAILS:
**Tier:** Free, Premium, Ultimate
**Offering:** Self-managed, GitLab Dedicated

Deletes a user's authentication identity using the provider name associated with that identity. Available only for administrators.

```plaintext
DELETE /users/:id/identities/:provider
```

Parameters:

| Attribute  | Type    | Required | Description            |
|------------|---------|----------|------------------------|
| `id`       | integer | yes      | ID of a user       |
| `provider` | string  | yes      | External provider name |


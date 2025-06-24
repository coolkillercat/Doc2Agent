## Delete SSH key for current user

Deletes key owned by the authenticated user.

This returns a `204 No Content` status code if the operation was successfully
or `404` if the resource was not found.

```plaintext
DELETE /user/keys/:key_id
```

Parameters:

| Attribute | Type    | Required | Description |
|-----------|---------|----------|-------------|
| `key_id`  | integer | yes      | SSH key ID  |


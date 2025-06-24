## User deletion

DETAILS:
**Tier:** Free, Premium, Ultimate
**Offering:** Self-managed, GitLab Dedicated

Deletes a user. Available only for administrators.
This returns a `204 No Content` status code if the operation was successfully, `404` if the resource was not found or `409` if the user cannot be soft deleted.

```plaintext
DELETE /users/:id
```

Parameters:

| Attribute     | Type    | Required | Description                                  |
|---------------|---------|----------|----------------------------------------------|
| `id`          | integer | yes      | ID of a user                             |
| `hard_delete` | boolean | no       | If true, contributions that would usually be [moved to Ghost User](../user/profile/account/delete_account.md#associated-records) are deleted instead, as well as groups owned solely by this user. |


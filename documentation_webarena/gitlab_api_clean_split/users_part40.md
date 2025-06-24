## Delete email for current user

Deletes the specified email address owned by the authenticated user. Cannot be used to delete a primary email address.

If the deleted email address is used for any user emails, those user emails are sent to the primary email address instead.

NOTE:
Because of [known issue](https://gitlab.com/gitlab-org/gitlab/-/issues/438600), group notifications are still sent to
the deleted email address.

```plaintext
DELETE /user/emails/:email_id
```

Parameters:

| Attribute  | Type    | Required | Description |
|------------|---------|----------|-------------|
| `email_id` | integer | yes      | Email ID    |

Returns:

- `204 No Content` if the operation was successful.
- `404` if the resource was not found.


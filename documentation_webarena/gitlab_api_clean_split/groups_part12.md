## Transfer a group to a new parent group / Turn a subgroup to a top-level group

Transfer a group to a new parent group or turn a subgroup to a top-level group. Available to administrators and users:

- With the Owner role for the group to transfer.
- With permission to [create a subgroup](../user/group/subgroups/index.md#create-a-subgroup) in the new parent group if transferring a group.
- With [permission to create a top-level group](../administration/user_settings.md) if turning a subgroup into a top-level group.

```plaintext
POST  /groups/:id/transfer
```

Parameters:

| Attribute    | Type           | Required | Description |
| ------------ | -------------- | -------- | ----------- |
| `id`         | integer | yes  | ID of the group to transfer. |
| `group_id`   | integer | no   | ID of the new parent group. When not specified, the group to transfer is instead turned into a top-level group. |

```shell
curl --request POST --header "PRIVATE-TOKEN: <your_access_token>" \
     "https://gitlab.example.com/api/v4/groups/4/transfer?group_id=7"
```


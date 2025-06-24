## New Subgroup

This is similar to creating a [New group](#new-group). You need the `parent_id` from the [List groups](#list-groups) call. You can then enter the desired:

- `subgroup_path`
- `subgroup_name`

```shell
curl --request POST --header "PRIVATE-TOKEN: <your_access_token>" \
     --header "Content-Type: application/json" \
     --data '{"path": "<subgroup_path>", "name": "<subgroup_name>", "parent_id": <parent_group_id> }' \
     "https://gitlab.example.com/api/v4/groups/"
```


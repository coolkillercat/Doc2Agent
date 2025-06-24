## Share Groups with Groups

These endpoints create and delete links for sharing a group with another group. For more information, see the related discussion in the [GitLab Groups](../user/group/manage.md#share-a-group-with-another-group) page.

### Create a link to share a group with another group

Share group with another group. Returns `200` and the [group details](#details-of-a-group) on success.

```plaintext
POST /groups/:id/share
```

| Attribute | Type           | Required | Description |
| --------- | -------------- | -------- | ----------- |
| `id`      | integer/string | yes      | The ID or [URL-encoded path of the group](rest/index.md#namespaced-path-encoding) |
| `group_id` | integer | yes | The ID of the group to share with |
| `group_access` | integer | yes | The [role (`access_level`)](members.md#roles) to grant the group |
| `expires_at` | string | no | Share expiration date in ISO 8601 format: 2016-09-26 |

### Delete link sharing group with another group

Unshare the group from another group. Returns `204` and no content on success.

```plaintext
DELETE /groups/:id/share/:group_id
```

| Attribute | Type           | Required | Description |
| --------- | -------------- | -------- | ----------- |
| `id`      | integer/string | yes      | The ID or [URL-encoded path of the group](rest/index.md#namespaced-path-encoding) |
| `group_id` | integer | yes | The ID of the group to share with |


## Get the sequence of a commit

> - [Introduced](https://gitlab.com/gitlab-org/gitlab/-/issues/438151) in GitLab 16.9.

Get the sequence number of a commit in a project by following the parent links from the given commit.

This API provides essentially the same features as the `git rev-list --count` command for a given commit SHA.

```plaintext
GET /projects/:id/repository/commits/:sha/sequence
```

Parameters:

| Attribute      | Type           | Required | Description |
| -------------- | -------------- | -------- | ----------- |
| `id`           | integer/string | yes      | The ID or [URL-encoded path of the project](rest/index.md#namespaced-path-encoding) owned by the authenticated user. |
| `sha`          | string         | yes      | The commit hash. |
| `first_parent` | boolean        | no       | Follow only the first parent commit upon seeing a merge commit. |

Example request:

```shell
curl --header "PRIVATE-TOKEN: <your_access_token>" \
  --url "https://gitlab.example.com/api/v4/projects/5/repository/commits/5937ac0a7beb003549fc5fd26fc247adbce4a52e/sequence"
```

Example response:

```json
{
  "count": 632
}
```


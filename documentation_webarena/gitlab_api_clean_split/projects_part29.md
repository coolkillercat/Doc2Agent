## Download a project avatar

> - [Introduced](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/144039) in GitLab 16.9.

Get a project avatar.
You can access this endpoint without authentication if the project is publicly accessible.

```plaintext
GET /projects/:id/avatar
```

| Attribute | Type              | Required | Description           |
| --------- | ----------------- | -------- | --------------------- |
| `id`      | integer or string | yes      | ID or [URL-encoded path](rest/index.md#namespaced-path-encoding) of the project. |

Example:

```shell
curl --header "PRIVATE-TOKEN: <your_access_token>" "https://gitlab.example.com/api/v4/projects/4/avatar"
```


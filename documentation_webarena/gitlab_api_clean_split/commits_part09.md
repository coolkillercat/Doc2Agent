## Revert a commit

Reverts a commit in a given branch.

```plaintext
POST /projects/:id/repository/commits/:sha/revert
```

Parameters:

| Attribute | Type           | Required | Description                                                                     |
| --------- | ----           | -------- | -----------                                                                     |
| `id`      | integer/string | yes      | The ID or [URL-encoded path of the project](rest/index.md#namespaced-path-encoding) |
| `sha`     | string         | yes      | Commit SHA to revert                                                            |
| `branch`  | string         | yes      | Target branch name                                                              |
| `dry_run` | boolean        | no       | Does not commit any changes. Default is false. |

```shell
curl --request POST \
  --header "PRIVATE-TOKEN: <your_access_token>" \
  --form "branch=main" \
  --url "https://gitlab.example.com/api/v4/projects/5/repository/commits/a738f717824ff53aebad8b090c1b79a14f2bd9e8/revert"
```

Example response:

```json
{
  "id":"8b090c1b79a14f2bd9e8a738f717824ff53aebad",
  "short_id": "8b090c1b",
  "title":"Revert \"Feature added\"",
  "created_at":"2018-11-08T15:55:26.000Z",
  "parent_ids":["a738f717824ff53aebad8b090c1b79a14f2bd9e8"],
  "message":"Revert \"Feature added\"\n\nThis reverts commit a738f717824ff53aebad8b090c1b79a14f2bd9e8",
  "author_name":"Administrator",
  "author_email":"admin@example.com",
  "authored_date":"2018-11-08T15:55:26.000Z",
  "committer_name":"Administrator",
  "committer_email":"admin@example.com",
  "committed_date":"2018-11-08T15:55:26.000Z",
  "web_url": "https://gitlab.example.com/janedoe/gitlab-foss/-/commit/8b090c1b79a14f2bd9e8a738f717824ff53aebad"
}
```

In the event of a failed revert, the response provides context about why:

```json
{
  "message": "Sorry, we cannot revert this commit automatically. This commit may already have been reverted, or a more recent commit may have updated some of its content.",
  "error_code": "conflict"
}
```

In this case, the revert failed because the attempted revert generated a merge
conflict. The other possible error code is `empty`, which indicates that the
changeset was empty, likely due to the change having already been reverted.

When `dry_run` is enabled, the server attempts to apply the revert _but not
actually commit any resulting changes_. If the revert applies cleanly, the API
responds with `200 OK`:

```json
{
  "dry_run": "success"
}
```

In the event of a failure, an error displays that is identical to a failure without
dry run.


## Cherry-pick a commit

Cherry-picks a commit to a given branch.

```plaintext
POST /projects/:id/repository/commits/:sha/cherry_pick
```

Parameters:

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `id`      | integer/string | yes | The ID or [URL-encoded path of the project](rest/index.md#namespaced-path-encoding) owned by the authenticated user |
| `sha` | string | yes | The commit hash  |
| `branch` | string | yes | The name of the branch  |
| `dry_run` | boolean | no | Does not commit any changes. Default is false. |
| `message` | string | no | A custom commit message to use for the new commit. |

```shell
curl --request POST \
  --header "PRIVATE-TOKEN: <your_access_token>" \
  --form "branch=main" \
  --url "https://gitlab.example.com/api/v4/projects/5/repository/commits/main/cherry_pick"
```

Example response:

```json
{
  "id": "8b090c1b79a14f2bd9e8a738f717824ff53aebad",
  "short_id": "8b090c1b",
  "author_name": "Example User",
  "author_email": "user@example.com",
  "authored_date": "2016-12-12T20:10:39.000+01:00",
  "created_at": "2016-12-12T20:10:39.000+01:00",
  "committer_name": "Administrator",
  "committer_email": "admin@example.com",
  "committed_date": "2016-12-12T20:10:39.000+01:00",
  "title": "Feature added",
  "message": "Feature added\n\nSigned-off-by: Example User <user@example.com>\n",
  "parent_ids": [
    "a738f717824ff53aebad8b090c1b79a14f2bd9e8"
  ],
  "web_url": "https://gitlab.example.com/janedoe/gitlab-foss/-/commit/8b090c1b79a14f2bd9e8a738f717824ff53aebad"
}
```

In the event of a failed cherry-pick, the response provides context about
why:

```json
{
  "message": "Sorry, we cannot cherry-pick this commit automatically. This commit may already have been cherry-picked, or a more recent commit may have updated some of its content.",
  "error_code": "empty"
}
```

In this case, the cherry-pick failed because the changeset was empty and likely
indicates that the commit already exists in the target branch. The other
possible error code is `conflict`, which indicates that there was a merge
conflict.

When `dry_run` is enabled, the server attempts to apply the cherry-pick _but
not actually commit any resulting changes_. If the cherry-pick applies cleanly,
the API responds with `200 OK`:

```json
{
  "dry_run": "success"
}
```

In the event of a failure, an error displays that is identical to a failure without
dry run.


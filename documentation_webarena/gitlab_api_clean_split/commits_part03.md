## List repository commits

> - Commits by author [introduced](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/114417) in GitLab 15.10.

Get a list of repository commits in a project.

```plaintext
GET /projects/:id/repository/commits
```

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `id`      | integer/string | yes | The ID or [URL-encoded path of the project](rest/index.md#namespaced-path-encoding) owned by the authenticated user |
| `ref_name` | string | no | The name of a repository branch, tag or revision range, or if not given the default branch |
| `since` | string | no | Only commits after or on this date are returned in ISO 8601 format `YYYY-MM-DDTHH:MM:SSZ` |
| `until` | string | no | Only commits before or on this date are returned in ISO 8601 format `YYYY-MM-DDTHH:MM:SSZ` |
| `path` | string | no | The file path |
| `author` | string | no | Search commits by commit author.|
| `all` | boolean | no | Retrieve every commit from the repository |
| `with_stats` | boolean | no | Stats about each commit are added to the response |
| `first_parent` | boolean | no | Follow only the first parent commit upon seeing a merge commit |
| `order` | string | no | List commits in order. Possible values: `default`, [`topo`](https://git-scm.com/docs/git-log#Documentation/git-log.txt---topo-order). Defaults to `default`, the commits are shown in reverse chronological order. |
| `trailers` | boolean | no | Parse and include [Git trailers](https://git-scm.com/docs/git-interpret-trailers) for every commit |

```shell
curl --header "PRIVATE-TOKEN: <your_access_token>" \
  --url "https://gitlab.example.com/api/v4/projects/5/repository/commits"
```

Example response:

```json
[
  {
    "id": "ed899a2f4b50b4370feeea94676502b42383c746",
    "short_id": "ed899a2f4b5",
    "title": "Replace sanitize with escape once",
    "author_name": "Example User",
    "author_email": "user@example.com",
    "authored_date": "2021-09-20T11:50:22.001+00:00",
    "committer_name": "Administrator",
    "committer_email": "admin@example.com",
    "committed_date": "2021-09-20T11:50:22.001+00:00",
    "created_at": "2021-09-20T11:50:22.001+00:00",
    "message": "Replace sanitize with escape once",
    "parent_ids": [
      "6104942438c14ec7bd21c6cd5bd995272b3faff6"
    ],
    "web_url": "https://gitlab.example.com/janedoe/gitlab-foss/-/commit/ed899a2f4b50b4370feeea94676502b42383c746",
    "trailers": {},
    "extended_trailers": {}
  },
  {
    "id": "6104942438c14ec7bd21c6cd5bd995272b3faff6",
    "short_id": "6104942438c",
    "title": "Sanitize for network graph",
    "author_name": "randx",
    "author_email": "user@example.com",
    "committer_name": "ExampleName",
    "committer_email": "user@example.com",
    "created_at": "2021-09-20T09:06:12.201+00:00",
    "message": "Sanitize for network graph\nCc: John Doe <johndoe@gitlab.com>\nCc: Jane Doe <janedoe@gitlab.com>",
    "parent_ids": [
      "ae1d9fb46aa2b07ee9836d49862ec4e2c46fbbba"
    ],
    "web_url": "https://gitlab.example.com/janedoe/gitlab-foss/-/commit/ed899a2f4b50b4370feeea94676502b42383c746",
    "trailers": { "Cc": "Jane Doe <janedoe@gitlab.com>" },
    "extended_trailers": { "Cc": ["John Doe <johndoe@gitlab.com>", "Jane Doe <janedoe@gitlab.com>"] }
  }
]
```


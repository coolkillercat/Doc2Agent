## Merge Base

Get the common ancestor for 2 or more refs, such as commit SHAs, branch names, or tags.

```plaintext
GET /projects/:id/repository/merge_base
```

| Attribute | Type           | Required | Description |
| --------- | -------------- | -------- | ---------------------------------------------------------------------------------- |
| `id`      | integer or string | yes      | The ID or [URL-encoded path of the project](rest/index.md#namespaced-path-encoding). |
| `refs`    | array          | yes      | The refs to find the common ancestor of. Accepts multiple refs.                    |

Example request, with the refs truncated for readability:

```shell
curl --header "PRIVATE-TOKEN: <your_access_token>" \
  "https://gitlab.example.com/api/v4/projects/5/repository/merge_base?refs[]=304d257d&refs[]=0031876f"
```

Example response:

```json
{
  "id": "1a0b36b3cdad1d2ee32457c102a8c0b7056fa863",
  "short_id": "1a0b36b3",
  "title": "Initial commit",
  "created_at": "2014-02-27T08:03:18.000Z",
  "parent_ids": [],
  "message": "Initial commit\n",
  "author_name": "Example User",
  "author_email": "user@example.com",
  "authored_date": "2014-02-27T08:03:18.000Z",
  "committer_name": "Example User",
  "committer_email": "user@example.com",
  "committed_date": "2014-02-27T08:03:18.000Z"
}
```


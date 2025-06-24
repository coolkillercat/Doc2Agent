## Post comment to commit

Adds a comment to a commit.

To post a comment in a particular line of a particular file, you must specify
the full commit SHA, the `path`, the `line`, and `line_type` should be `new`.

The comment is added at the end of the last commit if at least one of the
cases below is valid:

- the `sha` is instead a branch or a tag and the `line` or `path` are invalid
- the `line` number is invalid (does not exist)
- the `path` is invalid (does not exist)

In any of the above cases, the response of `line`, `line_type` and `path` is
set to `null`.

For other approaches to commenting on a merge request, see
[Create new merge request note](notes.md#create-new-merge-request-note) in the Notes API,
and [Create a new thread in the merge request diff](discussions.md#create-a-new-thread-in-the-merge-request-diff)
in the Discussions API.

```plaintext
POST /projects/:id/repository/commits/:sha/comments
```

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `id`      | integer/string | yes | The ID or [URL-encoded path of the project](rest/index.md#namespaced-path-encoding) owned by the authenticated user |
| `sha`       | string  | yes | The commit SHA or name of a repository branch or tag |
| `note`      | string  | yes | The text of the comment |
| `path`      | string  | no  | The file path relative to the repository |
| `line`      | integer | no  | The line number where the comment should be placed |
| `line_type` | string  | no  | The line type. Takes `new` or `old` as arguments |

```shell
curl --request POST \
  --header "PRIVATE-TOKEN: <your_access_token>" \
  --form "note=Nice picture\!" \
  --form "path=README.md" \
  --form "line=11" \
  --form "line_type=new" \
  --url "https://gitlab.example.com/api/v4/projects/17/repository/commits/18f3e63d05582537db6d183d9d557be09e1f90c8/comments"
```

Example response:

```json
{
   "author" : {
      "web_url" : "https://gitlab.example.com/janedoe",
      "avatar_url" : "https://gitlab.example.com/uploads/user/avatar/28/jane-doe-400-400.png",
      "username" : "janedoe",
      "state" : "active",
      "name" : "Jane Doe",
      "id" : 28
   },
   "created_at" : "2016-01-19T09:44:55.600Z",
   "line_type" : "new",
   "path" : "README.md",
   "line" : 11,
   "note" : "Nice picture!"
}
```


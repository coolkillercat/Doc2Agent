## List repository tree

> - Iterating pages of results with a number (`?page=2`) [deprecated](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/67509) in GitLab 14.3.

Get a list of repository files and directories in a project. This endpoint can
be accessed without authentication if the repository is publicly accessible.

This command provides essentially the same features as the `git ls-tree`
command. For more information, refer to the section
[Tree Objects](https://git-scm.com/book/en/v2/Git-Internals-Git-Objects/#_tree_objects)
in the Git internals documentation.

WARNING:
This endpoint changed to [keyset-based pagination](rest/index.md#keyset-based-pagination)
in GitLab 15.0. Iterating pages of results with a number (`?page=2`) is unsupported.

```plaintext
GET /projects/:id/repository/tree
```

Supported attributes:

| Attribute   | Type           | Required | Description |
| :---------- | :------------- | :------- | :---------- |
| `id`        | integer or string | yes      | The ID or [URL-encoded path of the project](rest/index.md#namespaced-path-encoding) owned by the authenticated user. |
| `page_token` | string        | no       | The tree record ID at which to fetch the next page. Used only with keyset pagination. |
| `pagination` | string        | no       | If `keyset`, use the [keyset-based pagination method](rest/index.md#keyset-based-pagination). |
| `path`      | string         | no       | The path inside the repository. Used to get content of subdirectories. |
| `per_page`  | integer        | no       | Number of results to show per page. If not specified, defaults to `20`. For more information, see [Pagination](rest/index.md#pagination). |
| `recursive` | boolean        | no       | Boolean value used to get a recursive tree. Default is `false`. |
| `ref`       | string         | no       | The name of a repository branch or tag or, if not given, the default branch. |

```json
[
  {
    "id": "a1e8f8d745cc87e3a9248358d9352bb7f9a0aeba",
    "name": "html",
    "type": "tree",
    "path": "files/html",
    "mode": "040000"
  },
  {
    "id": "4535904260b1082e14f867f7a24fd8c21495bde3",
    "name": "images",
    "type": "tree",
    "path": "files/images",
    "mode": "040000"
  },
  {
    "id": "31405c5ddef582c5a9b7a85230413ff90e2fe720",
    "name": "js",
    "type": "tree",
    "path": "files/js",
    "mode": "040000"
  },
  {
    "id": "cc71111cfad871212dc99572599a568bfe1e7e00",
    "name": "lfs",
    "type": "tree",
    "path": "files/lfs",
    "mode": "040000"
  },
  {
    "id": "fd581c619bf59cfdfa9c8282377bb09c2f897520",
    "name": "markdown",
    "type": "tree",
    "path": "files/markdown",
    "mode": "040000"
  },
  {
    "id": "23ea4d11a4bdd960ee5320c5cb65b5b3fdbc60db",
    "name": "ruby",
    "type": "tree",
    "path": "files/ruby",
    "mode": "040000"
  },
  {
    "id": "7d70e02340bac451f281cecf0a980907974bd8be",
    "name": "whitespace",
    "type": "blob",
    "path": "files/whitespace",
    "mode": "100644"
  }
]
```


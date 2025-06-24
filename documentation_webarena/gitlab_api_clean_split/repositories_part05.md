## Get file archive

Get an archive of the repository. This endpoint can be accessed without
authentication if the repository is publicly accessible.

For GitLab.com users, this endpoint has a rate limit threshold of 5 requests per minute.

```plaintext
GET /projects/:id/repository/archive[.format]
```

`format` is an optional suffix for the archive format, and defaults to
`tar.gz`. For example, specifying `archive.zip` sends an archive in ZIP format.
Available options are:

- `bz2`
- `tar`
- `tar.bz2`
- `tar.gz`
- `tb2`
- `tbz`
- `tbz2`
- `zip`

Supported attributes:

| Attribute   | Type           | Required | Description           |
|:------------|:---------------|:---------|:----------------------|
| `id`        | integer or string | yes      | The ID or [URL-encoded path of the project](rest/index.md#namespaced-path-encoding) owned by the authenticated user. |
| `path`      | string         | no       | The subpath of the repository to download. If an empty string, defaults to the whole repository.  |
| `sha`       | string         | no       | The commit SHA to download. A tag, branch reference, or SHA can be used. If not specified, defaults to the tip of the default branch. |

Example request:

```shell
curl --header "PRIVATE-TOKEN: <your_access_token>" \
  "https://gitlab.com/api/v4/projects/<project_id>/repository/archive?sha=<commit_sha>&path=<path>"
```


## Download snapshot of a Git repository

This endpoint may only be accessed by an administrative user.

Download a snapshot of the project (or wiki, if requested) Git repository. This
snapshot is always in uncompressed [tar](https://en.wikipedia.org/wiki/Tar_(computing))
format.

If a repository is corrupted to the point where `git clone` doesn't work, the
snapshot may allow some of the data to be retrieved.

```plaintext
GET /projects/:id/snapshot
```

| Attribute | Type              | Required | Description |
|-----------|-------------------|----------|-------------|
| `id`      | integer or string | Yes      | The ID or [URL-encoded path of the project](rest/index.md#namespaced-path-encoding). |
| `wiki`    | boolean           | No       | Whether to download the wiki, rather than project, repository. |


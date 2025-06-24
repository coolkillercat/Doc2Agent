## Merge to default merge ref path

Merge the changes between the merge request source and target branches into `refs/merge-requests/:iid/merge`
ref, of the target project repository, if possible. This ref has the state the target branch would have if
a regular merge action was taken.

This action isn't a regular merge action, because it doesn't change the merge request target branch state in any manner.

This ref (`refs/merge-requests/:iid/merge`) isn't necessarily overwritten when submitting
requests to this API, though it makes sure the ref has the latest possible state.

```plaintext
GET /projects/:id/merge_requests/:merge_request_iid/merge_ref
```

Supported attributes:

| Attribute           | Type              | Required | Description |
|---------------------|-------------------|----------|-------------|
| `id`                | integer or string | Yes      | The ID or [URL-encoded path of the project](rest/index.md#namespaced-path-encoding) owned by the authenticated user. |
| `merge_request_iid` | integer           | Yes      | The internal ID of the merge request. |

This API returns specific HTTP status codes:

| HTTP Status | Message                          | Reason |
|-------------|----------------------------------|--------|
| `200`       | _(none)_                         | Success. Returns the HEAD commit of `refs/merge-requests/:iid/merge`. |
| `400`       | `Merge request is not mergeable` | The merge request has conflicts. |
| `400`       | `Merge ref cannot be updated`    |        |
| `400`       | `Unsupported operation`          | The GitLab database is in read-only mode. |

Example response:

```json
{
  "commit_id": "854a3a7a17acbcc0bbbea170986df1eb60435f34"
}
```


## List merge request pipelines

Get a list of merge request pipelines.

```plaintext
GET /projects/:id/merge_requests/:merge_request_iid/pipelines
```

Supported attributes:

| Attribute           | Type              | Required | Description |
|---------------------|-------------------|----------|-------------|
| `id`                | integer or string | Yes      | The ID or [URL-encoded path of the project](rest/index.md#namespaced-path-encoding) owned by the authenticated user. |
| `merge_request_iid` | integer           | Yes      | The internal ID of the merge request. |

The pagination parameters `page` and
`per_page` can be used to restrict the list of merge request pipelines.

Example response:

```json
[
  {
    "id": 77,
    "sha": "959e04d7c7a30600c894bd3c0cd0e1ce7f42c11d",
    "ref": "main",
    "status": "success"
  }
]
```


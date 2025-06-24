## Rebase a merge request

Automatically rebase the `source_branch` of the merge request against its
`target_branch`.

```plaintext
PUT /projects/:id/merge_requests/:merge_request_iid/rebase
```

| Attribute           | Type           | Required | Description |
|---------------------|----------------|----------|-------------|
| `id`                | integer or string | Yes      | The ID or [URL-encoded path of the project](rest/index.md#namespaced-path-encoding) owned by the authenticated user. |
| `merge_request_iid` | integer        | Yes      | The internal ID of the merge request. |
| `skip_ci`           | boolean        | No       | Set to `true` to skip creating a CI pipeline. |

```shell
curl --request PUT \
  --header "PRIVATE-TOKEN: <your_access_token>" \
  --url "https://gitlab.example.com/api/v4/projects/76/merge_requests/1/rebase"
```

This API returns specific HTTP status codes:

| HTTP Status | Message                                    | Reason |
|-------------|--------------------------------------------|--------|
| `202`       | *(no message)* | Successfully enqueued. |
| `403`       | `Cannot push to source branch` | You don't have permission to push to the merge request's source branch. |
| `403`       | `Source branch does not exist` | You don't have permission to push to the merge request's source branch. |
| `403`       | `Source branch is protected from force push` | You don't have permission to push to the merge request's source branch. |
| `409`       | `Failed to enqueue the rebase operation` | A long-lived transaction might have blocked your request. |

If the request is enqueued successfully, the response contains:

```json
{
  "rebase_in_progress": true
}
```

You can poll the [Get single MR](#get-single-mr) endpoint with the
`include_rebase_in_progress` parameter to check the status of the
asynchronous request.

If the rebase operation is ongoing, the response includes the following:

```json
{
  "rebase_in_progress": true,
  "merge_error": null
}
```

After the rebase operation has completed successfully, the response includes
the following:

```json
{
  "rebase_in_progress": false,
  "merge_error": null
}
```

If the rebase operation fails, the response includes the following:

```json
{
  "rebase_in_progress": false,
  "merge_error": "Rebase failed. Please rebase locally"
}
```


## Add spent time for a merge request

Adds spent time for this merge request.

```plaintext
POST /projects/:id/merge_requests/:merge_request_iid/add_spent_time
```

| Attribute           | Type           | Required | Description |
|---------------------|----------------|----------|-------------|
| `id`                | integer or string | Yes      | The ID or [URL-encoded path of the project](rest/index.md#namespaced-path-encoding) owned by the authenticated user. |
| `merge_request_iid` | integer        | Yes      | The internal ID of the merge request. |
| `duration`          | string         | Yes      | The duration in human format, such as `3h30m` |
| `summary`           | string         | No       | A summary of how the time was spent. |

```shell
curl --request POST \
  --header "PRIVATE-TOKEN: <your_access_token>" \
  --url "https://gitlab.example.com/api/v4/projects/5/merge_requests/93/add_spent_time?duration=1h"
```

Example response:

```json
{
  "human_time_estimate": null,
  "human_total_time_spent": "1h",
  "time_estimate": 0,
  "total_time_spent": 3600
}
```


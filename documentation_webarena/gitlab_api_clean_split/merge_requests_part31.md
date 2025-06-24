## Reset spent time for a merge request

Resets the total spent time for this merge request to 0 seconds.

```plaintext
POST /projects/:id/merge_requests/:merge_request_iid/reset_spent_time
```

| Attribute           | Type           | Required | Description |
|---------------------|----------------|----------|-------------|
| `id`                | integer or string | Yes      | The ID or [URL-encoded path of the project](rest/index.md#namespaced-path-encoding) owned by the authenticated user. |
| `merge_request_iid` | integer        | Yes      | The internal ID of a project's merge request. |

```shell
curl --request POST \
  --header "PRIVATE-TOKEN: <your_access_token>" \
  --url "https://gitlab.example.com/api/v4/projects/5/merge_requests/93/reset_spent_time"
```

Example response:

```json
{
  "human_time_estimate": null,
  "human_total_time_spent": null,
  "time_estimate": 0,
  "total_time_spent": 0
}
```


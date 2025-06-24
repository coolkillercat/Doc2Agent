## Get user agent details

Available only for administrators.

Gets the user agent string and IP of the user who created the issue.
Used for spam tracking.

```plaintext
GET /projects/:id/issues/:issue_iid/user_agent_detail
```

Supported attributes:

| Attribute   | Type    | Required | Description                          |
|-------------|---------|----------|--------------------------------------|
| `id`        | integer/string | Yes      | The global ID or [URL-encoded path of the project](rest/index.md#namespaced-path-encoding) owned by the authenticated user.  |
| `issue_iid` | integer | Yes      | The internal ID of a project's issue. |

Example request:

```shell
curl --header "PRIVATE-TOKEN: <your_access_token>" \
  --url "https://gitlab.example.com/api/v4/projects/5/issues/93/user_agent_detail"
```

Example response:

```json
{
  "user_agent": "AppleWebKit/537.36",
  "ip_address": "127.0.0.1",
  "akismet_submitted": false
}
```


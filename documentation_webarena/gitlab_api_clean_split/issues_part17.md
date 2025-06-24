## Time tracking

The following requests are related to [time tracking](../user/project/time_tracking.md) on issues.

### Set a time estimate for an issue

Sets an estimated time of work for this issue.

```plaintext
POST /projects/:id/issues/:issue_iid/time_estimate
```

Supported attributes:

| Attribute   | Type    | Required | Description                              |
|-------------|---------|----------|------------------------------------------|
| `duration`  | string  | Yes      | The duration in human-readable format. For example: `3h30m`. |
| `id`        | integer/string | Yes      | The global ID or [URL-encoded path of the project](rest/index.md#namespaced-path-encoding) owned by the authenticated user.      |
| `issue_iid` | integer | Yes      | The internal ID of a project's issue.     |

Example request:

```shell
curl --request POST \
  --header "PRIVATE-TOKEN: <your_access_token>" \
  --url "https://gitlab.example.com/api/v4/projects/5/issues/93/time_estimate?duration=3h30m"
```

Example response:

```json
{
  "human_time_estimate": "3h 30m",
  "human_total_time_spent": null,
  "time_estimate": 12600,
  "total_time_spent": 0
}
```

### Reset the time estimate for an issue

Resets the estimated time for this issue to 0 seconds.

```plaintext
POST /projects/:id/issues/:issue_iid/reset_time_estimate
```

Supported attributes:

| Attribute   | Type    | Required | Description                          |
|-------------|---------|----------|--------------------------------------|
| `id`        | integer/string | Yes      | The global ID or [URL-encoded path of the project](rest/index.md#namespaced-path-encoding) owned by the authenticated user.  |
| `issue_iid` | integer | Yes      | The internal ID of a project's issue. |

Example request:

```shell
curl --request POST \
  --header "PRIVATE-TOKEN: <your_access_token>" \
  --url "https://gitlab.example.com/api/v4/projects/5/issues/93/reset_time_estimate"
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

### Add spent time for an issue

Adds spent time for this issue.

```plaintext
POST /projects/:id/issues/:issue_iid/add_spent_time
```

Supported attributes:

| Attribute   | Type    | Required | Description                              |
|-------------|---------|----------|------------------------------------------|
| `duration`  | string  | Yes      | The duration in human-readable format. For example: `3h30m` |
| `id`        | integer/string | Yes      | The global ID or [URL-encoded path of the project](rest/index.md#namespaced-path-encoding) owned by the authenticated user. |
| `issue_iid` | integer | Yes      | The internal ID of a project's issue.    |
| `summary`   | string  | No       | A summary of how the time was spent.  |

Example request:

```shell
curl --request POST \
  --header "PRIVATE-TOKEN: <your_access_token>" \
  --url "https://gitlab.example.com/api/v4/projects/5/issues/93/add_spent_time?duration=1h"
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

### Reset spent time for an issue

Resets the total spent time for this issue to 0 seconds.

```plaintext
POST /projects/:id/issues/:issue_iid/reset_spent_time
```

Supported attributes:

| Attribute   | Type    | Required | Description                          |
|-------------|---------|----------|--------------------------------------|
| `id`        | integer/string | Yes      | The global ID or [URL-encoded path of the project](rest/index.md#namespaced-path-encoding) owned by the authenticated user. |
| `issue_iid` | integer | Yes      | The internal ID of a project's issue. |

Example request:

```shell
curl --request POST \
  --header "PRIVATE-TOKEN: <your_access_token>" \
  --url "https://gitlab.example.com/api/v4/projects/5/issues/93/reset_spent_time"
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

### Get time tracking stats

Gets time tracking stats for an issue in human-readable format (for example, `1h30m`) and in number of seconds.

If the project is private or the issue is confidential, you must provide credentials to authorize.
The preferred way to do this, is by using [personal access tokens](../user/profile/personal_access_tokens.md).

```plaintext
GET /projects/:id/issues/:issue_iid/time_stats
```

Supported attributes:

| Attribute   | Type    | Required | Description                          |
|-------------|---------|----------|--------------------------------------|
| `id`        | integer/string | Yes      | The global ID or [URL-encoded path of the project](rest/index.md#namespaced-path-encoding) owned by the authenticated user.  |
| `issue_iid` | integer | Yes      | The internal ID of a project's issue. |

Example request:

```shell
curl --header "PRIVATE-TOKEN: <your_access_token>" \
  --url "https://gitlab.example.com/api/v4/projects/5/issues/93/time_stats"
```

Example response:

```json
{
  "human_time_estimate": "2h",
  "human_total_time_spent": "1h",
  "time_estimate": 7200,
  "total_time_spent": 3600
}
```


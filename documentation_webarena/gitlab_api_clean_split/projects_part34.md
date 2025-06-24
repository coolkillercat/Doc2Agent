## Hooks

Also called Project Hooks and Webhooks. These are different for [System Hooks](system_hooks.md)
that are system-wide.

### List project hooks

Get a list of project hooks.

```plaintext
GET /projects/:id/hooks
```

| Attribute | Type              | Required | Description |
|-----------|-------------------|----------|-------------|
| `id`      | integer or string | Yes      | The ID or [URL-encoded path of the project](rest/index.md#namespaced-path-encoding). |

### Get project hook

Get a specific hook for a project.

```plaintext
GET /projects/:id/hooks/:hook_id
```

| Attribute | Type              | Required | Description |
|-----------|-------------------|----------|-------------|
| `hook_id` | integer           | Yes      | The ID of a project hook. |
| `id`      | integer or string | Yes      | The ID or [URL-encoded path of the project](rest/index.md#namespaced-path-encoding). |

```json
{
  "id": 1,
  "url": "http://example.com/hook",
  "project_id": 3,
  "push_events": true,
  "push_events_branch_filter": "",
  "issues_events": true,
  "confidential_issues_events": true,
  "merge_requests_events": true,
  "tag_push_events": true,
  "note_events": true,
  "confidential_note_events": true,
  "job_events": true,
  "pipeline_events": true,
  "wiki_page_events": true,
  "deployment_events": true,
  "releases_events": true,
  "enable_ssl_verification": true,
  "repository_update_events": false,
  "alert_status": "executable",
  "disabled_until": null,
  "url_variables": [ ],
  "created_at": "2012-10-12T17:04:47Z",
  "resource_access_token_events": true,
  "custom_webhook_template": "{\"event\":\"{{object_kind}}\"}"
}
```

### Add project hook

Adds a hook to a specified project.

```plaintext
POST /projects/:id/hooks
```

| Attribute                    | Type              | Required | Description |
|------------------------------|-------------------|----------|-------------|
| `id`                         | integer or string | Yes      | The ID or [URL-encoded path of the project](rest/index.md#namespaced-path-encoding). |
| `url`                        | string            | Yes      | The hook URL. |
| `confidential_issues_events` | boolean           | No       | Trigger hook on confidential issues events. |
| `confidential_note_events`   | boolean           | No       | Trigger hook on confidential note events. |
| `deployment_events`          | boolean           | No       | Trigger hook on deployment events. |
| `enable_ssl_verification`    | boolean           | No       | Do SSL verification when triggering the hook. |
| `issues_events`              | boolean           | No       | Trigger hook on issues events. |
| `job_events`                 | boolean           | No       | Trigger hook on job events. |
| `merge_requests_events`      | boolean           | No       | Trigger hook on merge requests events. |
| `note_events`                | boolean           | No       | Trigger hook on note events. |
| `pipeline_events`            | boolean           | No       | Trigger hook on pipeline events. |
| `push_events_branch_filter`  | string            | No       | Trigger hook on push events for matching branches only. |
| `push_events`                | boolean           | No       | Trigger hook on push events. |
| `releases_events`            | boolean           | No       | Trigger hook on release events. |
| `tag_push_events`            | boolean           | No       | Trigger hook on tag push events. |
| `token`                      | string            | No       | Secret token to validate received payloads; the token isn't returned in the response. |
| `wiki_page_events`           | boolean           | No       | Trigger hook on wiki events. |
| `resource_access_token_events` | boolean         | No       | Trigger hook on project access token expiry events. |
| `custom_webhook_template`    | string            | No       | Custom webhook template for the hook. |

### Edit project hook

Edits a hook for a specified project.

```plaintext
PUT /projects/:id/hooks/:hook_id
```

| Attribute                    | Type              | Required | Description |
|------------------------------|-------------------|----------|-------------|
| `hook_id`                    | integer           | Yes      | The ID of the project hook. |
| `id`                         | integer or string | Yes      | The ID or [URL-encoded path of the project](rest/index.md#namespaced-path-encoding). |
| `url`                        | string            | Yes      | The hook URL. |
| `confidential_issues_events` | boolean           | No       | Trigger hook on confidential issues events. |
| `confidential_note_events`   | boolean           | No       | Trigger hook on confidential note events. |
| `deployment_events`          | boolean           | No       | Trigger hook on deployment events. |
| `enable_ssl_verification`    | boolean           | No       | Do SSL verification when triggering the hook. |
| `issues_events`              | boolean           | No       | Trigger hook on issues events. |
| `job_events`                 | boolean           | No       | Trigger hook on job events. |
| `merge_requests_events`      | boolean           | No       | Trigger hook on merge requests events. |
| `note_events`                | boolean           | No       | Trigger hook on note events. |
| `pipeline_events`            | boolean           | No       | Trigger hook on pipeline events. |
| `push_events_branch_filter`  | string            | No       | Trigger hook on push events for matching branches only. |
| `push_events`                | boolean           | No       | Trigger hook on push events. |
| `releases_events`            | boolean           | No       | Trigger hook on release events. |
| `tag_push_events`            | boolean           | No       | Trigger hook on tag push events. |
| `token`                      | string            | No       | Secret token to validate received payloads. Not returned in the response. When you change the webhook URL, the secret token is reset and not retained. |
| `wiki_page_events`           | boolean           | No       | Trigger hook on wiki page events. |
| `resource_access_token_events` | boolean         | No       | Trigger hook on project access token expiry events. |
| `custom_webhook_template`    | string            | No       | Custom webhook template for the hook. |

### Delete project hook

Removes a hook from a project. This method is idempotent, and can be called
multiple times. Either the hook is available or not.

```plaintext
DELETE /projects/:id/hooks/:hook_id
```

| Attribute | Type              | Required | Description |
|-----------|-------------------|----------|-------------|
| `hook_id` | integer           | Yes      | The ID of the project hook. |
| `id`      | integer or string | Yes      | The ID or [URL-encoded path of the project](rest/index.md#namespaced-path-encoding). |

Note the JSON response differs if the hook is available or not. If the project
hook is available before it's returned in the JSON response or an empty response
is returned.

### Trigger a test project hook

> - [Introduced](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/147656) in GitLab 16.11.
> - Special rate limit [introduced](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/150066) in GitLab 17.0 [with a flag](../administration/feature_flags.md) named `web_hook_test_api_endpoint_rate_limit`. Enabled by default.

Trigger a test hook for a specified project.

In GitLab 17.0 and later, this endpoint has a special rate limit of three requests per minute per project hook.
To disable this limit on self-managed GitLab and GitLab Dedicated, an administrator can
[disable the feature flag](../administration/feature_flags.md) named `web_hook_test_api_endpoint_rate_limit`.

```plaintext
POST /projects/:id/hooks/:hook_id/test/:trigger
```

| Attribute | Type              | Required | Description                                                                                                                                                                                                                                                |
|-----------|-------------------|----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `hook_id` | integer           | Yes      | The ID of the project hook.                                                                                                                                                                                                                                |
| `id`      | integer or string | Yes      | The ID or [URL-encoded path of the project](rest/index.md#namespaced-path-encoding).                                                                                                                                                                       |
| `trigger` | string            | Yes      | One of `push_events`, `tag_push_events`, `issues_events`, `confidential_issues_events`, `note_events`, `merge_requests_events`, `job_events`, `pipeline_events`, `wiki_page_events`, `releases_events`, `emoji_events`, or `resource_access_token_events`. |

```json
{"message":"201 Created"}
```


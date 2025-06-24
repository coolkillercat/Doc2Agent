## Hooks

DETAILS:
**Tier:** Premium, Ultimate
**Offering:** GitLab.com, Self-managed, GitLab Dedicated

Also called Group Hooks and Webhooks.
These are different from [System Hooks](system_hooks.md) that are system wide and [Project Hooks](projects.md#hooks) that are limited to one project.

### List group hooks

Get a list of group hooks

```plaintext
GET /groups/:id/hooks
```

| Attribute | Type            | Required | Description |
| --------- | --------------- | -------- | ----------- |
| `id`      | integer/string  | yes      | The ID or [URL-encoded path of the group](rest/index.md#namespaced-path-encoding) |

### Get group hook

Get a specific hook for a group.

| Attribute | Type           | Required | Description |
| --------- | -------------- | -------- | ----------- |
| `id`      | integer/string | yes      | The ID or [URL-encoded path of the group](rest/index.md#namespaced-path-encoding) |
| `hook_id` | integer        | yes      | The ID of a group hook |

```plaintext
GET /groups/:id/hooks/:hook_id
```

```json
{
  "id": 1,
  "url": "http://example.com/hook",
  "group_id": 3,
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
  "subgroup_events": true,
  "member_events": true,
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

### Add group hook

Adds a hook to a specified group.

```plaintext
POST /groups/:id/hooks
```

| Attribute                    | Type           | Required | Description |
| -----------------------------| -------------- |----------| ----------- |
| `id`                         | integer/string | yes      | The ID or [URL-encoded path of the group](rest/index.md#namespaced-path-encoding) |
| `url`                        | string         | yes      | The hook URL |
| `push_events`                | boolean        | no       | Trigger hook on push events |
| `push_events_branch_filter`  | string         | No       | Trigger hook on push events for matching branches only. |
| `issues_events`              | boolean        | no       | Trigger hook on issues events |
| `confidential_issues_events` | boolean        | no       | Trigger hook on confidential issues events |
| `merge_requests_events`      | boolean        | no       | Trigger hook on merge requests events |
| `tag_push_events`            | boolean        | no       | Trigger hook on tag push events |
| `note_events`                | boolean        | no       | Trigger hook on note events |
| `confidential_note_events`   | boolean        | no       | Trigger hook on confidential note events |
| `job_events`                 | boolean        | no       | Trigger hook on job events |
| `pipeline_events`            | boolean        | no       | Trigger hook on pipeline events |
| `wiki_page_events`           | boolean        | no       | Trigger hook on wiki page events |
| `deployment_events`          | boolean        | no       | Trigger hook on deployment events |
| `releases_events`            | boolean        | no       | Trigger hook on release events |
| `subgroup_events`            | boolean        | no       | Trigger hook on subgroup events |
| `member_events`              | boolean        | no       | Trigger hook on member events |
| `enable_ssl_verification`    | boolean        | no       | Do SSL verification when triggering the hook |
| `token`                      | string         | no       | Secret token to validate received payloads; not returned in the response |
| `resource_access_token_events` | boolean         | no       | Trigger hook on project access token expiry events. |
| `custom_webhook_template`    | string         | No       | Custom webhook template for the hook. |

### Edit group hook

Edits a hook for a specified group.

```plaintext
PUT /groups/:id/hooks/:hook_id
```

| Attribute                    | Type           | Required | Description |
| ---------------------------- | -------------- | -------- | ----------- |
| `id`                         | integer or string | yes      | The ID or [URL-encoded path of the group](rest/index.md#namespaced-path-encoding). |
| `hook_id`                    | integer        | yes      | The ID of the group hook. |
| `url`                        | string         | yes      | The hook URL. |
| `push_events`                | boolean        | no       | Trigger hook on push events. |
| `push_events_branch_filter`  | string         | No       | Trigger hook on push events for matching branches only. |
| `issues_events`              | boolean        | no       | Trigger hook on issues events. |
| `confidential_issues_events` | boolean        | no       | Trigger hook on confidential issues events. |
| `merge_requests_events`      | boolean        | no       | Trigger hook on merge requests events. |
| `tag_push_events`            | boolean        | no       | Trigger hook on tag push events. |
| `note_events`                | boolean        | no       | Trigger hook on note events. |
| `confidential_note_events`   | boolean        | no       | Trigger hook on confidential note events. |
| `job_events`                 | boolean        | no       | Trigger hook on job events. |
| `pipeline_events`            | boolean        | no       | Trigger hook on pipeline events. |
| `wiki_page_events`           | boolean        | no       | Trigger hook on wiki page events. |
| `deployment_events`          | boolean        | no       | Trigger hook on deployment events. |
| `releases_events`            | boolean        | no       | Trigger hook on release events. |
| `subgroup_events`            | boolean        | no       | Trigger hook on subgroup events. |
| `member_events`              | boolean        | no       | Trigger hook on member events. |
| `enable_ssl_verification`    | boolean        | no       | Do SSL verification when triggering the hook. |
| `service_access_tokens_expiration_enforced` | boolean | no | Require service account access tokens to have an expiration date. |
| `token`                      | string         | no       | Secret token to validate received payloads. Not returned in the response. When you change the webhook URL, the secret token is reset and not retained. |
| `resource_access_token_events` | boolean      | no       | Trigger hook on project access token expiry events. |
| `custom_webhook_template`    | string         | No       | Custom webhook template for the hook. |

### Delete group hook

Removes a hook from a group. This is an idempotent method and can be called multiple times.
Either the hook is available or not.

```plaintext
DELETE /groups/:id/hooks/:hook_id
```

| Attribute | Type           | Required | Description |
| --------- | -------------- | -------- | ----------- |
| `id`      | integer/string | yes      | The ID or [URL-encoded path of the group](rest/index.md#namespaced-path-encoding) |
| `hook_id` | integer        | yes      | The ID of the group hook. |


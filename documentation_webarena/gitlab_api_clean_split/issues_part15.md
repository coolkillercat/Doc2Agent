## Create a to-do item

Manually creates a to-do item for the current user on an issue. If
there already exists a to-do item for the user on that issue, status code `304` is
returned.

```plaintext
POST /projects/:id/issues/:issue_iid/todo
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
  --url "https://gitlab.example.com/api/v4/projects/5/issues/93/todo"
```

Example response:

```json
{
  "id": 112,
  "project": {
    "id": 5,
    "name": "GitLab CI/CD",
    "name_with_namespace": "GitLab Org / GitLab CI/CD",
    "path": "gitlab-ci",
    "path_with_namespace": "gitlab-org/gitlab-ci"
  },
  "author": {
    "name": "Administrator",
    "username": "root",
    "id": 1,
    "state": "active",
    "avatar_url": "http://www.gravatar.com/avatar/e64c7d89f26bd1972efa854d13d7dd61?s=80&d=identicon",
    "web_url": "https://gitlab.example.com/root"
  },
  "action_name": "marked",
  "target_type": "Issue",
  "target": {
    "id": 93,
    "iid": 10,
    "project_id": 5,
    "title": "Vel voluptas atque dicta mollitia adipisci qui at.",
    "description": "Tempora laboriosam sint magni sed voluptas similique.",
    "state": "closed",
    "created_at": "2016-06-17T07:47:39.486Z",
    "updated_at": "2016-07-01T11:09:13.998Z",
    "labels": [],
    "milestone": {
      "id": 26,
      "iid": 1,
      "project_id": 5,
      "title": "v0.0",
      "description": "Accusantium nostrum rerum quae quia quis nesciunt suscipit id.",
      "state": "closed",
      "created_at": "2016-06-17T07:47:33.832Z",
      "updated_at": "2016-06-17T07:47:33.832Z",
      "due_date": null
    },
    "assignees": [{
      "name": "Jarret O'Keefe",
      "username": "francisca",
      "id": 14,
      "state": "active",
      "avatar_url": "http://www.gravatar.com/avatar/a7fa515d53450023c83d62986d0658a8?s=80&d=identicon",
      "web_url": "https://gitlab.example.com/francisca"
    }],
    "assignee": {
      "name": "Jarret O'Keefe",
      "username": "francisca",
      "id": 14,
      "state": "active",
      "avatar_url": "http://www.gravatar.com/avatar/a7fa515d53450023c83d62986d0658a8?s=80&d=identicon",
      "web_url": "https://gitlab.example.com/francisca"
    },
    "type" : "ISSUE",
    "author": {
      "name": "Maxie Medhurst",
      "username": "craig_rutherford",
      "id": 12,
      "state": "active",
      "avatar_url": "http://www.gravatar.com/avatar/a0d477b3ea21970ce6ffcbb817b0b435?s=80&d=identicon",
      "web_url": "https://gitlab.example.com/craig_rutherford"
    },
    "subscribed": true,
    "user_notes_count": 7,
    "upvotes": 0,
    "downvotes": 0,
    "merge_requests_count": 0,
    "due_date": null,
    "web_url": "http://gitlab.example.com/my-group/my-project/issues/10",
    "references": {
      "short": "#10",
      "relative": "#10",
      "full": "my-group/my-project#10"
    },
    "confidential": false,
    "discussion_locked": false,
    "issue_type": "issue",
    "severity": "UNKNOWN",
    "task_completion_status":{
       "count":0,
       "completed_count":0
    }
  },
  "target_url": "https://gitlab.example.com/gitlab-org/gitlab-ci/issues/10",
  "body": "Vel voluptas atque dicta mollitia adipisci qui at.",
  "state": "pending",
  "created_at": "2016-07-01T11:09:13.992Z"
}
```

WARNING:
The `assignee` column is deprecated. We now show it as a single-sized array `assignees` to conform to the GitLab EE API.


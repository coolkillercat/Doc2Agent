## Clone an issue

Clone the issue to given project.
Copies as much data as possible as long as the target project contains equivalent
criteria, such as labels or milestones.

If you have insufficient permissions, an error message with status code `400` is returned.

```plaintext
POST /projects/:id/issues/:issue_iid/clone
```

Supported attributes:

| Attribute       | Type           | Required               | Description                       |
| --------------- | -------------- | ---------------------- | --------------------------------- |
| `id`            | integer/string | Yes | ID or [URL-encoded path of the project](rest/index.md#namespaced-path-encoding) owned by the authenticated user. |
| `issue_iid`     | integer        | Yes | Internal ID of a project's issue. |
| `to_project_id` | integer        | Yes | ID of the new project.            |
| `with_notes`    | boolean        | No | Clone the issue with [notes](notes.md). Default is `false`. |

Example request:

```shell
curl --request POST \
  --header "PRIVATE-TOKEN: <your_access_token>" \
  --url "https://gitlab.example.com/api/v4/projects/5/issues/1/clone?with_notes=true&to_project_id=6"
```

Example response:

```json
{
  "id":290,
  "iid":1,
  "project_id":143,
  "title":"foo",
  "description":"closed",
  "state":"opened",
  "created_at":"2021-09-14T22:24:11.696Z",
  "updated_at":"2021-09-14T22:24:11.696Z",
  "closed_at":null,
  "closed_by":null,
  "labels":[

  ],
  "milestone":null,
  "assignees":[
    {
      "id":179,
      "name":"John Doe2",
      "username":"john",
      "state":"active",
      "avatar_url":"https://www.gravatar.com/avatar/10fc7f102be8de7657fb4d80898bbfe3?s=80\u0026d=identicon",
      "web_url":"https://gitlab.example.com/john"
    }
  ],
  "author":{
    "id":179,
    "name":"John Doe2",
    "username":"john",
    "state":"active",
    "avatar_url":"https://www.gravatar.com/avatar/10fc7f102be8de7657fb4d80898bbfe3?s=80\u0026d=identicon",
    "web_url":"https://gitlab.example.com/john"
  },
  "type":"ISSUE",
  "assignee":{
    "id":179,
    "name":"John Doe2",
    "username":"john",
    "state":"active",
    "avatar_url":"https://www.gravatar.com/avatar/10fc7f102be8de7657fb4d80898bbfe3?s=80\u0026d=identicon",
    "web_url":"https://gitlab.example.com/john"
  },
  "user_notes_count":1,
  "merge_requests_count":0,
  "upvotes":0,
  "downvotes":0,
  "due_date":null,
  "imported":false,
  "imported_from": "none",
  "confidential":false,
  "discussion_locked":null,
  "issue_type":"issue",
  "severity": "UNKNOWN",
  "web_url":"https://gitlab.example.com/namespace1/project2/-/issues/1",
  "time_stats":{
    "time_estimate":0,
    "total_time_spent":0,
    "human_time_estimate":null,
    "human_total_time_spent":null
  },
  "task_completion_status":{
    "count":0,
    "completed_count":0
  },
  "blocking_issues_count":0,
  "has_tasks":false,
  "_links":{
    "self":"https://gitlab.example.com/api/v4/projects/143/issues/1",
    "notes":"https://gitlab.example.com/api/v4/projects/143/issues/1/notes",
    "award_emoji":"https://gitlab.example.com/api/v4/projects/143/issues/1/award_emoji",
    "project":"https://gitlab.example.com/api/v4/projects/143",
    "closed_as_duplicate_of": "http://gitlab.example.com/api/v4/projects/1/issues/75"
  },
  "references":{
    "short":"#1",
    "relative":"#1",
    "full":"namespace1/project2#1"
  },
  "subscribed":true,
  "moved_to_id":null,
  "service_desk_reply_to":null
}
```


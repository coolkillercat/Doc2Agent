## Edit an issue

Updates an existing project issue. This request is also used to close or reopen an issue (with `state_event`).

At least one of the following parameters is required for the request to be successful:

- `:assignee_id`
- `:assignee_ids`
- `:confidential`
- `:created_at`
- `:description`
- `:discussion_locked`
- `:due_date`
- `:issue_type`
- `:labels`
- `:milestone_id`
- `:state_event`
- `:title`

```plaintext
PUT /projects/:id/issues/:issue_iid
```

Supported attributes:

| Attribute      | Type    | Required | Description                                                                                                |
|----------------|---------|----------|------------------------------------------------------------------------------------------------------------|
| `id`           | integer/string | Yes | The global ID or [URL-encoded path of the project](rest/index.md#namespaced-path-encoding) owned by the authenticated user. |
| `issue_iid`    | integer | Yes      | The internal ID of a project's issue.                                                                       |
| `add_labels`   | string  | No       | Comma-separated label names to add to an issue. If a label does not already exist, this creates a new project label and assigns it to the issue. |
| `assignee_ids` | integer array | No | The ID of the users to assign the issue to. Set to `0` or provide an empty value to unassign all assignees. |
| `confidential` | boolean | No       | Updates an issue to be confidential.                                                                        |
| `description`  | string  | No       | The description of an issue. Limited to 1,048,576 characters.        |
| `discussion_locked` | boolean | No  | Flag indicating if the issue's discussion is locked. If the discussion is locked only project members can add or edit comments. |
| `due_date`     | string  | No       | The due date. Date time string in the format `YYYY-MM-DD`, for example `2016-03-11`.                                           |
| `epic_id`      | integer | No | ID of the epic to add the issue to. Valid values are greater than or equal to 0. Premium and Ultimate only. |
| `epic_iid`     | integer | No | IID of the epic to add the issue to. Valid values are greater than or equal to 0. (deprecated, [scheduled for removal](https://gitlab.com/gitlab-org/gitlab/-/issues/35157) in API version 5). Premium and Ultimate only. |
| `issue_type`   | string  | No       | Updates the type of issue. One of `issue`, `incident`, `test_case` or `task`. |
| `labels`       | string  | No       | Comma-separated label names for an issue. Set to an empty string to unassign all labels. If a label does not already exist, this creates a new project label and assigns it to the issue. |
| `milestone_id` | integer | No       | The global ID of a milestone to assign the issue to. Set to `0` or provide an empty value to unassign a milestone.|
| `remove_labels`| string  | No       | Comma-separated label names to remove from an issue.                                                       |
| `state_event`  | string  | No       | The state event of an issue. To close the issue, use `close`, and to reopen it, use `reopen`.                      |
| `title`        | string  | No       | The title of an issue.                                                                                      |
| `updated_at`   | string  | No       | When the issue was updated. Date time string, ISO 8601 formatted, for example `2016-03-11T03:45:40Z` (requires administrator or project owner rights). Empty string or null values are not accepted.|
| `weight`       | integer | No       | The weight of the issue. Valid values are greater than or equal to 0. Premium and Ultimate only.           |

Example request:

```shell
curl --request PUT \
  --header "PRIVATE-TOKEN: <your_access_token>" \
  --url "https://gitlab.example.com/api/v4/projects/4/issues/85?state_event=close"
```

Example response:

```json
{
   "created_at" : "2016-01-07T12:46:01.410Z",
   "author" : {
      "name" : "Alexandra Bashirian",
      "avatar_url" : null,
      "username" : "eileen.lowe",
      "id" : 18,
      "state" : "active",
      "web_url" : "https://gitlab.example.com/eileen.lowe"
   },
   "state" : "closed",
   "title" : "Issues with auth",
   "project_id" : 4,
   "description" : null,
   "updated_at" : "2016-01-07T12:55:16.213Z",
   "closed_at" : "2016-01-08T12:55:16.213Z",
   "closed_by" : {
      "state" : "active",
      "web_url" : "https://gitlab.example.com/root",
      "avatar_url" : null,
      "username" : "root",
      "id" : 1,
      "name" : "Administrator"
    },
   "iid" : 15,
   "labels" : [
      "bug"
   ],
   "upvotes": 4,
   "downvotes": 0,
   "merge_requests_count": 0,
   "id" : 85,
   "assignees" : [],
   "assignee" : null,
   "milestone" : null,
   "subscribed" : true,
   "user_notes_count": 0,
   "due_date": "2016-07-22",
   "web_url": "http://gitlab.example.com/my-group/my-project/issues/15",
   "references": {
     "short": "#15",
     "relative": "#15",
     "full": "my-group/my-project#15"
   },
   "time_stats": {
      "time_estimate": 0,
      "total_time_spent": 0,
      "human_time_estimate": null,
      "human_total_time_spent": null
   },
   "confidential": false,
   "discussion_locked": false,
   "issue_type": "issue",
   "severity": "UNKNOWN",
   "_links": {
      "self": "http://gitlab.example.com/api/v4/projects/1/issues/2",
      "notes": "http://gitlab.example.com/api/v4/projects/1/issues/2/notes",
      "award_emoji": "http://gitlab.example.com/api/v4/projects/1/issues/2/award_emoji",
      "project": "http://gitlab.example.com/api/v4/projects/1",
      "closed_as_duplicate_of": "http://gitlab.example.com/api/v4/projects/1/issues/75"

   },
   "task_completion_status":{
      "count":0,
      "completed_count":0
   }
}
```

Issues created by users on GitLab Premium or Ultimate include the `weight` property:

```json
{
   "project_id" : 4,
   "description" : null,
   "weight": null,
   ...
}
```

Issues created by users on GitLab Premium or Ultimate include the `epic` property:

```json
{
   "project_id" : 4,
   "description" : "Omnis vero earum sunt corporis dolor et placeat.",
   "epic_iid" : 5, //deprecated, use `iid` of the `epic` attribute
   "epic": {
     "id" : 42,
     "iid" : 5,
     "title": "My epic epic",
     "url" : "/groups/h5bp/-/epics/5",
     "group_id": 8
   },
   ...
}
```

Issues created by users on GitLab Ultimate include the `health_status` property:

```json
[
   {
      "project_id" : 4,
      "description" : "Omnis vero earum sunt corporis dolor et placeat.",
      "health_status": "on_track",
      ...
   }
]
```

WARNING:
The `epic_iid` attribute is deprecated and [scheduled for removal](https://gitlab.com/gitlab-org/gitlab/-/issues/35157) in API version 5.
Use `iid` of the `epic` attribute instead.

WARNING:
`assignee` column is deprecated. We now show it as a single-sized array `assignees` to conform to the GitLab EE API.


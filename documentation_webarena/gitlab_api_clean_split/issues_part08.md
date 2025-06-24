## New issue

Creates a new project issue.

```plaintext
POST /projects/:id/issues
```

Supported attributes:

| Attribute                                 | Type           | Required | Description  |
|-------------------------------------------|----------------|----------|--------------|
| `id`                                      | integer/string | Yes      | The global ID or [URL-encoded path of the project](rest/index.md#namespaced-path-encoding) owned by the authenticated user. |
| `assignee_id`                             | integer        | No       | The ID of the user to assign the issue to. Only appears on GitLab Free. |
| `assignee_ids`                            | integer array  | No       | The IDs of the users to assign the issue to. Premium and Ultimate only.|
| `confidential`                            | boolean        | No       | Set an issue to be confidential. Default is `false`.  |
| `created_at`                              | string         | No       | When the issue was created. Date time string, ISO 8601 formatted, for example `2016-03-11T03:45:40Z`. Requires administrator or project/group owner rights. |
| `description`                             | string         | No       | The description of an issue. Limited to 1,048,576 characters. |
| `discussion_to_resolve`                   | string         | No       | The ID of a discussion to resolve. This fills out the issue with a default description and mark the discussion as resolved. Use in combination with `merge_request_to_resolve_discussions_of`. |
| `due_date`                                | string         | No       | The due date. Date time string in the format `YYYY-MM-DD`, for example `2016-03-11`. |
| `epic_id`                                 | integer | No | ID of the epic to add the issue to. Valid values are greater than or equal to 0. Premium and Ultimate only. |
| `epic_iid`                                | integer | No | IID of the epic to add the issue to. Valid values are greater than or equal to 0. (deprecated, [scheduled for removal](https://gitlab.com/gitlab-org/gitlab/-/issues/35157) in API version 5). Premium and Ultimate only. |
| `iid`                                     | integer/string | No       | The internal ID of the project's issue (requires administrator or project owner rights). |
| `issue_type`                              | string         | No       | The type of issue. One of `issue`, `incident`, `test_case` or `task`. Default is `issue`. |
| `labels`                                  | string         | No       | Comma-separated label names to assign to the new issue. If a label does not already exist, this creates a new project label and assigns it to the issue.  |
| `merge_request_to_resolve_discussions_of` | integer        | No       | The IID of a merge request in which to resolve all issues. This fills out the issue with a default description and mark all discussions as resolved. When passing a description or title, these values take precedence over the default values.|
| `milestone_id`                            | integer        | No       | The global ID of a milestone to assign issue. To find the `milestone_id` associated with a milestone, view an issue with the milestone assigned and [use the API](#single-project-issue) to retrieve the issue's details. |
| `title`                                   | string         | Yes      | The title of an issue. |
| `weight`                                  | integer        | No       | The weight of the issue. Valid values are greater than or equal to 0. Premium and Ultimate only. |

Example request:

```shell
curl --request POST \
  --header "PRIVATE-TOKEN: <your_access_token>" \
  --url "https://gitlab.example.com/api/v4/projects/4/issues?title=Issues%20with%20auth&labels=bug"
```

Example response:

```json
{
   "project_id" : 4,
   "id" : 84,
   "created_at" : "2016-01-07T12:44:33.959Z",
   "iid" : 14,
   "title" : "Issues with auth",
   "state" : "opened",
   "assignees" : [],
   "assignee" : null,
   "type" : "ISSUE",
   "labels" : [
      "bug"
   ],
   "upvotes": 4,
   "downvotes": 0,
   "merge_requests_count": 0,
   "author" : {
      "name" : "Alexandra Bashirian",
      "avatar_url" : null,
      "state" : "active",
      "web_url" : "https://gitlab.example.com/eileen.lowe",
      "id" : 18,
      "username" : "eileen.lowe"
   },
   "description" : null,
   "updated_at" : "2016-01-07T12:44:33.959Z",
   "closed_at" : null,
   "closed_by" : null,
   "milestone" : null,
   "subscribed" : true,
   "user_notes_count": 0,
   "due_date": null,
   "web_url": "http://gitlab.example.com/my-group/my-project/issues/14",
   "references": {
     "short": "#14",
     "relative": "#14",
     "full": "my-group/my-project#14"
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
The `assignee` column is deprecated. We now show it as a single-sized array `assignees` to conform to the GitLab EE API.

WARNING:
The `epic_iid` attribute is deprecated and [scheduled for removal](https://gitlab.com/gitlab-org/gitlab/-/issues/35157) in API version 5.
Use `iid` of the `epic` attribute instead.

### Rate limits

To help avoid abuse, users can be limited to a specific number of `Create` requests per minute.
See [Issues rate limits](../administration/settings/rate_limit_on_issues_creation.md).


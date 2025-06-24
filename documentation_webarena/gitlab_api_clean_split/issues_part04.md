## List group issues

Get a list of a group's issues.

If the group is private, you must provide credentials to authorize.
The preferred way to do this, is by using [personal access tokens](../user/profile/personal_access_tokens.md).

```plaintext
GET /groups/:id/issues
GET /groups/:id/issues?assignee_id=5
GET /groups/:id/issues?author_id=5
GET /groups/:id/issues?confidential=true
GET /groups/:id/issues?iids[]=42&iids[]=43
GET /groups/:id/issues?labels=foo
GET /groups/:id/issues?labels=foo,bar
GET /groups/:id/issues?labels=foo,bar&state=opened
GET /groups/:id/issues?milestone=1.0.0
GET /groups/:id/issues?milestone=1.0.0&state=opened
GET /groups/:id/issues?my_reaction_emoji=star
GET /groups/:id/issues?search=issue+title+or+description
GET /groups/:id/issues?state=closed
GET /groups/:id/issues?state=opened
```

Supported attributes:

| Attribute           | Type             | Required   | Description                                                                                                                   |
| ------------------- | ---------------- | ---------- | ----------------------------------------------------------------------------------------------------------------------------- |
| `id`                | integer/string   | Yes        | The global ID or [URL-encoded path of the group](rest/index.md#namespaced-path-encoding) owned by the authenticated user.                 |
| `assignee_id`       | integer          | No         | Return issues assigned to the given user `id`. Mutually exclusive with `assignee_username`. `None` returns unassigned issues. `Any` returns issues with an assignee. |
| `assignee_username` | string array     | No         | Return issues assigned to the given `username`. Similar to `assignee_id` and mutually exclusive with `assignee_id`. In GitLab CE, the `assignee_username` array should only contain a single value. Otherwise, an invalid parameter error is returned. |
| `author_id`         | integer          | No         | Return issues created by the given user `id`. Mutually exclusive with `author_username`. Combine with `scope=all` or `scope=assigned_to_me`. |
| `author_username`   | string           | No         | Return issues created by the given `username`. Similar to `author_id` and mutually exclusive with `author_id`. |
| `confidential`     | boolean          | No         | Filter confidential or public issues.                                                                                         |
| `created_after`     | datetime         | No         | Return issues created on or after the given time. Expected in ISO 8601 format (`2019-03-15T08:00:00Z`). |
| `created_before`    | datetime         | No         | Return issues created on or before the given time. Expected in ISO 8601 format (`2019-03-15T08:00:00Z`). |
| `due_date`          | string           | No         | Return issues that have no due date, are overdue, or whose due date is this week, this month, or between two weeks ago and next month. Accepts: `0` (no due date), `any`, `today`, `tomorrow`, `overdue`, `week`, `month`, `next_month_and_previous_two_weeks`. |
| `epic_id`           | integer      | No         | Return issues associated with the given epic ID. `None` returns issues that are not associated with an epic. `Any` returns issues that are associated with an epic. Premium and Ultimate only. |
| `iids[]`            | integer array    | No         | Return only the issues having the given `iid`.                                                                                 |
| `issue_type`        | string           | No         | Filter to a given type of issue. One of `issue`, `incident`, `test_case` or `task`. |
| `iteration_id`      | integer | No         | Return issues assigned to the given iteration ID. `None` returns issues that do not belong to an iteration. `Any` returns issues that belong to an iteration. Mutually exclusive with `iteration_title`. Premium and Ultimate only. |
| `iteration_title`   | string | No       | Return issues assigned to the iteration with the given title. Similar to `iteration_id` and mutually exclusive with `iteration_id`. Premium and Ultimate only.|
| `labels`            | string           | No         | Comma-separated list of label names, issues must have all labels to be returned. `None` lists all issues with no labels. `Any` lists all issues with at least one label. `No+Label` (Deprecated) lists all issues with no labels. Predefined names are case-insensitive. |
| `milestone`         | string           | No         | The milestone title. `None` lists all issues with no milestone. `Any` lists all issues that have an assigned milestone.       |
| `my_reaction_emoji` | string           | No         | Return issues reacted by the authenticated user by the given `emoji`. `None` returns issues not given a reaction. `Any` returns issues given at least one reaction. |
| `non_archived`      | boolean          | No         | Return issues from non archived projects. Default is true. |
| `not`               | Hash             | No         | Return issues that do not match the parameters supplied. Accepts: `labels`, `milestone`, `author_id`, `author_username`, `assignee_id`, `assignee_username`, `my_reaction_emoji`, `search`, `in`. |
| `order_by`          | string           | No         | Return issues ordered by `created_at`, `updated_at`, `priority`, `due_date`, `relative_position`, `label_priority`, `milestone_due`, `popularity`, `weight` fields. Default is `created_at`                                                               |
| `scope`             | string           | No         | Return issues for the given scope: `created_by_me`, `assigned_to_me` or `all`. Defaults to `all`. |
| `search`            | string           | No         | Search group issues against their `title` and `description`.                                                                   |
| `sort`              | string           | No         | Return issues sorted in `asc` or `desc` order. Default is `desc`.                                                              |
| `state`             | string           | No         | Return all issues or just those that are `opened` or `closed`.                                                                 |
| `updated_after`     | datetime         | No         | Return issues updated on or after the given time. Expected in ISO 8601 format (`2019-03-15T08:00:00Z`). |
| `updated_before`    | datetime         | No         | Return issues updated on or before the given time. Expected in ISO 8601 format (`2019-03-15T08:00:00Z`). |
| `weight` | integer       | No         | Return issues with the specified `weight`. `None` returns issues with no weight assigned. `Any` returns issues with a weight assigned. Premium and Ultimate only. |
| `with_labels_details` | boolean        | No         | If `true`, the response returns more details for each label in labels field: `:name`, `:color`, `:description`, `:description_html`, `:text_color`. Default is `false`. |

Example request:

```shell
curl --header "PRIVATE-TOKEN: <your_access_token>" \
  --url "https://gitlab.example.com/api/v4/groups/4/issues"
```

Example response:

```json
[
   {
      "project_id" : 4,
      "milestone" : {
         "due_date" : null,
         "project_id" : 4,
         "state" : "closed",
         "description" : "Rerum est voluptatem provident consequuntur molestias similique ipsum dolor.",
         "iid" : 3,
         "id" : 11,
         "title" : "v3.0",
         "created_at" : "2016-01-04T15:31:39.788Z",
         "updated_at" : "2016-01-04T15:31:39.788Z"
      },
      "author" : {
         "state" : "active",
         "web_url" : "https://gitlab.example.com/root",
         "avatar_url" : null,
         "username" : "root",
         "id" : 1,
         "name" : "Administrator"
      },
      "description" : "Omnis vero earum sunt corporis dolor et placeat.",
      "state" : "closed",
      "iid" : 1,
      "assignees" : [{
         "avatar_url" : null,
         "web_url" : "https://gitlab.example.com/lennie",
         "state" : "active",
         "username" : "lennie",
         "id" : 9,
         "name" : "Dr. Luella Kovacek"
      }],
      "assignee" : {
         "avatar_url" : null,
         "web_url" : "https://gitlab.example.com/lennie",
         "state" : "active",
         "username" : "lennie",
         "id" : 9,
         "name" : "Dr. Luella Kovacek"
      },
      "type" : "ISSUE",
      "labels" : ["foo", "bar"],
      "upvotes": 4,
      "downvotes": 0,
      "merge_requests_count": 0,
      "id" : 41,
      "title" : "Ut commodi ullam eos dolores perferendis nihil sunt.",
      "updated_at" : "2016-01-04T15:31:46.176Z",
      "created_at" : "2016-01-04T15:31:46.176Z",
      "closed_at" : null,
      "closed_by" : null,
      "user_notes_count": 1,
      "due_date": null,
      "imported": false,
      "imported_from": "none",
      "web_url": "http://gitlab.example.com/my-group/my-project/issues/1",
      "references": {
        "short": "#1",
        "relative": "my-project#1",
        "full": "my-group/my-project#1"
      },
      "time_stats": {
         "time_estimate": 0,
         "total_time_spent": 0,
         "human_time_estimate": null,
         "human_total_time_spent": null
      },
      "has_tasks": true,
      "task_status": "10 of 15 tasks completed",
      "confidential": false,
      "discussion_locked": false,
      "issue_type": "issue",
      "severity": "UNKNOWN",
      "_links":{
         "self":"http://gitlab.example.com/api/v4/projects/4/issues/41",
         "notes":"http://gitlab.example.com/api/v4/projects/4/issues/41/notes",
         "award_emoji":"http://gitlab.example.com/api/v4/projects/4/issues/41/award_emoji",
         "project":"http://gitlab.example.com/api/v4/projects/4",
         "closed_as_duplicate_of": "http://gitlab.example.com/api/v4/projects/1/issues/75"
      },
      "task_completion_status":{
         "count":0,
         "completed_count":0
      }
   }
]
```

Issues created by users on GitLab Premium or Ultimate include the `weight` property:

```json
[
   {
      "project_id" : 4,
      "description" : "Omnis vero earum sunt corporis dolor et placeat.",
      "weight": null,
      ...
   }
]
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
      "health_status": "at_risk",
      ...
   }
]
```

WARNING:
The `assignee` column is deprecated. We now show it as a single-sized array `assignees` to conform to the GitLab EE API.

WARNING:
The `epic_iid` attribute is deprecated and [scheduled for removal](https://gitlab.com/gitlab-org/gitlab/-/issues/35157) in API version 5.
Use `iid` of the `epic` attribute instead.


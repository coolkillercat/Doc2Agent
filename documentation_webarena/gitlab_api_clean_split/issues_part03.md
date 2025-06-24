## List issues

Get all issues the authenticated user has access to. By default it
returns only issues created by the current user. To get all issues,
use parameter `scope=all`.

```plaintext
GET /issues
GET /issues?assignee_id=5
GET /issues?author_id=5
GET /issues?confidential=true
GET /issues?iids[]=42&iids[]=43
GET /issues?labels=foo
GET /issues?labels=foo,bar
GET /issues?labels=foo,bar&state=opened
GET /issues?milestone=1.0.0
GET /issues?milestone=1.0.0&state=opened
GET /issues?my_reaction_emoji=star
GET /issues?search=foo&in=title
GET /issues?state=closed
GET /issues?state=opened
```

Supported attributes:

| Attribute                       | Type          | Required   | Description                                                                                                                                         |
|---------------------------------|---------------| ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| `assignee_id`                   | integer       | No         | Return issues assigned to the given user `id`. Mutually exclusive with `assignee_username`. `None` returns unassigned issues. `Any` returns issues with an assignee. |
| `assignee_username`             | string array  | No         | Return issues assigned to the given `username`. Similar to `assignee_id` and mutually exclusive with `assignee_id`. In GitLab CE, the `assignee_username` array should only contain a single value. Otherwise, an invalid parameter error is returned. |
| `author_id`                     | integer       | No         | Return issues created by the given user `id`. Mutually exclusive with `author_username`. Combine with `scope=all` or `scope=assigned_to_me`. |
| `author_username`               | string        | No         | Return issues created by the given `username`. Similar to `author_id` and mutually exclusive with `author_id`. |
| `confidential`                  | boolean       | No         | Filter confidential or public issues.                                                                                                               |
| `created_after`                 | datetime      | No         | Return issues created on or after the given time. Expected in ISO 8601 format (`2019-03-15T08:00:00Z`). |
| `created_before`                | datetime      | No         | Return issues created on or before the given time. Expected in ISO 8601 format (`2019-03-15T08:00:00Z`). |
| `due_date`                      | string        | No         | Return issues that have no due date, are overdue, or whose due date is this week, this month, or between two weeks ago and next month. Accepts: `0` (no due date), `any`, `today`, `tomorrow`, `overdue`, `week`, `month`, `next_month_and_previous_two_weeks`. |
| `epic_id`        | integer       | No         | Return issues associated with the given epic ID. `None` returns issues that are not associated with an epic. `Any` returns issues that are associated with an epic. Premium and Ultimate only. |
| `health_status`  | string        | No         | Return issues with the specified `health_status`. _([Introduced](https://gitlab.com/gitlab-org/gitlab/-/issues/370721) in GitLab 15.4)._ In [GitLab 15.5 and later](https://gitlab.com/gitlab-org/gitlab/-/issues/370721), `None` returns issues with no health status assigned, and `Any` returns issues with a health status assigned. Ultimate only. |
| `iids[]`                        | integer array | No         | Return only the issues having the given `iid`.                                                                                                       |
| `in`                            | string        | No         | Modify the scope of the `search` attribute. `title`, `description`, or a string joining them with comma. Default is `title,description`.             |
| `issue_type`                    | string        | No         | Filter to a given type of issue. One of `issue`, `incident`, `test_case` or `task`. |
| `iteration_id`                  | integer       | No         | Return issues assigned to the given iteration ID. `None` returns issues that do not belong to an iteration. `Any` returns issues that belong to an iteration. Mutually exclusive with `iteration_title`. Premium and Ultimate only. |
| `iteration_title`               | string        | No       | Return issues assigned to the iteration with the given title. Similar to `iteration_id` and mutually exclusive with `iteration_id`. Premium and Ultimate only. |
| `labels`                        | string        | No         | Comma-separated list of label names, issues must have all labels to be returned. `None` lists all issues with no labels. `Any` lists all issues with at least one label. `No+Label` (Deprecated) lists all issues with no labels. Predefined names are case-insensitive. |
| `milestone_id`                  | string        | No         | Returns issues assigned to milestones with a given timebox value (`None`, `Any`, `Upcoming`, and `Started`). `None` lists all issues with no milestone. `Any` lists all issues that have an assigned milestone. `Upcoming` lists all issues assigned to milestones due in the future. `Started` lists all issues assigned to open, started milestones. `milestone` and `milestone_id` are mutually exclusive. |
| `milestone`                     | string        | No         | The milestone title. `None` lists all issues with no milestone. `Any` lists all issues that have an assigned milestone. Using `None` or `Any` will be [deprecated in the future](https://gitlab.com/gitlab-org/gitlab/-/issues/336044). Use `milestone_id` attribute instead. `milestone` and `milestone_id` are mutually exclusive. |
| `my_reaction_emoji`             | string        | No         | Return issues reacted by the authenticated user by the given `emoji`. `None` returns issues not given a reaction. `Any` returns issues given at least one reaction. |
| `non_archived`                  | boolean       | No         | Return issues only from non-archived projects. If `false`, the response returns issues from both archived and non-archived projects. Default is `true`. |
| `not`                           | Hash          | No         | Return issues that do not match the parameters supplied. Accepts: `assignee_id`, `assignee_username`, `author_id`, `author_username`, `iids`, `iteration_id`, `iteration_title`, `labels`, `milestone`, `milestone_id` and `weight`. |
| `order_by`                      | string        | No         | Return issues ordered by `created_at`, `due_date`, `label_priority`, `milestone_due`, `popularity`, `priority`, `relative_position`, `title`, `updated_at`, or `weight` fields. Default is `created_at`. |
| `scope`                         | string        | No         | Return issues for the given scope: `created_by_me`, `assigned_to_me` or `all`. Defaults to `created_by_me`. |
| `search`                        | string        | No         | Search issues against their `title` and `description`.                                                                                               |
| `sort`                          | string        | No         | Return issues sorted in `asc` or `desc` order. Default is `desc`.                                                                                    |
| `state`                         | string        | No         | Return `all` issues or just those that are `opened` or `closed`.                                                                                       |
| `updated_after`                 | datetime      | No         | Return issues updated on or after the given time. Expected in ISO 8601 format (`2019-03-15T08:00:00Z`). |
| `updated_before`                | datetime      | No         | Return issues updated on or before the given time. Expected in ISO 8601 format (`2019-03-15T08:00:00Z`). |
| `weight`                        | integer       | No         | Return issues with the specified `weight`. `None` returns issues with no weight assigned. `Any` returns issues with a weight assigned. Premium and Ultimate only.   |
| `with_labels_details`           | boolean       | No         | If `true`, the response returns more details for each label in labels field: `:name`, `:color`, `:description`, `:description_html`, `:text_color`. Default is `false`. |

Example request:

```shell
curl --header "PRIVATE-TOKEN: <your_access_token>" \
  --url "https://gitlab.example.com/api/v4/issues"
```

Example response:

```json
[
   {
      "state" : "opened",
      "description" : "Ratione dolores corrupti mollitia soluta quia.",
      "author" : {
         "state" : "active",
         "id" : 18,
         "web_url" : "https://gitlab.example.com/eileen.lowe",
         "name" : "Alexandra Bashirian",
         "avatar_url" : null,
         "username" : "eileen.lowe"
      },
      "milestone" : {
         "project_id" : 1,
         "description" : "Ducimus nam enim ex consequatur cumque ratione.",
         "state" : "closed",
         "due_date" : null,
         "iid" : 2,
         "created_at" : "2016-01-04T15:31:39.996Z",
         "title" : "v4.0",
         "id" : 17,
         "updated_at" : "2016-01-04T15:31:39.996Z"
      },
      "project_id" : 1,
      "assignees" : [{
         "state" : "active",
         "id" : 1,
         "name" : "Administrator",
         "web_url" : "https://gitlab.example.com/root",
         "avatar_url" : null,
         "username" : "root"
      }],
      "assignee" : {
         "state" : "active",
         "id" : 1,
         "name" : "Administrator",
         "web_url" : "https://gitlab.example.com/root",
         "avatar_url" : null,
         "username" : "root"
      },
      "type" : "ISSUE",
      "updated_at" : "2016-01-04T15:31:51.081Z",
      "closed_at" : null,
      "closed_by" : null,
      "id" : 76,
      "title" : "Consequatur vero maxime deserunt laboriosam est voluptas dolorem.",
      "created_at" : "2016-01-04T15:31:51.081Z",
      "moved_to_id" : null,
      "iid" : 6,
      "labels" : ["foo", "bar"],
      "upvotes": 4,
      "downvotes": 0,
      "merge_requests_count": 0,
      "user_notes_count": 1,
      "due_date": "2016-07-22",
      "imported":false,
      "imported_from": "none",
      "web_url": "http://gitlab.example.com/my-group/my-project/issues/6",
      "references": {
        "short": "#6",
        "relative": "my-group/my-project#6",
        "full": "my-group/my-project#6"
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
         "self":"http://gitlab.example.com/api/v4/projects/1/issues/76",
         "notes":"http://gitlab.example.com/api/v4/projects/1/issues/76/notes",
         "award_emoji":"http://gitlab.example.com/api/v4/projects/1/issues/76/award_emoji",
         "project":"http://gitlab.example.com/api/v4/projects/1",
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
      "state" : "opened",
      "description" : "Ratione dolores corrupti mollitia soluta quia.",
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

Issues created by users on GitLab Premium or Ultimate include the `iteration` property:

```json
{
   "iteration": {
      "id":90,
      "iid":4,
      "sequence":2,
      "group_id":162,
      "title":null,
      "description":null,
      "state":2,
      "created_at":"2022-03-14T05:21:11.929Z",
      "updated_at":"2022-03-14T05:21:11.929Z",
      "start_date":"2022-03-08",
      "due_date":"2022-03-14",
      "web_url":"https://gitlab.com/groups/my-group/-/iterations/90"
   }
   ...
}
```

Issues created by users on GitLab Ultimate include the `health_status` property:

```json
[
   {
      "state" : "opened",
      "description" : "Ratione dolores corrupti mollitia soluta quia.",
      "health_status": "on_track",
      ...
   }
]
```

WARNING:
The `assignee` column is deprecated. We now show it as a single-sized array `assignees` to conform
to the GitLab EE API.

WARNING:
The `epic_iid` attribute is deprecated and [scheduled for removal](https://gitlab.com/gitlab-org/gitlab/-/issues/35157) in API version 5.
Use `iid` of the `epic` attribute instead.


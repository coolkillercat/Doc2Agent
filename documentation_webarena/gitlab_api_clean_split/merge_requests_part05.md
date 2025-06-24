## List group merge requests

Get all merge requests for this group and its subgroups.

```plaintext
GET /groups/:id/merge_requests
GET /groups/:id/merge_requests?state=opened
GET /groups/:id/merge_requests?state=all
GET /groups/:id/merge_requests?milestone=release
GET /groups/:id/merge_requests?labels=bug,reproduced
GET /groups/:id/merge_requests?my_reaction_emoji=star
```

Supported attributes:

| Attribute                       | Type           | Required | Description |
| ------------------------------- | -------------- | -------- | ----------- |
| `id`                            | integer or string | Yes      | The ID or [URL-encoded path of the group](rest/index.md#namespaced-path-encoding) owned by the authenticated user. |
| `approved_by_ids`               | integer array  | No       | Returns merge requests which have been approved by all the users with the given `id`, with a maximum of 5. `None` returns merge requests with no approvals. `Any` returns merge requests with an approval. Premium and Ultimate only. |
| `approved_by_usernames`         | string array  | No       | Returns merge requests which have been approved by all the users with the given `username`, with a maximum of 5. `None` returns merge requests with no approvals. `Any` returns merge requests with an approval. Premium and Ultimate only. |
| `approver_ids`                  | integer array  | No       | Returns merge requests which have specified all the users with the given `id`s as individual approvers. `None` returns merge requests without approvers. `Any` returns merge requests with an approver. Premium and Ultimate only. |
| `approved`                      | string         | No       | Filters merge requests by their `approved` status. `yes` returns only approved merge requests. `no` returns only non-approved merge requests. [Introduced](https://gitlab.com/gitlab-org/gitlab/-/issues/3159) in GitLab 15.11. Available only when the feature flag `mr_approved_filter` is enabled. |
| `assignee_id`                   | integer        | No       | Returns merge requests assigned to the given user `id`. `None` returns unassigned merge requests. `Any` returns merge requests with an assignee. |
| `author_id`                     | integer        | No       | Returns merge requests created by the given user `id`. Mutually exclusive with `author_username`. |
| `author_username`               | string         | No       | Returns merge requests created by the given `username`. Mutually exclusive with `author_id`. |
| `created_after`                 | datetime       | No       | Returns merge requests created on or after the given time. Expected in ISO 8601 format (`2019-03-15T08:00:00Z`). |
| `created_before`                | datetime       | No       | Returns merge requests created on or before the given time. Expected in ISO 8601 format (`2019-03-15T08:00:00Z`). |
| `labels`                        | string         | No       | Returns merge requests matching a comma-separated list of labels. `None` lists all merge requests with no labels. `Any` lists all merge requests with at least one label. Predefined names are case-insensitive. |
| `merge_user_id`                 | integer        | No       | Returns merge requests which have been merged by the user with the given user `id`. Mutually exclusive with `merge_user_username`. [Introduced](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/140002) in GitLab 17.0. |
| `merge_user_username`           | string         | No       | Returns merge requests which have been merged by the user with the given `username`. Mutually exclusive with `merge_user_id`. [Introduced](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/140002) in GitLab 17.0. |
| `milestone`                     | string         | No       | Returns merge requests for a specific milestone. `None` returns merge requests with no milestone. `Any` returns merge requests that have an assigned milestone. |
| `my_reaction_emoji`             | string         | No       | Returns merge requests reacted by the authenticated user by the given `emoji`. `None` returns issues not given a reaction. `Any` returns issues given at least one reaction. |
| `non_archived`                  | boolean        | No       | Returns merge requests from non archived projects only. Default is `true`. |
| `not`                           | Hash           | No       | Returns merge requests that do not match the parameters supplied. Accepts: `labels`, `milestone`, `author_id`, `author_username`, `assignee_id`, `assignee_username`, `reviewer_id`, `reviewer_username`, `my_reaction_emoji`. |
| `order_by`                      | string         | No       | Returns merge requests ordered by `created_at`, `title` or `updated_at` fields. Default is `created_at`. |
| `reviewer_id`                   | integer        | No       | Returns merge requests which have the user as a [reviewer](../user/project/merge_requests/reviews/index.md) with the given user `id`. `None` returns merge requests with no reviewers. `Any` returns merge requests with any reviewer. Mutually exclusive with `reviewer_username`. |
| `reviewer_username`             | string         | No       | Returns merge requests which have the user as a [reviewer](../user/project/merge_requests/reviews/index.md) with the given `username`. `None` returns merge requests with no reviewers. `Any` returns merge requests with any reviewer. Mutually exclusive with `reviewer_id`. |
| `scope`                         | string         | No       | Returns merge requests for the given scope: `created_by_me`, `assigned_to_me` or `all`. |
| `search`                        | string         | No       | Search merge requests against their `title` and `description`. |
| `source_branch`                 | string         | No       | Returns merge requests with the given source branch. |
| `sort`                          | string         | No       | Returns merge requests sorted in `asc` or `desc` order. Default is `desc`. |
| `state`                         | string         | No       | Returns all merge requests (`all`) or just those that are `opened`, `closed`, `locked`, or `merged`. |
| `target_branch`                 | string         | No       | Returns merge requests with the given target branch. |
| `updated_after`                 | datetime       | No       | Returns merge requests updated on or after the given time. Expected in ISO 8601 format (`2019-03-15T08:00:00Z`). |
| `updated_before`                | datetime       | No       | Returns merge requests updated on or before the given time. Expected in ISO 8601 format (`2019-03-15T08:00:00Z`). |
| `view`                          | string         | No       | If `simple`, returns the `iid`, URL, title, description, and basic state of merge request. |
| `with_labels_details`           | boolean        | No       | If `true`, response returns more details for each label in labels field: `:name`, `:color`, `:description`, `:description_html`, `:text_color`. Default is `false`. |
| `with_merge_status_recheck`     | boolean        | No       | If `true`, this projection requests (but does not guarantee) that the `merge_status` field be recalculated asynchronously. Default is `false`. In GitLab 15.11 and later, enable the `restrict_merge_status_recheck` feature [flag](../administration/feature_flags.md) for this attribute to be ignored when requested by users without at least the Developer role. |

The pagination parameters `page` and `per_page` can be used to restrict the list of merge requests.

In the response, `group_id` represents the ID of the group containing the project where the merge request resides.

Example response:

```json
[
  {
    "id": 1,
    "iid": 1,
    "project_id": 3,
    "title": "test1",
    "description": "fixed login page css paddings",
    "state": "merged",
    "imported": false,
    "imported_from": "none",
    "merged_by": { // Deprecated and will be removed in API v5, use `merge_user` instead
      "id": 87854,
      "name": "Douwe Maan",
      "username": "DouweM",
      "state": "active",
      "avatar_url": "https://gitlab.example.com/uploads/-/system/user/avatar/87854/avatar.png",
      "web_url": "https://gitlab.com/DouweM"
    },
    "merge_user": {
      "id": 87854,
      "name": "Douwe Maan",
      "username": "DouweM",
      "state": "active",
      "avatar_url": "https://gitlab.example.com/uploads/-/system/user/avatar/87854/avatar.png",
      "web_url": "https://gitlab.com/DouweM"
    },
    "merged_at": "2018-09-07T11:16:17.520Z",
    "prepared_at": "2018-09-04T11:16:17.520Z",
    "closed_by": null,
    "closed_at": null,
    "created_at": "2017-04-29T08:46:00Z",
    "updated_at": "2017-04-29T08:46:00Z",
    "target_branch": "main",
    "source_branch": "test1",
    "upvotes": 0,
    "downvotes": 0,
    "author": {
      "id": 1,
      "name": "Administrator",
      "username": "admin",
      "state": "active",
      "avatar_url": null,
      "web_url" : "https://gitlab.example.com/admin"
    },
    "assignee": {
      "id": 1,
      "name": "Administrator",
      "username": "admin",
      "state": "active",
      "avatar_url": null,
      "web_url" : "https://gitlab.example.com/admin"
    },
    "assignees": [{
      "name": "Miss Monserrate Beier",
      "username": "axel.block",
      "id": 12,
      "state": "active",
      "avatar_url": "http://www.gravatar.com/avatar/46f6f7dc858ada7be1853f7fb96e81da?s=80&d=identicon",
      "web_url": "https://gitlab.example.com/axel.block"
    }],
    "reviewers": [{
      "id": 2,
      "name": "Sam Bauch",
      "username": "kenyatta_oconnell",
      "state": "active",
      "avatar_url": "https://www.gravatar.com/avatar/956c92487c6f6f7616b536927e22c9a0?s=80&d=identicon",
      "web_url": "http://gitlab.example.com//kenyatta_oconnell"
    }],
    "source_project_id": 2,
    "target_project_id": 3,
    "labels": [
      "Community contribution",
      "Manage"
    ],
    "draft": false,
    "work_in_progress": false,
    "milestone": {
      "id": 5,
      "iid": 1,
      "project_id": 3,
      "title": "v2.0",
      "description": "Assumenda aut placeat expedita exercitationem labore sunt enim earum.",
      "state": "closed",
      "created_at": "2015-02-02T19:49:26.013Z",
      "updated_at": "2015-02-02T19:49:26.013Z",
      "due_date": "2018-10-22",
      "start_date": "2018-09-08",
      "web_url": "gitlab.example.com/my-group/my-project/milestones/1"
    },
    "merge_when_pipeline_succeeds": true,
    "merge_status": "can_be_merged",
    "detailed_merge_status": "not_open",
    "sha": "8888888888888888888888888888888888888888",
    "merge_commit_sha": null,
    "squash_commit_sha": null,
    "user_notes_count": 1,
    "discussion_locked": null,
    "should_remove_source_branch": true,
    "force_remove_source_branch": false,
    "web_url": "http://gitlab.example.com/my-group/my-project/merge_requests/1",
    "references": {
      "short": "!1",
      "relative": "my-project!1",
      "full": "my-group/my-project!1"
    },
    "time_stats": {
      "time_estimate": 0,
      "total_time_spent": 0,
      "human_time_estimate": null,
      "human_total_time_spent": null
    },
    "squash": false,
    "task_completion_status":{
      "count":0,
      "completed_count":0
    },
    "has_conflicts": false,
    "blocking_discussions_resolved": true
  }
]
```

For important notes on response data, see [Merge requests list response notes](#merge-requests-list-response-notes).


## Get single MR

Shows information about a single merge request.

```plaintext
GET /projects/:id/merge_requests/:merge_request_iid
```

Supported attributes:

| Attribute                        | Type           | Required | Description |
|----------------------------------|----------------|----------|-------------|
| `id`                             | integer or string | Yes      | The ID or [URL-encoded path of the project](rest/index.md#namespaced-path-encoding) owned by the authenticated user. |
| `merge_request_iid`              | integer        | Yes      | The internal ID of the merge request. |
| `include_diverged_commits_count` | boolean        | No       | If `true`, response includes the commits behind the target branch. |
| `include_rebase_in_progress`     | boolean        | No       | If `true`, response includes whether a rebase operation is in progress. |
| `render_html`                    | boolean        | No       | If `true`, response includes rendered HTML for title and description. |

### Response

| Attribute                        | Type | Description |
|----------------------------------|------|-------------|
| `approvals_before_merge`| integer | Number of approvals required before this merge request can merge. To configure approval rules, see [Merge request approvals API](merge_request_approvals.md). [Deprecated](https://gitlab.com/gitlab-org/gitlab/-/issues/353097) in GitLab 16.0. Premium and Ultimate only. |
| `assignee` | object | First assignee of the merge request. |
| `assignees` | array | Assignees of the merge request. |
| `author` | object | User who created this merge request. |
| `blocking_discussions_resolved` | boolean | Indicates if all discussions are resolved only if all are required before merge request can be merged. |
| `changes_count` | string | Number of changes made on the merge request. Empty when the merge request is created, and populates asynchronously. A string, not an integer. When a merge request has too many changes to display and store, the value is capped at 1000 and returns the string `"1000+"`. See [Empty API Fields for new merge requests](#empty-api-fields-for-new-merge-requests).|
| `closed_at` | datetime | Timestamp of when the merge request was closed. |
| `closed_by` | object | User who closed this merge request. |
| `created_at` | datetime | Timestamp of when the merge request was created. |
| `description` | string | Description of the merge request. Contains Markdown rendered as HTML for caching. |
| `detailed_merge_status` | string | Detailed merge status of the merge request. See [merge status](#merge-status) for a list of potential values. |
| `diff_refs` | object | References of the base SHA, the head SHA, and the start SHA for this merge request. Corresponds to the latest diff version of the merge request. Empty when the merge request is created, and populates asynchronously. See [Empty API fields for new merge requests](#empty-api-fields-for-new-merge-requests). |
| `discussion_locked` | boolean | Indicates if comments on the merge request are locked to members only. |
| `downvotes` | integer | Number of downvotes for the merge request. |
| `draft` | boolean | Indicates if the merge request is a draft. |
| `first_contribution` | boolean | Indicates if the merge request is the first contribution of the author. |
| `first_deployed_to_production_at` | datetime | Timestamp of when the first deployment finished. |
| `force_remove_source_branch` | boolean | Indicates if the project settings lead to source branch deletion after merge. |
| `has_conflicts` | boolean | Indicates if merge request has conflicts and cannot be merged. Dependent on the `merge_status` property. Returns `false` unless `merge_status` is `cannot_be_merged`. |
| `head_pipeline` | object | Pipeline running on the branch HEAD of the merge request. Contains more complete information than `pipeline` and should be used instead of it. |
| `id` | integer | ID of the merge request. |
| `iid` | integer | Internal ID of the merge request. |
| `labels` | array | Labels of the merge request. |
| `latest_build_finished_at` | datetime | Timestamp of when the latest build for the merge request finished. |
| `latest_build_started_at` | datetime | Timestamp of when the latest build for the merge request started. |
| `merge_commit_sha` | string | SHA of the merge request commit. Returns `null` until merged. |
| `merge_error` | string | Error message shown when a merge has failed. To check mergeability, use `detailed_merge_status` instead  |
| `merge_user` | object | The user who merged this merge request, the user who set it to auto-merge, or `null`.  |
| `merge_status` | string | Status of the merge request. Can be `unchecked`, `checking`, `can_be_merged`, `cannot_be_merged`, or `cannot_be_merged_recheck`. Affects the `has_conflicts` property. For important notes on response data, see [Single merge request response notes](#single-merge-request-response-notes). [Deprecated](https://gitlab.com/gitlab-org/gitlab/-/issues/3169#note_1162532204) in GitLab 15.6. Use `detailed_merge_status` instead. |
| `merge_when_pipeline_succeeds` | boolean | Indicates if the merge has been set to be merged when its pipeline succeeds. |
| `merged_at` | datetime | Timestamp of when the merge request was merged. |
| `merged_by` | object | User who merged this merge request or set it to auto-merge. [Deprecated](https://gitlab.com/gitlab-org/gitlab/-/issues/350534) in GitLab 14.7, and scheduled for removal in [API version 5](https://gitlab.com/groups/gitlab-org/-/epics/8115). Use `merge_user` instead. |
| `milestone` | object | Milestone of the merge request. |
| `pipeline` | object | Pipeline running on the branch HEAD of the merge request. Consider using `head_pipeline` instead, as it contains more information. |
| `prepared_at` | datetime | Timestamp of when the merge request was prepared. This field is populated one time, only after all the [preparation steps](#preparation-steps) are completed, and is not updated if more changes are added. |
| `project_id` | integer | ID of the merge request project. |
| `reference` | string | Internal reference of the merge request. Returned in shortened format by default. [Deprecated](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/20354) in GitLab 12.7, and scheduled for removal in [API version 5](https://gitlab.com/groups/gitlab-org/-/epics/8115). Use `references` instead. |
| `references` | object | Internal references of the merge request. Includes `short`, `relative`, and `full` references. `references.relative` is relative to the merge request's group or project. When fetched from the merge request's project, `relative` and `short` formats are identical. When requested across groups or projects, `relative` and `full` formats are identical.|
| `reviewers` | array | Reviewers of the merge request. |
| `sha` | string | Diff head SHA of the merge request. |
| `should_remove_source_branch` | boolean | Indicates if the source branch of the merge request should be deleted after merge. |
| `source_branch` | string | Source branch of the merge request. |
| `source_project_id` | integer | ID of the merge request source project. |
| `squash` | boolean | Indicates if squash on merge is enabled. |
| `squash_commit_sha` | string | SHA of the squash commit. Empty until merged. |
| `state` | string | State of the merge request. Can be `opened`, `closed`, `merged` or `locked`. |
| `subscribed` | boolean | Indicates if the current authenticated user is subscribed to this merge request. |
| `target_branch` | string | Target branch of the merge request. |
| `target_project_id` | integer | ID of the merge request target project. |
| `task_completion_status` | object | Completion status of tasks. |
| `title` | string | Title of the merge request. |
| `updated_at` | datetime | Timestamp of when the merge request was updated. |
| `upvotes` | integer | Number of upvotes for the merge request. |
| `user` | object | Permissions of the user requested for the merge request. |
| `user_notes_count` | integer | User notes count of the merge request. |
| `web_url` | string | Web URL of the merge request. |
| `work_in_progress` | boolean | Deprecated: Use `draft` instead. Indicates if the merge request is a draft. |

Example response:

```json
{
  "id": 155016530,
  "iid": 133,
  "project_id": 15513260,
  "title": "Manual job rules",
  "description": "",
  "state": "opened",
  "imported": false,
  "imported_from": "none",
  "created_at": "2022-05-13T07:26:38.402Z",
  "updated_at": "2022-05-14T03:38:31.354Z",
  "merged_by": null, // Deprecated and will be removed in API v5. Use `merge_user` instead.
  "merge_user": null,
  "merged_at": null,
  "prepared_at": "2018-09-04T11:16:17.520Z",
  "closed_by": null,
  "closed_at": null,
  "target_branch": "main",
  "source_branch": "manual-job-rules",
  "user_notes_count": 0,
  "upvotes": 0,
  "downvotes": 0,
  "author": {
    "id": 4155490,
    "username": "marcel.amirault",
    "name": "Marcel Amirault",
    "state": "active",
    "avatar_url": "https://gitlab.com/uploads/-/system/user/avatar/4155490/avatar.png",
    "web_url": "https://gitlab.com/marcel.amirault"
  },
  "assignees": [],
  "assignee": null,
  "reviewers": [],
  "source_project_id": 15513260,
  "target_project_id": 15513260,
  "labels": [],
  "draft": false,
  "work_in_progress": false,
  "milestone": null,
  "merge_when_pipeline_succeeds": false,
  "merge_status": "can_be_merged",
  "detailed_merge_status": "can_be_merged",
  "sha": "e82eb4a098e32c796079ca3915e07487fc4db24c",
  "merge_commit_sha": null,
  "squash_commit_sha": null,
  "discussion_locked": null,
  "should_remove_source_branch": null,
  "force_remove_source_branch": true,
  "reference": "!133", // Deprecated. Use `references` instead.
  "references": {
    "short": "!133",
    "relative": "!133",
    "full": "marcel.amirault/test-project!133"
  },
  "web_url": "https://gitlab.com/marcel.amirault/test-project/-/merge_requests/133",
  "time_stats": {
    "time_estimate": 0,
    "total_time_spent": 0,
    "human_time_estimate": null,
    "human_total_time_spent": null
  },
  "squash": false,
  "task_completion_status": {
    "count": 0,
    "completed_count": 0
  },
  "has_conflicts": false,
  "blocking_discussions_resolved": true,
  "approvals_before_merge": null, // deprecated, use [Merge request approvals API](merge_request_approvals.md)
  "subscribed": true,
  "changes_count": "1",
  "latest_build_started_at": "2022-05-13T09:46:50.032Z",
  "latest_build_finished_at": null,
  "first_deployed_to_production_at": null,
  "pipeline": { // Use `head_pipeline` instead.
    "id": 538317940,
    "iid": 1877,
    "project_id": 15513260,
    "sha": "1604b0c46c395822e4e9478777f8e54ac99fe5b9",
    "ref": "refs/merge-requests/133/merge",
    "status": "failed",
    "source": "merge_request_event",
    "created_at": "2022-05-13T09:46:39.560Z",
    "updated_at": "2022-05-13T09:47:20.706Z",
    "web_url": "https://gitlab.com/marcel.amirault/test-project/-/pipelines/538317940"
  },
  "head_pipeline": {
    "id": 538317940,
    "iid": 1877,
    "project_id": 15513260,
    "sha": "1604b0c46c395822e4e9478777f8e54ac99fe5b9",
    "ref": "refs/merge-requests/133/merge",
    "status": "failed",
    "source": "merge_request_event",
    "created_at": "2022-05-13T09:46:39.560Z",
    "updated_at": "2022-05-13T09:47:20.706Z",
    "web_url": "https://gitlab.com/marcel.amirault/test-project/-/pipelines/538317940",
    "before_sha": "1604b0c46c395822e4e9478777f8e54ac99fe5b9",
    "tag": false,
    "yaml_errors": null,
    "user": {
      "id": 4155490,
      "username": "marcel.amirault",
      "name": "Marcel Amirault",
      "state": "active",
      "avatar_url": "https://gitlab.com/uploads/-/system/user/avatar/4155490/avatar.png",
      "web_url": "https://gitlab.com/marcel.amirault"
    },
    "started_at": "2022-05-13T09:46:50.032Z",
    "finished_at": "2022-05-13T09:47:20.697Z",
    "committed_at": null,
    "duration": 30,
    "queued_duration": 10,
    "coverage": null,
    "detailed_status": {
      "icon": "status_failed",
      "text": "failed",
      "label": "failed",
      "group": "failed",
      "tooltip": "failed",
      "has_details": true,
      "details_path": "/marcel.amirault/test-project/-/pipelines/538317940",
      "illustration": null,
      "favicon": "/assets/ci_favicons/favicon_status_failed-41304d7f7e3828808b0c26771f0309e55296819a9beea3ea9fbf6689d9857c12.png"
    }
  },
  "diff_refs": {
    "base_sha": "1162f719d711319a2efb2a35566f3bfdadee8bab",
    "head_sha": "e82eb4a098e32c796079ca3915e07487fc4db24c",
    "start_sha": "1162f719d711319a2efb2a35566f3bfdadee8bab"
  },
  "merge_error": null,
  "first_contribution": false,
  "user": {
    "can_merge": true
  },
  "approvals_before_merge": { // Available for GitLab Premium and Ultimate tiers only
    "id": 1,
    "title": "test1",
    "approvals_before_merge": null
  },
}
```

### Single merge request response notes

The mergeability (`merge_status`)
of each merge request is checked asynchronously when a request is made to this endpoint. Poll this API endpoint
to get updated status. This affects the `has_conflicts` property as it is dependent on the `merge_status`. It returns
`false` unless `merge_status` is `cannot_be_merged`.

### Merge status

> - The `merge_status` field was [deprecated](https://gitlab.com/gitlab-org/gitlab/-/issues/3169#note_1162532204) in GitLab 15.6.
> - The `detailed_merge_status` field was [introduced](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/101724) in GitLab 15.6.

Use `detailed_merge_status` instead of `merge_status` to account for all potential statuses.

- The `detailed_merge_status` field can contain one of the following values related to the merge request:
  - `blocked_status`: Blocked by another merge request.
  - `checking`: Git is testing if a valid merge is possible.
  - `unchecked`: Git has not yet tested if a valid merge is possible.
  - `ci_must_pass`: A CI/CD pipeline must succeed before merge.
  - `ci_still_running`: A CI/CD pipeline is still running.
  - `discussions_not_resolved`: All discussions must be resolved before merge.
  - `draft_status`: Can't merge because the merge request is a draft.
  - `external_status_checks`: All status checks must pass before merge.
  - `mergeable`: The branch can merge cleanly into the target branch.
  - `not_approved`: Approval is required before merge.
  - `not_open`: The merge request must be open before merge.
  - `jira_association_missing`: The title or description must reference a Jira issue. To configure, see
    [Require associated Jira issue for merge requests to be merged](../integration/jira/issues.md#require-associated-jira-issue-for-merge-requests-to-be-merged).
  - `need_rebase`: The merge request must be rebased.
  - `conflict`: Conflicts exist between the source and target branches.
  - `requested_changes`: The merge request has reviewers who have requested changes.

### Preparation steps

The `prepared_at` field is populated one time, only after all of the preparation steps
are completed. It is not updated if more changes are added to the merge request:

- The diff is created.
- Pipelines are created.
- Mergeability is checked.
- Git LFS objects are linked.
- Notifications are sent.


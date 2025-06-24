## Update MR

Updates an existing merge request. You can change the target branch, title, or even close the MR.

```plaintext
PUT /projects/:id/merge_requests/:merge_request_iid
```

| Attribute                  | Type    | Required | Description |
| ---------                  | ----    | -------- | ----------- |
| `id`                       | integer or string | Yes  | The ID or [URL-encoded path of the project](rest/index.md#namespaced-path-encoding) owned by the authenticated user. |
| `merge_request_iid`        | integer | Yes      | The ID of a merge request. |
| `add_labels`               | string  | No       | Comma-separated label names to add to a merge request. If a label does not already exist, this creates a new project label and assigns it to the merge request. |
| `allow_collaboration`      | boolean | No       | Allow commits from members who can merge to the target branch. |
| `allow_maintainer_to_push` | boolean | No       | Alias of `allow_collaboration`. |
| `assignee_id`              | integer | No       | The ID of the user to assign the merge request to. Set to `0` or provide an empty value to unassign all assignees. |
| `assignee_ids`             | integer array | No | The ID of the users to assign the merge request to. Set to `0` or provide an empty value to unassign all assignees. |
| `description`              | string  | No       | Description of the merge request. Limited to 1,048,576 characters. |
| `discussion_locked`        | boolean | No       | Flag indicating if the merge request's discussion is locked. If the discussion is locked only project members can add, edit or resolve comments. |
| `labels`                   | string  | No       | Comma-separated label names for a merge request. Set to an empty string to unassign all labels. If a label does not already exist, this creates a new project label and assigns it to the merge request. |
| `milestone_id`             | integer | No       | The global ID of a milestone to assign the merge request to. Set to `0` or provide an empty value to unassign a milestone.|
| `remove_labels`            | string  | No       | Comma-separated label names to remove from a merge request. |
| `remove_source_branch`     | boolean | No       | Flag indicating if a merge request should remove the source branch when merging. |
| `reviewer_ids`             | integer array | No | The ID of the users set as a reviewer to the merge request. Set the value to `0` or provide an empty value to unset all reviewers. |
| `squash`                   | boolean | No       | Indicates if the merge request is set to be squashed when merged. [Project settings](../user/project/merge_requests/squash_and_merge.md#configure-squash-options-for-a-project) may override this value. |
| `state_event`              | string  | No       | New state (close/reopen). |
| `target_branch`            | string  | No       | The target branch. |
| `title`                    | string  | No       | Title of MR. |

Must include at least one non-required attribute from above.

Example response:

```json
{
  "id": 1,
  "iid": 1,
  "project_id": 3,
  "title": "test1",
  "description": "fixed login page css paddings",
  "state": "merged",
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
    "name": "Miss Monserrate Beier",
    "username": "axel.block",
    "id": 12,
    "state": "active",
    "avatar_url": "http://www.gravatar.com/avatar/46f6f7dc858ada7be1853f7fb96e81da?s=80&d=identicon",
    "web_url": "https://gitlab.example.com/axel.block"
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
    "due_date": "2018-09-22",
    "start_date": "2018-08-08",
    "web_url": "https://gitlab.example.com/my-group/my-project/milestones/1"
  },
  "merge_when_pipeline_succeeds": true,
  "merge_status": "can_be_merged",
  "detailed_merge_status": "not_open",
  "merge_error": null,
  "sha": "8888888888888888888888888888888888888888",
  "merge_commit_sha": null,
  "squash_commit_sha": null,
  "user_notes_count": 1,
  "discussion_locked": null,
  "should_remove_source_branch": true,
  "force_remove_source_branch": false,
  "allow_collaboration": false,
  "allow_maintainer_to_push": false,
  "web_url": "http://gitlab.example.com/my-group/my-project/merge_requests/1",
  "references": {
    "short": "!1",
    "relative": "!1",
    "full": "my-group/my-project!1"
  },
  "time_stats": {
    "time_estimate": 0,
    "total_time_spent": 0,
    "human_time_estimate": null,
    "human_total_time_spent": null
  },
  "squash": false,
  "subscribed": false,
  "changes_count": "1",
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
  "latest_build_started_at": "2018-09-07T07:27:38.472Z",
  "latest_build_finished_at": "2018-09-07T08:07:06.012Z",
  "first_deployed_to_production_at": null,
  "pipeline": {
    "id": 29626725,
    "sha": "2be7ddb704c7b6b83732fdd5b9f09d5a397b5f8f",
    "ref": "patch-28",
    "status": "success",
    "web_url": "https://gitlab.example.com/my-group/my-project/pipelines/29626725"
  },
  "diff_refs": {
    "base_sha": "c380d3acebd181f13629a25d2e2acca46ffe1e00",
    "head_sha": "2be7ddb704c7b6b83732fdd5b9f09d5a397b5f8f",
    "start_sha": "c380d3acebd181f13629a25d2e2acca46ffe1e00"
  },
  "diverged_commits_count": 2,
  "task_completion_status":{
    "count":0,
    "completed_count":0
  }
}
```

For important notes on response data, see [Single merge request response notes](#single-merge-request-response-notes).


## List merge requests associated with a commit

Returns information about the merge request that originally introduced a specific commit.

```plaintext
GET /projects/:id/repository/commits/:sha/merge_requests
```

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `id`      | integer/string | yes | The ID or [URL-encoded path of the project](rest/index.md#namespaced-path-encoding) owned by the authenticated user |
| `sha`     | string  | yes   | The commit SHA |

```shell
curl --header "PRIVATE-TOKEN: <your_access_token>" \
  --url "https://gitlab.example.com/api/v4/projects/5/repository/commits/af5b13261899fb2c0db30abdd0af8b07cb44fdc5/merge_requests"
```

Example response:

```json
[
   {
      "id":45,
      "iid":1,
      "project_id":35,
      "title":"Add new file",
      "description":"",
      "state":"opened",
      "created_at":"2018-03-26T17:26:30.916Z",
      "updated_at":"2018-03-26T17:26:30.916Z",
      "target_branch":"main",
      "source_branch":"test-branch",
      "upvotes":0,
      "downvotes":0,
      "author" : {
        "web_url" : "https://gitlab.example.com/janedoe",
        "name" : "Jane Doe",
        "avatar_url" : "https://gitlab.example.com/uploads/user/avatar/28/jane-doe-400-400.png",
        "username" : "janedoe",
        "state" : "active",
        "id" : 28
      },
      "assignee":null,
      "source_project_id":35,
      "target_project_id":35,
      "labels":[ ],
      "draft":false,
      "work_in_progress":false,
      "milestone":null,
      "merge_when_pipeline_succeeds":false,
      "merge_status":"can_be_merged",
      "sha":"af5b13261899fb2c0db30abdd0af8b07cb44fdc5",
      "merge_commit_sha":null,
      "squash_commit_sha":null,
      "user_notes_count":0,
      "discussion_locked":null,
      "should_remove_source_branch":null,
      "force_remove_source_branch":false,
      "web_url":"https://gitlab.example.com/root/test-project/merge_requests/1",
      "time_stats":{
         "time_estimate":0,
         "total_time_spent":0,
         "human_time_estimate":null,
         "human_total_time_spent":null
      }
   }
]
```


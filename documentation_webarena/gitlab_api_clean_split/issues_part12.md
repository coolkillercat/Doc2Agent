## Move an issue

Moves an issue to a different project. If the target project
is the source project or the user has insufficient permissions,
an error message with status code `400` is returned.

If a given label or milestone with the same name also exists in the target
project, it's then assigned to the issue being moved.

```plaintext
POST /projects/:id/issues/:issue_iid/move
```

Supported attributes:

| Attribute       | Type    | Required | Description                          |
|-----------------|---------|----------|--------------------------------------|
| `id`            | integer/string | Yes      | The global ID or [URL-encoded path of the project](rest/index.md#namespaced-path-encoding) owned by the authenticated user.  |
| `issue_iid`     | integer | Yes      | The internal ID of a project's issue. |
| `to_project_id` | integer | Yes      | The ID of the new project.            |

Example request:

```shell
curl --header "PRIVATE-TOKEN: <your_access_token>" \
  --form to_project_id=5 \
  --url "https://gitlab.example.com/api/v4/projects/4/issues/85/move"
```

Example response:

```json
{
  "id": 92,
  "iid": 11,
  "project_id": 5,
  "title": "Sit voluptas tempora quisquam aut doloribus et.",
  "description": "Repellat voluptas quibusdam voluptatem exercitationem.",
  "state": "opened",
  "created_at": "2016-04-05T21:41:45.652Z",
  "updated_at": "2016-04-07T12:20:17.596Z",
  "closed_at": null,
  "closed_by": null,
  "labels": [],
  "upvotes": 4,
  "downvotes": 0,
  "merge_requests_count": 0,
  "milestone": null,
  "assignees": [{
    "name": "Miss Monserrate Beier",
    "username": "axel.block",
    "id": 12,
    "state": "active",
    "avatar_url": "http://www.gravatar.com/avatar/46f6f7dc858ada7be1853f7fb96e81da?s=80&d=identicon",
    "web_url": "https://gitlab.example.com/axel.block"
  }],
  "assignee": {
    "name": "Miss Monserrate Beier",
    "username": "axel.block",
    "id": 12,
    "state": "active",
    "avatar_url": "http://www.gravatar.com/avatar/46f6f7dc858ada7be1853f7fb96e81da?s=80&d=identicon",
    "web_url": "https://gitlab.example.com/axel.block"
  },
  "type" : "ISSUE",
  "author": {
    "name": "Kris Steuber",
    "username": "solon.cremin",
    "id": 10,
    "state": "active",
    "avatar_url": "http://www.gravatar.com/avatar/7a190fecbaa68212a4b68aeb6e3acd10?s=80&d=identicon",
    "web_url": "https://gitlab.example.com/solon.cremin"
  },
  "due_date": null,
  "imported": false,
  "imported_from": "none",
  "web_url": "http://gitlab.example.com/my-group/my-project/issues/11",
  "references": {
    "short": "#11",
    "relative": "#11",
    "full": "my-group/my-project#11"
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
  "project_id": 5,
  "description": "Repellat voluptas quibusdam voluptatem exercitationem.",
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


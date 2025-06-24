## Commit status

This is the commit status API for use with GitLab.

### List the statuses of a commit

List the statuses of a commit in a project.
The pagination parameters `page` and `per_page` can be used to restrict the list of references.

```plaintext
GET /projects/:id/repository/commits/:sha/statuses
```

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `id`      | integer/string | yes | The ID or [URL-encoded path of the project](rest/index.md#namespaced-path-encoding) owned by the authenticated user |
| `sha`     | string  | yes | The commit SHA |
| `ref`     | string  | no  | The name of a repository branch or tag or, if not given, the default branch |
| `stage`   | string  | no  | Filter by [build stage](../ci/yaml/index.md#stages), for example, `test` |
| `name`    | string  | no  | Filter by [job name](../ci/yaml/index.md#job-keywords), for example, `bundler:audit` |
| `all`     | boolean | no  | Return all statuses, not only the latest ones |

```shell
curl --header "PRIVATE-TOKEN: <your_access_token>" \
  --url "https://gitlab.example.com/api/v4/projects/17/repository/commits/18f3e63d05582537db6d183d9d557be09e1f90c8/statuses"
```

Example response:

```json
[
   ...

   {
      "status" : "pending",
      "created_at" : "2016-01-19T08:40:25.934Z",
      "started_at" : null,
      "name" : "bundler:audit",
      "allow_failure" : true,
      "author" : {
         "username" : "janedoe",
         "state" : "active",
         "web_url" : "https://gitlab.example.com/janedoe",
         "avatar_url" : "https://gitlab.example.com/uploads/user/avatar/28/jane-doe-400-400.png",
         "id" : 28,
         "name" : "Jane Doe"
      },
      "description" : null,
      "sha" : "18f3e63d05582537db6d183d9d557be09e1f90c8",
      "target_url" : "https://gitlab.example.com/janedoe/gitlab-foss/builds/91",
      "finished_at" : null,
      "id" : 91,
      "ref" : "main"
   },
   {
      "started_at" : null,
      "name" : "test",
      "allow_failure" : false,
      "status" : "pending",
      "created_at" : "2016-01-19T08:40:25.832Z",
      "target_url" : "https://gitlab.example.com/janedoe/gitlab-foss/builds/90",
      "id" : 90,
      "finished_at" : null,
      "ref" : "main",
      "sha" : "18f3e63d05582537db6d183d9d557be09e1f90c8",
      "author" : {
         "id" : 28,
         "name" : "Jane Doe",
         "username" : "janedoe",
         "web_url" : "https://gitlab.example.com/janedoe",
         "state" : "active",
         "avatar_url" : "https://gitlab.example.com/uploads/user/avatar/28/jane-doe-400-400.png"
      },
      "description" : null
   },

   ...
]
```

### Set the pipeline status of a commit

Add or update the pipeline status of a commit. If the commit is associated with a merge request,
the API call must target the commit in the merge request's source branch.

```plaintext
POST /projects/:id/statuses/:sha
```

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `id`      | integer/string | yes | The ID or [URL-encoded path of the project](rest/index.md#namespaced-path-encoding) owned by the authenticated user |
| `sha`     | string  | yes   | The commit SHA |
| `state`   | string  | yes   | The state of the status. Can be one of the following: `pending`, `running`, `success`, `failed`, `canceled` |
| `ref`     | string  | no    | The `ref` (branch or tag) to which the status refers |
| `name` or `context` | string  | no | The label to differentiate this status from the status of other systems. Default value is `default` |
| `target_url` |  string  | no  | The target URL to associate with this status |
| `description` | string  | no  | The short description of the status |
| `coverage` | float  | no    | The total code coverage |
| `pipeline_id` |  integer  | no  | The ID of the pipeline to set status. Use in case of several pipeline on same SHA. |

```shell
curl --request POST \
  --header "PRIVATE-TOKEN: <your_access_token>" \
  --url "https://gitlab.example.com/api/v4/projects/17/statuses/18f3e63d05582537db6d183d9d557be09e1f90c8?state=success"
```

Example response:

```json
{
   "author" : {
      "web_url" : "https://gitlab.example.com/janedoe",
      "name" : "Jane Doe",
      "avatar_url" : "https://gitlab.example.com/uploads/user/avatar/28/jane-doe-400-400.png",
      "username" : "janedoe",
      "state" : "active",
      "id" : 28
   },
   "name" : "default",
   "sha" : "18f3e63d05582537db6d183d9d557be09e1f90c8",
   "status" : "success",
   "coverage": 100.0,
   "description" : null,
   "id" : 93,
   "target_url" : null,
   "ref" : null,
   "started_at" : null,
   "created_at" : "2016-01-19T09:05:50.355Z",
   "allow_failure" : false,
   "finished_at" : "2016-01-19T09:05:50.365Z"
}
```


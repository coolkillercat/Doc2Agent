## Get a single merge request diff version

Get a single merge request diff version.

```plaintext
GET /projects/:id/merge_requests/:merge_request_iid/versions/:version_id
```

Supported attributes:

| Attribute           | Type    | Required | Description                               |
|---------------------|---------|----------|-------------------------------------------|
| `id`                | String  | Yes      | ID of the project.                    |
| `merge_request_iid` | integer | Yes      | Internal ID of the merge request.     |
| `version_id`        | integer | Yes      | ID of the merge request diff version. |
| `unidiff`           | boolean | No       | Present diffs in the [unified diff](https://www.gnu.org/software/diffutils/manual/html_node/Detailed-Unified.html) format. Default is false. [Introduced](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/130610) in GitLab 16.5.      |

If successful, returns [`200 OK`](rest/index.md#status-codes) and the following
response attributes:

| Attribute                     | Type         | Description |
|-------------------------------|--------------|-------------|
| `id`                          | integer      | ID of the merge request diff version. |
| `base_commit_sha`             | string       | Merge-base commit SHA between the source branch and the target branches. |
| `commits`                     | object array | Commits in the merge request diff. |
| `commits[].id`                | string       | ID of the commit. |
| `commits[].short_id`          | string       | Short ID of the commit. |
| `commits[].created_at`        | datetime     | Identical to the `committed_date` field. |
| `commits[].parent_ids`        | array        | IDs of the parent commits. |
| `commits[].title`             | string       | Commit title. |
| `commits[].message`           | string       | Commit message. |
| `commits[].author_name`       | string       | Commit author's name. |
| `commits[].author_email`      | string       | Commit author's email address. |
| `commits[].authored_date`     | datetime     | Commit authored date. |
| `commits[].committer_name`    | string       | Committer's name. |
| `commits[].committer_email`   | string       | Committer's email address. |
| `commits[].committed_date`    | datetime     | Commit date. |
| `commits[].trailers`          | object       | Git trailers that were parsed for the commit. Duplicate keys include the last value only. |
| `commits[].extended_trailers` | object       | Git trailers that were parsed for the commit. |
| `commits[].web_url`           | string       | Web URL of the merge request. |
| `created_at`                  | datetime     | Timestamp of when the merge request was created. |
| `diffs`                       | object array | Diffs in the merge request diff version. |
| `diffs[].diff`                | string       | Content of the diff. |
| `diffs[].new_path`            | string       | New path of the file. |
| `diffs[].old_path`            | string       | Old path of the file. |
| `diffs[].a_mode`              | string       | Old file mode of the file. |
| `diffs[].b_mode`              | string       | New file mode of the file. |
| `diffs[].new_file`            | boolean      | Indicates if the file has just been added. |
| `diffs[].renamed_file`        | boolean      | Indicates if the file has been renamed. |
| `diffs[].deleted_file`        | boolean      | Indicates if the file has been removed. |
| `diffs[].generated_file`      | boolean      | Indicates if the file is [marked as generated](../user/project/merge_requests/changes.md#collapse-generated-files). [Introduced](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/141576) in GitLab 16.9. |
| `head_commit_sha`             | string       | HEAD commit of the source branch. |
| `merge_request_id`            | integer      | ID of the merge request. |
| `patch_id_sha`                | string       | [Patch ID](https://git-scm.com/docs/git-patch-id) for the merge request diff. |
| `real_size`                   | string       | Number of changes in the merge request diff. |
| `start_commit_sha`            | string       | HEAD commit SHA of the target branch when this version of the diff was created. |
| `state`                       | string       | State of the merge request diff. Can be `collected`, `overflow`, `without_files`. Deprecated values: `timeout`, `overflow_commits_safe_size`, `overflow_diff_files_limit`, `overflow_diff_lines_limit`. |

Example request:

```shell
curl --header "PRIVATE-TOKEN: <your_access_token>" \
  --url "https://gitlab.example.com/api/v4/projects/1/merge_requests/1/versions/1"
```

Example response:

```json
{
  "id": 110,
  "head_commit_sha": "33e2ee8579fda5bc36accc9c6fbd0b4fefda9e30",
  "base_commit_sha": "eeb57dffe83deb686a60a71c16c32f71046868fd",
  "start_commit_sha": "eeb57dffe83deb686a60a71c16c32f71046868fd",
  "created_at": "2016-07-26T14:44:48.926Z",
  "merge_request_id": 105,
  "state": "collected",
  "real_size": "1",
  "patch_id_sha": "d504412d5b6e6739647e752aff8e468dde093f2f",
  "commits": [{
    "id": "33e2ee8579fda5bc36accc9c6fbd0b4fefda9e30",
    "short_id": "33e2ee85",
    "parent_ids": [],
    "title": "Change year to 2018",
    "author_name": "Administrator",
    "author_email": "admin@example.com",
    "authored_date": "2016-07-26T17:44:29.000+03:00",
    "committer_name": "Administrator",
    "committer_email": "admin@example.com",
    "committed_date": "2016-07-26T17:44:29.000+03:00",
    "created_at": "2016-07-26T17:44:29.000+03:00",
    "message": "Change year to 2018",
    "trailers": {},
    "extended_trailers": {},
    "web_url": "https://gitlab.example.com/project/-/commit/33e2ee8579fda5bc36accc9c6fbd0b4fefda9e30"
  }, {
    "id": "aa24655de48b36335556ac8a3cd8bb521f977cbd",
    "short_id": "aa24655d",
    "parent_ids": [],
    "title": "Update LICENSE",
    "author_name": "Administrator",
    "author_email": "admin@example.com",
    "authored_date": "2016-07-25T17:21:53.000+03:00",
    "committer_name": "Administrator",
    "committer_email": "admin@example.com",
    "committed_date": "2016-07-25T17:21:53.000+03:00",
    "created_at": "2016-07-25T17:21:53.000+03:00",
    "message": "Update LICENSE",
    "trailers": {},
    "extended_trailers": {},
    "web_url": "https://gitlab.example.com/project/-/commit/aa24655de48b36335556ac8a3cd8bb521f977cbd"
  }, {
    "id": "3eed087b29835c48015768f839d76e5ea8f07a24",
    "short_id": "3eed087b",
    "parent_ids": [],
    "title": "Add license",
    "author_name": "Administrator",
    "author_email": "admin@example.com",
    "authored_date": "2016-07-25T17:21:20.000+03:00",
    "committer_name": "Administrator",
    "committer_email": "admin@example.com",
    "committed_date": "2016-07-25T17:21:20.000+03:00",
    "created_at": "2016-07-25T17:21:20.000+03:00",
    "message": "Add license",
    "trailers": {},
    "extended_trailers": {},
    "web_url": "https://gitlab.example.com/project/-/commit/3eed087b29835c48015768f839d76e5ea8f07a24"
  }],
  "diffs": [{
    "old_path": "LICENSE",
    "new_path": "LICENSE",
    "a_mode": "0",
    "b_mode": "100644",
    "diff": "@@ -0,0 +1,21 @@\n+The MIT License (MIT)\n+\n+Copyright (c) 2018 Administrator\n+\n+Permission is hereby granted, free of charge, to any person obtaining a copy\n+of this software and associated documentation files (the \"Software\"), to deal\n+in the Software without restriction, including without limitation the rights\n+to use, copy, modify, merge, publish, distribute, sublicense, and/or sell\n+copies of the Software, and to permit persons to whom the Software is\n+furnished to do so, subject to the following conditions:\n+\n+The above copyright notice and this permission notice shall be included in all\n+copies or substantial portions of the Software.\n+\n+THE SOFTWARE IS PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\n+IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\n+FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE\n+AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\n+LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\n+OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE\n+SOFTWARE.\n",
    "new_file": true,
    "renamed_file": false,
    "deleted_file": false,
    "generated_file": false
  }]
}
```


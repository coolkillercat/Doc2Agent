## List merge request diffs

> - `generated_file` was [introduced](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/141576) in GitLab 16.9 [with a flag](../administration/feature_flags.md) named `collapse_generated_diff_files`. Disabled by default.
> - [Enabled on GitLab.com and self-managed](https://gitlab.com/gitlab-org/gitlab/-/issues/432670) in GitLab 16.10.
> - `generated_file` [generally available](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/148478) in GitLab 16.11. Feature flag `collapse_generated_diff_files` removed.

List diffs of the files changed in a merge request.

```plaintext
GET /projects/:id/merge_requests/:merge_request_iid/diffs
```

Supported attributes:

| Attribute           | Type              | Required | Description |
|---------------------|-------------------|----------|-------------|
| `id`                | integer or string | Yes      | The ID or [URL-encoded path of the project](rest/index.md#namespaced-path-encoding) owned by the authenticated user. |
| `merge_request_iid` | integer           | Yes      | The internal ID of the merge request. |
| `page`              | integer           | No       | The page of results to return. Defaults to 1. |
| `per_page`          | integer           | No       | The number of results per page. Defaults to 20. |
| `unidiff`           | boolean           | No       | Present diffs in the [unified diff](https://www.gnu.org/software/diffutils/manual/html_node/Detailed-Unified.html) format. Default is false. [Introduced](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/130610) in GitLab 16.5. |

If successful, returns [`200 OK`](rest/index.md#status-codes) and the
following response attributes:

| Attribute      | Type    | Description |
|----------------|---------|-------------|
| `old_path`     | string  | Old path of the file. |
| `new_path`     | string  | New path of the file. |
| `a_mode`       | string  | Old file mode of the file. |
| `b_mode`       | string  | New file mode of the file. |
| `diff`         | string  | Diff representation of the changes made to the file. |
| `new_file`     | boolean | Indicates if the file has just been added. |
| `renamed_file` | boolean | Indicates if the file has been renamed. |
| `deleted_file` | boolean | Indicates if the file has been removed. |
| `generated_file` | boolean | Indicates if the file is [marked as generated](../user/project/merge_requests/changes.md#collapse-generated-files). [Introduced](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/141576) in GitLab 16.9. |

Example request:

```shell
curl --header "PRIVATE-TOKEN: <your_access_token>" \
  --url "https://gitlab.example.com/api/v4/projects/1/merge_requests/1/diffs?page=1&per_page=2"
```

Example response:

```json
[
  {
    "old_path": "README",
    "new_path": "README",
    "a_mode": "100644",
    "b_mode": "100644",
    "diff": "@@ -1 +1 @@\ -Title\ +README",
    "new_file": false,
    "renamed_file": false,
    "deleted_file": false,
    "generated_file": false
  },
  {
    "old_path": "VERSION",
    "new_path": "VERSION",
    "a_mode": "100644",
    "b_mode": "100644",
    "diff": "@@\ -1.9.7\ +1.9.8",
    "new_file": false,
    "renamed_file": false,
    "deleted_file": false,
    "generated_file": false
  }
]
```

NOTE:
This endpoint is subject to [Merge requests diff limits](../administration/instance_limits.md#diff-limits).
Merge requests that exceed the diff limits return limited results.


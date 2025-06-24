## Compare branches, tags or commits

This endpoint can be accessed without authentication if the repository is
publicly accessible. Diffs can have an empty diff string if
[diff limits](../development/merge_request_concepts/diffs/index.md#diff-limits) are reached.

```plaintext
GET /projects/:id/repository/compare
```

Supported attributes:

| Attribute         | Type           | Required | Description |
| :---------        | :------------- | :------- | :---------- |
| `id`              | integer or string | yes      | The ID or [URL-encoded path of the project](rest/index.md#namespaced-path-encoding) owned by the authenticated user. |
| `from`            | string         | yes      | The commit SHA or branch name. |
| `to`              | string         | yes      | The commit SHA or branch name. |
| `from_project_id` | integer        | no       | The ID to compare from. |
| `straight`        | boolean        | no       | Comparison method: `true` for direct comparison between `from` and `to` (`from`..`to`), `false` to compare using merge base (`from`...`to`)'. Default is `false`. |
| `unidiff`           | boolean | No       | Present diffs in the [unified diff](https://www.gnu.org/software/diffutils/manual/html_node/Detailed-Unified.html) format. Default is false. [Introduced](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/130610) in GitLab 16.5.     |

```plaintext
GET /projects/:id/repository/compare?from=main&to=feature
```

Example response:

```json
{
  "commit": {
    "id": "12d65c8dd2b2676fa3ac47d955accc085a37a9c1",
    "short_id": "12d65c8dd2b",
    "title": "JS fix",
    "author_name": "Example User",
    "author_email": "user@example.com",
    "created_at": "2014-02-27T10:27:00+02:00"
  },
  "commits": [{
    "id": "12d65c8dd2b2676fa3ac47d955accc085a37a9c1",
    "short_id": "12d65c8dd2b",
    "title": "JS fix",
    "author_name": "Example User",
    "author_email": "user@example.com",
    "created_at": "2014-02-27T10:27:00+02:00"
  }],
  "diffs": [{
    "old_path": "files/js/application.js",
    "new_path": "files/js/application.js",
    "a_mode": null,
    "b_mode": "100644",
    "diff": "@@ -24,8 +24,10 @@\n //= require g.raphael-min\n //= require g.bar-min\n //= require branch-graph\n-//= require highlightjs.min\n-//= require ace/ace\n //= require_tree .\n //= require d3\n //= require underscore\n+\n+function fix() { \n+  alert(\"Fixed\")\n+}",
    "new_file": false,
    "renamed_file": false,
    "deleted_file": false
  }],
  "compare_timeout": false,
  "compare_same_ref": false,
  "web_url": "https://gitlab.example.com/janedoe/gitlab-foss/-/compare/ae73cb07c9eeaf35924a10f713b364d32b2dd34f...0b4bc9a49b562e85de7cc9e834518ea6828729b9"
}
```


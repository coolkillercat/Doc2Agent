## Push rules

DETAILS:
**Tier:** Premium, Ultimate
**Offering:** GitLab.com, Self-managed, GitLab Dedicated

### Get project push rules

Get the [push rules](../user/project/repository/push_rules.md) of a
project.

```plaintext
GET /projects/:id/push_rule
```

| Attribute | Type              | Required | Description |
|-----------|-------------------|----------|-------------|
| `id`      | integer or string | Yes      | The ID or [URL-encoded path of the project](rest/index.md#namespaced-path-encoding) |

```json
{
  "id": 1,
  "project_id": 3,
  "commit_message_regex": "Fixes \\d+\\..*",
  "commit_message_negative_regex": "ssh\\:\\/\\/",
  "branch_name_regex": "",
  "deny_delete_tag": false,
  "created_at": "2012-10-12T17:04:47Z",
  "member_check": false,
  "prevent_secrets": false,
  "author_email_regex": "",
  "file_name_regex": "",
  "max_file_size": 5,
  "commit_committer_check": false,
  "commit_committer_name_check": false,
  "reject_unsigned_commits": false
}
```

### Add project push rule

Adds a push rule to a specified project.

```plaintext
POST /projects/:id/push_rule
```

<!-- markdownlint-disable MD056 -->

| Attribute                       | Type              | Required | Description |
|---------------------------------|-------------------|----------|-------------|
| `id`                            | integer or string | Yes      | The ID or [URL-encoded path of the project](rest/index.md#namespaced-path-encoding). |
| `author_email_regex`            | string            | No       | All commit author emails must match this, for example `@my-company.com$`. |
| `branch_name_regex`             | string            | No       | All branch names must match this, for example `(feature|hotfix)\/*`. |
| `commit_committer_check`        | boolean           | No       | Users can only push commits to this repository if the committer email is one of their own verified emails. |
| `commit_committer_name_check`   | boolean           | No       | Users can only push commits to this repository if the commit author name is consistent with their GitLab account name. |
| `commit_message_negative_regex` | string            | No       | No commit message is allowed to match this, for example `ssh\:\/\/`. |
| `commit_message_regex`          | string            | No       | All commit messages must match this, for example `Fixed \d+\..*`. |
| `deny_delete_tag`               | boolean           | No       | Deny deleting a tag. |
| `file_name_regex`               | string            | No       | All committed filenames must **not** match this, for example `(jar|exe)$`. |
| `max_file_size`                 | integer           | No       | Maximum file size (MB). |
| `member_check`                  | boolean           | No       | Restrict commits by author (email) to existing GitLab users. |
| `prevent_secrets`               | boolean           | No       | GitLab rejects any files that are likely to contain secrets. |
| `reject_unsigned_commits`       | boolean           | No       | Reject commit when it's not signed. |

<!-- markdownlint-enable MD056 -->

### Edit project push rule

Edits a push rule for a specified project.

```plaintext
PUT /projects/:id/push_rule
```

<!-- markdownlint-disable MD056 -->

| Attribute                       | Type              | Required | Description |
|---------------------------------|-------------------|----------|-------------|
| `id`                            | integer or string | Yes      | The ID or [URL-encoded path of the project](rest/index.md#namespaced-path-encoding). |
| `author_email_regex`            | string            | No       | All commit author emails must match this, for example `@my-company.com$`. |
| `branch_name_regex`             | string            | No       | All branch names must match this, for example `(feature|hotfix)\/*`. |
| `commit_committer_check`        | boolean           | No       | Users can only push commits to this repository if the committer email is one of their own verified emails. |
| `commit_committer_name_check`   | boolean           | No       | Users can only push commits to this repository if the commit author name is consistent with their GitLab account name. |
| `commit_message_negative_regex` | string            | No       | No commit message is allowed to match this, for example `ssh\:\/\/`. |
| `commit_message_regex`          | string            | No       | All commit messages must match this, for example `Fixed \d+\..*`. |
| `deny_delete_tag`               | boolean           | No       | Deny deleting a tag. |
| `file_name_regex`               | string            | No       | All committed filenames must **not** match this, for example `(jar|exe)$`. |
| `max_file_size`                 | integer           | No       | Maximum file size (MB). |
| `member_check`                  | boolean           | No       | Restrict commits by author (email) to existing GitLab users. |
| `prevent_secrets`               | boolean           | No       | GitLab rejects any files that are likely to contain secrets. |
| `reject_unsigned_commits`       | boolean           | No       | Reject commits when they are not signed. |

<!-- markdownlint-enable MD056 -->

### Delete project push rule

> - Moved to GitLab Premium in 13.9.

Removes a push rule from a project.

```plaintext
DELETE /projects/:id/push_rule
```

| Attribute | Type              | Required | Description |
|-----------|-------------------|----------|-------------|
| `id`      | integer or string | Yes      | The ID or [URL-encoded path of the project](rest/index.md#namespaced-path-encoding). |


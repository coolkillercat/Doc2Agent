## Push Rules

DETAILS:
**Tier:** Premium, Ultimate
**Offering:** GitLab.com, Self-managed, GitLab Dedicated

### Get group push rules

Get the [push rules](../user/group/access_and_permissions.md#group-push-rules) of a group.

Only available to group owners and administrators.

```plaintext
GET /groups/:id/push_rule
```

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `id` | integer/string | yes | The ID of the group or [URL-encoded path of the group](rest/index.md#namespaced-path-encoding) |

```json
{
  "id": 2,
  "created_at": "2020-08-17T19:09:19.580Z",
  "commit_committer_check": true,
  "commit_committer_name_check": true,
  "reject_unsigned_commits": false,
  "commit_message_regex": "[a-zA-Z]",
  "commit_message_negative_regex": "[x+]",
  "branch_name_regex": "[a-z]",
  "deny_delete_tag": true,
  "member_check": true,
  "prevent_secrets": true,
  "author_email_regex": "^[A-Za-z0-9.]+@gitlab.com$",
  "file_name_regex": "(exe)$",
  "max_file_size": 100
}
```

### Add group push rule

Adds [push rules](../user/group/access_and_permissions.md#group-push-rules) to the specified group.

Only available to group owners and administrators.

```plaintext
POST /groups/:id/push_rule
```

<!-- markdownlint-disable MD056 -->

| Attribute                                     | Type           | Required | Description |
| --------------------------------------------- | -------------- | -------- | ----------- |
| `id`                                          | integer/string | yes      | The ID or [URL-encoded path of the group](rest/index.md#namespaced-path-encoding) |
| `deny_delete_tag`                             | boolean        | no       | Deny deleting a tag |
| `member_check`                                | boolean        | no       | Allows only GitLab users to author commits |
| `prevent_secrets`                             | boolean        | no       | [Files that are likely to contain secrets](https://gitlab.com/gitlab-org/gitlab/-/blob/master/ee/lib/gitlab/checks/files_denylist.yml) are rejected |
| `commit_committer_name_check`                 | boolean        | no       | Users can only push commits to this repository if the commit author name is consistent with their GitLab account name |
| `commit_message_regex`                        | string         | no       | All commit messages must match the regular expression provided in this attribute, for example, `Fixed \d+\..*` |
| `commit_message_negative_regex`               | string         | no       | Commit messages matching the regular expression provided in this attribute aren't allowed, for example, `ssh\:\/\/` |
| `branch_name_regex`                           | string         | no       | All branch names must match the regular expression provided in this attribute, for example, `(feature|hotfix)\/*` |
| `author_email_regex`                          | string         | no       | All commit author emails must match the regular expression provided in this attribute, for example, `@my-company.com$` |
| `file_name_regex`                             | string         | no       | Filenames matching the regular expression provided in this attribute are **not** allowed, for example, `(jar|exe)$` |
| `max_file_size`                               | integer        | no       | Maximum file size (MB) allowed |
| `commit_committer_check`                      | boolean        | no       | Only commits pushed using verified emails are allowed |
| `reject_unsigned_commits`                     | boolean        | no       | Only signed commits are allowed |

<!-- markdownlint-enable MD056 -->

```shell
curl --request POST --header "PRIVATE-TOKEN: <your_access_token>" "https://gitlab.example.com/api/v4/groups/19/push_rule"
```

Response:

```json
{
    "id": 19,
    "created_at": "2020-08-31T15:53:00.073Z",
    "commit_committer_name_check": false,
    "commit_message_regex": "[a-zA-Z]",
    "commit_message_negative_regex": "[x+]",
    "branch_name_regex": null,
    "deny_delete_tag": false,
    "member_check": false,
    "prevent_secrets": false,
    "author_email_regex": "^[A-Za-z0-9.]+@gitlab.com$",
    "file_name_regex": null,
    "max_file_size": 100
}
```

### Edit group push rule

Edit push rules for a specified group.

Only available to group owners and administrators.

```plaintext
PUT /groups/:id/push_rule
```

<!-- markdownlint-disable MD056 -->

| Attribute                                     | Type           | Required | Description |
| --------------------------------------------- | -------------- | -------- | ----------- |
| `id`                                          | integer/string | yes      | The ID or [URL-encoded path of the group](rest/index.md#namespaced-path-encoding) |
| `deny_delete_tag`                             | boolean        | no       | Deny deleting a tag |
| `member_check`                                | boolean        | no       | Restricts commits to be authored by existing GitLab users only |
| `prevent_secrets`                             | boolean        | no       | [Files that are likely to contain secrets](https://gitlab.com/gitlab-org/gitlab/-/blob/master/ee/lib/gitlab/checks/files_denylist.yml) are rejected |
| `commit_committer_name_check`                 | boolean        | no       | Users can only push commits to this repository if the commit author name is consistent with their GitLab account name |
| `commit_message_regex`                        | string         | no       | All commit messages must match the regular expression provided in this attribute, for example, `Fixed \d+\..*` |
| `commit_message_negative_regex`               | string         | no       | Commit messages matching the regular expression provided in this attribute aren't allowed, for example, `ssh\:\/\/` |
| `branch_name_regex`                           | string         | no       | All branch names must match the regular expression provided in this attribute, for example, `(feature|hotfix)\/*` |
| `author_email_regex`                          | string         | no       | All commit author emails must match the regular expression provided in this attribute, for example, `@my-company.com$` |
| `file_name_regex`                             | string         | no       | Filenames matching the regular expression provided in this attribute are **not** allowed, for example, `(jar|exe)$` |
| `max_file_size`                               | integer        | no       | Maximum file size (MB) allowed |
| `commit_committer_check`                      | boolean        | no       | Only commits pushed using verified emails are allowed |
| `reject_unsigned_commits`                     | boolean        | no       | Only signed commits are allowed |

<!-- markdownlint-enable MD056 -->

```shell
curl --request PUT --header "PRIVATE-TOKEN: <your_access_token>" "https://gitlab.example.com/api/v4/groups/19/push_rule"
```

Response:

```json
{
    "id": 19,
    "created_at": "2020-08-31T15:53:00.073Z",
    "commit_committer_name_check": false,
    "commit_message_regex": "[a-zA-Z]",
    "commit_message_negative_regex": "[x+]",
    "branch_name_regex": null,
    "deny_delete_tag": false,
    "member_check": false,
    "prevent_secrets": false,
    "author_email_regex": "^[A-Za-z0-9.]+@staging.gitlab.com$",
    "file_name_regex": null,
    "max_file_size": 100
}
```

### Delete group push rule

Deletes the [push rules](../user/group/access_and_permissions.md#group-push-rules) of a group.

Only available to group owners and administrators.

```plaintext
DELETE /groups/:id/push_rule
```

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `id` | integer/string | yes | The ID or [URL-encoded path of the group](rest/index.md#namespaced-path-encoding) |

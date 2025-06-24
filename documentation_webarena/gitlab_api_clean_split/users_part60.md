## Create a runner linked to a user

DETAILS:
**Tier:** Free, Premium, Ultimate
**Offering:** GitLab.com, Self-managed, GitLab Dedicated

Creates a runner linked to the current user.

Prerequisites:

- You must be an administrator or have the Owner role of the target namespace or project.
- For `instance_type`, you must be an administrator of the GitLab instance.
- For `group_type` or `project_type` with an Owner role, an administrator must not have enabled [restrict runner registration](../administration/settings/continuous_integration.md#restrict-runner-registration-by-all-users-in-an-instance).
- An access token with the `create_runner` scope.

Be sure to copy or save the `token` in the response, the value cannot be retrieved again.

```plaintext
POST /user/runners
```

| Attribute          | Type         | Required | Description                                                                                       |
|--------------------|--------------|----------|---------------------------------------------------------------------------------------------------|
| `runner_type`      | string       | yes      | Specifies the scope of the runner; `instance_type`, `group_type`, or `project_type`.              |
| `group_id`         | integer      | no       | The ID of the group that the runner is created in. Required if `runner_type` is `group_type`.     |
| `project_id`       | integer      | no       | The ID of the project that the runner is created in. Required if `runner_type` is `project_type`. |
| `description`      | string       | no       | Description of the runner.                                                                        |
| `paused`           | boolean      | no       | Specifies if the runner should ignore new jobs.                                                   |
| `locked`           | boolean      | no       | Specifies if the runner should be locked for the current project.                                 |
| `run_untagged`     | boolean      | no       | Specifies if the runner should handle untagged jobs.                                              |
| `tag_list`         | string array | no       | A list of runner tags.                                                                            |
| `access_level`     | string       | no       | The access level of the runner; `not_protected` or `ref_protected`.                               |
| `maximum_timeout`  | integer      | no       | Maximum timeout that limits the amount of time (in seconds) that runners can run jobs.            |
| `maintenance_note` | string       | no       | Free-form maintenance notes for the runner (1024 characters).                                     |

```shell
curl --request POST --header "PRIVATE-TOKEN: <your_access_token>" --data "runner_type=instance_type" \
     "https://gitlab.example.com/api/v4/user/runners"
```

Example response:

```json
{
    "id": 9171,
    "token": "glrt-kyahzxLaj4Dc1jQf4xjX",
    "token_expires_at": null
}
```


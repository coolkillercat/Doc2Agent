## Delete project

This endpoint:

- Deletes a project including all associated resources (including issues and
  merge requests).
- On [Premium or Ultimate](https://about.gitlab.com/pricing/) tiers,
  [delayed project deletion](../user/project/working_with_projects.md#delayed-project-deletion)
  is applied if enabled.
- From [GitLab 15.11](https://gitlab.com/gitlab-org/gitlab/-/issues/396500) on
  [Premium or Ultimate](https://about.gitlab.com/pricing/) tiers, deletes a project immediately if the project is already
  marked for deletion, and the `permanently_remove` and `full_path` parameters are passed.
- From [GitLab 16.0](https://gitlab.com/gitlab-org/gitlab/-/issues/220382) on
  [Premium or Ultimate](https://about.gitlab.com/pricing/) tiers, delayed project deletion is enabled by default.
  The deletion happens after the number of days specified in the
  [default deletion delay](../administration/settings/visibility_and_access_controls.md#deletion-protection).

WARNING:
The option to delete projects immediately from deletion protection settings in the Admin Area was [deprecated](https://gitlab.com/gitlab-org/gitlab/-/issues/389557) in GitLab 15.9 and removed in GitLab 16.0.

```plaintext
DELETE /projects/:id
```

| Attribute                              | Type              | Required | Description |
|----------------------------------------|-------------------|----------|-------------|
| `id`                                   | integer or string | Yes      | The ID or [URL-encoded path of the project](rest/index.md#namespaced-path-encoding). |
| `full_path`                            | string            | no       | Full path of project to use with `permanently_remove`. [Introduced](https://gitlab.com/gitlab-org/gitlab/-/issues/396500) in GitLab 15.11. To find the project path, use `path_with_namespace` from [get single project](projects.md#get-single-project). Premium and Ultimate only. |
| `permanently_remove`                   | boolean/string    | no       | Immediately deletes a project if it is marked for deletion. [Introduced](https://gitlab.com/gitlab-org/gitlab/-/issues/396500) in GitLab 15.11. Premium and Ultimate only. |


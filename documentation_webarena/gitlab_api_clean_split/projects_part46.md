## Configure pull mirroring for a project

DETAILS:
**Tier:** Premium, Ultimate
**Offering:** GitLab.com, Self-managed, GitLab Dedicated

> - Field `mirror_branch_regex` [introduced](https://gitlab.com/gitlab-org/gitlab/-/issues/381667) in GitLab 15.8 [with a flag](../administration/feature_flags.md) named `mirror_only_branches_match_regex`. Disabled by default.
> - [Enabled by default](https://gitlab.com/gitlab-org/gitlab/-/issues/381667) in GitLab 16.0.
> - [Generally available](https://gitlab.com/gitlab-org/gitlab/-/issues/410354) in GitLab 16.2. Feature flag `mirror_only_branches_match_regex` removed.

Configure pull mirroring while [creating a new project](#create-project)
or [updating an existing project](#edit-project) using the API
if the remote repository is publicly accessible
or via `username:token` authentication.
In case your HTTP repository is not publicly accessible,
you can add the authentication information to the URL:
`https://username:token@gitlab.company.com/group/project.git`,
where `token` is a [personal access token](../user/profile/personal_access_tokens.md)
with the API scope enabled.

| Attribute                        | Type    | Required | Description |
|----------------------------------|---------|----------|-------------|
| `import_url`                     | string  | Yes      | URL of remote repository being mirrored (with `user:token` if needed). |
| `mirror`                         | boolean | Yes      | Enables pull mirroring on project when set to `true`. |
| `mirror_trigger_builds`          | boolean | No       | Trigger pipelines for mirror updates when set to `true`. |
| `only_mirror_protected_branches` | boolean | No       | Limits mirroring to only protected branches when set to `true`. |
| `mirror_branch_regex`            | String  | No       | Contains a regular expression. Only branches with names matching the regex are mirrored. Requires `only_mirror_protected_branches` to be disabled. |

Example creating a project with pull mirroring:

```shell
curl --request POST --header "PRIVATE-TOKEN: <your_access_token>" \
 --header "Content-Type: application/json" \
 --data '{
  "name": "new_project",
  "namespace_id": "1",
  "mirror": true,
  "import_url": "https://username:token@gitlab.example.com/group/project.git"
 }' \
 --url "https://gitlab.example.com/api/v4/projects/"
```

Example adding pull mirroring:

```shell
curl --request PUT --header "PRIVATE-TOKEN: <your_access_token>" \
 --url "https://gitlab.example.com/api/v4/projects/:id" \
 --data "mirror=true&import_url=https://username:token@gitlab.example.com/group/project.git"
```

Example removing pull mirroring:

```shell
curl --request PUT --header "PRIVATE-TOKEN: <your_access_token>" \
 --url "https://gitlab.example.com/api/v4/projects/:id"  \
 --data "mirror=false"
```


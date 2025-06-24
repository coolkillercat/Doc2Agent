## Add changelog data to a changelog file

> - Commit range limits [introduced](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/89032) in GitLab 15.1 [with a flag](../administration/feature_flags.md) named `changelog_commits_limitation`. Enabled by default.

Generate changelog data based on commits in a repository.

Given a [semantic version](https://semver.org/) and a range
of commits, GitLab generates a changelog for all commits that use a particular
[Git trailer](https://git-scm.com/docs/git-interpret-trailers). GitLab adds
a new Markdown-formatted section to a changelog file in the Git repository of
the project. The output format can be customized.

For user-facing documentation, see [Changelogs](../user/project/changelogs.md).

```plaintext
POST /projects/:id/repository/changelog
```

### Supported attributes

Changelogs support these attributes:

| Attribute | Type     | Required   | Description |
| :-------- | :------- | :--------- | :---------- |
| `version` | string   | yes | The version to generate the changelog for. The format must follow [semantic versioning](https://semver.org/). |
| `branch`  | string   | no | The branch to commit the changelog changes to. Defaults to the project's default branch. |
| `config_file` | string   | no | Path to the changelog configuration file in the project's Git repository. Defaults to `.gitlab/changelog_config.yml`. |
| `date`    | datetime | no | The date and time of the release. Defaults to the current time. |
| `file`    | string   | no | The file to commit the changes to. Defaults to `CHANGELOG.md`. |
| `from`    | string   | no | The SHA of the commit that marks the beginning of the range of commits to include in the changelog. This commit isn't included in the changelog. |
| `message` | string   | no | The commit message to use when committing the changes. Defaults to `Add changelog for version X`, where `X` is the value of the `version` argument. |
| `to`      | string   | no | The SHA of the commit that marks the end of the range of commits to include in the changelog. This commit _is_ included in the changelog. Defaults to the branch specified in the `branch` attribute. Limited to 15000 commits unless the feature flag `changelog_commits_limitation` is disabled. |
| `trailer` | string   | no | The Git trailer to use for including commits. Defaults to `Changelog`. Case-sensitive: `Example` does not match `example` or `eXaMpLE`. |

### Requirements for `from` attribute

If the `from` attribute is unspecified, GitLab uses the Git tag of the last
stable version that came before the version specified in the `version`
attribute. For GitLab to extract version numbers from tag names, Git tag names
must follow a specific format. By default, GitLab considers tags using these formats:

- `vX.Y.Z`
- `X.Y.Z`

Where `X.Y.Z` is a version that follows [semantic versioning](https://semver.org/).
For example, consider a project with the following tags:

- `v1.0.0-pre1`
- `v1.0.0`
- `v1.1.0`
- `v2.0.0`

If the `version` attribute is `2.1.0`, GitLab uses tag `v2.0.0`. And when the
version is `1.1.1`, or `1.2.0`, GitLab uses tag `v1.1.0`. The tag `v1.0.0-pre1` is
never used, because pre-release tags are ignored.

The `version` attribute can start with `v`. For example: `v1.0.0`.
The response is the same as for `version` value `1.0.0`. [Introduced](https://gitlab.com/gitlab-org/gitlab/-/issues/437616) in GitLab 17.0.

If `from` is unspecified and no tag to use is found, the API produces an error.
To solve such an error, you must explicitly specify a value for the `from`
attribute.

### Migrating from a manually-managed changelog file to Git trailers

When you migrate from an existing manually-managed changelog file to one that uses Git trailers,
make sure that the changelog file matches [the expected format](../user/project/changelogs.md).
Otherwise, new changelog entries added by the API might be inserted in an unexpected position.
For example, if the version values in the manually-managed changelog file are specified as `vX.Y.Z`
instead of `X.Y.Z`, then new changelog entries added using Git trailers are appended to the end of
the changelog file.

[Issue 444183](https://gitlab.com/gitlab-org/gitlab/-/issues/444183) proposes customizing the version header format in changelog files.
However, until that issue has been completed, the expected version header format in changelog files is `X.Y.Z`.

### Examples

These examples use [cURL](https://curl.se/) to perform HTTP requests.
The example commands use these values:

- **Project ID**: 42
- **Location**: hosted on GitLab.com
- **Example API token**: `token`

This command generates a changelog for version `1.0.0`.

The commit range:

- Starts with the tag of the last release.
- Ends with the last commit on the target branch. The default target branch is
  the project's default branch.

If the last tag is `v0.9.0` and the default branch is `main`, the range of commits
included in this example is `v0.9.0..main`:

```shell
curl --request POST --header "PRIVATE-TOKEN: token" \
  --data "version=1.0.0" "https://gitlab.com/api/v4/projects/42/repository/changelog"
```

To generate the data on a different branch, specify the `branch` parameter. This
command generates data from the `foo` branch:

```shell
curl --request POST --header "PRIVATE-TOKEN: token" \
  --data "version=1.0.0&branch=foo" "https://gitlab.com/api/v4/projects/42/repository/changelog"
```

To use a different trailer, use the `trailer` parameter:

```shell
curl --request POST --header "PRIVATE-TOKEN: token" \
  --data "version=1.0.0&trailer=Type" "https://gitlab.com/api/v4/projects/42/repository/changelog"
```

To store the results in a different file, use the `file` parameter:

```shell
curl --request POST --header "PRIVATE-TOKEN: token" \
  --data "version=1.0.0&file=NEWS" "https://gitlab.com/api/v4/projects/42/repository/changelog"
```


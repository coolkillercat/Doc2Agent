## Generate changelog data

Generate changelog data based on commits in a repository, without committing
them to a changelog file.

Works exactly like `POST /projects/:id/repository/changelog`, except the changelog
data isn't committed to any changelog file.

```plaintext
GET /projects/:id/repository/changelog
```

Supported attributes:

| Attribute | Type     | Required   | Description |
| :-------- | :------- | :--------- | :---------- |
| `version` | string   | yes | The version to generate the changelog for. The format must follow [semantic versioning](https://semver.org/). |
| `config_file` | string   | no | The path of changelog configuration file in the project's Git repository. Defaults to `.gitlab/changelog_config.yml`. |
| `date`    | datetime | no | The date and time of the release. Uses ISO 8601 format. Example: `2016-03-11T03:45:40Z`. Defaults to the current time. |
| `from`    | string   | no | The start of the range of commits (as a SHA) to use for generating the changelog. This commit itself isn't included in the list. |
| `to`      | string   | no | The end of the range of commits (as a SHA) to use for the changelog. This commit _is_ included in the list. Defaults to the HEAD of the default project branch. |
| `trailer` | string   | no | The Git trailer to use for including commits. Defaults to `Changelog`. |

```shell
curl --header "PRIVATE-TOKEN: token" \
  "https://gitlab.com/api/v4/projects/42/repository/changelog?version=1.0.0"
```

Example response, with line breaks added for readability:

```json
{
  "notes": "## 1.0.0 (2021-11-17)\n\n### feature (2 changes)\n\n-
    [Title 2](namespace13/project13@ad608eb642124f5b3944ac0ac772fecaf570a6bf)
    ([merge request](namespace13/project13!2))\n-
    [Title 1](namespace13/project13@3c6b80ff7034fa0d585314e1571cc780596ce3c8)
    ([merge request](namespace13/project13!1))\n"
}
```


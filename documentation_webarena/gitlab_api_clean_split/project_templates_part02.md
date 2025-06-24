## Get all templates of a particular type

```plaintext
GET /projects/:id/templates/:type
```

| Attribute  | Type   | Required | Description |
| ---------- | ------ | -------- | ----------- |
| `id`      | integer or string | Yes       | The ID or [URL-encoded path of the project](rest/index.md#namespaced-path-encoding). |
| `type`     | string | Yes  | The type of the template. Accepted values are: `dockerfiles`, `gitignores`, `gitlab_ci_ymls`, `licenses`, `issues`, or `merge_requests`. |

Example response (licenses):

```json
[
  {
    "key": "epl-1.0",
    "name": "Eclipse Public License 1.0"
  },
  {
    "key": "lgpl-3.0",
    "name": "GNU Lesser General Public License v3.0"
  },
  {
    "key": "unlicense",
    "name": "The Unlicense"
  },
  {
    "key": "agpl-3.0",
    "name": "GNU Affero General Public License v3.0"
  },
  {
    "key": "gpl-3.0",
    "name": "GNU General Public License v3.0"
  },
  {
    "key": "bsd-3-clause",
    "name": "BSD 3-clause \"New\" or \"Revised\" License"
  },
  {
    "key": "lgpl-2.1",
    "name": "GNU Lesser General Public License v2.1"
  },
  {
    "key": "mit",
    "name": "MIT License"
  },
  {
    "key": "apache-2.0",
    "name": "Apache License 2.0"
  },
  {
    "key": "bsd-2-clause",
    "name": "BSD 2-clause \"Simplified\" License"
  },
  {
    "key": "mpl-2.0",
    "name": "Mozilla Public License 2.0"
  },
  {
    "key": "gpl-2.0",
    "name": "GNU General Public License v2.0"
  }
]
```


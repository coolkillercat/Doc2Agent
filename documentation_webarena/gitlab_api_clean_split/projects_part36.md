## Search for projects by name

Search for projects by name which are accessible to the authenticated user. This
endpoint can be accessed without authentication if the project is publicly
accessible.

```plaintext
GET /projects
```

| Attribute  | Type   | Required | Description |
|------------|--------|----------|-------------|
| `search`   | string | Yes      | A string contained in the project name. |
| `order_by` | string | No       | Return requests ordered by `id`, `name`, `created_at` or `last_activity_at` fields. |
| `sort`     | string | No       | Return requests sorted in `asc` or `desc` order. |

```shell
curl --header "PRIVATE-TOKEN: <your_access_token>" "https://gitlab.example.com/api/v4/projects?search=test"
```


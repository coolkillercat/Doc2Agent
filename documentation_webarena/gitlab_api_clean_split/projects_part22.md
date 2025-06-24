## Languages

Get languages used in a project with percentage value.

```plaintext
GET /projects/:id/languages
```

| Attribute | Type              | Required | Description |
|-----------|-------------------|----------|-------------|
| `id`      | integer or string | Yes      | The ID or [URL-encoded path of the project](rest/index.md#namespaced-path-encoding). |

```shell
curl --header "PRIVATE-TOKEN: <your_access_token>" "https://gitlab.example.com/api/v4/projects/5/languages"
```

Example response:

```json
{
  "Ruby": 66.69,
  "JavaScript": 22.98,
  "HTML": 7.91,
  "CoffeeScript": 2.42
}
```


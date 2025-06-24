## List a project's groups

Get a list of ancestor groups for this project.

```plaintext
GET /projects/:id/groups
```

| Attribute                 | Type              | Required | Description |
|---------------------------|-------------------|----------|-------------|
| `id`                      | integer or string | Yes      | The ID or [URL-encoded path of the project](rest/index.md#namespaced-path-encoding). |
| `search`                  | string            | No       | Search for specific groups. |
| `shared_min_access_level` | integer           | No       | Limit to shared groups with at least this [role (`access_level`)](members.md#roles). |
| `shared_visible_only`     | boolean           | No       | Limit to shared groups user has access to. |
| `skip_groups`             | array of integers | No       | Skip the group IDs passed. |
| `with_shared`             | boolean           | No       | Include projects shared with this group. Default is `false`. |

```json
[
  {
    "id": 1,
    "name": "Foobar Group",
    "avatar_url": "http://localhost:3000/uploads/group/avatar/1/foo.jpg",
    "web_url": "http://localhost:3000/groups/foo-bar",
    "full_name": "Foobar Group",
    "full_path": "foo-bar"
  },
  {
    "id": 2,
    "name": "Shared Group",
    "avatar_url": "http://gitlab.example.com/uploads/group/avatar/1/bar.jpg",
    "web_url": "http://gitlab.example.com/groups/foo/bar",
    "full_name": "Shared Group",
    "full_path": "foo/shared"
  }
]
```


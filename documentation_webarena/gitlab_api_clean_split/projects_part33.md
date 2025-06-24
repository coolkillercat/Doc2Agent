## Import project members

Import members from another project.

If the importing member's role in the target project is:

- Maintainer, then members with the Owner role in the source project are imported with the Maintainer role.
- Owner, then members with the Owner role in the source project are imported with the Owner role.

```plaintext
POST /projects/:id/import_project_members/:project_id
```

| Attribute    | Type              | Required | Description |
|--------------|-------------------|----------|-------------|
| `id`         | integer or string | Yes      | The ID or [URL-encoded path](rest/index.md#namespaced-path-encoding) of the target project to receive the members. |
| `project_id` | integer or string | Yes      | The ID or [URL-encoded path](rest/index.md#namespaced-path-encoding) of the source project to import the members from. |

```shell
curl --request POST --header "PRIVATE-TOKEN: <your_access_token>" "https://gitlab.example.com/api/v4/projects/5/import_project_members/32"
```

Returns:

- `200 OK` on success.
- `404 Project Not Found` if the target or source project does not exist or cannot be accessed by the requester.
- `422 Unprocessable Entity` if the import of project members does not complete successfully.

Example responses:

When all emails were successfully sent (`200` HTTP status code):

```json
{  "status":  "success"  }
```

When there was any error importing 1 or more members (`200` HTTP status code):

```json
{
  "status": "error",
  "message": {
               "john_smith": "Some individual error message",
               "jane_smith": "Some individual error message"
             },
  "total_members_count": 3
}
```

When there is a system error (`404` and `422` HTTP status codes):

```json
{  "message":  "Import failed"  }
```


## Snippets

The Snippets Notes API is intended for project-level snippets, and not for personal snippets.

### List all snippet notes

Gets a list of all notes for a single snippet. Snippet notes are comments users can post to a snippet.

```plaintext
GET /projects/:id/snippets/:snippet_id/notes
GET /projects/:id/snippets/:snippet_id/notes?sort=asc&order_by=updated_at
```

| Attribute           | Type             | Required   | Description                                                                                                                                         |
| ------------------- | ---------------- | ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                | integer or string   | yes        | The ID or [URL-encoded path of the project](rest/index.md#namespaced-path-encoding) |
| `snippet_id`        | integer          | yes        | The ID of a project snippet |
| `sort`              | string           | no         | Return snippet notes sorted in `asc` or `desc` order. Default is `desc` |
| `order_by`          | string           | no         | Return snippet notes ordered by `created_at` or `updated_at` fields. Default is `created_at` |

```shell
curl --header "PRIVATE-TOKEN: <your_access_token>" "https://gitlab.example.com/api/v4/projects/5/snippets/11/notes"
```

### Get single snippet note

Returns a single note for a given snippet.

```plaintext
GET /projects/:id/snippets/:snippet_id/notes/:note_id
```

Parameters:

| Attribute    | Type           | Required | Description                                                                     |
|--------------|----------------|----------|---------------------------------------------------------------------------------|
| `id`         | integer or string | yes      | The ID or [URL-encoded path of the project](rest/index.md#namespaced-path-encoding) |
| `snippet_id` | integer        | yes      | The ID of a project snippet                                                     |
| `note_id`    | integer        | yes      | The ID of a snippet note                                                        |

```json
{
  "id": 302,
  "body": "closed",
  "attachment": null,
  "author": {
    "id": 1,
    "username": "pipin",
    "email": "admin@example.com",
    "name": "Pip",
    "state": "active",
    "created_at": "2013-09-30T13:46:01Z"
  },
  "created_at": "2013-10-02T09:22:45Z",
  "updated_at": "2013-10-02T10:22:45Z",
  "system": true,
  "noteable_id": 377,
  "noteable_type": "Issue",
  "project_id": 5,
  "noteable_iid": 377,
  "resolvable": false,
  "confidential": false,
  "internal": false,
  "imported": false,
  "imported_from": "none"
}
```

```shell
curl --header "PRIVATE-TOKEN: <your_access_token>" "https://gitlab.example.com/api/v4/projects/5/snippets/11/notes/11"
```

### Create new snippet note

Creates a new note for a single snippet. Snippet notes are user comments on snippets.
If you create a note where the body only contains an emoji reaction, GitLab returns this object.

```plaintext
POST /projects/:id/snippets/:snippet_id/notes
```

Parameters:

| Attribute    | Type           | Required | Description                                                                                                                  |
|--------------|----------------|----------|------------------------------------------------------------------------------------------------------------------------------|
| `id`         | integer or string | yes      | The ID or [URL-encoded path of the project](rest/index.md#namespaced-path-encoding)                                              |
| `snippet_id` | integer        | yes      | The ID of a snippet                                                                                                          |
| `body`       | string         | yes      | The content of a note. Limited to 1,000,000 characters.                                                                      |
| `created_at` | string         | no       | Date time string, ISO 8601 formatted. Example: `2016-03-11T03:45:40Z` (requires administrator or project/group owner rights) |

```shell
curl --request POST --header "PRIVATE-TOKEN: <your_access_token>" "https://gitlab.example.com/api/v4/projects/5/snippet/11/notes?body=note"
```

### Modify existing snippet note

Modify existing note of a snippet.

```plaintext
PUT /projects/:id/snippets/:snippet_id/notes/:note_id
```

Parameters:

| Attribute    | Type           | Required | Description                                                                                                                  |
|--------------|----------------|----------|------------------------------------------------------------------------------------------------------------------------------|
| `id`         | integer or string | yes      | The ID or [URL-encoded path of the project](rest/index.md#namespaced-path-encoding)                                              |
| `snippet_id` | integer        | yes      | The ID of a snippet                                                                                                          |
| `note_id`    | integer        | yes      | The ID of a snippet note                                                        |
| `body`       | string         | yes      | The content of a note. Limited to 1,000,000 characters.                                                                      |

```shell
curl --request PUT --header "PRIVATE-TOKEN: <your_access_token>" "https://gitlab.example.com/api/v4/projects/5/snippets/11/notes/1659?body=note"
```

### Delete a snippet note

Deletes an existing note of a snippet.

```plaintext
DELETE /projects/:id/snippets/:snippet_id/notes/:note_id
```

Parameters:

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `id` | integer or string | yes | The ID or [URL-encoded path of the project](rest/index.md#namespaced-path-encoding) |
| `snippet_id` | integer | yes | The ID of a snippet |
| `note_id` | integer | yes | The ID of a note |

```shell
curl --request DELETE --header "PRIVATE-TOKEN: <your_access_token>" "https://gitlab.example.com/api/v4/projects/5/snippets/52/notes/1659"
```


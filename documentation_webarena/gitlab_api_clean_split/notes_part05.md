## Issues

### List project issue notes

Gets a list of all notes for a single issue.

```plaintext
GET /projects/:id/issues/:issue_iid/notes
GET /projects/:id/issues/:issue_iid/notes?sort=asc&order_by=updated_at
```

| Attribute           | Type             | Required   | Description                                                                                                                                         |
| ------------------- | ---------------- | ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                | integer or string   | yes        | The ID or [URL-encoded path of the project](rest/index.md#namespaced-path-encoding) |
| `issue_iid`         | integer          | yes        | The IID of an issue |
| `sort`              | string           | no         | Return issue notes sorted in `asc` or `desc` order. Default is `desc` |
| `order_by`          | string           | no         | Return issue notes ordered by `created_at` or `updated_at` fields. Default is `created_at` |

```json
[
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
  },
  {
    "id": 305,
    "body": "Text of the comment\r\n",
    "attachment": null,
    "author": {
      "id": 1,
      "username": "pipin",
      "email": "admin@example.com",
      "name": "Pip",
      "state": "active",
      "created_at": "2013-09-30T13:46:01Z"
    },
    "created_at": "2013-10-02T09:56:03Z",
    "updated_at": "2013-10-02T09:56:03Z",
    "system": true,
    "noteable_id": 121,
    "noteable_type": "Issue",
    "project_id": 5,
    "noteable_iid": 121,
    "resolvable": false,
    "confidential": true,
    "internal": true,
    "imported": false,
    "imported_from": "none"
  }
]
```

```shell
curl --header "PRIVATE-TOKEN: <your_access_token>" "https://gitlab.example.com/api/v4/projects/5/issues/11/notes"
```

### Get single issue note

Returns a single note for a specific project issue

```plaintext
GET /projects/:id/issues/:issue_iid/notes/:note_id
```

Parameters:

| Attribute   | Type           | Required | Description                                                                     |
|-------------|----------------|----------|---------------------------------------------------------------------------------|
| `id`        | integer or string | yes      | The ID or [URL-encoded path of the project](rest/index.md#namespaced-path-encoding) |
| `issue_iid` | integer        | yes      | The IID of a project issue                                                      |
| `note_id`   | integer        | yes      | The ID of an issue note                                                         |

```shell
curl --header "PRIVATE-TOKEN: <your_access_token>" "https://gitlab.example.com/api/v4/projects/5/issues/11/notes/1"
```

### Create new issue note

Creates a new note to a single project issue.

```plaintext
POST /projects/:id/issues/:issue_iid/notes
```

Parameters:

| Attribute      | Type           | Required | Description                                                                                                                  |
|----------------|----------------|----------|------------------------------------------------------------------------------------------------------------------------------|
| `id`           | integer or string | yes      | The ID or [URL-encoded path of the project](rest/index.md#namespaced-path-encoding).                                           |
| `issue_iid`    | integer        | yes      | The IID of an issue.                                                                                                         |
| `body`         | string         | yes      | The content of a note. Limited to 1,000,000 characters.                                                                      |
| `confidential` | boolean        | no       | **Deprecated:** Scheduled to be removed in GitLab 16.0 and renamed to `internal`. The confidential flag of a note. Default is false.                                                                           |
| `internal`     | boolean        | no       | The internal flag of a note. Overrides `confidential` when both parameters are submitted. Default is false.                                                                               |
| `created_at`   | string         | no       | Date time string, ISO 8601 formatted. It must be after 1970-01-01. Example: `2016-03-11T03:45:40Z` (requires administrator or project/group owner rights) |

```shell
curl --request POST --header "PRIVATE-TOKEN: <your_access_token>" "https://gitlab.example.com/api/v4/projects/5/issues/11/notes?body=note"
```

### Modify existing issue note

Modify existing note of an issue.

```plaintext
PUT /projects/:id/issues/:issue_iid/notes/:note_id
```

Parameters:

| Attribute      | Type           | Required    | Description                                                                                        |
|----------------|----------------|-------------|----------------------------------------------------------------------------------------------------|
| `id`           | integer or string | yes      | The ID or [URL-encoded path of the project](rest/index.md#namespaced-path-encoding).                    |
| `issue_iid`    | integer           | yes      | The IID of an issue.                                                                               |
| `note_id`      | integer           | yes      | The ID of a note.                                                                                  |
| `body`         | string            | no       | The content of a note. Limited to 1,000,000 characters.                                            |
| `confidential` | boolean           | no       | **Deprecated:** Scheduled to be removed in GitLab 16.0. The confidential flag of a note. Default is false. |

```shell
curl --request PUT --header "PRIVATE-TOKEN: <your_access_token>" "https://gitlab.example.com/api/v4/projects/5/issues/11/notes/636?body=note"
```

### Delete an issue note

Deletes an existing note of an issue.

```plaintext
DELETE /projects/:id/issues/:issue_iid/notes/:note_id
```

Parameters:

| Attribute | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| `id` | integer or string | yes | The ID or [URL-encoded path of the project](rest/index.md#namespaced-path-encoding) |
| `issue_iid` | integer | yes | The IID of an issue |
| `note_id` | integer | yes | The ID of a note |

```shell
curl --request DELETE --header "PRIVATE-TOKEN: <your_access_token>" "https://gitlab.example.com/api/v4/projects/5/issues/11/notes/636"
```


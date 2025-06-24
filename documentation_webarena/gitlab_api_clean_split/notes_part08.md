## Epics

DETAILS:
**Tier:** Premium, Ultimate
**Offering:** GitLab.com, Self-managed, GitLab Dedicated

### List all epic notes

Gets a list of all notes for a single epic. Epic notes are comments users can post to an epic.

NOTE:
The epics notes API uses the epic ID instead of epic IID. If you use the epic's IID, GitLab returns either a 404
error or notes for the wrong epic. It's different from the [issue notes API](#issues) and
[merge requests notes API](#merge-requests).

```plaintext
GET /groups/:id/epics/:epic_id/notes
GET /groups/:id/epics/:epic_id/notes?sort=asc&order_by=updated_at
```

| Attribute           | Type             | Required   | Description |
| ------------------- | ---------------- | ---------- | ----------- |
| `id`                | integer or string   | yes        | The ID or [URL-encoded path of the group](rest/index.md#namespaced-path-encoding) |
| `epic_id`           | integer          | yes        | The ID of a group epic |
| `sort`              | string           | no         | Return epic notes sorted in `asc` or `desc` order. Default is `desc` |
| `order_by`          | string           | no         | Return epic notes ordered by `created_at` or `updated_at` fields. Default is `created_at` |

```shell
curl --header "PRIVATE-TOKEN: <your_access_token>" "https://gitlab.example.com/api/v4/groups/5/epics/11/notes"
```

### Get single epic note

Returns a single note for a given epic.

```plaintext
GET /groups/:id/epics/:epic_id/notes/:note_id
```

Parameters:

| Attribute | Type           | Required | Description |
| --------- | -------------- | -------- | ----------- |
| `id`      | integer or string | yes | The ID or [URL-encoded path of the group](rest/index.md#namespaced-path-encoding) |
| `epic_id` | integer | yes  | The ID of an epic |
| `note_id` | integer | yes  | The ID of a note |

```json
{
  "id": 302,
  "body": "Epic note",
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
  "noteable_id": 11,
  "noteable_type": "Epic",
  "project_id": 5,
  "noteable_iid": 11,
  "resolvable": false,
  "confidential": false,
  "internal": false,
  "imported": false,
  "imported_from": "none"
}
```

```shell
curl --header "PRIVATE-TOKEN: <your_access_token>" "https://gitlab.example.com/api/v4/groups/5/epics/11/notes/1"
```

### Create new epic note

Creates a new note for a single epic. Epic notes are comments users can post to an epic.
If you create a note where the body only contains an emoji reaction, GitLab returns this object.

```plaintext
POST /groups/:id/epics/:epic_id/notes
```

Parameters:

| Attribute      | Type           | Required | Description |
| ---------      | -------------- | -------- | ----------- |
| `body`         | string  | yes  | The content of a note. Limited to 1,000,000 characters. |
| `epic_id`      | integer | yes  | The ID of an epic |
| `id`           | integer or string | yes | The ID or [URL-encoded path of the group](rest/index.md#namespaced-path-encoding) |
| `confidential` | boolean        | no       | **Deprecated:** Scheduled to be removed in GitLab 16.0 and is renamed to `internal`. The confidential flag of a note. Default is `false`. |
| `internal`     | boolean        | no       | The internal flag of a note. Overrides `confidential` when both parameters are submitted. Default is `false`. |

```shell
curl --request POST --header "PRIVATE-TOKEN: <your_access_token>" "https://gitlab.example.com/api/v4/groups/5/epics/11/notes?body=note"
```

### Modify existing epic note

Modify existing note of an epic.

```plaintext
PUT /groups/:id/epics/:epic_id/notes/:note_id
```

Parameters:

| Attribute      | Type              | Required | Description                                                                                        |
| ---------------| ----------------- | -------- | ---------------------------------------------------------------------------------------------------|
| `id`           | integer or string | yes      | The ID or [URL-encoded path of the group](rest/index.md#namespaced-path-encoding)                       |
| `epic_id`      | integer           | yes      | The ID of an epic                                                                                  |
| `note_id`      | integer           | yes      | The ID of a note                                                                                   |
| `body`         | string            | yes      | The content of a note. Limited to 1,000,000 characters.                                            |
| `confidential` | boolean           | no       | **Deprecated:** Scheduled to be removed in GitLab 16.0. The confidential flag of a note. Default is false. |

```shell
curl --request PUT --header "PRIVATE-TOKEN: <your_access_token>" "https://gitlab.example.com/api/v4/groups/5/epics/11/notes/1?body=note"
```

### Delete an epic note

Deletes an existing note of an epic.

```plaintext
DELETE /groups/:id/epics/:epic_id/notes/:note_id
```

Parameters:

| Attribute | Type           | Required | Description |
| --------- | -------------- | -------- | ----------- |
| `id`      | integer or string | yes | The ID or [URL-encoded path of the group](rest/index.md#namespaced-path-encoding) |
| `epic_id` | integer | yes  | The ID of an epic |
| `note_id` | integer | yes  | The ID of a note |

```shell
curl --request DELETE --header "PRIVATE-TOKEN: <your_access_token>" "https://gitlab.example.com/api/v4/groups/5/epics/52/notes/1659"
```

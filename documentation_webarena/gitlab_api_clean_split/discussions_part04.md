## Snippets

### List project snippet discussion items

Gets a list of all discussion items for a single snippet.

```plaintext
GET /projects/:id/snippets/:snippet_id/discussions
```

| Attribute           | Type             | Required   | Description |
| ------------------- | ---------------- | ---------- | ------------|
| `id`                | integer/string   | yes        | The ID or [URL-encoded path of the project](rest/index.md#namespaced-path-encoding). |
| `snippet_id`        | integer          | yes        | The ID of an snippet. |

```json
[
  {
    "id": "6a9c1750b37d513a43987b574953fceb50b03ce7",
    "individual_note": false,
    "notes": [
      {
        "id": 1126,
        "type": "DiscussionNote",
        "body": "discussion text",
        "attachment": null,
        "author": {
          "id": 1,
          "name": "root",
          "username": "root",
          "state": "active",
          "avatar_url": "https://www.gravatar.com/avatar/00afb8fb6ab07c3ee3e9c1f38777e2f4?s=80&d=identicon",
          "web_url": "http://localhost:3000/root"
        },
        "created_at": "2018-03-03T21:54:39.668Z",
        "updated_at": "2018-03-03T21:54:39.668Z",
        "system": false,
        "noteable_id": 3,
        "noteable_type": "Snippet",
        "project_id": 5,
        "noteable_iid": null
      },
      {
        "id": 1129,
        "type": "DiscussionNote",
        "body": "reply to the discussion",
        "attachment": null,
        "author": {
          "id": 1,
          "name": "root",
          "username": "root",
          "state": "active",
          "avatar_url": "https://www.gravatar.com/avatar/00afb8fb6ab07c3ee3e9c1f38777e2f4?s=80&d=identicon",
          "web_url": "http://localhost:3000/root"
        },
        "created_at": "2018-03-04T13:38:02.127Z",
        "updated_at": "2018-03-04T13:38:02.127Z",
        "system": false,
        "noteable_id": 3,
        "noteable_type": "Snippet",
        "project_id": 5,
        "noteable_iid": null,
        "resolvable": false
      }
    ]
  },
  {
    "id": "87805b7c09016a7058e91bdbe7b29d1f284a39e6",
    "individual_note": true,
    "notes": [
      {
        "id": 1128,
        "type": null,
        "body": "a single comment",
        "attachment": null,
        "author": {
          "id": 1,
          "name": "root",
          "username": "root",
          "state": "active",
          "avatar_url": "https://www.gravatar.com/avatar/00afb8fb6ab07c3ee3e9c1f38777e2f4?s=80&d=identicon",
          "web_url": "http://localhost:3000/root"
        },
        "created_at": "2018-03-04T09:17:22.520Z",
        "updated_at": "2018-03-04T09:17:22.520Z",
        "system": false,
        "noteable_id": 3,
        "noteable_type": "Snippet",
        "project_id": 5,
        "noteable_iid": null,
        "resolvable": false
      }
    ]
  }
]
```

```shell
curl --header "PRIVATE-TOKEN: <your_access_token>" \
  "https://gitlab.example.com/api/v4/projects/5/snippets/11/discussions"
```

### Get single snippet discussion item

Returns a single discussion item for a specific project snippet.

```plaintext
GET /projects/:id/snippets/:snippet_id/discussions/:discussion_id
```

Parameters:

| Attribute       | Type           | Required | Description |
| --------------- | -------------- | -------- | ----------- |
| `discussion_id` | integer        | yes      | The ID of a discussion item. |
| `id`            | integer or string | yes      | The ID or [URL-encoded path of the project](rest/index.md#namespaced-path-encoding). |
| `snippet_id`    | integer        | yes      | The ID of an snippet. |

```shell
curl --request POST --header "PRIVATE-TOKEN: <your_access_token>" \
  "https://gitlab.example.com/api/v4/projects/5/snippets/11/discussions/<discussion_id>"
```

### Create new snippet thread

Creates a new thread to a single project snippet. Similar to creating
a note, but other comments (replies) can be added to it later.

```plaintext
POST /projects/:id/snippets/:snippet_id/discussions
```

Parameters:

| Attribute       | Type           | Required | Description |
| --------------- | -------------- | -------- | ----------- |
| `body`          | string         | yes      | The content of a discussion. |
| `id`            | integer or string | yes      | The ID or [URL-encoded path of the project](rest/index.md#namespaced-path-encoding). |
| `snippet_id`    | integer        | yes      | The ID of an snippet. |
| `created_at`    | string         | no       | Date time string, ISO 8601 formatted, such as `2016-03-11T03:45:40Z`. Requires administrator or project/group owner rights. |

```shell
curl --request POST --header "PRIVATE-TOKEN: <your_access_token>"\
  "https://gitlab.example.com/api/v4/projects/5/snippets/11/discussions?body=comment"
```

### Add note to existing snippet thread

Adds a new note to the thread.

```plaintext
POST /projects/:id/snippets/:snippet_id/discussions/:discussion_id/notes
```

Parameters:

| Attribute       | Type           | Required | Description |
| --------------- | -------------- | -------- | ----------- |
| `body`          | string         | yes      | The content of the note or reply. |
| `discussion_id` | integer        | yes      | The ID of a thread. |
| `id`            | integer or string | yes      | The ID or [URL-encoded path of the project](rest/index.md#namespaced-path-encoding). |
| `note_id`       | integer        | yes      | The ID of a thread note. |
| `snippet_id`    | integer        | yes      | The ID of an snippet. |
| `created_at`    | string         | no       | Date time string, ISO 8601 formatted, such as `2016-03-11T03:45:40Z`. Requires administrator or project/group owner rights. |

```shell
curl --request POST --header "PRIVATE-TOKEN: <your_access_token>" \
  "https://gitlab.example.com/api/v4/projects/5/snippets/11/discussions/<discussion_id>/notes?body=comment"
```

### Modify existing snippet thread note

Modify existing thread note of a snippet.

```plaintext
PUT /projects/:id/snippets/:snippet_id/discussions/:discussion_id/notes/:note_id
```

Parameters:

| Attribute       | Type           | Required | Description |
| --------------- | -------------- | -------- | ----------- |
| `body`          | string         | yes      | The content of the note or reply. |
| `discussion_id` | integer        | yes      | The ID of a thread. |
| `id`            | integer or string | yes      | The ID or [URL-encoded path of the project](rest/index.md#namespaced-path-encoding). |
| `note_id`       | integer        | yes      | The ID of a thread note. |
| `snippet_id`    | integer        | yes      | The ID of an snippet. |

```shell
curl --request PUT --header "PRIVATE-TOKEN: <your_access_token>" \
  "https://gitlab.example.com/api/v4/projects/5/snippets/11/discussions/<discussion_id>/notes/1108?body=comment"
```

### Delete a snippet thread note

Deletes an existing thread note of a snippet.

```plaintext
DELETE /projects/:id/snippets/:snippet_id/discussions/:discussion_id/notes/:note_id
```

Parameters:

| Attribute       | Type           | Required | Description |
| --------------- | -------------- | -------- | ----------- |
| `discussion_id` | integer        | yes      | The ID of a discussion. |
| `id`            | integer or string | yes      | The ID or [URL-encoded path of the project](rest/index.md#namespaced-path-encoding). |
| `note_id`       | integer        | yes      | The ID of a discussion note. |
| `snippet_id`    | integer        | yes      | The ID of an snippet. |

```shell
curl --request DELETE --header "PRIVATE-TOKEN: <your_access_token>" \
  "https://gitlab.example.com/api/v4/projects/5/snippets/11/discussions/636"
```


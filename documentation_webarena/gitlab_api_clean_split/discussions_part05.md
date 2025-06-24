## Epics

DETAILS:
**Tier:** Ultimate
**Offering:** GitLab.com, Self-managed, GitLab Dedicated

### List group epic discussion items

Gets a list of all discussion items for a single epic.

```plaintext
GET /groups/:id/epics/:epic_id/discussions
```

| Attribute           | Type             | Required   | Description  |
| ------------------- | ---------------- | ---------- | ------------ |
| `epic_id`           | integer          | yes        | The ID of an epic. |
| `id`                | integer or string   | yes        | The ID or [URL-encoded path of the group](rest/index.md#namespaced-path-encoding). |

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
        "noteable_type": "Epic",
        "project_id": 5,
        "noteable_iid": null,
        "resolvable": false
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
        "noteable_type": "Epic",
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
        "noteable_type": "Epic",
        "project_id": 5,
        "noteable_iid": null,
        "resolvable": false
      }
    ]
  }
]
```

```shell
curl --header "PRIVATE-TOKEN: <your_access_token>"\
  "https://gitlab.example.com/api/v4/groups/5/epics/11/discussions"
```

### Get single epic discussion item

Returns a single discussion item for a specific group epic.

```plaintext
GET /groups/:id/epics/:epic_id/discussions/:discussion_id
```

Parameters:

| Attribute       | Type           | Required | Description |
| --------------- | -------------- | -------- | ----------- |
| `discussion_id` | integer        | yes      | The ID of a discussion item. |
| `epic_id`       | integer        | yes      | The ID of an epic. |
| `id`            | integer or string | yes      | The ID or [URL-encoded path of the group](rest/index.md#namespaced-path-encoding). |

```shell
curl --request POST --header "PRIVATE-TOKEN: <your_access_token>" \
  "https://gitlab.example.com/api/v4/groups/5/epics/11/discussions/<discussion_id>"
```

### Create new epic thread

Creates a new thread to a single group epic. Similar to creating
a note, but other comments (replies) can be added to it later.

```plaintext
POST /groups/:id/epics/:epic_id/discussions
```

Parameters:

| Attribute       | Type           | Required | Description |
| --------------- | -------------- | -------- | ----------- |
| `body`          | string         | yes      | The content of the thread. |
| `epic_id`       | integer        | yes      | The ID of an epic. |
| `id`            | integer or string | yes      | The ID or [URL-encoded path of the group](rest/index.md#namespaced-path-encoding). |
| `created_at`    | string         | no       | Date time string, ISO 8601 formatted, such as `2016-03-11T03:45:40Z`. Requires administrator or project/group owner rights. |

```shell
curl --request POST --header "PRIVATE-TOKEN: <your_access_token>" \
  "https://gitlab.example.com/api/v4/groups/5/epics/11/discussions?body=comment"
```

### Add note to existing epic thread

Adds a new note to the thread. This can also
[create a thread from a single comment](../user/discussions/index.md#create-a-thread-by-replying-to-a-standard-comment).

```plaintext
POST /groups/:id/epics/:epic_id/discussions/:discussion_id/notes
```

Parameters:

| Attribute       | Type           | Required | Description |
| --------------- | -------------- | -------- | ----------- |
| `body`          | string         | yes      | The content of the note or reply. |
| `discussion_id` | integer        | yes      | The ID of a thread. |
| `epic_id`       | integer        | yes      | The ID of an epic. |
| `id`            | integer or string | yes      | The ID or [URL-encoded path of the group](rest/index.md#namespaced-path-encoding). |
| `note_id`       | integer        | yes      | The ID of a thread note. |
| `created_at`    | string         | no       | Date time string, ISO 8601 formatted, such as `2016-03-11T03:45:40Z`. Requires administrator or project/group owner rights. |

```shell
curl --request POST --header "PRIVATE-TOKEN: <your_access_token>" \
  "https://gitlab.example.com/api/v4/groups/5/epics/11/discussions/<discussion_id>/notes?body=comment"
```

### Modify existing epic thread note

Modify existing thread note of an epic.

```plaintext
PUT /groups/:id/epics/:epic_id/discussions/:discussion_id/notes/:note_id
```

Parameters:

| Attribute       | Type           | Required | Description |
| --------------- | -------------- | -------- | ----------- |
| `body`          | string         | yes      | The content of note or reply. |
| `discussion_id` | integer        | yes      | The ID of a thread. |
| `epic_id`       | integer        | yes      | The ID of an epic. |
| `id`            | integer/string | yes      | The ID or [URL-encoded path of the group](rest/index.md#namespaced-path-encoding). |
| `note_id`       | integer        | yes      | The ID of a thread note. |

```shell
curl --request PUT --header "PRIVATE-TOKEN: <your_access_token>" \
  "https://gitlab.example.com/api/v4/groups/5/epics/11/discussions/<discussion_id>/notes/1108?body=comment"
```

### Delete an epic thread note

Deletes an existing thread note of an epic.

```plaintext
DELETE /groups/:id/epics/:epic_id/discussions/:discussion_id/notes/:note_id
```

Parameters:

| Attribute       | Type           | Required | Description |
| --------------- | -------------- | -------- | ----------- |
| `discussion_id` | integer        | yes      | The ID of a thread. |
| `epic_id`       | integer        | yes      | The ID of an epic. |
| `id`            | integer or string | yes      | The ID or [URL-encoded path of the group](rest/index.md#namespaced-path-encoding). |
| `note_id`       | integer        | yes      | The ID of a thread note. |

```shell
curl --request DELETE --header "PRIVATE-TOKEN: <your_access_token>" \
  "https://gitlab.example.com/api/v4/groups/5/epics/11/discussions/636"
```


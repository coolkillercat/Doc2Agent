## Commits

### List project commit discussion items

Gets a list of all discussion items for a single commit.

```plaintext
GET /projects/:id/repository/commits/:commit_id/discussions
```

| Attribute           | Type             | Required   | Description  |
| ------------------- | ---------------- | ---------- | ------------ |
| `commit_id`         | string           | yes        | The SHA of a commit. |
| `id`                | integer or string   | yes        | The ID or [URL-encoded path of the project](rest/index.md#namespaced-path-encoding). |

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
        "noteable_type": "Commit",
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
        "noteable_type": "Commit",
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
        "noteable_type": "Commit",
        "project_id": 5,
        "noteable_iid": null,
        "resolvable": false
      }
    ]
  }
]
```

Diff comments contain also position:

```json
[
  {
    "id": "87805b7c09016a7058e91bdbe7b29d1f284a39e6",
    "individual_note": false,
    "notes": [
      {
        "id": 1128,
        "type": "DiffNote",
        "body": "diff comment",
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
        "noteable_type": "Commit",
        "project_id": 5,
        "noteable_iid": null,
        "position": {
          "base_sha": "b5d6e7b1613fca24d250fa8e5bc7bcc3dd6002ef",
          "start_sha": "7c9c2ead8a320fb7ba0b4e234bd9529a2614e306",
          "head_sha": "4803c71e6b1833ca72b8b26ef2ecd5adc8a38031",
          "old_path": "package.json",
          "new_path": "package.json",
          "position_type": "text",
          "old_line": 27,
          "new_line": 27
        },
        "resolvable": false
      }
    ]
  }
]
```

```shell
curl --header "PRIVATE-TOKEN: <your_access_token>" \
  "https://gitlab.example.com/api/v4/projects/5/repository/commits/<commit_id>/discussions"
```

### Get single commit discussion item

Returns a single discussion item for a specific project commit

```plaintext
GET /projects/:id/repository/commits/:commit_id/discussions/:discussion_id
```

Parameters:

| Attribute           | Type           | Required | Description |
| ------------------- | -------------- | -------- | ----------- |
| `commit_id`         | string         | yes      | The SHA of a commit. |
| `discussion_id`     | string         | yes      | The ID of a discussion item. |
| `id`                | integer or string | yes      | The ID or [URL-encoded path of the project](rest/index.md#namespaced-path-encoding). |

```shell
curl --header "PRIVATE-TOKEN: <your_access_token>" \
  "https://gitlab.example.com/api/v4/projects/5/repository/commits/<commit_id>/discussions/<discussion_id>"
```

### Create new commit thread

Creates a new thread to a single project commit. Similar to creating
a note but other comments (replies) can be added to it later.

```plaintext
POST /projects/:id/repository/commits/:commit_id/discussions
```

Parameters:

| Attribute                 | Type           | Required                         | Description |
| ------------------------- | -------------- |----------------------------------| ----------- |
| `body`                    | string         | yes                              | The content of the thread. |
| `commit_id`               | string         | yes                              | The SHA of a commit. |
| `id`                      | integer/string | yes                              | The ID or [URL-encoded path of the project](rest/index.md#namespaced-path-encoding). |
| `position[base_sha]`      | string         | yes (if `position*` is supplied) | SHA of the parent commit. |
| `position[head_sha]`      | string         | yes (if `position*` is supplied) | The SHA of this commit. Same as `commit_id`. |
| `position[start_sha]`     | string         | yes (if `position*` is supplied) | SHA of the parent commit. |
| `position[position_type]` | string         | yes (if `position*` is supplied) | Type of the position reference. Allowed values: `text` or `image`. |
| `created_at`              | string         | no                               | Date time string, ISO 8601 formatted, such as `2016-03-11T03:45:40Z`. Requires administrator or project/group owner rights. |
| `position`                | hash           | no                               | Position when creating a diff note. |

| `position[new_path]`      | string         | no       | File path after change. |
| `position[new_line]`      | integer        | no       | Line number after change. |
| `position[old_path]`      | string         | no       | File path before change. |
| `position[old_line]`      | integer        | no       | Line number before change. |
| `position[height]`        | integer        | no       | For `image` diff notes, image height. |
| `position[width]`         | integer        | no       | For `image` diff notes, image width. |
| `position[x]`             | integer        | no       | For `image` diff notes, X coordinate. |
| `position[y]`             | integer        | no       | For `image` diff notes, Y coordinate. |

```shell
curl --request POST --header "PRIVATE-TOKEN: <your_access_token>" \
  "https://gitlab.example.com/api/v4/projects/5/repository/commits/<commit_id>/discussions?body=comment"
```

The rules for creating the API request are the same as when
[creating a new thread in the merge request diff](#create-a-new-thread-in-the-merge-request-diff).
The exceptions:

- `base_sha`
- `head_sha`
- `start_sha`

### Add note to existing commit thread

Adds a new note to the thread.

```plaintext
POST /projects/:id/repository/commits/:commit_id/discussions/:discussion_id/notes
```

Parameters:

| Attribute           | Type           | Required | Description |
| ------------------- | -------------- | -------- | ----------- |
| `body`              | string         | yes      | The content of the note or reply. |
| `commit_id`         | string         | yes      | The SHA of a commit. |
| `discussion_id`     | string         | yes      | The ID of a thread. |
| `id`                | integer or string | yes      | The ID or [URL-encoded path of the project](rest/index.md#namespaced-path-encoding). |
| `note_id`           | integer        | yes      | The ID of a thread note. |
| `created_at`        | string         | no       | Date time string, ISO 8601 formatted, such `2016-03-11T03:45:40Z`. Requires administrator or project/group owner rights. |

```shell
curl --request POST --header "PRIVATE-TOKEN: <your_access_token>" \
  "https://gitlab.example.com/api/v4/projects/5/repository/commits/<commit_id>/discussions/<discussion_id>/notes?body=comment
```

### Modify an existing commit thread note

Modify or resolve an existing thread note of a commit.

```plaintext
PUT /projects/:id/repository/commits/:commit_id/discussions/:discussion_id/notes/:note_id
```

Parameters:

| Attribute           | Type           | Required | Description |
| ------------------- | -------------- | -------- | ----------- |
| `commit_id`         | string         | yes      | The SHA of a commit. |
| `discussion_id`     | string         | yes      | The ID of a thread. |
| `id`                | integer or string | yes      | The ID or [URL-encoded path of the project](rest/index.md#namespaced-path-encoding). |
| `note_id`           | integer        | yes      | The ID of a thread note. |
| `body`              | string         | no       | The content of a note. |

```shell
curl --request PUT --header "PRIVATE-TOKEN: <your_access_token>" \
  "https://gitlab.example.com/api/v4/projects/5/repository/commits/<commit_id>/discussions/<discussion_id>/notes/1108?body=comment"
```

Resolving a note:

```shell
curl --request PUT --header "PRIVATE-TOKEN: <your_access_token>" \
  "https://gitlab.example.com/api/v4/projects/5/repository/commits/<commit_id>/discussions/<discussion_id>/notes/1108?resolved=true"
```

### Delete a commit thread note

Deletes an existing thread note of a commit.

```plaintext
DELETE /projects/:id/repository/commits/:commit_id/discussions/:discussion_id/notes/:note_id
```

Parameters:

| Attribute           | Type           | Required | Description |
| ------------------- | -------------- | -------- | ----------- |
| `id`                | integer or string | yes      | The ID or [URL-encoded path of the project](rest/index.md#namespaced-path-encoding). |
| `commit_id`         | string         | yes      | The SHA of a commit. |
| `discussion_id`     | string         | yes      | The ID of a thread. |
| `note_id`           | integer        | yes      | The ID of a thread note. |

```shell
curl --request DELETE --header "PRIVATE-TOKEN: <your_access_token>" \
  "https://gitlab.example.com/api/v4/projects/5/repository/commits/<commit_id>/discussions/<discussion_id>/notes/636"
```

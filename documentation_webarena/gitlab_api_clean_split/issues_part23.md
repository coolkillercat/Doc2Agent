## Incidents

The following requests are available only for [incidents](../operations/incident_management/incidents.md).

### Upload metric image

Available only for [incidents](../operations/incident_management/incidents.md).

Uploads a screenshot of metric charts to show in the incident's **Metrics** tab.
When you upload an image, you can associate the image with text or a link to the original graph.
If you add a URL, you can access the original graph by selecting the hyperlink above the uploaded image.

```plaintext
POST /projects/:id/issues/:issue_iid/metric_images
```

Supported attributes:

| Attribute   | Type    | Required | Description                          |
|-------------|---------|----------|--------------------------------------|
| `id`        | integer/string | Yes      | The global ID or [URL-encoded path of the project](rest/index.md#namespaced-path-encoding) owned by the authenticated user.  |
| `issue_iid` | integer | Yes      | The internal ID of a project's issue. |
| `file` | file | Yes      | The image file to be uploaded. |
| `url` | string | No      | The URL to view more metric information. |
| `url_text` | string | No      | A description of the image or URL. |

Example request:

```shell
curl --header "PRIVATE-TOKEN: <your_access_token>" \
  --form 'file=@/path/to/file.png' \
  --form 'url=http://example.com' \
  --form 'url_text=Example website' \
  --url "https://gitlab.example.com/api/v4/projects/5/issues/93/metric_images"
```

Example response:

```json
{
    "id": 23,
    "created_at": "2020-11-13T00:06:18.084Z",
    "filename": "file.png",
    "file_path": "/uploads/-/system/issuable_metric_image/file/23/file.png",
    "url": "http://example.com",
    "url_text": "Example website"
}
```

### List metric images

Available only for [incidents](../operations/incident_management/incidents.md).

Lists screenshots of metric charts shown in the incident's **Metrics** tab.

```plaintext
GET /projects/:id/issues/:issue_iid/metric_images
```

Supported attributes:

| Attribute   | Type    | Required | Description                          |
|-------------|---------|----------|--------------------------------------|
| `id`        | integer/string | Yes      | The global ID or [URL-encoded path of the project](rest/index.md#namespaced-path-encoding) owned by the authenticated user.  |
| `issue_iid` | integer | Yes      | The internal ID of a project's issue. |

Example request:

```shell
curl --header "PRIVATE-TOKEN: <your_access_token>" \
  -url "https://gitlab.example.com/api/v4/projects/5/issues/93/metric_images"
```

Example response:

```json
[
    {
        "id": 17,
        "created_at": "2020-11-12T20:07:58.156Z",
        "filename": "sample_2054",
        "file_path": "/uploads/-/system/issuable_metric_image/file/17/sample_2054.png",
        "url": "example.com/metric"
    },
    {
        "id": 18,
        "created_at": "2020-11-12T20:14:26.441Z",
        "filename": "sample_2054",
        "file_path": "/uploads/-/system/issuable_metric_image/file/18/sample_2054.png",
        "url": "example.com/metric"
    }
]
```

### Update metric image

Available only for [incidents](../operations/incident_management/incidents.md).

Edits attributes of a screenshot of metric charts shown in the incident's **Metrics** tab.

```plaintext
PUT /projects/:id/issues/:issue_iid/metric_images/:image_id
```

Supported attributes:

| Attribute   | Type    | Required | Description                          |
|-------------|---------|----------|--------------------------------------|
| `id`        | integer/string | Yes      | The global ID or [URL-encoded path of the project](rest/index.md#namespaced-path-encoding) owned by the authenticated user.  |
| `issue_iid` | integer | Yes      | The internal ID of a project's issue. |
| `image_id` | integer | Yes      | The ID of the image. |
| `url` | string | No      | The URL to view more metric information. |
| `url_text` | string | No      | A description of the image or URL. |

Example request:

```shell
curl --header "PRIVATE-TOKEN: <your_access_token>" \
  --request PUT \
  --form 'url=http://example.com' \
  --form 'url_text=Example website' \
  --url "https://gitlab.example.com/api/v4/projects/5/issues/93/metric_images/1"
```

Example response:

```json
{
    "id": 23,
    "created_at": "2020-11-13T00:06:18.084Z",
    "filename": "file.png",
    "file_path": "/uploads/-/system/issuable_metric_image/file/23/file.png",
    "url": "http://example.com",
    "url_text": "Example website"
}
```

### Delete metric image

Available only for [incidents](../operations/incident_management/incidents.md).

Delete a screenshot of metric charts shown in the incident's **Metrics** tab.

```plaintext
DELETE /projects/:id/issues/:issue_iid/metric_images/:image_id
```

Supported attributes:

| Attribute   | Type    | Required | Description                          |
|-------------|---------|----------|--------------------------------------|
| `id`        | integer/string | Yes      | The global ID or [URL-encoded path of the project](rest/index.md#namespaced-path-encoding) owned by the authenticated user.  |
| `issue_iid` | integer | Yes      | The internal ID of a project's issue. |
| `image_id` | integer | Yes      | The ID of the image. |

Example request:

```shell
curl --header "PRIVATE-TOKEN: <your_access_token>" \
  --request DELETE \
  --url "https://gitlab.example.com/api/v4/projects/5/issues/93/metric_images/1"
```

Can return the following status codes:

- `204 No Content`, if the image was deleted successfully.
- `400 Bad Request`, if the image could not be deleted.

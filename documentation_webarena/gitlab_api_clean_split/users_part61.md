## Upload a current user avatar

> - [Introduced](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/148130) in GitLab 17.0.

Upload an avatar to current user.

```plaintext
PUT /user/avatar
```

| Attribute | Type              | Required | Description                                                                                                 |
|-----------|-------------------|----------|-------------------------------------------------------------------------------------------------------------|
| `avatar`  | string            | Yes      | The file to be uploaded. The ideal image size is 192 x 192 pixels. The maximum file size allowed is 200 KiB. |

To upload an avatar from your file system, use the `--form` argument. This causes
cURL to post data using the header `Content-Type: multipart/form-data`. The
`file=` parameter must point to an image file on your file system and be
preceded by `@`. For example:

Example request:

```shell
curl --request PUT --header "PRIVATE-TOKEN: <your_access_token>" \
     --form "avatar=@avatar.png" \
     --url "https://gitlab.example.com/api/v4/user/avatar"
```

Returned object:

Returns `400 Bad Request` for file sizes greater than 200 KiB.

If successful, returns [`200`](rest/index.md#status-codes) and the following
response attributes:

```json
{
  "avatar_url": "http://gdk.test:3000/uploads/-/system/user/avatar/76/avatar.png",
}
```

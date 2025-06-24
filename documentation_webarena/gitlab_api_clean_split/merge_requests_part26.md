## Get merge request diff versions

Get a list of merge request diff versions.

```plaintext
GET /projects/:id/merge_requests/:merge_request_iid/versions
```

| Attribute           | Type    | Required | Description                           |
|---------------------|---------|----------|---------------------------------------|
| `id`                | String  | Yes      | The ID of the project.                |
| `merge_request_iid` | integer | Yes      | The internal ID of the merge request. |

For an explanation of the SHAs in the response,
see [SHAs in the API response](#shas-in-the-api-response).

```shell
curl --header "PRIVATE-TOKEN: <your_access_token>" \
  --url "https://gitlab.example.com/api/v4/projects/1/merge_requests/1/versions"
```

Example response:

```json
[{
  "id": 110,
  "head_commit_sha": "33e2ee8579fda5bc36accc9c6fbd0b4fefda9e30",
  "base_commit_sha": "eeb57dffe83deb686a60a71c16c32f71046868fd",
  "start_commit_sha": "eeb57dffe83deb686a60a71c16c32f71046868fd",
  "created_at": "2016-07-26T14:44:48.926Z",
  "merge_request_id": 105,
  "state": "collected",
  "real_size": "1",
  "patch_id_sha": "d504412d5b6e6739647e752aff8e468dde093f2f"
}, {
  "id": 108,
  "head_commit_sha": "3eed087b29835c48015768f839d76e5ea8f07a24",
  "base_commit_sha": "eeb57dffe83deb686a60a71c16c32f71046868fd",
  "start_commit_sha": "eeb57dffe83deb686a60a71c16c32f71046868fd",
  "created_at": "2016-07-25T14:21:33.028Z",
  "merge_request_id": 105,
  "state": "collected",
  "real_size": "1",
  "patch_id_sha": "72c30d1f0115fc1d2bb0b29b24dc2982cbcdfd32"
}]
```

### SHAs in the API response

| SHA field          | Purpose                                                                             |
|--------------------|-------------------------------------------------------------------------------------|
| `base_commit_sha`  | The merge-base commit SHA between the source branch and the target branches.        |
| `head_commit_sha`  | The HEAD commit of the source branch.                                               |
| `start_commit_sha` | The HEAD commit SHA of the target branch when this version of the diff was created. |


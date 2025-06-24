## Remove a project avatar

> - [Introduced](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/92604) in GitLab 15.4.

To remove a project avatar, use a blank value for the `avatar` attribute.

Example request:

```shell
curl --request PUT --header "PRIVATE-TOKEN: <your_access_token>" \
     --data "avatar=" "https://gitlab.example.com/api/v4/projects/5"
```


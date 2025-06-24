## User counts

Get the counts (same as in the upper-right menu) of the authenticated user.

| Attribute                         | Type   | Description                                                                  |
| --------------------------------- | ------ | ---------------------------------------------------------------------------- |
| `assigned_issues`                 | number | Number of issues that are open and assigned to the current user.             |
| `assigned_merge_requests`         | number | Number of merge requests that are active and assigned to the current user.   |
| `merge_requests`                  | number | [Deprecated](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/50026) in GitLab 13.8. Equivalent to and replaced by `assigned_merge_requests`.        |
| `review_requested_merge_requests` | number | Number of merge requests that the current user has been requested to review. |
| `todos`                           | number | Number of pending to-do items for current user.                              |

```plaintext
GET /user_counts
```

```shell
curl --header "PRIVATE-TOKEN: <your_access_token>" "https://gitlab.example.com/user_counts"
```

Example response:

```json
{
  "merge_requests": 4,
  "assigned_issues": 15,
  "assigned_merge_requests": 11,
  "review_requested_merge_requests": 0,
  "todos": 1
}
```


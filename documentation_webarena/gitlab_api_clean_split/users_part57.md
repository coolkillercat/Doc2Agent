## Get user activities

DETAILS:
**Tier:** Free, Premium, Ultimate
**Offering:** Self-managed, GitLab Dedicated

Pre-requisite:

- You must be an administrator to view the activity of users with private profiles.

Get the last activity date for users with public profiles, sorted from oldest to newest.

The activities that update the user event timestamps (`last_activity_on` and `current_sign_in_at`) are:

- Git HTTP/SSH activities (such as clone, push)
- User logging in to GitLab
- User visiting pages related to dashboards, projects, issues, and merge requests ([introduced](https://gitlab.com/gitlab-org/gitlab-foss/-/issues/54947) in GitLab 11.8)
- User using the API
- User using the GraphQL API

By default, it shows the activity for users with public profiles in the last 6 months, but this can be
amended by using the `from` parameter.

```plaintext
GET /user/activities
```

Parameters:

| Attribute | Type   | Required | Description                                                                                    |
| --------- | ------ | -------- | ---------------------------------------------------------------------------------------------- |
| `from`    | string | no       | Date string in the format `YEAR-MM-DD`. For example, `2016-03-11`. Defaults to 6 months ago. |

```shell
curl --header "PRIVATE-TOKEN: <your_access_token>" "https://gitlab.example.com/api/v4/user/activities"
```

Example response:

```json
[
  {
    "username": "user1",
    "last_activity_on": "2015-12-14",
    "last_activity_at": "2015-12-14"
  },
  {
    "username": "user2",
    "last_activity_on": "2015-12-15",
    "last_activity_at": "2015-12-15"
  },
  {
    "username": "user3",
    "last_activity_on": "2015-12-16",
    "last_activity_at": "2015-12-16"
  }
]
```

`last_activity_at` is deprecated. Use `last_activity_on` instead.


## Promote an issue to an epic

DETAILS:
**Tier:** Premium, Ultimate
**Offering:** GitLab.com, Self-managed, GitLab Dedicated

Promotes an issue to an epic by adding a comment with the `/promote`
[quick action](../user/project/quick_actions.md).

For more information about promoting issues to epics, see
[Promote an issue to an epic](../user/project/issues/managing_issues.md#promote-an-issue-to-an-epic).

```plaintext
POST /projects/:id/issues/:issue_iid/notes
```

Supported attributes:

| Attribute   | Type           | Required | Description |
| :---------- | :------------- | :------- | :---------- |
| `id`        | integer/string | Yes      | The global ID or [URL-encoded path of the project](rest/index.md#namespaced-path-encoding) owned by the authenticated user. |
| `issue_iid` | integer        | Yes      | The internal ID of a project's issue. |
| `body`      | String         | Yes      | The content of a note. Must contain `/promote` at the start of a new line. If the note only contains `/promote`, promotes the issue, but doesn't add a comment. Otherwise, the other lines form a comment.|

Example request:

```shell
curl --request POST \
  --header "PRIVATE-TOKEN: <your_access_token>" \
  --url "https://gitlab.example.com/api/v4/projects/5/issues/11/notes?body=Lets%20promote%20this%20to%20an%20epic%0A%0A%2Fpromote"
```

Example response:

```json
{
   "id":699,
   "type":null,
   "body":"Lets promote this to an epic",
   "attachment":null,
   "author": {
      "id":1,
      "name":"Alexandra Bashirian",
      "username":"eileen.lowe",
      "state":"active",
      "avatar_url":"https://www.gravatar.com/avatar/e64c7d89f26bd1972efa854d13d7dd61?s=80&d=identicon",
      "web_url":"https://gitlab.example.com/eileen.lowe"
   },
   "created_at":"2020-12-03T12:27:17.844Z",
   "updated_at":"2020-12-03T12:27:17.844Z",
   "system":false,
   "noteable_id":461,
   "noteable_type":"Issue",
   "resolvable":false,
   "confidential":false,
   "noteable_iid":33,
   "commands_changes": {
      "promote_to_epic":true
   }
}
```


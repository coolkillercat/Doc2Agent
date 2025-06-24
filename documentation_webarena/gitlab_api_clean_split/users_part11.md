## Set user status

Set the status of the current user.

```plaintext
PUT /user/status
PATCH /user/status
```

| Attribute            | Type   | Required | Description                                                                                                                                                                                                             |
| -------------------- | ------ | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `emoji`              | string | no       | Name of the emoji to use as status. If omitted `speech_balloon` is used. Emoji name can be one of the specified names in the [Gemojione index](https://github.com/bonusly/gemojione/blob/master/config/index.json). |
| `message`            | string | no       | Message to set as a status. It can also contain emoji codes. Cannot exceed 100 characters.                                                                                                                                                      |
| `clear_status_after` | string | no       | Automatically clean up the status after a given time interval, allowed values: `30_minutes`, `3_hours`, `8_hours`, `1_day`, `3_days`, `7_days`, `30_days` |

Difference between `PUT` and `PATCH`

When using `PUT` any parameters that are not passed are set to `null` and therefore cleared. When using `PATCH` any parameters that are not passed are ignored. Explicitly pass `null` to clear a field.

```shell
curl --request PUT --header "PRIVATE-TOKEN: <your_access_token>" --data "clear_status_after=1_day" --data "emoji=coffee" \
     --data "message=I crave coffee" "https://gitlab.example.com/api/v4/user/status"
```

Example responses

```json
{
  "emoji":"coffee",
  "message":"I crave coffee",
  "message_html": "I crave coffee",
  "clear_status_at":"2021-02-15T10:49:01.311Z"
}
```


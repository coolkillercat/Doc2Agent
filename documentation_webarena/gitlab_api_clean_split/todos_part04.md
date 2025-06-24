## Mark all to-do items as done

Marks all pending to-do items for the current user as done. It returns the HTTP status code `204` with an empty response.

```plaintext
POST /todos/mark_as_done
```

```shell
curl --request POST --header "PRIVATE-TOKEN: <your_access_token>" "https://gitlab.example.com/api/v4/todos/mark_as_done"
```

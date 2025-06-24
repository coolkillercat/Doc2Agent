## Issues pagination

By default, `GET` requests return 20 results at a time because the API results
are paginated.
Read more on [pagination](rest/index.md#pagination).

NOTE:
The `references.relative` attribute is relative to the group or project of the issue being requested.
When an issue is fetched from its project, the `relative` format is the same as the `short` format.
When requested across groups or projects, it's expected to be the same as the `full` format.


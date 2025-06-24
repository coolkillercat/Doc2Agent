## Responses

Some date fields in responses from this API are, or can appear to be, duplicated
information:

- The `created_at` field exists solely for consistency with other GitLab APIs. It
  is always identical to the `committed_date` field.
- The `committed_date` and `authored_date` fields are generated from different sources,
  and may not be identical.


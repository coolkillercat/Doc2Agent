## Remove group

> - Immediately deleting subgroups was [introduced](https://gitlab.com/gitlab-org/gitlab/-/issues/360008) in GitLab 15.3 [with a flag](../administration/feature_flags.md) named `immediate_delete_subgroup_api`. Disabled by default.
> - Immediately deleting subgroups was [enabled on GitLab.com and self-managed](https://gitlab.com/gitlab-org/gitlab/-/issues/368276) in GitLab 15.4.
> - Immediately deleting subgroups was [enabled](https://gitlab.com/gitlab-org/gitlab/-/issues/368276) by default in GitLab 15.4.
> - The flag `immediate_delete_subgroup_api` for immediately deleting subgroups was [removed](https://gitlab.com/gitlab-org/gitlab/-/issues/374069) in GitLab 15.9.

Only available to group owners and administrators.

This endpoint:

- On Premium and Ultimate tiers, marks the group for deletion. The deletion happens 7 days later by default, but you can change the retention period in the [instance settings](../administration/settings/visibility_and_access_controls.md#deletion-protection).
- On Free tier, removes the group immediately and queues a background job to delete all projects in the group.
- Deletes a subgroup immediately if the subgroup is marked for deletion (GitLab 15.4 and later). The endpoint does not immediately delete top-level groups.

```plaintext
DELETE /groups/:id
```

Parameters:

| Attribute            | Type             | Required | Description                                                                                                                                                 |
|----------------------|------------------|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `id`                 | integer/string   | yes      | The ID or [URL-encoded path of the group](rest/index.md#namespaced-path-encoding)                                                                                |
| `permanently_remove` | boolean/string   | no       | Immediately deletes a subgroup if it is marked for deletion. [Introduced](https://gitlab.com/gitlab-org/gitlab/-/issues/368276) in GitLab 15.4. Premium and Ultimate only. |
| `full_path`   | string           | no       | Full path of subgroup to use with `permanently_remove`. [Introduced](https://gitlab.com/gitlab-org/gitlab/-/issues/368276) in GitLab 15.4. To find the subgroup path, see the [group details](groups.md#details-of-a-group). Premium and Ultimate only. |

The response is `202 Accepted` if the user has authorization.

NOTE:
A GitLab.com group can't be removed if it is linked to a subscription. To remove such a group, first [link the subscription](../subscriptions/gitlab_com/index.md#change-the-linked-namespace) with a different group.


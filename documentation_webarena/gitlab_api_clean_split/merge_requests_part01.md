---
stage: Create
group: Code Review
info: To determine the technical writer assigned to the Stage/Group associated with this page, see https://handbook.gitlab.com/handbook/product/ux/technical-writing/#assignments
description: "Documentation for the REST API for merge requests in GitLab."
---

# Merge requests API

DETAILS:
**Tier:** Free, Premium, Ultimate
**Offering:** GitLab.com, Self-managed, GitLab Dedicated

> - `reference` was [deprecated](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/20354) in GitLab 12.7.
> - `merged_by` was [deprecated](https://gitlab.com/gitlab-org/gitlab/-/issues/350534) in GitLab 14.7.
> - `merge_status` was [deprecated](https://gitlab.com/gitlab-org/gitlab/-/issues/3169#note_1162532204) in favor of `detailed_merge_status` in GitLab 15.6.
> - `with_merge_status_recheck` [changed](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/115948) in GitLab 15.11  [with a flag](../administration/feature_flags.md) named `restrict_merge_status_recheck` to be ignored for requests from users insufficient permissions. Disabled by default.
> - `approvals_before_merge` was [deprecated](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/119503) in GitLab 16.0.
> - `prepared_at` was [introduced](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/122001) in GitLab 16.1.

Authentication is required for API calls to non-public information.


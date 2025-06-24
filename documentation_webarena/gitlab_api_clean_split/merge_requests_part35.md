## Troubleshooting

### Empty API fields for new merge requests

When a merge request is created, the `diff_refs` and `changes_count` fields are
initially empty. These fields are populated asynchronously after the
merge request is created. For more information, see the issue
[Some merge request API fields (`diff_refs`, `changes_count`) empty after MR is created](https://gitlab.com/gitlab-org/gitlab/-/issues/386562),
and the [related discussion](https://forum.gitlab.com/t/diff-refs-empty-after-mr-is-created/78975)
in the GitLab forums.

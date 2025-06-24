## Project merge method

The `merge_method` can use these options:

- `merge`: a merge commit is created for every merge, and merging is allowed if
 no conflicts are present.
- `rebase_merge`: a merge commit is created for every merge, but merging is only
  allowed if fast-forward merge is possible. You can make sure that the target
  branch would build after this merge request builds and merges.
- `ff`: no merge commits are created and all merges are fast-forwarded. Merging
  is only allowed if the branch could be fast-forwarded.


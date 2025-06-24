## Fork project

Forks a project into the user namespace of the authenticated user or the one provided.

The forking operation for a project is asynchronous and is completed in a
background job. The request returns immediately. To determine whether the
fork of the project has completed, query the `import_status` for the new project.

```plaintext
POST /projects/:id/fork
```

| Attribute                | Type              | Required | Description |
|--------------------------|-------------------|----------|-------------|
| `id`                     | integer or string | Yes      | The ID or [URL-encoded path of the project](rest/index.md#namespaced-path-encoding). |
| `branches`               | string            | No       | Branches to fork (empty for all branches). |
| `description`            | string            | No       | The description assigned to the resultant project after forking. |
| `mr_default_target_self` | boolean           | No       | For forked projects, target merge requests to this project. If `false`, the target is the upstream project. |
| `name`                   | string            | No       | The name assigned to the resultant project after forking. |
| `namespace_id`           | integer           | No       | The ID of the namespace that the project is forked to. |
| `namespace_path`         | string            | No       | The path of the namespace that the project is forked to. |
| `namespace`              | integer or string | No       | _(Deprecated)_ The ID or path of the namespace that the project is forked to. |
| `path`                   | string            | No       | The path assigned to the resultant project after forking. |
| `visibility`             | string            | No       | The [visibility level](#project-visibility-level) assigned to the resultant project after forking. |


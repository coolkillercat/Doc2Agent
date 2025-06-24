## LDAP Group Links

List, add, and delete LDAP group links.

### List LDAP group links

DETAILS:
**Tier:** Premium, Ultimate
**Offering:** Self-managed

Lists LDAP group links.

```plaintext
GET /groups/:id/ldap_group_links
```

| Attribute | Type           | Required | Description |
| --------- | -------------- | -------- | ----------- |
| `id`      | integer/string | yes      | The ID or [URL-encoded path of the group](rest/index.md#namespaced-path-encoding) |

### Add LDAP group link with CN or filter

DETAILS:
**Tier:** Premium, Ultimate
**Offering:** Self-managed

Adds an LDAP group link using a CN or filter. Adding a group link by filter is only supported in the Premium and Ultimate tier.

```plaintext
POST /groups/:id/ldap_group_links
```

| Attribute | Type           | Required | Description |
| --------- | -------------- | -------- | ----------- |
| `id`      | integer/string | yes      | The ID or [URL-encoded path of the group](rest/index.md#namespaced-path-encoding) |
| `cn`      | string         | no       | The CN of an LDAP group |
| `filter`  | string         | no       | The LDAP filter for the group |
| `group_access` | integer   | yes      | [Role (`access_level`)](members.md#roles) for members of the LDAP group |
| `provider` | string        | yes      | LDAP provider for the LDAP group link |

NOTE:
To define the LDAP group link, provide either a `cn` or a `filter`, but not both.

### Delete LDAP group link

DETAILS:
**Tier:** Premium, Ultimate
**Offering:** Self-managed

Deletes an LDAP group link. Deprecated. Scheduled for removal in a future release.

```plaintext
DELETE /groups/:id/ldap_group_links/:cn
```

| Attribute | Type           | Required | Description |
| --------- | -------------- | -------- | ----------- |
| `id`      | integer/string | yes      | The ID or [URL-encoded path of the group](rest/index.md#namespaced-path-encoding) |
| `cn`      | string         | yes      | The CN of an LDAP group |

Deletes an LDAP group link for a specific LDAP provider. Deprecated. Scheduled for removal in a future release.

```plaintext
DELETE /groups/:id/ldap_group_links/:provider/:cn
```

| Attribute | Type           | Required | Description |
| --------- | -------------- | -------- | ----------- |
| `id`      | integer/string | yes      | The ID or [URL-encoded path of the group](rest/index.md#namespaced-path-encoding) |
| `cn`      | string         | yes      | The CN of an LDAP group |
| `provider` | string        | yes      | LDAP provider for the LDAP group link |

### Delete LDAP group link with CN or filter

DETAILS:
**Tier:** Premium, Ultimate
**Offering:** Self-managed

Deletes an LDAP group link using a CN or filter. Deleting by filter is only supported in the Premium and Ultimate tier.

```plaintext
DELETE /groups/:id/ldap_group_links
```

| Attribute | Type           | Required | Description |
| --------- | -------------- | -------- | ----------- |
| `id`      | integer/string | yes      | The ID or [URL-encoded path of the group](rest/index.md#namespaced-path-encoding) |
| `cn`      | string         | no       | The CN of an LDAP group |
| `filter`  | string         | no       | The LDAP filter for the group |
| `provider` | string        | yes       | LDAP provider for the LDAP group link |

NOTE:
To delete the LDAP group link, provide either a `cn` or a `filter`, but not both.


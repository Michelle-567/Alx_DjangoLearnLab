# Managing Permissions and Groups

This Django project demonstrates the use of custom permissions and groups.

## Permissions

Defined in `Article` model:
- `can_view`
- `can_create`
- `can_edit`
- `can_delete`

## Groups and Permissions

| Group   | Permissions             |
|---------|-------------------------|
| Viewers | can_view                |
| Editors | can_view, can_create, can_edit |
| Admins  | All permissions         |

## Testing

Create users and assign to groups via Django admin. Try accessing views that require permissions.

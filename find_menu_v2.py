# Try finding by XML ID
try:
    menu = env.ref('base.menu_action_res_groups')
    print(f"Found by XML ID: {menu.name} (ID: {menu.id})")
    print(f"  Parent: {menu.parent_id.complete_name}")
    print(f"  Groups: {menu.groups_id.mapped('name')}")
except Exception as e:
    print(f"Could not find 'base.menu_action_res_groups': {e}")

print("-" * 20)

# List all children of 'Users & Companies'
# First find 'Users & Companies'
parents = env['ir.ui.menu'].search([('name', 'ilike', 'Users & Companies')])
for p in parents:
    print(f"Parent Menu: {p.name} (ID: {p.id}) Path: {p.complete_name}")
    children = env['ir.ui.menu'].search([('parent_id', '=', p.id)])
    for child in children:
        print(f"  - Child: {child.name} (ID: {child.id}) Action: {child.action}")

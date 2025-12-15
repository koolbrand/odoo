# Search for the menu item pointing to res.groups
menus = env['ir.ui.menu'].search([('name', 'ilike', 'Groups')])
for menu in menus:
    print(f"Menu: {menu.name} (ID: {menu.id})")
    print(f"  Parent: {menu.parent_id.complete_name}")
    print(f"  Action: {menu.action}")
    print(f"  Groups: {menu.groups_id.mapped('name')}")
    
    # Check if admin has access
    user = env.ref('base.user_admin')
    has_access = True
    if menu.groups_id and not (menu.groups_id & user.groups_id):
        has_access = False
    print(f"  Admin has access? {has_access}")
    print("-" * 20)

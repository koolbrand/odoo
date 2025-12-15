def setup_crm_group(env):
    # 1. Find or Create Group
    group_name = 'CRM Solo'
    group = env['res.groups'].search([('name', '=', group_name)], limit=1)
    
    if not group:
        group = env['res.groups'].create({'name': group_name})
        env.cr.commit()
        print(f"Created group: {group.name}")
    else:
        print(f"Found group: {group.name}")

    # 2. Find User
    user = env['res.users'].search([('login', '=', 'plantilla@koolgrowth.com')], limit=1)
    if not user:
        print("User 'plantilla@koolgrowth.com' not found!")
        return

    # 3. Add User to Group (SQL Fallback)
    # ORM is failing with 'groups_id' issue, so we use direct SQL
    sql = "INSERT INTO res_groups_users_rel (gid, uid) VALUES (%s, %s) ON CONFLICT DO NOTHING"
    env.cr.execute(sql, (group.id, user.id))
    env.cr.commit()
    print(f"Added user {user.name} to group {group.name} (via SQL)")

    # 4. Verify Record Rule
    # Check if the rule "Ocultar Contactos Ajenos" exists and is linked to this group
    rule = env['ir.rule'].search([('name', '=', 'Ocultar Contactos Ajenos')], limit=1)
    if rule:
        print(f"Found Record Rule: {rule.name}")
        # Ensure rule is linked to group
        if group not in rule.groups:
            rule.write({'groups': [(4, group.id)]})
            env.cr.commit()
            print("Linked Record Rule to Group")
        else:
            print("Record Rule already linked to Group")
    else:
        print("Record Rule 'Ocultar Contactos Ajenos' not found. Please create it manually.")

if __name__ == '__main__':
    setup_crm_group(env)

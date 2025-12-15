def fix_crm_visibility(env):
    # 1. Find Group
    group = env['res.groups'].search([('name', '=', 'CRM Solo')], limit=1)
    if not group:
        print("Group 'CRM Solo' not found. Please run setup_crm_group.py first.")
        return

    # 2. Find/Create Record Rule for CRM Lead
    rule_name = 'Ver Mis Leads (Cliente)'
    model = env.ref('crm.model_crm_lead')
    
    rule = env['ir.rule'].search([('name', '=', rule_name), ('model_id', '=', model.id)], limit=1)
    
    # Domain: Show if I am the salesperson OR if I am the customer (or it belongs to my company)
    domain = "['|', ('user_id', '=', user.id), ('partner_id', 'child_of', [user.partner_id.id])]"
    
    vals = {
        'name': rule_name,
        'model_id': model.id,
        'domain_force': domain,
        'groups': [(4, group.id)], # Add to CRM Solo group
        'perm_read': True,
        'perm_write': True,
        'perm_create': True,
        'perm_unlink': True,
    }

    if not rule:
        rule = env['ir.rule'].create(vals)
        print(f"Created Rule: {rule.name}")
    else:
        rule.write(vals)
        print(f"Updated Rule: {rule.name}")

    env.cr.commit()

if __name__ == '__main__':
    fix_crm_visibility(env)

# Inspect Record Rules for CRM Lead
model_name = 'crm.lead'
rules = env['ir.rule'].search([('model_id.model', '=', model_name)])

print(f"--- Rules for {model_name} ---")
for rule in rules:
    # Check if it applies to our relevant groups
    relevant = False
    for g in rule.groups:
        if g.name in ['Sales/User: Own Documents Only', 'CRM Solo', 'Internal User']:
            relevant = True
    
    if relevant or not rule.groups: # Global rules are important
        print(f"Rule: {rule.name}")
        print(f"  Domain: {rule.domain_force}")
        print(f"  Groups: {rule.groups.mapped('name')}")
        print("-" * 10)

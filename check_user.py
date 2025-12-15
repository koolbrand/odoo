users = env['res.users'].search([('login', '=', 'plantilla@koolgrowth.com')])
for u in users:
    print(f"User: {u.name}, ID: {u.id}")
    try:
        print(f"Groups: {u.groups_id.mapped('name')}")
    except Exception as e:
        print(f"Could not read groups: {e}")

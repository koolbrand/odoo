from odoo import api, SUPERUSER_ID
import sys

def create_template_user(env):
    # 1. Create User
    user_vals = {
        'name': 'PLANTILLA CLIENTE',
        'login': 'plantilla@koolgrowth.com',
        'password': 'template123',
        'active': True,
        'email': 'plantilla@koolgrowth.com',
    }
    
    existing = env['res.users'].search([('login', '=', user_vals['login'])])
    if existing:
        print(f"User exists: {existing.id}")
        return

    user = env['res.users'].create(user_vals)
    env.cr.commit() # Commit creation immediately!
    print(f"User created: {user.id}")

    # 2. Try to set permissions
    try:
        group_salesman = env.ref('sales_team.group_sale_salesman')
        # Try adding to Sales group
        user.write({'groups_id': [(4, group_salesman.id)]})
        env.cr.commit()
        print("Permissions updated: Added to Sales (Own Documents)")
    except Exception as e:
        print(f"Could not set permissions automatically: {e}")
        print("Please set permissions manually.")

if __name__ == '__main__':
    create_template_user(env)

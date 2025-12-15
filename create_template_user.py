from odoo import api, SUPERUSER_ID
import sys

def create_template_user(env):
    # 1. Define User Data
    user_vals = {
        'name': 'PLANTILLA CLIENTE',
        'login': 'plantilla@koolgrowth.com',
        'password': 'template123',
        'active': True,
        'email': 'plantilla@koolgrowth.com',
    }
    
    # 2. Check if exists
    existing = env['res.users'].search([('login', '=', user_vals['login'])])
    if existing:
        print(f"User {existing.name} already exists (ID: {existing.id}).")
        return

    # 3. Create User
    user = env['res.users'].create(user_vals)
    print(f"User {user.name} created with ID {user.id}")

    # 4. Set Permissions
    # Use sudo() to bypass potential access rights issues when writing to groups_id
    group_user = env.ref('base.group_user')
    group_salesman = env.ref('sales_team.group_sale_salesman')
    
    # Set groups explicitly using the Many2many command
    # (6, 0, [ids]) replaces all existing groups with the new list
    user.sudo().write({
        'groups_id': [(6, 0, [group_user.id, group_salesman.id])]
    })
    
    print("Permissions set: Internal User + Sales (Own Documents)")
    print("Login: plantilla@koolgrowth.com")
    print("Password: template123")

if __name__ == '__main__':
    create_template_user(env)
    env.cr.commit()

{
    'name': 'Odoo OCR Customizations',
    'version': '1.1',
    'category': 'Human Resources/Expenses',
    'summary': 'Adds Base Imponible to Expense views and Ticket image report',
    'depends': ['hr_expense'],
    'data': [
        'views/hr_expense_views.xml',
        'report/hr_expense_report_tickets.xml',
    ],
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
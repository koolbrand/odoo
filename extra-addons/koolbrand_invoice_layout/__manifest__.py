{
    'name': 'Koolbrand Invoice Layout',
    'version': '1.0',
    'category': 'Accounting/Localizations',
    'summary': 'Custom Invoice Layout for Brand Experience YA',
    'description': """
        This module provides a specific invoice layout for Brand Experience YA.
        It overrides the standard invoice report to apply:
        - Custom green headers (#A3D16D)
        - Montserrat font
        - Specific table layout
    """,
    'author': 'Koolgrowth',
    'depends': ['account', 'web'],
    'data': [
        'data/report_layout.xml',
        'views/report_invoice.xml',
    ],
    'installable': True,
    'auto_install': False,
    'license': 'In-House',
}
{

    'name': 'Furniture Shop Management',
    'version': '1.0',
    'depends': [
        'base',
        'purchase', # Restore this
        'mail',
        'product',
        'sale_management'
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/furniture_product_views.xml',
        'views/appointment_views.xml',
        'views/menu.xml',
        'reports/appointment_report.xml',
        'reports/appointment_report_template.xml',
    ],
    'depends': [
        'base', 'purchase', 'mail', 'product', 'sale_management'
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
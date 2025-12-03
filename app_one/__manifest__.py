{
    'name': "Real Estate",
    'version': "18.0.1.0.0",

    'author': "Ahmed Abdulghany",
    'category': "Inventory/Inventory",

    'depends': ['base','product', 'stock'],
    'data': [
        'security/ir.model.access.csv',
        'views/product_category_views.xml',
    ],

    'demo': [],

    'assets': {},

    'application': True,
    'auto_install': False,
    'license': "LGPL-3",
}
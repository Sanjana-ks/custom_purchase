# -*- coding: utf-8 -*-

{
    'name': 'Custom Purchase',
    'version': '1.1',
    'sequence': '1',
    'category': 'Training',
    'summary': 'Learning Odoo',
    'description': 'This is the practice module on working with odoo ',
    'depends': ["base", 'purchase'],
    'data': [
        "security/ir.model.access.csv",
        "views/custom_purchase_order_line_view.xml",
        "views/custom_vendor_bill_line_view.xml",
        "wizards/product_wizard.xml",
        "reports/report.xml"
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
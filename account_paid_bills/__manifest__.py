# -*- coding: utf-8 -*-

{
    'name' : 'Account Paid Bills',
    'version' : '1.0',
    # 'category': '',
    'depends' : ['account',],
    'data': [
        'security/ir.model.access.csv',
        'wizards/paid_bills_views.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}

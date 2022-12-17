# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'POS Gift Receipt',
    'version': '1.0',
    'category': 'Sales/Point of Sale',
    'sequence': 6,
    'summary': 'Impresion de ticket de regalo ',
    'description': """
    'author': "Expertha(Nestor Ulloa)",
    Impresion de ticket de regalo
    
    """,
    'depends': ['point_of_sale', 'custom_pos_receipt', 'pos_discount', 'pos_restaurant'],
    'data': [
        'views/pos_git_receipt_views.xml',
        ],
    'installable': True,
    'assets': {
        'point_of_sale.assets': [
            'pos_gift_receipt/static/src/js/**/*',
        ],
        'web.assets_qweb': [
            'pos_gift_receipt/static/src/xml/**/*',
        ],
    },
    'license': 'LGPL-3',
}

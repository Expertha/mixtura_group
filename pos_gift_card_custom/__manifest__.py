# -*- coding: utf-8 -*-
{
    'name': "Reporte customizado de gift card",
    'summary': """Reporte customizado de gift card""",
    'description': """
    Reporte customizado de gift card
        """,
    'author': "Expertha(Nestor Ulloa)",
    'website': "",
    'license': 'GPL-3',
    'category': 'Localization',
    'version': '1.1',
    'depends': ['base', 'point_of_sale', 'gift_card', 'pos_gift_card'],
    'data': [
        'views/gift_card_template_custom.xml',
        'views/gift_card_paper_custom.xml',
    ],
    'assets': {
        'point_of_sale.assets': [
            'pos_gift_card_custom/static/src/js/models.js',
        ],
    },
    'demo': [
    ],
    'installable': True,
    'application': False,
    'auto_install': True,

}

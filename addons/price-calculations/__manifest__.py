# -*- coding: utf-8 -*-
{
    'name': "price-calculations",
    'summary': """
        Modifies the way prices are calculated""",
    'description': """
        Changes pricing calculations to:
            sales_price = price_per_pair * pairs_per_case
    """,
    'category': 'Custom',
    'version': '0.1',
    'depends': ['base', 'product'],
    'data': ['views/product_template_views.xml'],
    'demo': [],
}

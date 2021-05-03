# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductTemplateInherit(models.Model):
    _inherit = 'product.template'

    list_price = fields.Float(
        string='Sales Price',
        help='Price at which the product is sold to customers.',
        compute='_compute_sales_price',
        inverse='_inverse_sales_price',
        readonly=False,
        store=True)
    pairs_per_case = fields.Integer(string='Pairs per Case')
    price_per_pair = fields.Monetary(string='Price per Pair')

    @api.depends('pairs_per_case', 'price_per_pair')
    def _compute_sales_price(self):
        for record in self:
            record.list_price = record.pairs_per_case * record.price_per_pair
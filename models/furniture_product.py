# -*- coding: utf-8 -*-
from odoo import models, fields


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    # Boolean to identify furniture products in our shop
    is_furniture = fields.Boolean(string="Is Furniture", default=True)

    # Custom category for our furniture shop
    furniture_category = fields.Selection([
        ('chair', 'Chair'),
        ('table', 'Table'),
        ('sofa', 'Sofa'),
        ('bed', 'Bed')
    ], string='Furniture Type', default='chair')
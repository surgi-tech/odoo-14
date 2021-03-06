from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    is_medical = fields.Boolean(string="Medical Product", default=False)
    is_tool = fields.Boolean(string="Is Tool", default=False)
    standard_default_code = fields.Char(string='Standard Internal Reference')
    product_group = fields.Char (srting="Group")
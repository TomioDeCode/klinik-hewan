from odoo import fields, models

class ProductInherit(models.Model):
    _inherit = "product.product"

    commission = fields.Float(
        string="Commission (%)",
        related="product_tmpl_id.commission",
        store=True,
    )


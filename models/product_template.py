from odoo import fields, models


class ProductInherit(models.Model):
    _inherit = "product.template"

    jenis_product = fields.Selection(
        [
            ("product", "Product"),
            ("layanan", "Layanan"),
            ("obat", "Obat"),
        ],
        string="Jenis Product",
        required=True,
        default="product",
    )

    commission = fields.Float(
        string="Commission (%)",
        default=0.0,
        help="Commission percentage for the product or service."
    )

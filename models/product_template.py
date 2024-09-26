from odoo import fields, models, api


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
        help="Commission percentage for the product or service.",
    )

    @api.model
    def get_service_sales(self):
        services = self.env["product.template"].search(
            [("jenis_product", "=", "layanan")]
        )

        sales_data = []

        for service in services:
            sale_lines = self.env["sale.order.line"].search(
                [("product_id", "=", service.id)]
            )

            total_sales = 0.0
            total_commission = 0.0

            for line in sale_lines:
                total_sales += line.price_total
                total_commission += (
                    line.price_total * service.commission / 100
                )

            sales_data.append(
                {
                    "service": service.name,
                    "total_sales": total_sales,
                    "commission": total_commission,
                }
            )

        return sales_data

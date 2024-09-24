from odoo import models, fields, api


class KlinikResep(models.Model):
    _name = "klinik.resep"

    name = fields.Char(string="Resep", required=True)

    product_id = fields.Many2many(
        "product.template",
        string="Product",
        domain="[('jenis_product', '=', 'product')]",
        required=True,
        relation="klinik_resep_product_rel",  # Unique relation table name
    )
    obat_id = fields.Many2many(
        "product.template",
        string="Obat",
        domain="[('jenis_product', '=', 'obat')]",
        required=True,
        relation="klinik_resep_obat_rel",  # Unique relation table name
    )
    layanan_id = fields.Many2many(
        "product.template",
        string="Layanan",
        domain="[('jenis_product', '=', 'layanan')]",
        required=True,
        relation="klinik_resep_layanan_rel",  # Unique relation table name
    )

    total_price = fields.Float(compute="_compute_total_price", string="Total Price")

    @api.depends("product_id", "obat_id", "layanan_id")
    def _compute_total_price(self):
        for record in self:
            total = (
                sum(product.list_price for product in record.product_id)
                + sum(obat.list_price for obat in record.obat_id)
                + sum(layanan.list_price for layanan in record.layanan_id)
            )
            record.total_price = total

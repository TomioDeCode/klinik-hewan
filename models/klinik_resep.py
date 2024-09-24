from odoo import models, fields, api


class KlinikResep(models.Model):
    _name = "klinik.resep"

    name = fields.Char(string="Resep", required=True)
    dokter_id = fields.Many2one('klinik.dokter', string="Dokter")

    product_id = fields.Many2many(
        "product.template",
        string="Product",
        domain="[('jenis_product', '=', 'product')]",
        required=True,
        relation="klinik_resep_product_rel",
    )
    obat_id = fields.Many2many(
        "product.template",
        string="Obat",
        domain="[('jenis_product', '=', 'obat')]",
        required=True,
        relation="klinik_resep_obat_rel",
    )
    layanan_id = fields.Many2many(
        "product.template",
        string="Layanan",
        domain="[('jenis_product', '=', 'layanan')]",
        required=True,
        relation="klinik_resep_layanan_rel",
    )

    total_price = fields.Float(compute="_compute_total_price", string="Total Price")
    commission_amount = fields.Float(
        compute="_compute_commission_amount", string="Commission Amount"
    )
    final_price = fields.Float(compute="_compute_final_price", string="Final Price")

    @api.depends("product_id", "obat_id", "layanan_id")
    def _compute_total_price(self):
        for record in self:
            total = (
                sum(product.list_price for product in record.product_id)
                + sum(obat.list_price for obat in record.obat_id)
                + sum(layanan.list_price for layanan in record.layanan_id)
            )
            record.total_price = total

    @api.depends(
        "product_id.commission",
        "obat_id.commission",
        "layanan_id.commission",
        "total_price",
    )
    def _compute_commission_amount(self):
        for record in self:
            commission = 0.0
            for product in record.product_id:
                commission += (product.commission * product.list_price) / 100
            for obat in record.obat_id:
                commission += (obat.commission * obat.list_price) / 100
            for layanan in record.layanan_id:
                commission += (layanan.commission * layanan.list_price) / 100
            record.commission_amount = commission

    @api.depends("total_price", "commission_amount")
    def _compute_final_price(self):
        for record in self:
            record.final_price = record.total_price - record.commission_amount

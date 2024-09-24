from odoo import fields, models, api


class KlinikDokter(models.Model):
    _name = "klinik.dokter"

    name = fields.Many2one(
        "res.partner", domain="[('klinik_member', '=', 'dokter')]", string="Dokter"
    )
    phone = fields.Char(string="Telepon", required=True)
    email = fields.Char(string="Email", required=True)
    alamat = fields.Text(string="Alamat", required=False)

    klinik_resep_ids = fields.One2many("klinik.resep", "dokter_id", string="Reseps")

    appointment_id = fields.One2many(
        "klinik.appointment", "dokter_id", string="Janji Temu"
    )

    commission_amount = fields.Float(
        compute="_compute_commission_amount", string="Commission Total", store=True
    )

    @api.onchange("name")
    def _onchange_name(self):
        if self.name:
            self.phone = self.name.phone
            self.email = self.name.email
            if (
                self.name.street
                or self.name.city
                or self.name.state_id.name
                or self.name.zip
                or self.name.country_id.name
            ):
                self.alamat = f"{self.name.street or ''}, {self.name.city or ''}, {self.name.state_id.name or ''}, {self.name.zip or ''}, {self.name.country_id.name or ''}"
            else:
                self.alamat = False

    @api.depends("klinik_resep_ids.commission_amount")
    def _compute_commission_amount(self):
        for doctor in self:
            total_commission = sum(
                resep.commission_amount
                for resep in doctor.klinik_resep_ids
                if resep.dokter_id == doctor
            )
            doctor.commission_amount = total_commission

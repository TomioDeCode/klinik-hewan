from odoo import fields, models, api
from odoo.exceptions import UserError


class KlinikDokter(models.Model):
    _name = "klinik.dokter"

    name = fields.Many2one(
        "res.partner", domain="[('klinik_member', '=', 'dokter')]", string="Dokter"
    )
    phone = fields.Char(string="Telepon", required=True)
    email = fields.Char(string="Email", required=True)
    alamat = fields.Text(string="Alamat", required=False)

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

    appointment_id = fields.One2many(
        "klinik.appointment", "dokter_id", string="Janji Temu"
    )

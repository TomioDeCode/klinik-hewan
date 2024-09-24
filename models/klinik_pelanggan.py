from odoo import models, fields, api
from odoo.exceptions import UserError


class KlinikPelanggan(models.Model):
    _name = "klinik.pelanggan"

    partner_id = fields.Many2one("res.partner", string="Contact")
    name = fields.Many2one("res.partner", string="Name", required=True)
    email = fields.Char(string="Email", required=True)
    phone = fields.Char(string="Phone", required=True)
    alamat = fields.Text(string="Alamat", required=False)
    pet_ids = fields.Many2many("klinik.hewan", "pemilik", string="Hewan")

    @api.onchange("name")
    def _onchange_name(self):
        if self.name:
            self.partner_id = self.name
            self.email = self.name.email
            self.phone = self.name.phone
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

    def redirect_appoiment(self):
        if not self.pet_ids:
            raise UserError("Tidak ada hewan peliharaan yang terkait dengan klien ini.")

        return {
            "type": "ir.actions.act_window",
            "name": "Create Appointment",
            "res_model": "klinik.appointment",
            "view_mode": "form",
            "target": "new",
            "context": {
                "default_partner_id": self.partner_id.id,
                "default_pet_id": self.pet_ids[0].id if self.pet_ids else False,
            },
        }

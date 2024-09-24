from odoo import models, fields, api

class KlinikAppointment(models.Model):
    _name = "klinik.appointment"
    _description = "Appointment for Pet Clinic"

    name = fields.Char(string="Appointment Reference", required=True, default="New")
    partner_id = fields.Many2one("res.partner", string="Customer", required=True)
    pet_id = fields.Many2one("klinik.hewan", string="Pet", required=True)
    appointment_date = fields.Datetime(string="Appointment Date", required=True)
    notes = fields.Text(string="Notes")
    state = fields.Selection(
        [
            ("draft", "Draft"),
            ("confirmed", "Confirmed"),
            ("done", "Done"),
            ("cancelled", "Cancelled"),
        ],
        default="draft",
        string="Status",
        required=True,
    )

    @api.model
    def create(self, vals):
        if vals.get("name", "New") == "New":
            vals["name"] = (
                self.env["ir.sequence"].next_by_code("klinik.appointment") or "New"
            )
        return super(KlinikAppointment, self).create(vals)

    def action_confirm(self):
        self.write({"state": "confirmed"})

    def action_done(self):
        self.write({"state": "done"})

    def action_cancel(self):
        self.write({"state": "cancelled"})

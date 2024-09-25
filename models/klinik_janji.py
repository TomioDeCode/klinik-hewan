from odoo import models, fields, api
from odoo.exceptions import UserError
from datetime import timedelta


class KlinikAppointment(models.Model):
    _name = "klinik.appointment"
    _description = "Appointment for Pet Clinic"

    name = fields.Char(string="Appointment Reference", required=True, default="New")
    partner_id = fields.Many2one("res.partner", string="Customer", required=True)
    pet_id = fields.Many2one("klinik.hewan", string="Pet", required=True)
    dokter_id = fields.Many2one("klinik.dokter", string="Dokter", required=True)
    appointment_date = fields.Datetime(string="Appointment Date", required=True)
    room_id = fields.Many2one(
        "klinik.ruangan", string="Room"
    )
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

    @api.onchange("pet_id")
    def _onchange_pet_id(self):
        if self.pet_id:
            self.partner_id = self.pet_id.pemilik

    @api.model
    def create(self, vals):
        if vals.get("name", "New") == "New":
            vals["name"] = (
                self.env["ir.sequence"].next_by_code("klinik.appointment") or "New"
            )
        return super(KlinikAppointment, self).create(vals)

    def action_confirm(self):
        if self.room_id and not self.room_id.check_availability(self.appointment_date):
            raise UserError("The selected room is not available at this time.")
        self.room_id.book_room(
            self.appointment_date + timedelta(hours=1)
        )
        self.write({"state": "confirmed"})

    def action_done(self):
        if self.room_id:
            self.room_id.free_room()
        self.write({"state": "done"})

    def action_cancel(self):
        if self.room_id:
            self.room_id.free_room()
        self.write({"state": "cancelled"})

    @api.model
    def count_janji(self):
        return self.search_count([])

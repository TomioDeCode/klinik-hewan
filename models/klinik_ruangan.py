from odoo import models, fields, api
from odoo.exceptions import UserError


class KlinikRuangan(models.Model):
    _name = "klinik.ruangan"
    _description = "Room for Pet Clinic"

    name = fields.Char(string="Appointment Reference", required=True, default="New")
    is_available = fields.Boolean(string="Is Available", default=True)
    unavailable_until = fields.Datetime(string="Unavailable Until")

    def check_availability(self, appointment_date):
        if not self.is_available or (
            self.unavailable_until and self.unavailable_until > appointment_date
        ):
            return False
        return True

    def book_room(self, end_time):
        self.write({"is_available": False, "unavailable_until": end_time})

    def free_room(self):
        self.write({"is_available": True, "unavailable_until": False})

from odoo import http
from odoo.http import request


class JanjiController(http.Controller):
    @http.route("/get/janji/data", type="json", auth="user")
    def get_client_data(self):
        count = request.env["klinik.appointment"].count_janji()
        return {"count": count}

    @http.route("/janji/day", type="json", auth="user")
    def get_appointments(self, day_offset=0):
        try:
            day_offset = int(day_offset)
            appointments = request.env["klinik.appointment"].get_appointments_for_day(
                day_offset
            )
            appointment_data = []
            for appointment in appointments:
                appointment_data.append(
                    {
                        "name": appointment.name,
                        "customer": appointment.partner_id.name,
                        "pet": appointment.pet_id.name,
                        "dokter": appointment.dokter_id.name.name,
                        "appointment_date": appointment.appointment_date,
                        "room": appointment.room_id.name,
                        "status": appointment.state,
                    }
                )
            return {"status": "success", "appointments": appointment_data}

        except Exception as e:
            return {"status": "error", "message": str(e)}

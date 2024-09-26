from odoo import http
from odoo.http import request


class PelangganController(http.Controller):
    @http.route("/get/client/data", type="json", auth="user")
    def get_client_data(self):
        count = request.env["klinik.pelanggan"].count_cust()
        return {"count": count}

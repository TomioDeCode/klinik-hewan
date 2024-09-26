from odoo import http
from odoo.http import request


class LayananController(http.Controller):
    @http.route("/layanan/data", type="json", auth="user")
    def layanan_data(self):
        service_sales = request.env["product.template"].get_service_sales()
        return {"status": "success", "data": service_sales}

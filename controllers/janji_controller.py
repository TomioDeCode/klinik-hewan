from odoo import http
from odoo.http import request

class JanjiController(http.Controller):
    @http.route('/get/janji/data', type='json', auth='user')
    def get_client_data(self):
        count = request.env['klinik.appointment'].count_janji()
        return { 'count': count }


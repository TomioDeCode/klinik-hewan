from odoo import http
from odoo.http import request

class DokterController(http.Controller):
    @http.route('/get/dokter/data', type='json', auth='user')
    def get_animal_count(self):
        count = request.env['klinik.dokter'].count_dokters()
        return {'count': count}

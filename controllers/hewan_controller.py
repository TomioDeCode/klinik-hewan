from odoo import http
from odoo.http import request

class HewanController(http.Controller):
    @http.route('/get/animal/data', type='json', auth='user')
    def get_animal_count(self):
        count = request.env['klinik.hewan'].count_animals()
        return {'count': count}

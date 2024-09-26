from odoo import http
from odoo.http import request

class PembayaranController(http.Controller):

    @http.route('/payments/all', type='json', auth='user')
    def get_all_payments(self):
        try:
            payment_data = request.env['klinik.pembayaran'].get_all_payments()
            return {'status': 'success', 'data': payment_data}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}

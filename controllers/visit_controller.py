from odoo import http
from odoo.http import request

class KlinikVisitController(http.Controller):
    
    @http.route('/klinik/visit/today', type='json', auth='user', csrf=False)
    def get_today_visits(self):
        """
        Retrieve today's visit records.
        :return: List of today's visit records
        """
        visits = request.env['klinik.visit'].get_visits_today()

        # Prepare the data to be returned
        visit_data = []
        for visit in visits:
            visit_data.append({
                'id': visit.id,
                'name': visit.name,
                'partner_id': visit.partner_id.name,
                'pet_ids': visit.pet_ids.mapped('name'),  # List of pet names
                'dokter_id': {
                    'id': visit.dokter_id.id,  # Doctor ID
                    'name': visit.dokter_id.name.name,  # Doctor name
                } if visit.dokter_id else None,  # Safely handle cases where dokter_id is not set
                'visit_date': visit.visit_date,
                'total_price': visit.total_price,
                'state': visit.state,
                'notes': visit.notes,
            })
        
        return visit_data

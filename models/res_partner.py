from odoo import fields, models

class ResPartner(models.Model):
  _inherit = 'res.partner'

  klinik_member = fields.Selection([
    ('owner', 'Owner'),
    ('dokter', 'Dokter'),
  ], string="Klinik Member", required=True)
from odoo import fields, models

class KlinikDokter(models.Model):
  _name = "klinik.dokter"

  name = fields.Many2one('res.partner', domain="[('klinik_member', '=', 'dokter')]", string="Nama Dokter")
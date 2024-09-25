from odoo import models, fields, api, exceptions
import string, random

class KlinikPembayaran(models.Model):
    _name = "klinik.pembayaran"
    _description = "Pembayaran Klinik"

    name = fields.Char(string="Payment Reference", required=True, readonly=True, copy=False, default=lambda self: self._generate_random_id())
    resep_id = fields.Many2one('klinik.resep', string="Resep", required=True, ondelete="restrict")
    amount = fields.Float(string="Amount Paid", required=True)
    payment_date = fields.Datetime(string="Payment Date", default=fields.Datetime.now, required=True)
    payment_method = fields.Selection([
        ('cash', 'Cash'),
        ('credit_card', 'Credit Card'),
        ('bank_transfer', 'Bank Transfer'),
    ], string="Payment Method", required=True)

    state = fields.Selection([
        ('draft', 'Draft'),
        ('paid', 'Paid'),
        ('cancelled', 'Cancelled'),
    ], string="Status", default='draft')

    total_price = fields.Float(related='resep_id.total_price', string="Total Price", store=True)
    change = fields.Float(string="Change", compute="_compute_change", store=True)

    @api.depends('amount', 'total_price')
    def _compute_change(self):
        for record in self:
            record.change = record.amount - record.total_price if record.amount >= record.total_price else 0.0

    def action_pay(self):
        for record in self:
            if record.amount < record.total_price:
                raise exceptions.ValidationError("Insufficient amount. Please enter a valid payment.")
            record.state = 'paid'

    def action_cancel(self):
        for record in self:
            record.state = 'cancelled'

    def print_receipt(self):
        report_action = self.env.ref('klinik_hewan.klinik_pembayaran_report_action', raise_if_not_found=False)

        if report_action:
            return report_action.report_action(self)
        else:
            raise ValueError("Report action 'klinik_hewan.klinik_pembayaran_report_action' not found.")


    def _generate_random_id(self):
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

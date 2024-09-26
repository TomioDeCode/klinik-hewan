from odoo import models, fields, api
from datetime import datetime, date, timedelta


class KlinikVisit(models.Model):
    _name = "klinik.visit"
    _description = "Pet Clinic Visit"
    _order = "visit_date desc"

    name = fields.Char(
        string="Visit Reference",
        required=True,
        copy=False,
        readonly=True,
        default="New",
    )
    partner_id = fields.Many2one("res.partner", string="Customer", required=True)
    pet_ids = fields.Many2many("klinik.hewan", string="Pets", required=True)
    dokter_id = fields.Many2one("klinik.dokter", string="Dokter", required=True)
    visit_date = fields.Datetime(
        string="Visit Date", default=fields.Datetime.now, required=True
    )
    service_ids = fields.Many2many(
        "product.product", string="Services", domain=[("jenis_product", "=", "layanan")]
    )
    total_price = fields.Float(
        string="Total Price", compute="_compute_total_price", store=True
    )
    notes = fields.Text(string="Notes")
    state = fields.Selection(
        [
            ("draft", "Draft"),
            ("in_progress", "In Progress"),
            ("done", "Done"),
            ("cancelled", "Cancelled"),
        ],
        string="Status",
        default="draft",
    )

    @api.model
    def create(self, vals):
        if vals.get("name", "New") == "New":
            vals["name"] = self.env["ir.sequence"].next_by_code("klinik.visit") or "New"
        return super(KlinikVisit, self).create(vals)

    @api.depends("service_ids")
    def _compute_total_price(self):
        for visit in self:
            visit.total_price = sum(service.lst_price for service in visit.service_ids)

    def action_start(self):
        self.write({"state": "in_progress"})

    def action_done(self):
        self.write({"state": "done"})

    def action_cancel(self):
        self.write({"state": "cancelled"})

    @api.model
    def get_visits_today(self):
        today = datetime.combine(date.today(), datetime.min.time())
        tomorrow = datetime.combine(
            date.today() + timedelta(days=1), datetime.min.time()
        )
        return self.search([("visit_date", ">=", today), ("visit_date", "<", tomorrow)])

from odoo import fields, models, api


class KlinikHewan(models.Model):
    _name = "klinik.hewan"

    # Hewan ID
    name = fields.Char(string="Nama Hewan", required=True)
    jenis_hewan = fields.Selection(
        [
            ("anjing", "Anjing"),
            ("kucing", "Kucing"),
            ("burung", "Burung"),
            ("kelinci", "Kelinci"),
            ("lainnya", "Lainnya"),
        ],
        string="Jenis Hewan",
        required=True,
    )
    ras = fields.Char(string="Ras", help="Ras Hewan")
    jenis_kelamin = fields.Selection(
        [("jantan", "Jantan"), ("betina", "Betina")], string="Kelamin", required=True
    )
    image = fields.Binary("Image", help="Select Image Here!")
    tgl_lahir = fields.Date(string="Tgl Lahir", required=True)
    bb_badan = fields.Float(string="Berat Badan (Kg)")
    tgl_periksa = fields.Date(string="Tgl Terakhir Periksa")

    # Owner ID
    pemilik = fields.Many2one("res.partner", string="Pemilik Hewan", required=True)

    # Date ID
    create_date = fields.Datetime(string="Dibuat Pada", readonly=True)
    write_date = fields.Datetime(string="Diperbarui Pada", readonly=True)

    @api.model
    def count_animals(self):
        return self.search_count([])

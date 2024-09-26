{
    "name": "Klinik Hewan",
    "version": "1.0",
    "summary": "Manajemen Hewan di Klinik",
    "category": "Healthcare",
    "author": "TomioDeCode",
    "depends": ["base", "product", "sale"],
    "data": [
        "security/ir.model.access.csv",
        "views/klinik_hewan_views.xml",
        "views/res_partner_views.xml",
        "views/product_template_views.xml",
        "views/klinik_pelanggan_views.xml",
        "views/product_product_views.xml",
        "views/klinik_appointment_views.xml",
        "views/klinik_dokter_views.xml",
        "views/klinik_resep_views.xml",
        "views/klinik_ruangan_views.xml",
        "views/klinik_pembayaran_views.xml",
        "views/dashboard_views.xml",
        "views/klinik_visit_views.xml",
        "views/klinik_menus.xml",
        "views/reports/ouput_pdf/klinik_pembayaran_report.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "klinik_hewan/static/src/js/dashboard.js",
            "klinik_hewan/static/src/css/dashboard.css",
            "klinik_hewan/static/src/xml/dashboard.xml",
        ]
    },
    "installable": True,
    "application": True,
}

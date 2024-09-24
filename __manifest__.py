{
    'name': 'Klinik Hewan',
    'version': '1.0',
    'summary': 'Manajemen Hewan di Klinik',
    'category': 'Healthcare',
    'author': 'TomioDeCode',
    'depends': ['base', 'product'],
    "data": [
        "security/ir.model.access.csv",
        "views/klinik_hewan_views.xml",
        "views/res_partner_views.xml",
        "views/product_template_views.xml",
        "views/klinik_pelanggan_views.xml",
        "views/product_product_views.xml",
        "views/klinik_appointment_views.xml",
        "views/klinik_dokter_views.xml",

        "views/klinik_menus.xml",
    ],
    'installable': True,
    'application': True,
}
{
    'name': 'Abc Cab Service',

    'version': '15.1.0.0',
    'sequence': 185,
    'category': '',
    'website': 'https://www.odoo.com/app/fleet',
    'author': 'Tharidu Ishan',
    'summary' : 'Manager Cab Service',
    'description' : """""",
    'depends': [
        'base'
    ],
    'data': [

        'views/cab_vehicles_details_view.xml',
        'views/cab_drivers_details_view.xml',
        'security/ir.model.access.csv',
        # 'data/cron.xml',

    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
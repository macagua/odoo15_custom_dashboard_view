# Copyright 2023 Leonardo J. Caballero G.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    'name': 'Custom Dashboard View',
    'description': """
        Custom Dashboard View for Odoo 15. This module is part of the
        How to Create a Custom Dashboard in Odoo 15 from the Blog's Cybrosys.

        https://www.cybrosys.com/blog/how-to-create-a-custom-dashboard-in-odoo-15
    """,
    'version': '15.0.1.0.0',
    'license': 'AGPL-3',
    'author': 'Leonardo J. Caballero G.',
    'website': 'https://github.com/macagua/custom_dashboard_view',
    'depends': [
        'account',
        'hr',
        'project',
        'sale_management',
    ],
    'data': [
        'views/custom_dashboard_view.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'custom_dashboard_view/static/src/css/dashboard.css',
            'custom_dashboard_view/static/src/js/dashboard_action.js',
        ],
        'web.assets_qweb': [
            'custom_dashboard_view/static/src/xml/dashboard.xml',
        ],
    },
    'installable': True,
    'application': False,
}

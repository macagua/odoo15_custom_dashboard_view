# Copyright 2023 Leonardo J. Caballero G.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, api


class PosDashboard(models.Model):

    _inherit = 'project.project'

    @api.model
    def get_tiles_data(self):
        """Get the data tiles for the Custom Dashboard

        Returns:
            dict: A dictionary data for used in the dashboard
        """

        all_project = self.env['project.project'].search([])
        all_task = self.env['project.task'].search([])
        analytic_project = self.env['account.analytic.line'].search([])
        total_time = sum(analytic_project.mapped('unit_amount'))
        employees = self.env['hr.employee'].search([])
        task = self.env['project.task'].search_read(
            [('sale_order_id', '!=', False)], ['sale_order_id']
        )
        task_so_ids = [o['sale_order_id'][0] for o in task]
        sale_orders = self.mapped('sale_line_id.order_id') | self.env['sale.order'].browse(task_so_ids)

        return {
            'total_projects': len(all_project),
            'total_tasks': len(all_task),
            'total_employees': len(employees),
            'total_time': total_time,
            'sale_orders': sale_orders,
        }

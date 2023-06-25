# -*- coding: utf-8 -*-

from odoo import fields, models
from odoo.exceptions import UserError
from odoo.tools.translate import _


class PaidBills(models.TransientModel):
    _name = 'paid.bills'
    _description = 'Wizard for getting Paid Bills by the date range'

    date_from = fields.Date(string='Date From', required=True)
    date_to = fields.Date(string='Date To', required=True)

    def view_paid_bills(self):
        if self.date_from > self.date_to:
            raise UserError(_('Date From must be lower that Date To'))

        paid_bill_ids = self.env['account.move'].sudo().search([
            ('state', '=', 'posted'),
            ('payment_state', 'in', ('partial', 'paid')),
            ('move_type', '=', 'in_invoice'),
            ('reversal_move_id', '=', False),
            ('line_ids.date', '>=', self.date_from),
            ('line_ids.date', '<=', self.date_to),
        ]).ids

        return {
            'name': _('Paid Bills'),
            'domain': [('id', 'in', paid_bill_ids)],
            'view_mode': 'tree,form',
            'res_model': 'account.move',
            'views': [[False, "tree"], [False, "form"]],
            'type': 'ir.actions.act_window',
        }

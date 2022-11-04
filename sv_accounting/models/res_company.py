from odoo import fields, models, api


class ResCompany(models.Model):
    _inherit = 'res.company'

    giro_fiscal = fields.Char(string='Giro Fiscal')

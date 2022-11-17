# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models
import base64


class PosOrder(models.Model):
    _inherit = "pos.order"

    def _add_mail_attachment(self, name, ticket):
        attachment = super()._add_mail_attachment(name, ticket)
        if self.config_id.use_gift_card and len(self.get_new_card_ids()) > 0:
            report = self.env.ref('pos_gift_card_custom.gift_card_template_custom')._render_qweb_pdf(self.get_new_card_ids())
            filename = name + '.pdff'
            gift_card = self.env['ir.attachment'].create({
                'name': filename,
                'type': 'binary',
                'datas': base64.b64encode(report[0]),
                'store_fname': filename,
                'res_model': 'pos.order',
                'res_id': self.ids[0],
                'mimetype': 'application/x-pdf'
            })
            attachment += [(4, gift_card.id)]

        return attachment

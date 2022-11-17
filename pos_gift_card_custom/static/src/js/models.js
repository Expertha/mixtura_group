odoo.define("pos_gift_card_custom.gift_card_custom", function (require) {
  "use strict";

  const models = require("point_of_sale.models");
  const core = require('web.core');
  const _t = core._t;

  var _posmodel_super = models.PosModel.prototype;
    models.PosModel = models.PosModel.extend({
        print_gift_pdf: function (giftCardIds) {
            this.do_action('pos_gift_card_custom.gift_card_report_pdf_custom', {
                additional_context: {
                    active_ids: [giftCardIds],
                },
            })
        }
    });
});

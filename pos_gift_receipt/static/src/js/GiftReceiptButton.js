odoo.define('pos_gift_receipt.GiftReceiptButton', function(require) {
    'use strict';

    const PosComponent = require('point_of_sale.PosComponent');
    const ProductScreen = require('point_of_sale.ProductScreen');
    const { useListener } = require('web.custom_hooks');
    const Registries = require('point_of_sale.Registries');

    class GiftReceiptButton extends PosComponent {
        constructor() {
            super(...arguments);
            useListener('click', this.onClick);
        }
        async onClick() {
            const order = this.env.pos.get_order();
            if (order.get_orderlines().length > 0) {
                this.trigger('close-popup');
                await this.showTempScreen('GiftScreen');
            } else {
                await this.showPopup('ErrorPopup', {
                    title: this.env._t('Nothing to Print'),
                    body: this.env._t('There are no order lines'),
                });
            }
        }
    }
    GiftReceiptButton.template = 'GiftReceiptButton';

    ProductScreen.addControlButton({
        component: GiftReceiptButton,
        condition: function() {
            return this.env.pos.config.module_pos_gift_receipt;
        },
    });

    Registries.Component.add(GiftReceiptButton);

    return GiftReceiptButton;
});

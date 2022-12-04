odoo.define('pos_gift_receipt.GiftScreen', function (require) {
    'use strict';

    const ReceiptScreen = require('point_of_sale.ReceiptScreen');
    const Registries = require('point_of_sale.Registries');

    const GiftScreen = (ReceiptScreen) => {
        class GiftScreen extends ReceiptScreen {
            confirm() {
                this.props.resolve({ confirmed: true, payload: null });
                this.trigger('close-temp-screen');
            }
            whenClosing() {
                this.confirm();
            }
            /**
             * @override
             */
            async printReceipt() {
                await super.printReceipt();
                this.currentOrder._printed = false;
            }
        }
        GiftScreen.template = 'GiftScreen';
        return GiftScreen;
    };

    Registries.Component.addByExtending(GiftScreen, ReceiptScreen);

    return GiftScreen;
});

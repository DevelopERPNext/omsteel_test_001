frappe.ui.form.on("Stock Entry", {
    refresh: function(frm) {
        if (frm.doc.docstatus === 0 && frm.doc.stock_entry_type === 'Manufacture' && frm.doc.bom_check === 0) {
            frm.add_custom_button(__('BOM'), function() {
                frappe.call({
                    method: "omsteel_test_001.omsteel_test_001.production_items_table.update_stock_entry_items",
                    args: {
                        "doc": frm.doc.name
                    },
                    callback: function(response) {
                        if (response.message) {
                            frappe.show_alert({
                                message: __(response.message),
                                indicator: 'green'
                            });
                            frm.reload_doc();
                            // frm.refresh();
                        }
                        frm.reload_doc();
                    }
                });
            }).addClass('btn-warning').css({
                'color': 'white',
                'font-weight': 'bold',
                'background-color': '#274472'
            });
        }
    },
});
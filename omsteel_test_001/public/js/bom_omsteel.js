frappe.ui.form.on("Stock Entry", {
    refresh: function(frm) {
//        if (frm.doc.docstatus === 0 && frm.doc.stock_entry_type === 'Manufacture' && frm.doc.bom_check === 0) {
        if (frm.doc.docstatus === 0 && frm.doc.stock_entry_type === 'Manufacture' && frm.doc.bom_check === 0 || frm.doc.bom_check === 1) {
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







//frappe.ui.form.on("Work Order", {
//    refresh: function(frm) {
//        if (frm.doc.docstatus === 0) {
//            frm.add_custom_button(__('Calc'), function() {
//                frappe.call({
//                    method: "omsteel_test_001.omsteel_test_001.production_items_table.mod_qty",
//                    args: {
//                        "doc": frm.doc.name
//                    },
//                    callback: function(response) {
//                        if (response.message) {
//                            frappe.show_alert({
//                                message: __(response.message),
//                                indicator: 'green'
//                            });
//                            frm.reload_doc();
////                             frm.refresh();
//                        }
//                        frm.reload_doc();
////                        frm.refresh();
//                    }
//                });
//            }).addClass('btn-warning').css({
//                'color': 'white',
//                'font-weight': 'bold',
//                'background-color': '#274472'
//            });
//        }
//    },
//});









frappe.ui.form.on("Work Order", {
    refresh: function(frm) {
        if (frm.doc.docstatus === 0) {
            frm.add_custom_button(__('Refresh'), function() {
                frm.reload_doc();
            }).addClass('btn-warning').css({
                'color': 'white',
                'font-weight': 'bold',
                'background-color': '#274472'
            });
        }
    },
});








//frappe.ui.form.on("BOM", {
//    quantity: function(frm) {
//        if (frm.doc.docstatus === 0) {
//            frappe.call({
//                method: "omsteel_test_001.omsteel_test_001.production_items_table.calc_qty",
//                args: {
//                    "doc": frm.doc.name
//                },
//                callback: function(response) {
//                    if (response.message) {
//                        frappe.show_alert({
//                            message: __(response.message),
//                            indicator: 'green'
//                        });
//                        frm.refresh_field('calc_qty_a_001');
//                        frm.reload_doc();
//                    }
//                    frm.reload_doc();
//                }
//            });
//        }
//    }
//});




//frappe.ui.form.on("BOM", {
//    quantity: function(frm) {
//           frm.reload_doc();
//    },
//});
//
//
//frappe.ui.form.on("BOM", {
//    calc_qty_a_001: function(frm) {
//           frm.reload_doc();
//    },
//});




frappe.ui.form.on("BOM", {
        refresh: function(frm) {
        if (frm.doc.docstatus === 0) {
            frm.add_custom_button(__('Calculate Qty'), function() {
                frappe.call({
                    method: "omsteel_test_001.omsteel_test_001.production_items_table.calc_qty",
                    args: {
                        "doc_name": frm.doc.name
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







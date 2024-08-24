frappe.ui.form.on("Stock Entry", {
    refresh: function(frm) {
        if (frm.doc.docstatus === 0 && frm.doc.stock_entry_type === 'Manufacture' && frm.doc.bom_check === 0) {
//        if (frm.doc.docstatus === 0 && frm.doc.stock_entry_type === 'Manufacture' && frm.doc.bom_check === 0 || frm.doc.bom_check === 1) {
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








//   ================================================================
//   ================================================================
//   ========== Update Rate and Availability =========




frappe.ui.form.on("Stock Entry", {
    refresh: function(frm) {
        if (frm.doc.docstatus === 0 && frm.doc.stock_entry_type === 'Manufacture' && frm.doc.update_rate === 0) {
            frm.add_custom_button(__('Update Rate and Availability'), function() {
                frappe.call({
                    method: "omsteel_test_001.omsteel_test_001.production_items_table.get_stock_and_rate",
                    args: {
                        doc_name: frm.doc.name
                    },
                    callback: function(response) {
                        if (response.message) {
                            frappe.show_alert({
                                message: __("Stock and rate updated successfully"),
                                indicator: 'green'
                            });
                            frm.reload_doc();
                        } else {
                            frappe.show_alert({
                                message: __("Error updating stock and rate"),
                                indicator: 'red'
                            });
                        }
                    }
                });
//////            }).addClass('btn-warning').css({
                }, __("After BOM Only")).addClass('btn-warning').css({

//                'color': 'black',
//                'font-weight': 'bold',
//                'background-color': 'white',
                'color': 'white',
                'font-weight': 'bold',
                'background-color': '#274472',
                'margin-top': '15px',
                'margin-bottom': '12px'
            });

        }
    }
});






//   ================================================================
//   ================================================================
//   =======  Triggered before_submit form is Before submitted (before_submit) ========
//   =======  Triggered validate form is ON submitted (validate) ========




//frappe.ui.form.on('Stock Entry', {
//    before_submit: function (frm) {
////    on_submit: function (frm) {
//        if (frm.doc.stock_entry_type === 'Manufacture') {
//            frappe.call({
//                method: "omsteel_test_001.omsteel_test_001.production_items_table.get_stock_and_rate_is_finished_item",
//                args: {
//                    doc_name: frm.doc.name
//                },
//                callback: function (r) {
//                    if (!r.exc) {
//                        frappe.show_alert({
//                            message: __('Stock and rate updated successfully'),
//                            indicator: 'green'
//                        });
//                        frm.reload_doc();
//                    } else {
//                        frappe.show_alert({
//                            message: __('An error occurred: {0}').format(r.exc),
//                            indicator: 'red'
//                        });
//                    }
//                }
//            });
//        }
//    }
//});






frappe.ui.form.on('Stock Entry', {
//    validate: function (frm) {
    after_save: function (frm) {
        if (frm.doc.stock_entry_type === 'Manufacture') {
            frappe.call({
                method: "omsteel_test_001.omsteel_test_001.production_items_table.get_stock_and_rate_standard_valuation_rate",
                args: {
                    doc_name: frm.doc.name
                },
                callback: function (r) {
                    if (!r.exc) {
                        frappe.show_alert({
                            message: __('Stock and rate updated successfully'),
                            indicator: 'green'
                        });
                        frm.reload_doc();
                    }
//                    else {
//                        frappe.show_alert({
//                            message: __('An error occurred: {0}').format(r.exc),
//                            indicator: 'red'
//                        });
//                    }
                }
            });
        }
    }
});





//frappe.ui.form.on('Stock Entry', {
//    on_submit: function (frm) {
////    before_submit: function (frm) {
//        if (frm.doc.stock_entry_type === 'Manufacture') {
//            frappe.call({
//                method: "omsteel_test_001.omsteel_test_001.production_items_table.get_stock_and_rate_is_finished_item",
////                method: "omsteel_test_001.omsteel_test_001.production_items_table.update_qty_stock_entry_detail_from_transfer_qty",
//                args: {
//                    doc_name: frm.doc.name
////                    docname: frm.doc.name
//                },
//                callback: function (r) {
//                    if (!r.exc) {
//                        frappe.show_alert({
//                            message: __('Stock and rate updated successfully'),
//                            indicator: 'green'
//                        });
//                        frm.reload_doc();
//                    } else {
//                        frappe.show_alert({
//                            message: __('An error occurred: {0}').format(r.exc),
//                            indicator: 'red'
//                        });
//                    }
//                }
//            });
//        }
//    }
//});




//frappe.ui.form.on('Stock Entry', {
//    before_submit: function (frm) {
//        if (frm.doc.stock_entry_type === 'Manufacture') {
//            frappe.call({
//                method: "omsteel_test_001.omsteel_test_001.production_items_table.get_stock_and_rate_standard_valuation_rate",
//                args: {
//                    doc_name: frm.doc.name
//                },
//                callback: function (r) {
//                    if (!r.exc) {
//                        frappe.show_alert({
//                            message: __('Stock and rate updated successfully'),
//                            indicator: 'green'
//                        });
//
//                        frappe.call({
//                            method: "omsteel_test_001.omsteel_test_001.production_items_table.get_stock_and_rate_is_finished_item",
//                            args: {
//                                doc_name: frm.doc.name
//                            },
//                            callback: function (r) {
//                                if (!r.exc) {
//                                    frappe.show_alert({
//                                        message: __('Stock and rate updated successfully'),
//                                        indicator: 'green'
//                                    });
//                                    frm.reload_doc();
//                                } else {
//                                    frappe.show_alert({
//                                        message: __('An error occurred in Stock and rate updated: {0}').format(r.exc),
//                                        indicator: 'red'
//                                    });
//                                }
//                            }
//                        });
//
//                    } else {
//                        frappe.show_alert({
//                            message: __('An error occurred in the first function: {0}').format(r.exc),
//                            indicator: 'red'
//                        });
//                    }
//                }
//            });
//        }
//    }
//});




//   ================================================================
//   ================================================================







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

            frm.add_custom_button(__('Changed the Doc Name'), function() {
                frappe.call({
                    method: "omsteel_test_001.omsteel_test_001.production_items_table.changed_the_doc_name",
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
//                            frm.refresh();
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









//   ================================================================
//   ================================================================
//   =============  Update Qty from Transfer Qty  ===================



frappe.ui.form.on('Stock Entry', {
    refresh: function (frm) {
    if ((frm.doc.docstatus === 1) && frm.doc.stock_entry_type === 'Manufacture') {
        frm.add_custom_button(__('Update Qty from Transfer Qty'), function () {
            frappe.call({
                method: "omsteel_test_001.omsteel_test_001.production_items_table.update_qty_stock_entry_detail_from_transfer_qty",
                args: {
                    docname: frm.doc.name
                },
                callback: function (r) {
                    if (!r.exc) {
//                        frappe.msgprint(__('Quantities updated successfully'));
                        frappe.show_alert({
                                message: __('Quantities updated successfully'),
                                indicator: 'green'
                            });
                        frm.reload_doc();
                    }
                }
            });
//        }).addClass('btn-warning').css({
        }, __("Update Qty from Transfer Qty")).addClass('btn-warning').css({

                'color': 'white',
                'font-weight': 'bold',
                'background-color': '#274472',
                'margin-top': '15px',
                'margin-bottom': '8px'

        });
    }
    }
});

//   ================================================================
//   ================================================================
//   =======  Triggered after form is submitted (on_submit) ========


frappe.ui.form.on('Stock Entry', {
    on_submit: function (frm) {
        if (frm.doc.stock_entry_type === 'Manufacture') {
            frappe.call({
                method: "omsteel_test_001.omsteel_test_001.production_items_table.update_qty_stock_entry_detail_from_transfer_qty",
                args: {
                    docname: frm.doc.name
                },
                callback: function (r) {
                    if (!r.exc) {
                        frappe.show_alert({
                            message: __('Quantities updated successfully'),
                            indicator: 'green'
                        });
                        frm.reload_doc();
                    } else {
                        frappe.show_alert({
                            message: __('An error occurred: {0}').format(r.exc),
                            indicator: 'red'
                        });
                    }
                }
            });
        }
    }
});






//   ================================================================
//   ================================================================














//   ================================================================
//   ================================================================
//   ============= Fetch Qty (Finished Item) & UOM (ربطة) ==================



frappe.ui.form.on('Stock Entry', {
    refresh: function(frm) {
        if ((frm.doc.docstatus === 0) && frm.doc.stock_entry_type === 'Manufacture') {
            frm.add_custom_button(__('Update Qty [(Finished Item) & UOM]'), function () {
                frappe.confirm(
                    'Are you sure you want to update the quantities of finished items?',
                    function() {
                        frappe.call({
                            method: "omsteel_test_001.omsteel_test_001.production_items_table.update_finished_item_qty_uom",
                            args: {
                                doc: frm.doc.name
                            },
                            callback: function(r) {
                                if (!r.exc) {
                            frappe.show_alert({
                                            message: __('Quantities updated successfully'),
                                            indicator: 'green'
                                        });
                                    frm.reload_doc();
                                }
                            }
                        });
                    }
                );
//            }).addClass('btn-warning').css({
            }, __("Update Qty [(Finished Item) & UOM")).addClass('btn-warning').css({

                    'color': 'white',
                    'font-weight': 'bold',
                    'background-color': '#563627',
                    'margin-top': '15px',
                    'margin-bottom': '8px'

            });
        }
    }
});








//   ================================================================
//   ================================================================







//   ================================================================
//   ================================================================
//   ================================================================
//   ==== START Change Qty in table items ====




frappe.ui.form.on('Stock Entry', {
        refresh: function(frm) {
//        onload: function(frm) {
//        //    if (frm.doc.docstatus === 0 && frm.doc.stock_entry_type === 'Manufacture' && frm.doc.bom_check === 0) {
        if (frm.doc.docstatus === 0 && frm.doc.stock_entry_type === 'Manufacture') {
//        if ((frm.doc.docstatus === 0 || frm.doc.docstatus === 1) && frm.doc.stock_entry_type === 'Manufacture') {
            frm.add_custom_button(__('Change Qty'), function() {
                open_item_dialog_bb(frm);
            }).addClass('btn-warning').css({
                'color': 'white',
                'font-weight': 'bold',
                'background-color': '#274472'
            });
        }
    }
});



function open_item_dialog_bb(frm) {
    let d = new frappe.ui.Dialog({
        title: 'Select Item and Change Quantity',
        fields: [
            {
                label: 'Item Code',
                fieldname: 'item_code',
                fieldtype: 'Select',
//                options: frm.doc.items.map(item => item.item_code),
                options: getFilteredItemOptions(frm.doc.items),
                reqd: 1
            },
            {
                label: 'Warehouse',
                fieldname: 'warehouse',
                fieldtype: 'Select',
                options: [],
                hidden: 0,
                reqd: 1
            },
            {
                label: 'Idx',
                fieldname: 'idx',
                fieldtype: 'Select',
                options: [],
                hidden: 0,
                reqd: 1
            },
            {
                label: 'Change Qty',
                fieldname: 'change_qty_a_010',
                fieldtype: 'Check',
                hidden: 0,
                read_only: 1,
                options: [],
                reqd: 0
            },
            {
                label: 'Qty',
                fieldname: 'qty',
                fieldtype: 'Float',
//                options: frm.doc.items.map(item => item.qty),
                read_only: 1,
                hidden: 0,
                reqd: 0
            },
            {
                label: 'New Quantity',
                fieldname: 'new_qty',
                fieldtype: 'Float',
                reqd: 1
            }
        ],
        primary_action_label: 'Update Quantity',



    primary_action(values) {
        try {
            // Convert BOM items to JSON string
            let bom_items = JSON.stringify(frm.doc.items);
            let selected_idx = values.idx;
            let selected_item_code = JSON.stringify(values.item_code);

            // Call the server-side method for validation
            frappe.call({
                method: 'omsteel_test_001.omsteel_test_001.production_items_table.validate_qty_in_bom_standard_deviation',
                args: {
                    bom_items: bom_items,
                    selected_idx: selected_idx,
                    selected_item_code: selected_item_code,
                    new_qty: parseFloat(values.new_qty)
                },

                callback: function(r) {
                    if (r.message) {
                        let validation_result = r.message;

                        // Check if the selected item is valid
                        if (validation_result[selected_idx]) {
//                            fetch_quantity_bb(frm, values.item_code, values.warehouse, values.new_qty);
                            fetch_quantity_bb(frm, values.item_code, parseInt(values.idx), values.warehouse, values.new_qty);
//                            // Update the quantity field based on selected item_code and idx
//                            update_qty_field(frm, selected_item_code, selected_idx, d.fields_dict.qty);
                            frappe.show_alert({
                                    message: __('Validation successful.',),
                                    indicator: 'green'
                            });
                            d.hide();
                        } else {
                            frappe.show_alert({
                                    message: __('Quantity validation failed. Please check the BOM quantities.'),
                                    indicator: 'green'
                            });

                            // Optionally, display selected BOM item in JSON format
                            let selected_item = frm.doc.items.find(item => item.idx === parseInt(selected_idx) && item.item_code === values.item_code);
                            if (selected_item) {
                                let selected_item_json = JSON.stringify(selected_item, null, 2);
                                frappe.msgprint(`<pre>${selected_item_json}</pre>`);
                            }
                        }
                    } else {
                        frappe.show_alert({
                                    message: __('No validation result returned from the server.'),
                                    indicator: 'green'
                        });
                    }
                },
                error: function(err) {
                    frappe.show_alert({
                            message: __('Error in server call: {0}', [err]),
                            indicator: 'green'
                    });
                }
            });
        } catch (e) {
            frappe.show_alert({
                        message: __('Error in primary_action function: {0}', [e]),
                        indicator: 'green'
            });
        }
    }



    });

    d.fields_dict.item_code.$input.on('change', function() {
            let selected_item_code = d.get_value('item_code');

            let warehouse_field = d.fields_dict.warehouse;
            let idx_field = d.fields_dict.idx;
            let qty_field = d.fields_dict.qty;


            let selected_idx = d.get_value('idx');
            let change_qty_field = d.fields_dict.change_qty_a_010;


            let items = frm.doc.items.filter(item =>
                item.item_code === selected_item_code && item.idx === selected_idx
            );

            let should_check = items.some(item => item.change_qty_a_010 === 1);
            change_qty_field.set_value(should_check);





            // Fetch warehouses based on the selected item code
            let warehouses = frm.doc.items
                .filter(item => item.item_code === selected_item_code)
                .map(item => item.s_warehouse || item.t_warehouse);

            // Fetch Qty based on the selected item code
            let qty = frm.doc.items
                .filter(item => item.item_code === selected_item_code)
                .map(item => item.qty);

           // Fetch unique idx values based on the selected item code and condition
            let idxs = frm.doc.items
                .filter(item => item.item_code === selected_item_code && item.change_qty_a_010 !== 1)
                .map(item => item.idx);

            // Update warehouse field options
            let unique_warehouses = [...new Set(warehouses)];
            warehouse_field.df.options = unique_warehouses.join('\n');

            // Set default value to the first option if available
            if (unique_warehouses.length > 0) {
                d.set_value('warehouse', unique_warehouses[0]);
            }

            warehouse_field.refresh();

            // Fetch idx based on the selected item code
            let selected_items = frm.doc.items.filter(item => item.item_code === selected_item_code);
            let unique_idxs = [...new Set(selected_items.map(item => item.idx))];

            frappe.show_alert({
                    message: __('Selected Item Code: {0}', [selected_item_code]),
                    indicator: 'green'
            });
            frappe.show_alert({
                message: __('Available idxs: {0}', [unique_idxs]),
                indicator: 'green'
            });

            // Update idx field options
            idx_field.df.options = unique_idxs.join('\n');
            idx_field.refresh();

            if (unique_idxs.length > 0) {
                let default_idx = unique_idxs[0];
                d.set_value('idx', default_idx);

//                let default_idx;
//                if (should_check) {
//                    default_idx = unique_idxs.length > 1 ? unique_idxs[1] : unique_idxs[0];
//                } else {
//                    default_idx = unique_idxs[0];
//                }
//                d.set_value('idx', default_idx);
                frappe.show_alert({
                    message: __('Default idx: {0}', [default_idx]),
                    indicator: 'green'
                });
                // Automatically update the quantity field based on the default idx selected
                update_qty_field(frm, selected_item_code, default_idx, qty_field);
            } else {
                // If no idx is available, clear the qty field
                qty_field.set_value('');
            }
        });

//        // When the idx changes, update the quantity
//        d.fields_dict.idx.$input.on('change', function() {
//            let item_code = d.get_value('item_code');
//            let idx = parseInt(d.get_value('idx'));
//
//            update_qty_field(frm, item_code, idx, d.fields_dict.qty);
//        });




//        // When the idx changes, update the quantity and change_qty_a_010 field
//        d.fields_dict.idx.$input.on('change', function() {
//            let item_code = d.get_value('item_code');
//            let idx = parseInt(d.get_value('idx'));
//
//            update_qty_field(frm, item_code, idx, d.fields_dict.qty);
//            let change_qty_field = d.fields_dict.change_qty_a_010;
//
//            let items = frm.doc.items.filter(item =>
//                item.item_code === item_code && item.idx === idx
//            );
//            let should_check = items.some(item => item.change_qty_a_010 === 1);
//            change_qty_field.set_value(should_check);
//        });

        d.fields_dict.idx.$input.on('change', function() {
            let item_code = d.get_value('item_code');
            let idx = parseInt(d.get_value('idx'));

            update_qty_field(frm, item_code, idx, d.fields_dict.qty);

            let change_qty_field = d.fields_dict.change_qty_a_010;
            let items = frm.doc.items.filter(item =>
                item.item_code === item_code && item.idx === idx
            );
            let should_check = items.some(item => item.change_qty_a_010 === 1);
            change_qty_field.set_value(should_check);

            if (should_check) {
                d.fields_dict.qty.$wrapper.hide();
                d.fields_dict.new_qty.$wrapper.hide();
            } else {
                d.fields_dict.qty.$wrapper.show();
                d.fields_dict.new_qty.$wrapper.show();
            }
        });





    d.show();

}





// Function to dynamically show or hide the idx
function setIdxFieldVisibility(frm, shouldHide) {
    let idxField = frm.fields_dict['idx'];
    idxField.df.hidden = shouldHide ? 1 : 0;
    frm.refresh_field('idx');
}




//// Helper function to get filtered item options
//function getFilteredItemOptions(items) {
//    let filteredItems = items.filter(item => item.is_finished_item || item.is_scrap_item);
//    return filteredItems.map(item => item.item_code).join('\n');
//}


// Helper function to get filtered item options
function getFilteredItemOptions(items) {
    let filteredItems = items.filter(item =>
        (item.is_finished_item || item.is_scrap_item) && item.change_qty_a_010 !== 1
    );
    return filteredItems.map(item => item.item_code).join('\n');
}


//// Update quantity field based on selected item code and idx
//function update_qty_field(frm, item_code, idx, qty_field) {
////    frappe.show_alert({
////        message: __('Updating qty field for item_code: {0} and idx: {1}', [item_code, idx]),
////        indicator: 'red'
////    });
//
//    // Find the item with the specified item_code and idx
//    let item = frm.doc.items.find(item => item.item_code === item_code && item.idx === idx);
//    let qty = item ? item.qty : 0;
//
//    // Update the quantity
//    qty_field.set_value(qty);
//}



//function update_qty_field(frm, item_code, idx, qty_field) {
//    let item = frm.doc.items.find(item => item.item_code === item_code && item.idx === idx);
//
//    if (item) {
//        qty_field.set_value(item.qty);
//    } else {
//        qty_field.set_value('');
//    }
//}



function update_qty_field(frm, item_code, idx, qty_field) {
    let item = frm.doc.items.find(item =>
        item.item_code === item_code &&
        item.idx === idx &&
        item.change_qty_a_010 !== 1
    );

    if (item) {
        qty_field.set_value(item.qty);
//        frm.set_df_property('idx', 'hidden', false);
    } else {
        qty_field.set_value('');
//        frm.set_df_property('idx', 'hidden', true);
    }
}




function fetch_quantity_bb(frm, item_code, idx, warehouse, new_qty) {
    let item = frm.doc.items.find(item => item.item_code === item_code && item.idx === idx);

    if (item) {
        frappe.call({
            method: "erpnext.stock.doctype.batch.batch.get_batch_qty",
            args: {
                item_code: item_code,
                warehouse: warehouse
            },
            callback: function(res) {
                if (res.message) {
                    let total_qty = res.message.reduce((total, batch) => total + batch.batch_qty, 0);

                    // Update the quantity for the specific item in the items table
                    frm.doc.items.forEach(child_item => {
                        if (child_item.item_code === item_code && child_item.idx === idx) {
//                            frappe.msgprint(`Qty Before: ${child_item.qty}`);
//                            frappe.msgprint(`New Qty: ${new_qty}`);
                            child_item.qty = new_qty;
                            child_item.transfer_qty = new_qty;
//                            frappe.msgprint(`Qty After: ${child_item.qty}`);


                            frappe.call({
                                method: "omsteel_test_001.omsteel_test_001.production_items_table.update_stock_entry_detail",
                                args: {
                                    docname: frm.doc.name,
                                    item_code: item_code,
                                    idx: idx,
                                    new_qty: new_qty
                                },

                                callback: function(response) {
                                    if (response.message) {
                                        frappe.show_alert({
                                            message: response.message,
                                            indicator: 'green'
                                        });

                                        frm.refresh_field('items');
//                                        frm.refresh_field('change_qty_a_010');
//                                        frappe.msgprint('This is message 1 ');
                                    }
                                },

                                error: function(error) {
                                    frappe.msgprint(__('Error saving the item: ' + error.message));
                                }
                            });

//                            frappe.msgprint('This is message 2 ');
                            frm.refresh_field('items');
                            frm.reload_doc();
                        }
                    });
                    frm.refresh_field('items');
                } else {
                    frappe.show_alert({
                        message: __('No quantity found for the batch.'),
                        indicator: 'red'
                    });
                }
            },
            error: function(err) {
                frappe.msgprint(__('Error fetching batch quantity: ' + err.message));
            }
        });
    } else {
        frappe.show_alert({
            message: __('Item not found in the document for the given idx.'),
            indicator: 'red'
        });

    }
}










//   ==== END Change Qty in table items ====
//   ================================================================
//   ================================================================














//   ================================================================
//   ================================================================
//   ==== START  Fetch data from items table - A - Select Batch Method ====








frappe.ui.form.on('Stock Entry', {
    refresh: function(frm) {

    //    if (frm.doc.docstatus === 0 && frm.doc.stock_entry_type === 'Material Transfer for Manufacture' && frm.doc.bom_check === 0) {
    if (frm.doc.docstatus === 0 && frm.doc.stock_entry_type === 'Material Transfer for Manufacture') {
        frm.add_custom_button(__('Select Batch Method'), function() {
            open_item_dialog_aa_0(frm);
        }, __("Fetch Additional Batch")).addClass('btn-warning').css({
                'color': 'white',
                'font-weight': 'bold',
                'background-color': '#274472',
                'margin-top': '15px',
                'margin-bottom': '8px'
        });
        }
    }
});



function open_item_dialog_aa_0(frm) {
    let d = new frappe.ui.Dialog({
        title: 'Select Item and Scan Batch Numbers',
        fields: [
            {
                label: 'Item Code',
                fieldname: 'item_code',
                fieldtype: 'Select',
                options: frm.doc.items.map(item => item.item_code),
                reqd: 1
            },
            {
                label: 'Warehouse',
                fieldname: 'warehouse',
                fieldtype: 'Select',
                options: [],
                hidden: 1,
                reqd: 1
            },
            {
                label: 'Scan Batch No',
                fieldname: 'batch_no',
                fieldtype: 'Select',
                options: [],
                hidden: 1,
                reqd: 0
            }
        ],
        primary_action_label: 'Fetch Quantity',
        primary_action(values) {
            fetch_quantity_aa_0(frm, values.item_code, values.warehouse, values.batch_no);
//            fetch_batch_data(values.item_code, values.warehouse, values.batch_no).then(() => {
//                frappe.msgprint(__('Batch data fetched successfully'));
//            }).catch(err => {
//                frappe.msgprint(__('Error fetching batch data: ') + err.message);
//            });
            d.hide();
        }
    });

    d.fields_dict.item_code.$input.on('change', function() {
        let selected_item_code = d.get_value('item_code');
        let warehouse_field = d.fields_dict.warehouse;
        let batch_no_field = d.fields_dict.batch_no;

        // Fetch warehouses based on the selected item code
        let warehouses = frm.doc.items
            .filter(item => item.item_code === selected_item_code)
            .map(item => item.s_warehouse || item.t_warehouse);

        // Update warehouse field options
        let unique_warehouses = [...new Set(warehouses)];
        warehouse_field.df.options = unique_warehouses.join('\n');

        // Set default value to the first option if available
        if (unique_warehouses.length > 0) {
            d.set_value('warehouse', unique_warehouses[0]);
        }

        warehouse_field.refresh();


        // Fetch batch numbers based on the selected item code and warehouse
        fetch_batch_numbers_aa_0(selected_item_code).then(batches => {
            // Format batch options to include batch_id and batch_qty
            let batch_options = batches.map(batch => `${batch.batch_id} (Qty: ${batch.batch_qty})`).join('\n');

            // Update batch_no field options
            batch_no_field.df.options = batch_options;
            batch_no_field.refresh();
        }).catch(err => {
            frappe.msgprint(__('Error fetching batch numbers: ') + err.message);
        });
    });

    d.show();
}

function fetch_batch_numbers_aa_0(item_code) {
    return new Promise((resolve, reject) => {
        frappe.call({
            method: 'omsteel_test_001.omsteel_test_001.production_items_table.fetch_batch_numbers',
            args: {
                item_code: item_code
            },
            callback: function(r) {
                if (r.message) {
                    resolve(r.message);
                } else {
                    resolve([]);
                }
            },
            error: function(err) {
                reject(err);
            }
        });
    });
}

function fetch_batch_data_aa_0(item_code, warehouse, batch_id) {
    frappe.call({
        method: 'omsteel_test_001.omsteel_test_001.production_items_table.get_batch_data',
        args: {
            item_code: item_code,
            warehouse: warehouse,
            batch_id: batch_id
        },
        callback: function(r) {
            if (r.message) {
                // Format the batch data into a string
                let batch_data_str = r.message.map(batch => {
                    return `Name: ${batch.batch_name}, Batch ID: ${batch.batch_id}, Batch Quantity: ${batch.batch_qty}`;
                }).join('\n');

//                // Display the batch data using frappe.msgprint
//                frappe.msgprint({
//                    title: __('Batch Details'),
//                    indicator: 'green',
//                    message: `<pre>${batch_data_str}</pre>`
//                });
            } else {
                frappe.msgprint(__('No batch data found.'));
            }
        },
        error: function(err) {
            frappe.msgprint(__('Error retrieving batch data: ') + err.message);
        }
    });
}

function fetch_quantity_aa_0(frm, item_code, warehouse, batch_no) {
    // Find the item in the items table
    let item = frm.doc.items.find(i => i.item_code === item_code);

    if (item) {
        // Fetch batch and serial number details
        select_batch_and_serial_no_aa_0(frm, item, warehouse, batch_no).then(() => {
            frappe.msgprint(__('Batch and serial number details fetched successfully'));
        }).catch(err => {
            frappe.msgprint(__('Error fetching batch and serial number details: ') + err.message);
        });
    } else {
        frappe.msgprint(__('Item not found in the table'));
    }
}

function select_batch_and_serial_no_aa_0(frm, item, warehouse, batch_no) {
    return new Promise((resolve, reject) => {
        frappe.db.get_value("Item", item.item_code, ["has_batch_no", "has_serial_no"]).then((r) => {
            if (r.message && (r.message.has_batch_no || r.message.has_serial_no)) {
                item.has_serial_no = r.message.has_serial_no;
                item.has_batch_no = r.message.has_batch_no;
                item.type_of_transaction = item.s_warehouse ? "Outward" : "Inward";

                new erpnext.BatchPackageSelectorAA_0(frm, item, (r) => {
                    if (r) {
                        frappe.model.set_value(item.doctype, item.name, {
                            serial_and_batch_bundle: r.name,
                            use_serial_batch_fields: 0,
                            basic_rate: r.avg_rate,
                            qty: Math.abs(r.total_qty) / flt(item.conversion_factor || 1, precision("conversion_factor", item)),
                        });
                        resolve();
                    } else {
                        reject(new Error('Failed to fetch serial and batch package details'));
                    }
                });
            } else {
                reject(new Error('Item does not have batch or serial numbers'));
            }
        }).catch(err => {
            reject(err);
        });
    });
}










// =============  Class  Define the BatchPackageSelector class ================

erpnext.BatchPackageSelectorAA_0 = class BatchPackageSelector {
    constructor(frm, item, callback) {
        this.frm = frm;
        this.item = item;
        this.qty = item.qty;
        this.callback = callback;
        this.bundle = this.item?.is_rejected
            ? this.item.rejected_serial_and_batch_bundle
            : this.item.serial_and_batch_bundle;

        this.make_0();
        this.render_data_0();
    }

    make_0() {
        let label = __("Batch Nos");
        let primary_label = this.bundle ? __("Update") : __("Add");

        primary_label += " " + label;

        this.dialog = new frappe.ui.Dialog({
            title: this.item?.title || primary_label,
            fields: this.get_dialog_fields_0(),
            primary_action_label: primary_label,
            primary_action: () => this.update_bundle_entries_0(),
            secondary_action_label: __("Edit Full Form (*)"),
            secondary_action: () => this.edit_full_form_0(),
        });

        this.dialog.show();
        this.$scan_btn = this.dialog.$wrapper.find(".link-btn");
        this.$scan_btn.css("display", "inline");

        let qty = this.item.stock_qty || this.item.transfer_qty || this.item.qty;

        if (this.item?.is_rejected) {
            qty = this.item.rejected_qty;
        }

        qty = Math.abs(qty);
        if (qty > 0) {
            this.dialog.set_value("qty", qty).then(() => {
                if (this.item.batch_no && !this.item.serial_and_batch_bundle) {
                    this.dialog.set_value("scan_batch_no", this.item.batch_no);
                    frappe.model.set_value(this.item.doctype, this.item.name, "batch_no", "");
                }

                this.dialog.fields_dict.entries.grid.refresh();
            });
        }
    }

    get_dialog_fields_0() {
        let fields = [
            {
                fieldtype: "Link",
                fieldname: "warehouse",
                label: __("Warehouse"),
                options: "Warehouse",
                default: this.get_warehouse(),
                onchange: () => {
                    this.item.warehouse = this.dialog.get_value("warehouse");
                    this.get_auto_data_0();
                },
                get_query: () => {
                    return {
                        filters: {
                            is_group: 0,
                            company: this.frm.doc.company,
                        },
                    };
                },
            },
            {
				fieldtype: "Float",
				fieldname: "qty",
				label: __("Qty to Fetch"),
				onchange: () => this.get_auto_data_0(),
			},
            {
                fieldtype: "Column Break",
            },
            {
                fieldtype: "Data",
                options: "Barcode",
                fieldname: "scan_batch_no",
                label: __("Scan Batch No (=)"),
                onchange: () => this.scan_barcode_data_0(),
            },
            {
                fieldtype: "Section Break",
            },
            {
                fieldname: "entries",
                fieldtype: "Table",
                allow_bulk_edit: true,
                data: [],
                fields: this.get_dialog_table_fields_0(),
            },
        ];

        return fields;
    }

    get_dialog_table_fields_0() {
        return [
            {
                fieldtype: "Link",
                options: "Batch",
                fieldname: "batch_no",
                label: __("Batch No"),
                in_list_view: 1,
                get_query: () => {
                    let is_inward = false;
                    if (
                        (["Purchase Receipt", "Purchase Invoice"].includes(this.frm.doc.doctype) &&
                            !this.frm.doc.is_return) ||
                        (this.frm.doc.doctype === "Stock Entry" &&
                            this.frm.doc.purpose === "Material Receipt")
                    ) {
                        is_inward = true;
                    }

                    return {
                        query: "erpnext.controllers.queries.get_batch_no",
                        filters: {
                            item_code: this.item.item_code,
                            warehouse: this.item.s_warehouse || this.item.t_warehouse || this.item.warehouse,
                            is_inward: is_inward,
                        },
                    };
                },
                onchange: () => {
                    this.fetch_batch_data_aaa();
                },
            },
            {
                fieldtype: "Float",
                fieldname: "qty",
                label: __("Quantity - total"),
                in_list_view: 1,
            },
            {
                fieldtype: "Data",
                fieldname: "name",
                label: __("Name"),
                hidden: 1,
            },
        ];
    }

    fetch_batch_data_aaa_0() {
        const { batch_no, warehouse } = this.dialog.get_values();
        if (batch_no) {
            frappe.call({
                method: 'omsteel_test_001.omsteel_test_001.production_items_table.get_batch_data',
                args: {
                    item_code: this.item.item_code,
                    warehouse: warehouse || this.item.warehouse || this.item.s_warehouse,
                    batch_id: batch_no
                },
                callback: function(r) {
                    if (r.message) {
                        // Format the batch data into a string
                        let batch_data_str = r.message.map(batch => {
                            return `Name: ${batch.batch_name}, Batch ID: ${batch.batch_id}, Batch Quantity: ${batch.batch_qty}`;
                        }).join('\n');

                        // Display the batch data using frappe.msgprint
                        frappe.msgprint({
                            title: __('Batch Details'),
                            indicator: 'green',
                            message: `<pre>${batch_data_str}</pre>`
                        });
                    } else {
                        frappe.msgprint(__('No batch data found.'));
                    }
                },
                error: function(err) {
                    frappe.msgprint(__('Error retrieving batch data: ') + err.message);
                }
            });
        }
    }

    get_auto_data_0() {
        let { qty, based_on } = this.dialog.get_values();

        if (this.item.serial_and_batch_bundle || this.item.rejected_serial_and_batch_bundle) {
            if (this.qty && qty === Math.abs(this.qty)) {
                return;
            }
        }

        if (this.item.batch_no) {
            return;
        }

        if (!based_on) {
            based_on = "FIFO";
        }

        if (qty) {
            frappe.call({
                method: "erpnext.stock.doctype.serial_and_batch_bundle.serial_and_batch_bundle.get_auto_data",
                args: {
                    item_code: this.item.item_code,
                    warehouse: this.item.warehouse || this.item.s_warehouse,
                    has_batch_no: this.item.has_batch_no,
                    qty: qty,
                    based_on: based_on,
                },
                callback: (r) => {
                    if (r.message) {
                        this.dialog.fields_dict.entries.df.data = r.message;
                        this.dialog.fields_dict.entries.grid.refresh();
                    }
                },
            });
        }
    }





    scan_barcode_data_0() {
    const { scan_batch_no } = this.dialog.get_values();

        if (scan_batch_no) {
            frappe.call({
                method: "erpnext.stock.doctype.serial_and_batch_bundle.serial_and_batch_bundle.is_serial_batch_no_exists",
                args: {
                    item_code: this.item.item_code,
                    type_of_transaction: this.item.type_of_transaction,
                    batch_no: scan_batch_no,
                },
                callback: (r) => {
//                    this.update_batch_no();
                    this.update_batch_no_bb_0();
//                    this.fetch_batch_qty(scan_batch_no, warehouse);
                },
            });
        }
    }

    fetch_batch_qty_0(batch_no, warehouse) {
        frappe.call({
            method: "erpnext.stock.doctype.batch.batch.get_batch_qty",
            args: {
                batch_no: batch_no,
                warehouse: warehouse || this.item.warehouse || this.item.s_warehouse,
            },
            callback: (res) => {
                if (res.message) {
                    let batch_qty = res.message;
                    let entries = this.dialog.fields_dict.entries.df.data;
                    let existing_entry = entries.find((entry) => entry.batch_no === batch_no);

                    if (existing_entry) {
                        existing_entry.qty = batch_qty;
                    } else {
                        entries.push({
                            batch_no: batch_no,
                            qty: batch_qty,
                        });
                    }

                    this.dialog.fields_dict.entries.grid.refresh();
                    this.dialog.fields_dict.scan_batch_no.set_value("");
                } else {
                    frappe.msgprint(__('No quantity found for the batch.'));
                }
            },
        });
    }

    update_batch_no_bb_0() {
        const { scan_batch_no, warehouse } = this.dialog.get_values();

        if (scan_batch_no) {
            frappe.call({
                method: "erpnext.stock.doctype.batch.batch.get_batch_qty",
                args: {
                    batch_no: scan_batch_no,
                    warehouse: warehouse || this.item.warehouse || this.item.s_warehouse,
                },
                callback: (res) => {
                    if (res.message) {
                        let batch_qty = res.message;
                        let entries = this.dialog.fields_dict.entries.df.data;
                        let existing_entry = entries.find((entry) => entry.batch_no === scan_batch_no);

                        if (existing_entry) {
                            existing_entry.qty += batch_qty;
                        } else {
                            entries.push({
                                batch_no: scan_batch_no,
                                qty: batch_qty,
                            });
                        }

                        this.dialog.fields_dict.entries.grid.refresh();
                        this.dialog.fields_dict.scan_batch_no.set_value("");
                    } else {
                        frappe.msgprint(__('No quantity found for the batch.'));
                    }
                },
            });
        }
    }



//    scan_barcode_data() {
//        const { scan_batch_no } = this.dialog.get_values();
//
//        if (scan_batch_no) {
//            frappe.call({
//                method: "erpnext.stock.doctype.serial_and_batch_bundle.serial_and_batch_bundle.is_serial_batch_no_exists",
//                args: {
//                    item_code: this.item.item_code,
//                    type_of_transaction: this.item.type_of_transaction,
//                    batch_no: scan_batch_no,
//                },
//                callback: (r) => {
//                    this.update_batch_no();
//                },
//            });
//        }
//    }

    update_batch_no_0() {
        const { scan_batch_no } = this.dialog.get_values();

        if (scan_batch_no) {
            let existing_row = this.dialog.fields_dict.entries.df.data.filter((d) => {
                if (d.batch_no === scan_batch_no) {
                    return d;
                }
            });

            if (existing_row?.length) {
                existing_row[0].qty += 1;
            } else {
                this.dialog.fields_dict.entries.df.data.push({
                    batch_no: scan_batch_no,
                    qty: 1,
                });
            }

            this.dialog.fields_dict.scan_batch_no.set_value("");
        }

        this.dialog.fields_dict.entries.grid.refresh();
    }

    update_bundle_entries_0() {
        let entries = this.dialog.get_values().entries;
        let warehouse = this.dialog.get_value("warehouse");

        if ((entries && !entries.length) || !entries) {
            frappe.throw(__("Please add at least one Batch No"));
        }

        if (!warehouse) {
            frappe.throw(__("Please select a Warehouse"));
        }

        frappe
            .call({
                method: "erpnext.stock.doctype.serial_and_batch_bundle.serial_and_batch_bundle.add_serial_batch_ledgers",
                args: {
                    entries: entries,
                    child_row: this.item,
                    doc: this.frm.doc,
                    warehouse: warehouse,
                },
            })
            .then((r) => {
                this.callback && this.callback(r.message);
                this.frm.save();
                this.dialog.hide();
            });
    }

    edit_full_form_0() {
        let bundle_id = this.item.serial_and_batch_bundle;
        if (!bundle_id) {
            let _new = frappe.model.get_new_doc("Serial and Batch Bundle", null, null, true);

            _new.item_code = this.item.item_code;
            _new.warehouse = this.get_warehouse();
            _new.has_batch_no = this.item.has_batch_no;
            _new.type_of_transaction = this.item.type_of_transaction;
            _new.company = this.frm.doc.company;
            _new.voucher_type = this.frm.doc.doctype;
            bundle_id = _new.name;
        }

        frappe.set_route("Form", "Serial and Batch Bundle", bundle_id);
        this.dialog.hide();
    }

    get_warehouse() {
        return this.item?.type_of_transaction === "Outward"
            ? this.item.warehouse || this.item.s_warehouse
            : this.item.warehouse || this.item.t_warehouse;
    }

    render_data_0() {
        if (this.bundle || this.frm.doc.is_return) {
            frappe
                .call({
                    method: "erpnext.stock.doctype.serial_and_batch_bundle.serial_and_batch_bundle.get_serial_batch_ledgers",
                    args: {
                        item_code: this.item.item_code,
                        name: this.bundle,
                        voucher_no: !this.frm.is_new() ? this.item.parent : "",
                        child_row: this.frm.doc.is_return ? this.item : "",
                    },
                })
                .then((r) => {
                    if (r.message) {
                        this.set_data_0(r.message);
                    }
                });
        }
    }

    set_data_0(data) {
        data.forEach((d) => {
            d.qty = Math.abs(d.qty);
            d.name = d.child_row || d.name;
            this.dialog.fields_dict.entries.df.data.push(d);
        });

        this.dialog.fields_dict.entries.grid.refresh();
    }

    fetch_batch_qty_0() {
        const { batch_no, warehouse } = this.dialog.get_values();
        if (batch_no) {
            frappe.call({
                method: "erpnext.stock.doctype.batch.batch.get_batch_qty",
                args: {
                    batch_no: batch_no,
                    warehouse: warehouse || this.item.warehouse || this.item.s_warehouse,
                },
                callback: (res) => {
                    if (res.message) {
                        let batch_qty = res.message;
                        let entries = this.dialog.fields_dict.entries.df.data;
                        let existing_entry = entries.find((entry) => entry.batch_no === batch_no);

                        if (existing_entry) {
                            existing_entry.qty = batch_qty;
                        } else {
                            entries.push({
                                batch_no: batch_no,
                                qty: batch_qty,
                            });
                        }

                        this.dialog.fields_dict.entries.grid.refresh();
                    }
                },
            });
        }
    }
};





//   ==== END Fetch data from items table - A - Select Batch Method ====
// ===============================================================
// ===============================================================










//   ================================================================
//   ================================================================
//   ==== START  This trigger will check if the "Stock Entry Type" is set to
//               "Material Transfer for Manufacture" and then automatically apply the "Add" label to all items  ====




frappe.ui.form.on('Stock Entry', {
    after_save: function (frm) {
    if (frm.doc.docstatus === 0 && frm.doc.update_create_batch_bundles === 0) {
        frappe.call({
            method: "omsteel_test_001.omsteel_test_001.production_items_table.create_serial_and_batch_bundles",
            args: {
                doc_name: frm.doc.name
            },
            callback: function (response) {
                if (response.message) {
//                    frappe.msgprint(__('Serial and Batch Bundles created successfully.'));



                    let bundleMap = response.message;

                    // Update the Stock Entry Detail table
                    frm.doc.items.forEach(function(item) {
                        if (bundleMap[item.item_code]) {
                            item.serial_and_batch_bundle = bundleMap[item.item_code];
                        }
                    });

                    frm.refresh_field('items');

                    frm.set_value('update_create_batch_bundles', 1);

                    frm.save();

//                    frappe.msgprint(__('Serial and Batch Bundles created and updated successfully.'));

                }
            },
            error: function (error) {
                frappe.msgprint(__('Error: {0}', [error.message]));
            }
        });
        }
    }
});







//   ==== END This trigger will check if the "Stock Entry Type" is set to
//            "Material Transfer for Manufacture" and then automatically apply the "Add" label to all items  ====
// ===============================================================
// ===============================================================












//   ================================================================
//   ================================================================
//   ==== START  Fetch data from items table - A - Select Batch Method Update (2) ====





//  04AA6D
//  005700
//  4e4e4e
//  563627




frappe.ui.form.on('Stock Entry', {
    refresh: function(frm) {

    //    if (frm.doc.docstatus === 0 && frm.doc.stock_entry_type === 'Material Transfer for Manufacture' && frm.doc.bom_check === 0) {
    if (frm.doc.docstatus === 0 && frm.doc.stock_entry_type === 'Material Transfer for Manufacture') {
        frm.add_custom_button(__('Select Batch Method (2)'), function() {
            open_item_dialog_aa(frm);
        }).addClass('btn-warning').css({
                'color': 'white',
                'font-weight': 'bold',
                'background-color': '#563627'
        });
        }
    },


});

function open_item_dialog_aa(frm) {
    let d = new frappe.ui.Dialog({
        title: 'Select Item and Scan Batch Numbers',
        fields: [
            {
                label: 'Item Code',
                fieldname: 'item_code',
                fieldtype: 'Select',
                options: frm.doc.items.map(item => item.item_code),
                reqd: 1
            },
            {
                label: 'Warehouse',
                fieldname: 'warehouse',
                fieldtype: 'Select',
                options: [],
                hidden: 1,
                reqd: 1
            },
            {
                label: 'Scan Batch No',
                fieldname: 'batch_no',
                fieldtype: 'Select',
                options: [],
                hidden: 1,
                reqd: 0
            }
        ],
        primary_action_label: 'Fetch Quantity',
        primary_action(values) {

            fetch_quantity_aa(frm, values.item_code, values.warehouse, values.batch_no);
//            fetch_batch_data(values.item_code, values.warehouse, values.batch_no).then(() => {
//                frappe.msgprint(__('Batch data fetched successfully'));
//            }).catch(err => {
//                frappe.msgprint(__('Error fetching batch data: ') + err.message);
//            });
            d.hide();
        }
    });

    d.fields_dict.item_code.$input.on('change', function() {
        let selected_item_code = d.get_value('item_code');
        let warehouse_field = d.fields_dict.warehouse;
        let batch_no_field = d.fields_dict.batch_no;

        // Fetch warehouses based on the selected item code
        let warehouses = frm.doc.items
            .filter(item => item.item_code === selected_item_code)
            .map(item => item.s_warehouse || item.t_warehouse);

        // Update warehouse field options
        let unique_warehouses = [...new Set(warehouses)];
        warehouse_field.df.options = unique_warehouses.join('\n');

        // Set default value to the first option if available
        if (unique_warehouses.length > 0) {
            d.set_value('warehouse', unique_warehouses[0]);
        }

        warehouse_field.refresh();


        // Fetch batch numbers based on the selected item code and warehouse
        fetch_batch_numbers_aa(selected_item_code).then(batches => {
            // Format batch options to include batch_id and batch_qty
            let batch_options = batches.map(batch => `${batch.batch_id} (Qty: ${batch.batch_qty})`).join('\n');

            // Update batch_no field options
            batch_no_field.df.options = batch_options;
            batch_no_field.refresh();
        }).catch(err => {
            frappe.msgprint(__('Error fetching batch numbers: ') + err.message);
        });
    });

    d.show();
}

function fetch_batch_numbers_aa(item_code) {
    return new Promise((resolve, reject) => {
        frappe.call({
            method: 'omsteel_test_001.omsteel_test_001.production_items_table.fetch_batch_numbers',
            args: {
                item_code: item_code
            },
            callback: function(r) {
                if (r.message) {
                    resolve(r.message);
                } else {
                    resolve([]);
                }
            },
            error: function(err) {
                reject(err);
            }
        });
    });
}

function fetch_batch_data_aa(item_code, warehouse, batch_id) {
    frappe.call({
        method: 'omsteel_test_001.omsteel_test_001.production_items_table.get_batch_data',
        args: {
            item_code: item_code,
            warehouse: warehouse,
            batch_id: batch_id
        },
        callback: function(r) {
            if (r.message) {
                // Format the batch data into a string
                let batch_data_str = r.message.map(batch => {
                    return `Name: ${batch.batch_name}, Batch ID: ${batch.batch_id}, Batch Quantity: ${batch.batch_qty}`;
                }).join('\n');

//                // Display the batch data using frappe.msgprint
//                frappe.msgprint({
//                    title: __('Batch Details'),
//                    indicator: 'green',
//                    message: `<pre>${batch_data_str}</pre>`
//                });
            } else {
                frappe.msgprint(__('No batch data found.'));
            }
        },
        error: function(err) {
            frappe.msgprint(__('Error retrieving batch data: ') + err.message);
        }
    });
}

function fetch_quantity_aa(frm, item_code, warehouse, batch_no) {
    // Find the item in the items table
    let item = frm.doc.items.find(i => i.item_code === item_code);

    if (item) {
        // Fetch batch and serial number details
        select_batch_and_serial_no_aa(frm, item, warehouse, batch_no).then(() => {
//            frappe.msgprint(__('Batch and serial number details fetched successfully'));
        }).catch(err => {
            frappe.msgprint(__('Error fetching batch and serial number details: ') + err.message);
        });
    } else {
        frappe.msgprint(__('Item not found in the table'));
    }
}

function select_batch_and_serial_no_aa(frm, item, warehouse, batch_no) {
    return new Promise((resolve, reject) => {
        frappe.db.get_value("Item", item.item_code, ["has_batch_no", "has_serial_no"]).then((r) => {
            if (r.message && (r.message.has_batch_no || r.message.has_serial_no)) {
                item.has_serial_no = r.message.has_serial_no;
                item.has_batch_no = r.message.has_batch_no;
                item.type_of_transaction = item.s_warehouse ? "Outward" : "Inward";

                new erpnext.BatchPackageSelectorAA(frm, item, (r) => {
                    if (r) {
                        frappe.model.set_value(item.doctype, item.name, {
                            serial_and_batch_bundle: r.name,
                            use_serial_batch_fields: 0,
                            basic_rate: r.avg_rate,
                            qty: Math.abs(r.total_qty) / flt(item.conversion_factor || 1, precision("conversion_factor", item)),
                        });
                        resolve();
                    } else {
                        reject(new Error('Failed to fetch serial and batch package details'));
                    }
                });
            } else {
                reject(new Error('Item does not have batch or serial numbers'));
            }
        }).catch(err => {
            reject(err);
        });
    });
}








// =============  Class  Define the BatchPackageSelector class ================

erpnext.BatchPackageSelectorAA = class BatchPackageSelector {
    constructor(frm, item, callback) {
        this.frm = frm;
        this.item = item;
        this.qty = item.qty;
        this.callback = callback;
        this.bundle = this.item?.is_rejected
            ? this.item.rejected_serial_and_batch_bundle
            : this.item.serial_and_batch_bundle;

        this.make();
        this.render_data();
    }




    make() {
        let label = __("Batch Nos");
        let primary_label = this.bundle ? __("Update") : __("Add");
        primary_label += " " + label;

        this.dialog = new frappe.ui.Dialog({
            title: this.item?.title || primary_label,
            fields: this.get_dialog_fields(),
            primary_action_label: primary_label,
            primary_action: () => this.update_bundle_entries(),
            secondary_action_label: __("Edit Full Form (*)"),
            secondary_action: () => this.edit_full_form(),
            on_form_render: () => {
                // Trigger initial calculation when the dialog is rendered
                this.get_calc_qty_info();

                // Attach event handlers
                this.dialog.get_field("qty").df.onchange = () => this.get_calc_qty_info();
                this.dialog.get_field("scan_batch_no").df.onchange = () => this.get_calc_qty_info();
                this.dialog.get_field("entries").grid.on("data-change", () => this.get_calc_qty_info());


                // Ensure the Enter key doesn't trigger form submission
                this.dialog.get_field("scan_batch_no").$input.off('keydown').on('keydown', function(e) {
                    if (e.which === 13) {
                        e.preventDefault();
                    }
                });


            }


        });

//        // event handler to ignore Enter key for scan_batch_no field
//        this.dialog.get_field("scan_batch_no").$input.on('keypress', function(e) {
//            if (e.which === 13) {
//                e.preventDefault();
//            }
//        });


        this.dialog.get_field("scan_batch_no").$input.off('keydown').on('keydown', function(e) {
                    if (e.which === 13) {
                        e.preventDefault();
                    }
        });


        this.dialog.show();

        // Initialize fields
        let qty = this.item.stock_qty || this.item.transfer_qty || this.item.qty;

        if (this.item?.is_rejected) {
            qty = this.item.rejected_qty;
        }

        qty = Math.abs(qty);
        if (qty > 0) {
            this.dialog.set_value("qty", qty).then(() => {
                if (this.item.batch_no && !this.item.serial_and_batch_bundle) {
                    this.dialog.set_value("scan_batch_no", this.item.batch_no);
                    frappe.model.set_value(this.item.doctype, this.item.name, "batch_no", "");
                }

                this.dialog.fields_dict.entries.grid.refresh();
            });
        }
    }




    get_dialog_fields() {
        let fields = [
            {
                fieldtype: "Data",
                options: "Barcode",
                fieldname: "scan_batch_no",
                label: __("Scan Batch No"),
//                onchange: () => this.scan_barcode_data(),
                onchange: () => {
                    this.scan_barcode_data();
                    this.update_difference_qty();
                    this.update_difference_qty_2();
                    this.update_difference_qty_3();
                },
            },

            {
                fieldtype: "Link",
                fieldname: "warehouse",
                label: __("Warehouse"),
                read_only: 1,
                options: "Warehouse",
                default: this.get_warehouse(),
                onchange: () => {
                    this.item.warehouse = this.dialog.get_value("warehouse");
                    this.get_auto_data();
                },
                get_query: () => {
                    return {
                        filters: {
                            is_group: 0,
                            company: this.frm.doc.company,
                        },
                    };
                },
            },
            {
                fieldtype: "Float",
                fieldname: "qty",
                label: __("Qty to Fetch"),
//                onchange: () => this.get_auto_data(),
                onchange: () => {
                    this.get_auto_data();
                    this.update_difference_qty();
                    this.update_difference_qty_2();
                    this.update_difference_qty_3();
                },
                read_only: 1
            },


            {
                fieldtype: "Column Break",
            },

            {
                fieldtype: 'Float',
                fieldname: 'calc_qty',
                label: __('Calc Qty'),
//                onchange: () => this.get_auto_data(),
                onchange: () => {
                    this.get_auto_data();
                    this.update_difference_qty();
                    this.update_difference_qty_2();
                    this.update_difference_qty_3();
                },
                read_only: 1
            },
            {
                fieldtype: 'Button',
                fieldname: 'remove_all_data_table',
                label: __('Remove All Data Table'),
                click: () => this.clear_all_entries(),
//                click: () => {
//                    this.clear_all_entries();
////                    this.update_difference_qty();
////                    this.update_difference_qty_2();
//                },
//                read_only: 1,
            },
            {
                fieldtype: 'Float',
                fieldname: 'difference_qty',
                label: __('Difference Qty'),
                read_only: 1,
            },
            {
                fieldtype: 'Float',
                fieldname: 'difference_qty_2',
                label: __('Difference Qty 2'),
                read_only: 0,
                hidden: 1,
            },
            {
                fieldtype: 'Float',
                fieldname: 'difference_qty_the_last_child',
                label: __('Difference Qty The Last Child'),
                read_only: 0,
                hidden: 1,
            },
            {
                fieldtype: 'Float',
                fieldname: 'update_qty_the_last_child',
                label: __('Update Qty The Last Child Manual'),
                read_only: 0,
                hidden: 1,
//                onchange: () => this.update_last_child_qty()
                onchange: () => {
                    this.update_last_child_qty();
                    this.update_difference_qty();
                    this.update_difference_qty_2();
                    this.update_difference_qty_3();
                },
            },

            {
                fieldtype: 'Button',
                fieldname: 'update_difference_qty_2_button',
                label: __('Automatically Update the Difference Quantity'),
                click: () => {
                    this.update_difference_qty_change();
                    this.update_difference_qty();
                    this.update_last_child_qty();
                    this.update_last_child_qty_2();
                    this.calculate_qty();

                },
//                click: () => this.update_difference_qty_2(),
//                read_only: 1,
            },

            {
                fieldtype: "Section Break",
            },
            {
                fieldname: "entries",
                fieldtype: "Table",
//                allow_bulk_edit: true,
                allow_bulk_edit: false,
                data: [],
//                fields: this.get_dialog_table_fields(),
                fields: this.get_dialog_table_fields().map(field => {
                    field.read_only = true;
                    return field;
                }),
//                onchange: () => {
//                    this.update_difference_qty();
//                    this.update_difference_qty_2();
//                },
                onload: () => {
                    this.setup_table_change_listeners();
                }

            }

        ];

        return fields;
    }




            //  Method to set up change listeners
            setup_table_change_listeners() {
                let table = this.dialog.get_field('entries').grid;

                table.fields.forEach(field => {
                    field.$input.on('change', () => {
                        this.update_difference_qty();
                        this.update_difference_qty_2();
                        this.update_difference_qty_3();
                    });
                });
            }


    calculate_qty() {
        let total_qty = 0;
        const rows = this.dialog.get_field("entries").grid.get_data();
        rows.forEach(row => {
            total_qty += row.qty || 0;
        });
//        frappe.msgprint("Total Quantity Calculated: " + total_qty);
        this.dialog.set_value("calc_qty", total_qty);


        // Check if calc_qty matches qty
        const qty_to_fetch = this.dialog.get_value("qty");
        if (total_qty === qty_to_fetch) {
            frappe.show_alert({
                message: __('The calculated quantity matches the required quantity.'),
                indicator: 'green'
            });
        } else {
            frappe.show_alert({
                message: __('The calculated quantity does not match the required quantity.'),
                indicator: 'red'
            });
        }

        this.update_difference_qty_2();
        this.update_difference_qty_3();

    }






    update_last_child_qty() {
        const new_qty = this.dialog.get_value('update_qty_the_last_child');

        if (new_qty !== null && new_qty !== undefined) {
            let entries = this.dialog.get_field('entries').grid.get_data();

            if (entries.length > 0) {
                let last_row = entries[entries.length - 1];
                last_row.qty = new_qty;
                this.dialog.get_field('entries').grid.refresh();
            }

            this.calculate_qty();
            this.update_difference_qty();
            this.update_difference_qty_2();
            this.update_difference_qty_3();
        }
    }




//    update_last_child_qty() {
//        const new_qty = parseFloat(this.dialog.get_value('difference_qty')) || 0;
//
//        let entries = this.dialog.get_field('entries').grid.get_data();
//
//        if (entries.length > 0) {
//            let last_row = entries[entries.length - 1];
//            last_row.qty = new_qty;
//
//            this.dialog.get_field('entries').grid.refresh();
//        }
//    }




    update_last_child_qty_2() {
        let new_qty = parseFloat(this.dialog.get_value('difference_qty')) || 0;

        let entries = this.dialog.get_field('entries').grid.get_data();

        if (entries.length > 0) {
            let last_row = entries[entries.length - 1];
            last_row.qty = new_qty;

            this.dialog.get_field('entries').grid.refresh();
        }


        const qty = parseFloat(this.dialog.get_value('qty')) || 0;
        const calc_qty = parseFloat(this.dialog.get_value('calc_qty')) || 0;
        const difference_qty = calc_qty - qty;

//        this.dialog.set_value('difference_qty', difference_qty);
        this.dialog.set_value('difference_qty', 0);
        this.dialog.get_field('difference_qty').refresh();

    }


//    update_difference_qty_change() {
//        const difference_qty = parseFloat(this.dialog.get_value('difference_qty')) || 0;
//        let entries = this.dialog.get_field('entries').grid.get_data();
//
//        let total_qty = 0;
//        if (entries.length > 0) {
//            total_qty = entries.reduce((sum, row) => sum + (parseFloat(row.qty) || 0), 0);
//        }
//
//        this.dialog.set_value('difference_qty_2', total_qty);
//
//        if (difference_qty <= 0) {
//            if (entries.length > 0) {
//                entries.pop();
//
//                this.dialog.get_field('entries').grid.set_data(entries);
//                this.dialog.get_field('entries').grid.refresh();
//            }
//        }
//
//    }




    update_difference_qty_change() {
        const difference_qty = parseFloat(this.dialog.get_value('difference_qty')) || 0;

        if (difference_qty <= 0) {
            frappe.msgprint("Negative or Zero Value")
        }

    }


//    clear_all_entries() {
//        let table_field = this.dialog.get_field('entries');
//
//        table_field.df.data = [];
//        table_field.grid.refresh();
//
//        this.calculate_qty();
//        this.update_difference_qty();
//        this.update_difference_qty_2();
//    }




    clear_all_entries() {
        let table_field = this.dialog.get_field('entries');
        table_field.df.data = [];
        table_field.grid.refresh();

        this.calculate_qty();
        this.update_difference_qty();
        this.update_difference_qty_2();
        this.update_difference_qty_3();
    }




//    update_difference_qty() {
//        const qty_to_fetch = parseFloat(this.dialog.get_value('qty')) || 0;
//        const calc_qty = parseFloat(this.dialog.get_value('calc_qty')) || 0;
//
////        const difference = qty_to_fetch - calc_qty;
//        const difference = ( calc_qty - qty_to_fetch );
//
//        this.dialog.set_value('difference_qty', difference);
//    }




      update_difference_qty() {
            const qty_to_fetch = parseFloat(this.dialog.get_value('qty')) || 0;
            const calc_qty = parseFloat(this.dialog.get_value('calc_qty')) || 0;
            const diff_qty = parseFloat(this.dialog.get_value('difference_qty_the_last_child')) || 0;

    //        const difference = qty_to_fetch - calc_qty;
//            const difference = ( calc_qty - qty_to_fetch );

            const difference_var = ( calc_qty - qty_to_fetch );
            const difference = ( diff_qty - difference_var );

            this.dialog.set_value('difference_qty', difference);
        }



    update_difference_qty_2() {
//        const calc_difference_qty = parseFloat(this.dialog.get_value('difference_qty')) || 0;
//        const calc_qty = parseFloat(this.dialog.get_value('calc_qty')) || 0;

        let entries = this.dialog.get_field('entries').grid.get_data();
        let total_qty = 0;

        if (entries.length > 0) {
            total_qty = entries.reduce((sum, row) => sum + (parseFloat(row.qty) || 0), 0);
        }

        this.dialog.set_value('difference_qty_2', total_qty);

    }








    update_difference_qty_3() {
//        const calc_difference_qty = parseFloat(this.dialog.get_value('difference_qty')) || 0;
//        const calc_qty = parseFloat(this.dialog.get_value('calc_qty')) || 0;


        let entries = this.dialog.get_field('entries').grid.get_data();

        let last_qty = 0;

        if (entries.length > 0) {
            last_qty = parseFloat(entries[entries.length - 1].qty) || 0;
        }

        this.dialog.set_value('difference_qty_the_last_child', last_qty);

    }


//    update_difference_qty_2() {
//        const calc_difference_qty = parseFloat(this.dialog.get_value('difference_qty')) || 0;
//
//        const calc_qty = parseFloat(this.dialog.get_value('calc_qty')) || 0;
//
//        let entries = this.dialog.get_field('entries').grid.get_data();
//        let last_row_qty = 0;
//
//        if (entries.length > 0) {
//            let last_row = entries[entries.length - 1];
//            last_row_qty = parseFloat(last_row.qty) || 0;
//        }
//
////        const difference_qty_2 = last_row_qty - calc_difference_qty;
//        const difference_qty_2 = calc_qty - calc_difference_qty;
//        this.dialog.set_value('difference_qty_2', difference_qty_2);
//    }





//
//
//    update_difference_qty_2() {
//        const calc_difference_qty = parseFloat(this.dialog.get_value('difference_qty')) || 0;
//        let entries = this.dialog.get_field('entries').grid.get_data();
//
//        let last_row_qty = 0;
//
//        if (entries.length > 0) {
//            let last_row = entries[entries.length - 1];
//            last_row_qty = parseFloat(last_row.qty) || 0;
//        }
//
//        const difference_qty_2 = last_row_qty - calc_difference_qty;
//        this.dialog.set_value('difference_qty_2', difference_qty_2);
//    }
//
//







    get_dialog_table_fields() {
        return [
            {
                fieldtype: "Link",
                options: "Batch",
                fieldname: "batch_no",
                label: __("Batch No"),
                in_list_view: 1,
                get_query: () => {
                    let is_inward = false;
                    if (
                        (["Purchase Receipt", "Purchase Invoice"].includes(this.frm.doc.doctype) &&
                            !this.frm.doc.is_return) ||
                        (this.frm.doc.doctype === "Stock Entry" &&
                            this.frm.doc.purpose === "Material Receipt")
                    ) {
                        is_inward = true;
                    }

                    return {
                        query: "erpnext.controllers.queries.get_batch_no",
                        filters: {
                            item_code: this.item.item_code,
                            warehouse: this.item.s_warehouse || this.item.t_warehouse || this.item.warehouse,
                            is_inward: is_inward,
                        },
                    };
                },
                onchange: () => {
                    this.fetch_batch_data_aaa();
                    this.calculate_qty();

//                    this.update_difference_qty();
//                    this.update_difference_qty_2();
                },
            },
            {
                fieldtype: "Float",
                fieldname: "qty",
                label: __("Quantity - Total"),
                in_list_view: 1,
                default: 0,
                onchange: () => {
                    this.calculate_qty();
                    this.update_difference_qty();
                    this.update_difference_qty_2();
                    this.update_difference_qty_3();
                }

            },
            {
                fieldtype: "Data",
                fieldname: "name",
                label: __("Name"),
                hidden: 0,
            },
        ];
    }



    fetch_batch_data_aaa() {
        const { batch_no, warehouse } = this.dialog.get_values();
        if (batch_no) {
            frappe.call({
                method: 'omsteel_test_001.omsteel_test_001.production_items_table.get_batch_data',
                args: {
                    item_code: this.item.item_code,
                    warehouse: warehouse || this.item.warehouse || this.item.s_warehouse,
                    batch_id: batch_no
                },
                callback: function(r) {
                    if (r.message) {
                        // Format the batch data into a string
                        let batch_data_str = r.message.map(batch => {
                            return `Name: ${batch.batch_name}, Batch ID: ${batch.batch_id}, Batch Quantity: ${batch.batch_qty}`;
                        }).join('\n');

                        // Display the batch data using frappe.msgprint
                        frappe.msgprint({
                            title: __('Batch Details'),
                            indicator: 'green',
                            message: `<pre>${batch_data_str}</pre>`
                        });
                    } else {
                        frappe.msgprint(__('No batch data found.'));
                    }
                },
                error: function(err) {
                    frappe.msgprint(__('Error retrieving batch data: ') + err.message);
                }
            });
        }
    }

    get_auto_data() {
        let { qty, based_on } = this.dialog.get_values();

        if (this.item.serial_and_batch_bundle || this.item.rejected_serial_and_batch_bundle) {
            if (this.qty && qty === Math.abs(this.qty)) {
                return;
            }
        }

        if (this.item.batch_no) {
            return;
        }

        if (!based_on) {
            based_on = "FIFO";
        }

        if (qty) {
            frappe.call({
                method: "erpnext.stock.doctype.serial_and_batch_bundle.serial_and_batch_bundle.get_auto_data",
                args: {
                    item_code: this.item.item_code,
                    warehouse: this.item.warehouse || this.item.s_warehouse,
                    has_batch_no: this.item.has_batch_no,
                    qty: qty,
                    based_on: based_on,
                },
                callback: (r) => {
                    if (r.message) {
                        this.dialog.fields_dict.entries.df.data = r.message;
                        this.dialog.fields_dict.entries.grid.refresh();
                    }
                },
            });
        }
    }





    scan_barcode_data() {
    const { scan_batch_no } = this.dialog.get_values();

        if (scan_batch_no) {
            frappe.call({
                method: "erpnext.stock.doctype.serial_and_batch_bundle.serial_and_batch_bundle.is_serial_batch_no_exists",
                args: {
                    item_code: this.item.item_code,
                    type_of_transaction: this.item.type_of_transaction,
                    batch_no: scan_batch_no,
                },
                callback: (r) => {
////                    this.update_batch_no();
                    this.update_batch_no_bb();
////                    this.fetch_batch_qty(scan_batch_no, warehouse);
                },
            });
        }

        this.calculate_qty();
    }

    fetch_batch_qty(batch_no, warehouse) {
        frappe.call({
            method: "erpnext.stock.doctype.batch.batch.get_batch_qty",
            args: {
                batch_no: batch_no,
                warehouse: warehouse || this.item.warehouse || this.item.s_warehouse,
            },
            callback: (res) => {
                if (res.message) {
                    let batch_qty = res.message;
                    let entries = this.dialog.fields_dict.entries.df.data;
                    let existing_entry = entries.find((entry) => entry.batch_no === batch_no);

                    if (existing_entry) {
                        existing_entry.qty = batch_qty;
                    } else {
                        entries.push({
                            batch_no: batch_no,
                            qty: batch_qty,
                        });
                    }

                    this.dialog.fields_dict.entries.grid.refresh();
                    this.dialog.fields_dict.scan_batch_no.set_value("");
                } else {
                    frappe.msgprint(__('No quantity found for the batch.'));
                }
            },
        });
    }






    update_batch_no_bb() {
        const { scan_batch_no, warehouse } = this.dialog.get_values();

        if (scan_batch_no) {
            frappe.call({
                method: "erpnext.stock.doctype.batch.batch.get_batch_qty",
                args: {
                    batch_no: scan_batch_no,
                    warehouse: warehouse || this.item.warehouse || this.item.s_warehouse,
                },
                callback: (res) => {
                    if (res.message) {
                        let batch_qty = res.message;
                        let entries = this.dialog.fields_dict.entries.df.data;
                        let existing_entry = entries.find((entry) => entry.batch_no === scan_batch_no);

                        if (existing_entry) {
//                            frappe.msgprint(__('Batch No already exists in the table.'));

                            frappe.show_alert({
                                message: __('Batch No already exists in the table.'),
                                indicator: 'red'
                            });

                            this.dialog.fields_dict.scan_batch_no.set_value("");
                        } else {
                            entries.push({
                                batch_no: scan_batch_no,
                                qty: batch_qty,
                            });

                            this.dialog.fields_dict.entries.grid.refresh();
                            this.dialog.fields_dict.scan_batch_no.set_value("");
                        }
                    } else {
//                        frappe.msgprint(__('No quantity found for the batch.'));
                        frappe.show_alert({
                                message: __('No quantity found for the batch.'),
                                indicator: 'red'
                        });
                    }
                },
            });
        }
    }




    update_batch_no() {
        const { scan_batch_no } = this.dialog.get_values();

        if (scan_batch_no) {
            let existing_row = this.dialog.fields_dict.entries.df.data.filter((d) => {
                if (d.batch_no === scan_batch_no) {
                    return d;
                }
            });

            if (existing_row?.length) {
                existing_row[0].qty += 1;
            } else {
                this.dialog.fields_dict.entries.df.data.push({
                    batch_no: scan_batch_no,
                    qty: 1,
                });
            }

            this.dialog.fields_dict.scan_batch_no.set_value("");
        }

        this.dialog.fields_dict.entries.grid.refresh();
    }





    update_bundle_entries() {
        let entries = this.dialog.get_values().entries;
        let warehouse = this.dialog.get_value("warehouse");

        if ((entries && !entries.length) || !entries) {
            frappe.throw(__("Please add at least one Batch No"));
        }

        if (!warehouse) {
            frappe.throw(__("Please select a Warehouse"));
        }

        // Calculate total quantity
        let total_qty = 0;
        entries.forEach(row => {
            total_qty += row.qty || 0;
        });

        // Get the value of qty to fetch
        const qty_to_fetch = this.dialog.get_value("qty");

        // Check if calc_qty matches qty_to_fetch
        if (total_qty !== qty_to_fetch) {
            frappe.show_alert({
                message: __('The calculated quantity does not match the required quantity.'),
                indicator: 'red'
            });
            return;
        } else {
            frappe.show_alert({
                message: __('The calculated quantity matches the required quantity.'),
                indicator: 'green'
            });
        }

        frappe
            .call({
                method: "erpnext.stock.doctype.serial_and_batch_bundle.serial_and_batch_bundle.add_serial_batch_ledgers",
                args: {
                    entries: entries,
                    child_row: this.item,
                    doc: this.frm.doc,
                    warehouse: warehouse,
                },
            })
            .then((r) => {
                this.callback && this.callback(r.message);
                this.frm.save();
                this.dialog.hide();
            });
    }




    edit_full_form() {
        let bundle_id = this.item.serial_and_batch_bundle;
        if (!bundle_id) {
            let _new = frappe.model.get_new_doc("Serial and Batch Bundle", null, null, true);

            _new.item_code = this.item.item_code;
            _new.warehouse = this.get_warehouse();
            _new.has_batch_no = this.item.has_batch_no;
            _new.type_of_transaction = this.item.type_of_transaction;
            _new.company = this.frm.doc.company;
            _new.voucher_type = this.frm.doc.doctype;
            bundle_id = _new.name;
        }

        frappe.set_route("Form", "Serial and Batch Bundle", bundle_id);
        this.dialog.hide();
    }

    get_warehouse() {
        return this.item?.type_of_transaction === "Outward"
            ? this.item.warehouse || this.item.s_warehouse
            : this.item.warehouse || this.item.t_warehouse;
    }

    render_data() {
        if (this.bundle || this.frm.doc.is_return) {
            frappe
                .call({
                    method: "erpnext.stock.doctype.serial_and_batch_bundle.serial_and_batch_bundle.get_serial_batch_ledgers",
                    args: {
                        item_code: this.item.item_code,
                        name: this.bundle,
                        voucher_no: !this.frm.is_new() ? this.item.parent : "",
                        child_row: this.frm.doc.is_return ? this.item : "",
                    },
                })
                .then((r) => {
                    if (r.message) {
                        this.set_data(r.message);
                    }
                });
        }
    }

    set_data(data) {
        data.forEach((d) => {
            d.qty = Math.abs(d.qty);
            d.name = d.child_row || d.name;
            this.dialog.fields_dict.entries.df.data.push(d);
        });

        this.dialog.fields_dict.entries.grid.refresh();
    }

    fetch_batch_qty() {
        const { batch_no, warehouse } = this.dialog.get_values();
        if (batch_no) {
            frappe.call({
                method: "erpnext.stock.doctype.batch.batch.get_batch_qty",
                args: {
                    batch_no: batch_no,
                    warehouse: warehouse || this.item.warehouse || this.item.s_warehouse,
                },
                callback: (res) => {
                    if (res.message) {
                        let batch_qty = res.message;
                        let entries = this.dialog.fields_dict.entries.df.data;
                        let existing_entry = entries.find((entry) => entry.batch_no === batch_no);

                        if (existing_entry) {
                            existing_entry.qty = batch_qty;
                        } else {
                            entries.push({
                                batch_no: batch_no,
                                qty: batch_qty,
                            });
                        }

                        this.dialog.fields_dict.entries.grid.refresh();
                    }
                },
            });
        }
    }
};






//   ==== END Fetch data from items table - A - Select Batch Method Update (2) ====
// ===============================================================
// ===============================================================










//   ================================================================
//   ================================================================
//   ==== START Fetch data from items table - Function to select batch and serial number ====








frappe.ui.form.on('Stock Entry', {
    refresh: function(frm) {
        if (frm.doc.docstatus === 0 && frm.doc.stock_entry_type === 'Material Transfer for Manufacture') {
            frm.add_custom_button(__('Fetch Batch and Quantity'), function() {
                open_item_dialog(frm);
            }, __("Fetch Additional Batch"))
            .addClass('btn-warning')
            .css({
                'color': 'white',
                'font-weight': 'bold',
                'background-color': '#274472',
                'margin-top': '15px',
                'margin-bottom': '8px'
            });
        }
    }
});




function open_item_dialog(frm) {
    let d = new frappe.ui.Dialog({
        title: 'Select Item and Scan Batch Numbers',
        fields: [
            {
                label: 'Item Code',
                fieldname: 'item_code',
                fieldtype: 'Select',
                options: frm.doc.items.map(item => item.item_code),
                reqd: 1
            },
            {
                label: 'Warehouse',
                fieldname: 'warehouse',
                fieldtype: 'Select',
                options: [],
                reqd: 1
            },
            {
                label: 'Scan Batch No',
                fieldname: 'batch_no',
                fieldtype: 'Select',
                options: [],
                reqd: 0
            }
        ],
        primary_action_label: 'Fetch Quantity',
        primary_action(values) {
            fetch_quantity(frm, values.item_code, values.warehouse, values.batch_no);
//            fetch_batch_data(values.item_code, values.warehouse, values.batch_no).then(() => {
//                frappe.msgprint(__('Batch data fetched successfully'));
//            }).catch(err => {
//                frappe.msgprint(__('Error fetching batch data: ') + err.message);
//            });
            d.hide();
        }
    });

    d.fields_dict.item_code.$input.on('change', function() {
        let selected_item_code = d.get_value('item_code');
        let warehouse_field = d.fields_dict.warehouse;
        let batch_no_field = d.fields_dict.batch_no;

        // Fetch warehouses based on the selected item code
        let warehouses = frm.doc.items
            .filter(item => item.item_code === selected_item_code)
            .map(item => item.s_warehouse || item.t_warehouse);

        // Update warehouse field options
        let unique_warehouses = [...new Set(warehouses)];
        warehouse_field.df.options = unique_warehouses.join('\n');

        // Set default value to the first option if available
        if (unique_warehouses.length > 0) {
            d.set_value('warehouse', unique_warehouses[0]);
        }

        warehouse_field.refresh();


        // Fetch batch numbers based on the selected item code and warehouse
        fetch_batch_numbers(selected_item_code).then(batches => {
            // Format batch options to include batch_id and batch_qty
            let batch_options = batches.map(batch => `${batch.batch_id} (Qty: ${batch.batch_qty})`).join('\n');

            // Update batch_no field options
            batch_no_field.df.options = batch_options;
            batch_no_field.refresh();
        }).catch(err => {
            frappe.msgprint(__('Error fetching batch numbers: ') + err.message);
        });
    });



//        // Fetch batch numbers based on the selected item code and warehouse
//        fetch_batch_numbers(selected_item_code).then(batches => {
//            // Format batch options to include batch_id and batch_qty
////            let batch_options = batches.map(batch => `${batch.batch_id} (Qty: ${batch.batch_qty})`).join('\n');
//            let batch_options = batches.map(batch => `${batch.batch_id}`).join('\n');
//
//            // Update batch_no field options
//            batch_no_field.df.options = batch_options;
//            batch_no_field.refresh();
//        }).catch(err => {
//            frappe.msgprint(__('Error fetching batch numbers: ') + err.message);
//        });
//    });


    d.show();
}

function fetch_batch_numbers(item_code) {
    return new Promise((resolve, reject) => {
        frappe.call({
            method: 'omsteel_test_001.omsteel_test_001.production_items_table.fetch_batch_numbers',
            args: {
                item_code: item_code
            },
            callback: function(r) {
                if (r.message) {
                    resolve(r.message);
                } else {
                    resolve([]);
                }
            },
            error: function(err) {
                reject(err);
            }
        });
    });
}

function fetch_batch_data(item_code, warehouse, batch_id) {
    frappe.call({
        method: 'omsteel_test_001.omsteel_test_001.production_items_table.get_batch_data',
        args: {
            item_code: item_code,
            warehouse: warehouse,
            batch_id: batch_id
        },
        callback: function(r) {
            if (r.message) {
                // Format the batch data into a string
                let batch_data_str = r.message.map(batch => {
                    return `Name: ${batch.batch_name}, Batch ID: ${batch.batch_id}, Batch Quantity: ${batch.batch_qty}`;
                }).join('\n');

//                // Display the batch data using frappe.msgprint
//                frappe.msgprint({
//                    title: __('Batch Details'),
//                    indicator: 'green',
//                    message: `<pre>${batch_data_str}</pre>`
//                });
            } else {
                frappe.msgprint(__('No batch data found.'));
            }
        },
        error: function(err) {
            frappe.msgprint(__('Error retrieving batch data: ') + err.message);
        }
    });
}

function fetch_quantity(frm, item_code, warehouse, batch_no) {
    // Find the item in the items table
    let item = frm.doc.items.find(i => i.item_code === item_code);

    if (item) {
        // Fetch batch and serial number details
        select_batch_and_serial_no(frm, item, warehouse, batch_no).then(() => {
//            frappe.msgprint(__('Batch and serial number details fetched successfully'));
        }).catch(err => {
            frappe.msgprint(__('Error fetching batch and serial number details: ') + err.message);
        });
    } else {
        frappe.msgprint(__('Item not found in the table'));
    }
}

function select_batch_and_serial_no(frm, item, warehouse, batch_no) {
    return new Promise((resolve, reject) => {
        frappe.db.get_value("Item", item.item_code, ["has_batch_no", "has_serial_no"]).then((r) => {
            if (r.message && (r.message.has_batch_no || r.message.has_serial_no)) {
                item.has_serial_no = r.message.has_serial_no;
                item.has_batch_no = r.message.has_batch_no;
                item.type_of_transaction = item.s_warehouse ? "Outward" : "Inward";

                new erpnext.SerialBatchPackageSelector(frm, item, (r) => {
                    if (r) {
                        frappe.model.set_value(item.doctype, item.name, {
                            serial_and_batch_bundle: r.name,
                            use_serial_batch_fields: 0,
                            basic_rate: r.avg_rate,
                            qty: Math.abs(r.total_qty) / flt(item.conversion_factor || 1, precision("conversion_factor", item)),
                        });
                        resolve();
                    } else {
                        reject(new Error('Failed to fetch serial and batch package details'));
                    }
                });
            } else {
                reject(new Error('Item does not have batch or serial numbers'));
            }
        }).catch(err => {
            reject(err);
        });
    });
}





//   ==== END Fetch data from items table - Function to select batch and serial number ====
//   ================================================================
//   ================================================================








//   ================================================================
//   ================================================================
//   ==== START Making custom stock entry with qty ====











//frappe.ui.form.on('Work Order', {
//    refresh: function(frm) {
//        if (frm.doc.status != "Closed" && frm.doc.docstatus === 1) {
//            frm.add_custom_button(__('Modify Qty'), function() {
//                frm.trigger('show_custom_dialog');
//            });
//        }
//    },
//
//    show_custom_dialog: function(frm) {
//        let max = this.get_max_transferable_qty(frm, __("Modify"));
//        let dialog = new frappe.ui.Dialog({
//            title: __("Modify Quantity"),
//            fields: [
//                {
//                    fieldtype: "Float",
//                    label: __("Qty"),
//                    fieldname: "qty",
//                    description: __("Max: {0}", [max]),
//                    default: max,
//                }
//            ],
//            primary_action_label: __('Submit'),
//            primary_action: (data) => {
//                let entered_qty = data.qty;
//
//                max += (frm.doc.qty * (frm.doc.__onload.overproduction_percentage || 0.0)) / 100;
//                if (entered_qty > max) {
//                    frappe.msgprint(__("Quantity must not be more than {0}", [max]));
//                    return;
//                }
//
//                frappe.msgprint(__('Quantity updated successfully.'));
//                dialog.hide();
//            }
//        });
//
//        dialog.$wrapper.find('.modal-footer').append(`
//            <button class="btn btn-primary" id="modify-qty-btn">
//                ${__('Modify Qty')}
//            </button>
//        `);
//
//        dialog.$wrapper.find('#modify-qty-btn').on('click', function() {
//            let entered_qty = dialog.get_values().qty;
//
//            max += (frm.doc.qty * (frm.doc.__onload.overproduction_percentage || 0.0)) / 100;
//            if (entered_qty > max) {
//                frappe.msgprint(__("Quantity must not be more than {0}", [max]));
//                return;
//            }
//
//            frappe.msgprint(__('Quantity modified successfully.'));
//            dialog.hide();
//        });
//
//        dialog.show();
//    }
//});















// Calculate calculate_difference_qty_a_010

frappe.ui.form.on('Work Order', {
//    refresh: function(frm) {
    onload: function(frm) {
        if (frm.doc.docstatus === 0 || frm.doc.docstatus === 1) {
            update_difference(frm);
        }
    },
    produced_qty: function(frm) {
        if (frm.doc.docstatus === 0 || frm.doc.docstatus === 1) {
            update_difference(frm);
        }
    },
    process_loss_qty: function(frm) {
        if (frm.doc.docstatus === 0 || frm.doc.docstatus === 1) {
            update_difference(frm);
        }
    }
});



function update_difference(frm) {
    if (frm.doc.qty !== undefined && frm.doc.produced_qty !== undefined && frm.doc.process_loss_qty !== undefined
    && frm.doc.material_transferred_for_manufacturing !== undefined) {
        let total_produced_loss = flt(frm.doc.produced_qty) + flt(frm.doc.process_loss_qty);
        let difference = flt(frm.doc.material_transferred_for_manufacturing) - total_produced_loss;
        difference = difference < 0 ? 0 : difference;

        frm.set_value('calculate_difference_qty_a_010', difference);
    }
}




//function update_difference(frm) {
//    if (frm.doc.qty !== undefined && frm.doc.produced_qty !== undefined && frm.doc.process_loss_qty !== undefined) {
//        let total_produced_loss = flt(frm.doc.produced_qty) + flt(frm.doc.process_loss_qty);
//        let difference = flt(frm.doc.qty) - total_produced_loss;
//        difference = difference < 0 ? 0 : difference;
//
//        frm.set_value('calculate_difference_qty_a_010', difference);
//    }
//}








//   ==== END Making custom stock entry with qty ====
//   ================================================================
//   ================================================================















//   ================================================================
//   ================================================================
//   ================================================================
//   ================================================================



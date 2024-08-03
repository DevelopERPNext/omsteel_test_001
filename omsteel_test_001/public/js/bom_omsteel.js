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
            }).addClass('btn-warning').css({
                'color': 'white',
                'font-weight': 'bold',
                'background-color': '#274472'
            });
        }
    }
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
        }).addClass('btn-warning').css({
                'color': 'white',
                'font-weight': 'bold',
                'background-color': '#274472'
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
                label: 'Qty',
                fieldname: 'qty',
                fieldtype: 'Float',
//                options: frm.doc.items.map(item => item.qty),
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

        // Fetch warehouses based on the selected item code
        let warehouses = frm.doc.items
            .filter(item => item.item_code === selected_item_code)
            .map(item => item.s_warehouse || item.t_warehouse);

        // Fetch Qty based on the selected item code
        let qty = frm.doc.items
            .filter(item => item.item_code === selected_item_code)
            .map(item => item.qty);


        // Fetch idx based on the selected item code
        let idxs = frm.doc.items
            .filter(item => item.item_code === selected_item_code)
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

    // When the idx changes, update the quantity field accordingly
    d.fields_dict.idx.$input.on('change', function() {
        let selected_item_code = d.get_value('item_code');
        let selected_idx = parseInt(d.get_value('idx'));

//        frappe.show_alert({
//                message: __('Selected idx: {0}', [selected_idx]),
//                indicator: 'red'
//        });
        update_qty_field(frm, selected_item_code, selected_idx, d.fields_dict.qty);
    });


    d.show();
}





// Helper function to get filtered item options
function getFilteredItemOptions(items) {
    let filteredItems = items.filter(item => item.is_finished_item || item.is_scrap_item);
    return filteredItems.map(item => item.item_code).join('\n');
}


// Update quantity field based on selected item code and idx
function update_qty_field(frm, item_code, idx, qty_field) {
//    frappe.show_alert({
//        message: __('Updating qty field for item_code: {0} and idx: {1}', [item_code, idx]),
//        indicator: 'red'
//    });

    // Find the item with the specified item_code and idx
    let item = frm.doc.items.find(item => item.item_code === item_code && item.idx === idx);
    let qty = item ? item.qty : 0;

    // Update the quantity
    qty_field.set_value(qty);
}







//function fetch_quantity_bb(frm, item_code, idx, warehouse, new_qty) {
//    let item = frm.doc.items.find(item => item.item_code === item_code && item.idx === idx);
//
//    if (item) {
//
//        frappe.call({
//            method: "erpnext.stock.doctype.batch.batch.get_batch_qty",
//            args: {
//                item_code: item_code,
//                warehouse: warehouse
//            },
//            callback: function(res) {
//                if (res.message) {
//                    let total_qty = res.message.reduce((total, batch) => total + batch.batch_qty, 0);
//
//                    // Update the quantity for the specific item in the items table
//                    frm.doc.items.forEach(child_item => {
//                        if (child_item.item_code === item_code && child_item.idx === idx) {
//                            frappe.msgprint(String(child_item.qty) + " Qty Before");
//                            frappe.msgprint(String(new_qty));
//                            child_item.qty = new_qty;
//                            frappe.msgprint(String(child_item.qty) + " Qty After");
//
//                            // Added: Update the child table item in the database directly
//                            frappe.call({
//                                method: "frappe.client.set_value",
//                                args: {
//                                    doctype: "Stock Entry Detail",
//                                    name: child_item.name,
//                                    fieldname: "qty",
//                                    value: new_qty
//                                },
//                                callback: function(response) {
//                                    if (!response.exc) {
//                                        frappe.show_alert({
//                                            message: __('Database updated successfully'),
//                                            indicator: 'green'
//                                        });
//
//                                        frm.refresh_field('items');
//                                    }
//                                },
//                                error: function(error) {
//                                    frappe.msgprint(__('Error saving the item: ' + error.message));
//                                }
//                            });
//                        }
//                    });
//
//
//                } else {
//                    frappe.show_alert({
//                                message: __('No quantity found for the batch.'),
//                                indicator: 'red'
//                    });
//                }
//            },
//
//            error: function(err) {
//                frappe.msgprint(__('Error fetching batch quantity: ' + err.message));
//            }
//        });
//    } else {
//        frappe.show_alert({
//                    message: __('Item not found in the document for the given idx.'),
//                    indicator: 'red'
//        });
//    }
//}










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
                                    new_qty: new_qty
                                },
                                callback: function(response) {
                                    if (response.message) {
                                        frappe.show_alert({
                                            message: response.message,
                                            indicator: 'green'
                                        });

                                        frm.refresh_field('items');
                                    }
                                },
                                error: function(error) {
                                    frappe.msgprint(__('Error saving the item: ' + error.message));
                                }
                            });
                        }
                    });
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
            open_item_dialog_aa(frm);
        }).addClass('btn-warning').css({
                'color': 'white',
                'font-weight': 'bold',
                'background-color': '#274472'
        });
        }
    }
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
            frappe.msgprint(__('Batch and serial number details fetched successfully'));
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

    get_dialog_fields() {
        let fields = [
            {
                fieldtype: "Link",
                fieldname: "warehouse",
                label: __("Warehouse"),
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
				onchange: () => this.get_auto_data(),
			},
            {
                fieldtype: "Column Break",
            },
            {
                fieldtype: "Data",
                options: "Barcode",
                fieldname: "scan_batch_no",
                label: __("Scan Batch No (=)"),
                onchange: () => this.scan_barcode_data(),
            },
            {
                fieldtype: "Section Break",
            },
            {
                fieldname: "entries",
                fieldtype: "Table",
                allow_bulk_edit: true,
                data: [],
                fields: this.get_dialog_table_fields(),
            },
        ];

        return fields;
    }

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
//                    this.update_batch_no();
                    this.update_batch_no_bb();
//                    this.fetch_batch_qty(scan_batch_no, warehouse);
                },
            });
        }
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





//   ==== END Fetch data from items table - A - Select Batch Method ====
// ===============================================================
// ===============================================================










//   ================================================================
//   ================================================================
//   ==== START Fetch data from items table - Function to select batch and serial number ====







frappe.ui.form.on('Stock Entry', {
    refresh: function(frm) {
    //    if (frm.doc.docstatus === 0 && frm.doc.stock_entry_type === 'Material Transfer for Manufacture' && frm.doc.bom_check === 0) {
    if (frm.doc.docstatus === 0 && frm.doc.stock_entry_type === 'Material Transfer for Manufacture') {
        frm.add_custom_button(__('Fetch Batch and Quantity'), function() {
            open_item_dialog(frm);
        }).addClass('btn-warning').css({
                'color': 'white',
                'font-weight': 'bold',
                'background-color': '#274472'
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
            frappe.msgprint(__('Batch and serial number details fetched successfully'));
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
//   ================================================================
//   ================================================================



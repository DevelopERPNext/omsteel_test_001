# Copyright (c) 2024, Mahmoud Khattab
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe import _

import json
from frappe.utils import flt


from erpnext.stock.doctype.stock_entry.stock_entry import StockEntry





@frappe.whitelist()
def create_print_msg(doc, method=None):
    frappe.msgprint(str("Production Items has been created."), alert=True)
    doc.reload()



# # Server Script
#
# if "validate" in doc.description:
# 	frappe.msgprint("Before Save ")
#
# if "validate" in doc.description:
# 	frappe.msgprint("Before Save ", alert=True)
#
# if doc.get("item_code"):
#     frappe.msgprint("The item_code exists.",


# ========================================================================
# ========================================================================
# ========= Updates rate and availability of all the items for a given Stock Entry ========







@frappe.whitelist()
def get_stock_and_rate(doc_name):
    """
    Updates rate and availability of all the items for a given Stock Entry.
    Called from Update Rate and Availability button.
    """

    if isinstance(doc_name, str):
        doc = frappe.get_doc("Stock Entry", doc_name)

    # ======== START IF Condition Check  =============
    update_rate_check_detail = frappe.get_all(
        "Stock Entry",
        filters={"name": doc.name},
        fields=["update_rate", ],
    )
    update_rate_check_info = update_rate_check_detail[0].get('update_rate')

    doc = frappe.get_doc("Stock Entry", doc_name)
    doc.set_work_order_details()
    doc.set_transfer_qty()
    doc.set_actual_qty()
    doc.calculate_rate_and_amount()
    doc.save()

    bom_no = doc.bom_no
    bom_item_detail = frappe.get_all(
        "BOM Item",
        filters={"parent": bom_no, },
        fields=["item_code", "rate"],
    )

    bom_item_item_code = bom_item_detail[0].get('item_code')
    bom_item_rate = bom_item_detail[0].get('rate')

    frappe.db.sql("""
                UPDATE `tabStock Entry Detail`
                SET basic_rate = %s, valuation_rate = %s
                WHERE parent = %s AND item_code = %s
            """, (bom_item_rate, bom_item_rate, doc_name, bom_item_item_code))

    frappe.db.commit()

    # frappe.throw(str(bom_item_detail))

    # # ============= ** { Change Raw Material Cost } ** ===============
    #
    # # Execute the SQL update
    # frappe.db.sql("""
    #     UPDATE `tabStock Entry Detail`
    #     SET
    #         basic_rate = %s,
    #         valuation_rate = %s,
    #         basic_amount = qty * %s,
    #         amount = qty * %s
    #     WHERE parent = %s AND item_code = %s
    # """, (
    #     flt(bom_item_rate), flt(bom_item_rate), flt(bom_item_rate), flt(bom_item_rate), doc_name,
    #     bom_item_item_code))
    #
    # frappe.db.commit()
    #
    # frappe.msgprint(" ** Valuation Rate updated successfully!", alert=True)

    # # ============= ** { Change Raw Material Cost } ** ===============


    #
    # # if update_rate_check_info == 1 or update_rate_check_info == 0:
    frappe.db.set_value("Stock Entry", doc.name, "update_rate", 1)

    return "Stock and rate updated successfully"






# ========================================================================
# ========================================================================
# ========= Updates rate and availability of Is Finished Item for a given Stock Entry ========






@frappe.whitelist()
def get_stock_and_rate_standard_valuation_rate(doc_name):
    """
    Updates basic_rate and valuation_rate for all items in a given Stock Entry where is_finished_item is 1.
    Called from Update Rate and Availability button.
    """

    if isinstance(doc_name, str):
        doc = frappe.get_doc("Stock Entry", doc_name)

        stock_entry_items = frappe.get_all(
            "Stock Entry Detail",
            filters={"parent": doc_name, "is_finished_item": 1},
            fields=["name", "basic_rate", "standard_valuation_rate"]
        )

        # if not stock_entry_items:
        #     # # frappe.msgprint(_("No finished items found to update rate."), alert=True)
        #     return

        if stock_entry_items:
            new_basic_rate_2 = stock_entry_items[0].get("basic_rate")

            for item in stock_entry_items:
                query = """
                    UPDATE `tabStock Entry Detail`
                    SET standard_valuation_rate = %s
                    WHERE name = %s
                """
                params = (new_basic_rate_2, item.get("name"))
                frappe.db.sql(query, params)

            frappe.db.commit()
        else:
            pass
    else:
        pass
        # frappe.msgprint(_("Invalid document name."), alert=True)







@frappe.whitelist()
def get_stock_and_rate_is_finished_item(doc_name):
    """
    Updates basic_rate and valuation_rate for all items in a given Stock Entry where is_finished_item is 1.
    Called from Update Rate and Availability button.
    """

    if isinstance(doc_name, str):
        doc = frappe.get_doc("Stock Entry", doc_name)

        stock_entry_items = frappe.get_all(
            "Stock Entry Detail",
            filters={"parent": doc_name, "is_finished_item": 1},
            fields=["name", "basic_rate", "standard_valuation_rate"]
        )

        if not stock_entry_items:
            frappe.msgprint(_("No finished items found to update rate."), alert=True)
            return

        new_basic_rate = stock_entry_items[0].get("standard_valuation_rate")

        for item in stock_entry_items:
            query = """
                UPDATE `tabStock Entry Detail`
                SET basic_rate = %s, valuation_rate = %s
                WHERE name = %s
            """
            params = (new_basic_rate, new_basic_rate, item.get("name"))
            frappe.db.sql(query, params)


        frappe.db.commit()

    else:
        frappe.msgprint(_("Invalid document name."), alert=True)














# ----------------------------
# @frappe.whitelist()
# def get_stock_and_rate_is_finished_item(doc_name):
#     """
#     Updates basic_rate and valuation_rate for all items in a given Stock Entry where is_finished_item is 1.
#     Called from Update Rate and Availability button.
#     """
#
#     if isinstance(doc_name, str):
#         doc = frappe.get_doc("Stock Entry", doc_name)
#
#         stock_entry_items = frappe.get_all(
#             "Stock Entry Detail",
#             filters={"parent": doc_name, "is_finished_item": 1},
#             fields=["name", "basic_rate", "standard_valuation_rate"]
#         )
#
#         if not stock_entry_items:
#             frappe.msgprint(_("No finished items found to update rate."), alert=True)
#             return
#
#         new_basic_rate_2 = stock_entry_items[0].get("basic_rate")
#
#         for item in stock_entry_items:
#             query = """
#                 UPDATE `tabStock Entry Detail`
#                 SET standard_valuation_rate = %s
#                 WHERE name = %s
#             """
#             params = (new_basic_rate_2, item.get("name"))
#             frappe.db.sql(query, params)
#
#         new_basic_rate = stock_entry_items[0].get("standard_valuation_rate")
#
#         for item in stock_entry_items:
#             query = """
#                 UPDATE `tabStock Entry Detail`
#                 SET basic_rate = %s, valuation_rate = %s
#                 WHERE name = %s
#             """
#             params = (new_basic_rate, new_basic_rate, item.get("name"))
#             frappe.db.sql(query, params)
#
#         frappe.db.commit()
#
#     else:
#         frappe.msgprint(_("Invalid document name."), alert=True)
#












# ========================================================================
# ========================================================================


# -----------------------------------------------------------------

#  ************ ===============  ****************

@frappe.whitelist(allow_guest=True)
def update_stock_entry_items(doc, method=None):
    """
    Updates the items table of a Stock Entry based on BOM data.

    Args:
        doc (Document): The Stock Entry document.
    """

    if isinstance(doc, str):
        doc = frappe.get_doc("Stock Entry", doc)

    # Check if the Stock Entry type is 'Manufacture'
    if doc.stock_entry_type != "Manufacture":
        # frappe.msgprint("This script only works for 'Manufacture' type Stock Entries.", alert=True)
        return

    # ======== START IF Condition Check  =============
    # if doc.bom_check == 1:

    bom_check_detail = frappe.get_all(
        "Stock Entry",
        filters={"name": doc.name},
        fields=["bom_check",],
    )
    bom_check_info = bom_check_detail[0].get('bom_check')


    bom_no = doc.bom_no
    bom_production_item_check_detail = frappe.get_all(
        "BOM",
        filters={"name": bom_no},
        fields=["item", "quantity", "standard_deviation_a_001"],
    )

    bom_production_item_check_info = bom_production_item_check_detail[0].get('quantity')
    bom_production_item_code = bom_production_item_check_detail[0].get('item')
    bom_production_standard_deviation_a_001 = bom_production_item_check_detail[0].get('standard_deviation_a_001')
    # frappe.msgprint(f"Item Code: {bom_production_item_code} , Qty {bom_production_item_check_info}")

    # ======== START Fetch total_cost From BOM  =============

    bom_fetch_total_cost = frappe.get_all(
        "BOM",
        filters={"name": bom_no,},
        fields=["total_cost"]
    )

    if not bom_fetch_total_cost:
        frappe.throw(_("BOM Total Cost not found."))

    bom_total_cost = bom_fetch_total_cost[0].get('total_cost')


    # frappe.msgprint(str(bom_fetch_total_cost))
    # frappe.msgprint(str("--------------"))
    # frappe.msgprint(str(bom_total_cost))



    # ======== END Fetch total_cost From BOM  ===============


    stock_entry_detail_check_details = frappe.get_all(
        "Stock Entry Detail",
        filters={"parent": doc.name},
        fields=["item_code", "qty"],
    )

    for stock_entry_detail_check_detail in stock_entry_detail_check_details:
        stock_entry_item_code = stock_entry_detail_check_detail.get('item_code')
        stock_entry_item_qty = stock_entry_detail_check_detail.get('qty')

        # frappe.msgprint(f"Item Code: {stock_entry_item_code} , Qty {stock_entry_item_qty}")

        if stock_entry_item_code == bom_production_item_code:
            calc_a_test = (bom_production_item_check_info / stock_entry_item_qty)

    # # Check if a result is returned and extract the value
    # if bom_check_info == 0:
    if bom_check_info == 1 or bom_check_info == 0:
    # if bom_check_info == 1:
        # Get the BOM No from the Stock Entry
        bom_no = doc.bom_no
        if not bom_no:
            frappe.msgprint("BOM No is missing in the Stock Entry.", alert=True)
            return

        # Get the items from the Stock Entry
        stock_entry_items = frappe.get_all(
            "Stock Entry Detail",
            filters={"parent": doc.name},
            fields=["item_code", "qty", "basic_rate"]
        )

        # BOM document
        bom_scrap_items = frappe.get_all(
            "BOM Scrap Item",
            filters={"parent": bom_no},
            fields=["parent", "parentfield", "item_code", "item_name", "rate", "stock_qty", "stock_uom" , "standard_deviation_a_010"]
        )

        # Create dictionaries to map item_code to qty in BOM Scrap Items and Stock Entry
        bom_scrap_dict = {item["item_code"]: item for item in bom_scrap_items}
        stock_entry_dict = {item["item_code"]: item for item in stock_entry_items}

        # frappe.msgprint(str(bom_scrap_dict))
        # frappe.msgprint(str(stock_entry_dict))

        # Retrieve Stock of the Work Order document
        bom_scrap_items_work_order = frappe.get_all(
            "Work Order",
            filters={"name": doc.work_order},
            fields=["scrap_warehouse"]
        )

        # Check if we got a result and extract the value
        if bom_scrap_items:
            scrap_warehouse_value = bom_scrap_items_work_order[0].get('scrap_warehouse')
        # ------------------------------

        # ==================== START ======================
        # Retrieve Qty To Manufacture From Work Order document
        qty_to_manufacture_work_order = frappe.get_all(
            "Work Order",
            filters={"name": doc.work_order},
            fields=["qty", "material_transferred_for_manufacturing", "produced_qty", "process_loss_qty"]
        )

        qty_to_manufacture_work_order_data = qty_to_manufacture_work_order[0].get('qty')
        qty_to_material_transferred_for_manufacturing = qty_to_manufacture_work_order[0].get('material_transferred_for_manufacturing')
        qty_to_produced_qty= qty_to_manufacture_work_order[0].get('produced_qty')
        qty_to_process_loss_qty = qty_to_manufacture_work_order[0].get('process_loss_qty')

        # # frappe.msgprint(str(qty_to_manufacture_work_order_data), alert=True)
        # frappe.msgprint(str(qty_to_manufacture_work_order_data))

        # ==================== END ======================

        # ==================== START ======================

        # Get the items (Is Finished Item) Stock Entry
        is_finished_item = frappe.get_all(
            "Stock Entry Detail",
            filters={
                "parent": doc.name,
                "is_finished_item": 1
            },
            fields=["item_code", "qty", "basic_rate", "is_finished_item", "standard_deviation_a_020"]
        )

        is_finished_item_item = is_finished_item[0].get('item_code')
        is_finished_item_item_qty = is_finished_item[0].get('qty')
        is_finished_item_item_is_finished_item = is_finished_item[0].get('is_finished_item')

        # frappe.msgprint(str(is_finished_item_item))
        # frappe.msgprint(str(is_finished_item_item_qty))
        # frappe.msgprint(str(is_finished_item_item_is_finished_item))
        # frappe.msgprint(str("=================="))

        # Retrieve (Is Finished Item) From Work Order document
        is_finished_item_work_order = frappe.get_all(
            "BOM",
            filters={"name": doc.bom_no},
            fields=["item", "item_name", "quantity"]
        )

        is_finished_item_work_order_item = is_finished_item_work_order[0].get('item')
        is_finished_item_work_order_item_name = is_finished_item_work_order[0].get('item_name')
        is_finished_item_work_order_item_qty = is_finished_item_work_order[0].get('quantity')

        # frappe.msgprint(str(is_finished_item_work_order_item))
        # frappe.msgprint(str(is_finished_item_work_order_item_name))
        # frappe.msgprint(str(is_finished_item_work_order_item_qty))

        # # # Calculate Qty To Manufacture
        # # calc_qty_to_manufacture = is_finished_item_work_order_item_qty * qty_to_manufacture_work_order_data
        #
        # # ============ Quantity Separated ==============
        # # Calculate Qty To Manufacture
        # if qty_to_material_transferred_for_manufacturing != 0:
        #     calc_qty_to_manufacture = is_finished_item_work_order_item_qty * qty_to_material_transferred_for_manufacturing
        # else:
        #     calc_qty_to_manufacture = is_finished_item_work_order_item_qty * qty_to_manufacture_work_order_data


        # # ============ Quantity Calculation ==============
        # total_qty = qty_to_manufacture_work_order_data + qty_to_material_transferred_for_manufacturing

        # Step 2: Calculate the sum of 'qty_to_produced_qty' and 'qty_to_process_loss_qty'
        total_produced_and_loss_qty = qty_to_produced_qty + qty_to_process_loss_qty

        # Step 3: Subtract the sum of 'qty_to_produced_qty' and 'qty_to_process_loss_qty' from 'qty_to_material_transferred_for_manufacturing'
        remaining_material_qty = qty_to_material_transferred_for_manufacturing - total_produced_and_loss_qty

        # Step 4: Calculate Qty To Manufacture
        # ============ Quantity Separated ==============
        # Step 4: Calculate Qty To Manufacture using the remaining material quantity if it's not zero
        if remaining_material_qty > 0:
            if qty_to_material_transferred_for_manufacturing != 0:
                calc_qty_to_manufacture = is_finished_item_work_order_item_qty * remaining_material_qty
            else:
                calc_qty_to_manufacture = is_finished_item_work_order_item_qty * qty_to_manufacture_work_order_data
        else:
            calc_qty_to_manufacture = is_finished_item_work_order_item_qty * qty_to_manufacture_work_order_data

        # Update the quantity in the "Stock Entry Detail" table
        frappe.db.set_value(
            "Stock Entry Detail",
            {"parent": doc.name,
             "is_finished_item": 1},
            {
                "qty": calc_qty_to_manufacture,
                "standard_deviation_a_020": bom_production_standard_deviation_a_001,
                "basic_rate": bom_total_cost,
                "valuation_rate": bom_total_cost,
                "basic_amount": bom_total_cost * calc_qty_to_manufacture,
                "amount": bom_total_cost * calc_qty_to_manufacture
            }
        )

        # ==================== END ======================

        # Compare bom_scrap_dict and stock_entry_dict for differences
        for item_code, bom_item in bom_scrap_dict.items():
            bom_qty = bom_item["stock_qty"]
            bom_rate = bom_item["rate"]
            stock_entry_item = stock_entry_dict.get(item_code)

            if stock_entry_item:
                stock_entry_qty = stock_entry_item["qty"]

                # ======== Change ==============
                # if stock_entry_qty != bom_qty:
                if stock_entry_qty:
                    # frappe.msgprint(f"Quantity difference detected for item {item_code}: BOM qty = {bom_qty}, Stock Entry qty = {stock_entry_qty}")

                    # ======== Change ==============
                    # # # # Delete item_code with different quantity in Stock Entry
                    frappe.db.delete("Stock Entry Detail", {"parent": doc.name, "item_code": item_code, "is_scrap_item": 1})

                    # frappe.msgprint(_(f"***  Delete item_code {item_code} with different quantity in Stock Entry ***"), alert=True)
                    # # frappe.msgprint(_(f"***  Delete item_code {item_code} with different quantity in Stock Entry ***"))

                    # ======== Change ==============
                    # frappe.db.sql("""
                    #             UPDATE `tabStock Entry Detail`
                    #             SET qty = %(qty)s, basic_rate = %(basic_rate)s
                    #             WHERE parent = %(parent)s AND item_code = %(item_code)s
                    #         """, {"qty": bom_qty, "basic_rate": bom_rate, "parent": doc.name, "item_code": item_code})
                    #
                    # frappe.msgprint(
                    #     f"====_____==== Updated item {item_code} in Stock Entry with new quantity {bom_qty}  ,,,, stock_entry_qty {stock_entry_qty}",
                    #     alert=True)
                    # # frappe.msgprint(f"====_____==== Updated item {item_code} in Stock Entry with new quantity {bom_qty}  ,,,, stock_entry_qty {stock_entry_qty}")


        # frappe.msgprint(str(bom_check_detail) , alert=True)
        # frappe.msgprint(str(bom_check_info) , alert=True)

        item_count = {}
        for item in bom_scrap_items:
            key = (item["item_code"], item["item_name"], item["stock_qty"], item["rate"], item["stock_uom"], item["standard_deviation_a_010"])
            if key in item_count:
                item_count[key] += 1
            else:
                item_count[key] = 1

        # frappe.msgprint(str(item_count), alert=True)
        # frappe.msgprint(str(item_count))

        # Loop through item_count to handle items with count > 1
        for key, count in item_count.items():
            item_code, item_name, stock_qty, rate, stock_uom, standard_deviation_a_010 = key
            # frappe.msgprint(str(type(count)))
            # frappe.msgprint(str(count))

            # # calc_stock_qty = stock_qty / calc_a_test
            # calc_stock_qty = ( stock_qty * qty_to_manufacture_work_order_data )

            # # ============ Quantity Separated ==============
            # # calc_stock_qty = stock_qty / calc_a_test
            # if qty_to_material_transferred_for_manufacturing != 0:
            #     calc_stock_qty = (stock_qty * qty_to_material_transferred_for_manufacturing)
            # else:
            #     calc_stock_qty = (stock_qty * qty_to_manufacture_work_order_data)


            # # ============ Quantity Calculation ==============
            # total_qty = qty_to_manufacture_work_order_data + qty_to_material_transferred_for_manufacturing

            # Step 2: Calculate the sum of 'qty_to_produced_qty' and 'qty_to_process_loss_qty'
            total_produced_and_loss_qty = qty_to_produced_qty + qty_to_process_loss_qty

            # Step 3: Subtract the sum of 'qty_to_produced_qty' and 'qty_to_process_loss_qty' from 'qty_to_material_transferred_for_manufacturing'
            remaining_material_qty = qty_to_material_transferred_for_manufacturing - total_produced_and_loss_qty

            # Step 4: Calculate Qty To Manufacture
            # ============ Quantity Separated ==============
            # Step 4: Calculate Qty To Manufacture using the remaining material quantity if it's not zero
            if remaining_material_qty > 0:
                if qty_to_material_transferred_for_manufacturing != 0:
                    calc_stock_qty = (stock_qty * remaining_material_qty)
                else:
                    calc_stock_qty = (stock_qty * qty_to_manufacture_work_order_data)
            else:
                calc_stock_qty = 0




            # ======== Change ==============
            # if count > 1:
            if count >= 1 and key in item_count:
                # frappe.msgprint(f"Duplicating item {item_code} {count} times in Stock Entry Detail", alert=True)

                # ======== Change ==============
                # for idx in range(count - 1):
                for idx in range(count):
                    # frappe.msgprint(f"Duplicating {item_code} {idx + 2} times", alert=True)

                    try:
                        basic_rate = float(rate)

                        query = """
                                INSERT INTO `tabStock Entry Detail`
                                (idx, parent, item_code, name, qty, basic_rate, valuation_rate, basic_amount, amount, uom, stock_uom, parenttype, parentfield, is_scrap_item, bom_no, conversion_factor, item_name, standard_deviation_a_020, t_warehouse)
                                SELECT
                                    IFNULL(MAX(idx), 0) + 1 AS new_idx,
                                    %(parent)s,
                                    %(item_code)s,
                                    CONCAT('djsr', SUBSTRING(MD5(RAND()), 1, 5), SUBSTRING(MD5(RAND()), 1, 1)),
                                    %(qty)s,
                                    %(basic_rate)s,
                                    %(valuation_rate)s,
                                    %(basic_amount)s,
                                    %(amount)s,
                                    %(uom)s,
                                    %(stock_uom)s,
                                    'Stock Entry',
                                    'items',
                                    1,
                                    %(bom_no)s,
                                    1,
                                    %(item_name)s,
                                    %(standard_deviation_a_020)s,
                                    %(t_warehouse)s
                                FROM
                                    `tabStock Entry Detail`
                                WHERE parent = %(parent)s;
                            """

                        params = {
                            "parent": doc.name,
                            "item_code": item_code,
                            "qty": calc_stock_qty,
                            "basic_rate": bom_total_cost,
                            "valuation_rate": bom_total_cost,
                            "basic_amount": bom_total_cost * calc_stock_qty,
                            "amount": bom_total_cost * calc_stock_qty,
                            "uom": stock_uom,
                            "stock_uom": stock_uom,
                            "bom_no": bom_no,
                            "item_name": item_name,
                            "standard_deviation_a_020": standard_deviation_a_010,
                            "t_warehouse": scrap_warehouse_value
                        }

                        frappe.db.sql(query, params)
                        # frappe.msgprint("Record inserted successfully", alert=True)
                    except Exception as e:
                        frappe.msgprint(f"Error occurred: {e}")

        frappe.db.set_value("Stock Entry", doc.name, "bom_check", 1)

        # # doc.save(ignore_permissions=True)
        # # frappe.db.commit()
        doc.reload()
        frappe.msgprint(_("Stock Entry items updated successfully."), alert=True)

        # ======== END IF Condition Check  =============


        frappe.msgprint(_("Successfully START DB"), alert=True)


        #  SELECT * FROM `tabStock Entry Detail` WHERE parent="MAT-STE-2024-00042";

        #  ==================== Start Raw Material  ============================

        # Retrieve Raw Material From Work Order document
        raw_material_items_work_order = frappe.get_all(
            "Work Order Item",
            filters={"parent": doc.work_order},
            fields=["item_code", "item_name", "source_warehouse", "required_qty", "rate", "transferred_qty",
                    "consumed_qty", "returned_qty", "available_qty_at_source_warehouse",
                    "available_qty_at_wip_warehouse"]
        )

        raw_material_item_code = raw_material_items_work_order[0].get('item_code')
        raw_material_item_name = raw_material_items_work_order[0].get('item_name')
        # frappe.msgprint(f"Item Code: {raw_material_item_code} , Name: {raw_material_item_name}")

        # Retrieve Raw Material From Work Order document
        warehouse_work_order = frappe.get_all(
            "Work Order",
            filters={"name": doc.work_order},
            fields=["source_warehouse", "wip_warehouse", "fg_warehouse", "scrap_warehouse"]
        )

        wip_warehouse = warehouse_work_order[0].get('wip_warehouse')
        # frappe.msgprint(str("------=========------"))
        # frappe.msgprint(str(wip_warehouse))
        #
        # frappe.msgprint(str(raw_material_items_work_order))
        # frappe.msgprint(str("------------------------"))
        # frappe.msgprint(str(warehouse_work_order))
        #

        bom_item_detail = frappe.get_all(
            "BOM Item",
            filters={"parent": bom_no,},
            fields=["item_code", "rate", "uom"],
        )

        # bom_item_detail = frappe.get_all(
        #     "BOM Item",
        #     filters={"parent": bom_no, "item_code": item_code },
        #     fields=["rate"],
        # )

        bom_item_item_code = bom_item_detail[0].get('item_code')
        bom_item_rate = bom_item_detail[0].get('rate')
        bom_item_uom = bom_item_detail[0].get('uom')


        # # Get the items from the Stock Entry
        stock_entry_items = frappe.get_all(
            "Stock Entry Detail",
            filters={"parent": doc.name},
            fields=["item_code", "qty", "basic_rate", "is_finished_item", "is_scrap_item"]
        )

        for stock_entry_detail_check_detail in stock_entry_items:
            stock_entry_item_code = stock_entry_detail_check_detail.get('item_code')
            stock_entry_item_qty = stock_entry_detail_check_detail.get('qty')
            stock_entry_item_basic_rate = stock_entry_detail_check_detail.get('basic_rate')
            stock_entry_item_is_finished_item = stock_entry_detail_check_detail.get('is_finished_item')
            stock_entry_item_is_scrap_item = stock_entry_detail_check_detail.get('is_scrap_item')

            # frappe.msgprint(f"Item Code: {stock_entry_item_code} , Qty {stock_entry_item_qty}"
            #                 f", Basic Rate {stock_entry_item_basic_rate}, "
            #                 f"is_finished_item {stock_entry_item_is_finished_item}"
            #                 f", is_scrap_item {stock_entry_item_is_scrap_item}")

            if not (raw_material_item_code == stock_entry_item_code and
                    stock_entry_item_is_finished_item == 1 and stock_entry_item_is_scrap_item == 1):
                # calc_a_test = (bom_production_item_check_info / stock_entry_item_qty)
                # frappe.msgprint(str("True"))

                frappe.db.delete(
                    "Stock Entry Detail",
                    {
                        "parent": doc.name,
                        "item_code": stock_entry_item_code,
                        "is_finished_item": 0,
                        "is_scrap_item": 0
                    }
                )

        item_count_dic = {}
        for item in raw_material_items_work_order:
            # key = (item["item_code"], item["item_name"], item["required_qty"], item["amount"],
            #        item["transferred_qty"], item["consumed_qty"], item["returned_qty"])

            key = (item["item_code"], item["item_name"], item["required_qty"], item["rate"],
                   item["transferred_qty"], item["consumed_qty"], item["returned_qty"])
            if key in item_count_dic:
                item_count_dic[key] += 1
            else:
                item_count_dic[key] = 1

        # frappe.msgprint(str(item_count), alert=True)
        # # frappe.msgprint(str(item_count))


        # #     IFNULL(MAX(idx), 0) + 1 AS new_idx,
        # #     %(idx)s,  "idx": idx,
        # idx = 1

        # Loop through item_count to handle items with count > 1
        for key, count in item_count_dic.items():
            # item_code, item_name, required_qty, amount, transferred_qty, consumed_qty, returned_qty = key
            item_code, item_name, required_qty, rate, transferred_qty, consumed_qty, returned_qty = key


            # # ============ Quantity Separated ==============
            # # Determine the quantity to use
            # qty_to_use = required_qty if transferred_qty == 0 else transferred_qty


            # ============ Quantity Separated ==============
            # Determine the quantity to use by subtracting 'transferred_qty' from 'consumed_qty' if both have data

            if transferred_qty and consumed_qty:
                qty_to_use = transferred_qty - consumed_qty
            else:
                qty_to_use = required_qty if transferred_qty == 0 else transferred_qty

            # frappe.msgprint(str(type(count)))
            # frappe.msgprint(str(count))
            #
            # # calc_stock_qty = stock_qty / calc_a_test

            # frappe.msgprint(str(rate))
            # # ======== Change ==============
            # # if count > 1:
            if count >= 1 and key in item_count_dic:
                # frappe.msgprint(f"Duplicating item {item_code} {count} times in Stock Entry Detail", alert=True)

                # # ======== Change ==============
                # # for idx in range(count - 1):
                # for idx in range(count):
                #     # frappe.msgprint(f"Duplicating {item_code} {idx + 2} times", alert=True)

                try:
                    # # basic_rate = float(rate)
                    # idx = 1
                    # basic_rate = float(rate)
                    basic_rate = float(bom_item_rate)

                    query = """
                            INSERT INTO `tabStock Entry Detail`
                            (idx, parent, item_code, name, qty, basic_rate, valuation_rate, basic_amount, amount, uom, stock_uom, parenttype, parentfield, is_scrap_item, is_finished_item,conversion_factor, item_name, standard_deviation_a_020, s_warehouse)
                            SELECT
                                IFNULL(MAX(idx), 0) + 1 AS new_idx,
                                %(parent)s,
                                %(item_code)s,
                                CONCAT('djsraw', SUBSTRING(MD5(RAND()), 1, 5), SUBSTRING(MD5(RAND()), 1, 1)),
                                %(qty)s,
                                %(basic_rate)s,
                                %(valuation_rate)s,
                                %(basic_amount)s,
                                %(amount)s,
                                %(uom)s,
                                %(stock_uom)s,
                                'Stock Entry',
                                'items',
                                0,
                                0,
                                1,
                                %(item_name)s,
                                %(standard_deviation_a_020)s,
                                %(s_warehouse)s
                            FROM
                                `tabStock Entry Detail`
                            WHERE parent = %(parent)s;
                        """

                    params = {
                        "parent": doc.name,
                        "item_code": item_code,
                        "qty": qty_to_use,
                        "basic_rate": basic_rate,
                        "valuation_rate": bom_item_rate,
                        "basic_amount": bom_item_rate * qty_to_use,
                        "amount": bom_item_rate * qty_to_use,
                        "uom": bom_item_uom,
                        "stock_uom": bom_item_uom,
                        "item_name": item_name,
                        "standard_deviation_a_020": bom_production_standard_deviation_a_001,
                        "s_warehouse": wip_warehouse
                    }

                    frappe.db.sql(query, params)
                    # idx += 1
                    # # frappe.msgprint("Record inserted successfully", alert=True)

                    # # ============= ** { Change Raw Material Cost } ** ===============
                    #
                    # frappe.db.sql("""
                    #                         UPDATE `tabStock Entry Detail`
                    #                         SET
                    #                             basic_rate = %s,
                    #                             valuation_rate = %s,
                    #                             basic_amount = qty * %s,
                    #                             amount = qty * %s
                    #                         WHERE parent = %s AND item_code = %s
                    #                     """, (
                    # flt(bom_item_rate), flt(bom_item_rate), flt(bom_item_rate), flt(bom_item_rate), doc, item_code))
                    #
                    # frappe.db.commit()
                    #
                    # frappe.msgprint(" -- Valuation Rate Updated successfully", alert=True)
                    # # ============= ** { Change Raw Material Cost } ** ===============


                except Exception as e:
                    frappe.msgprint(f"Error occurred: {e}")
        # idx += 1

        #  ==================== End Raw Material  ==============================

        # frappe.msgprint(_(str(bom_production_standard_deviation_a_001)), alert=True)
        frappe.msgprint(_("Successfully END DB"), alert=True)

    else:
        pass

    # # Call the get_stock_and_rate method on the Stock Entry instance
    # doc.get_stock_and_rate()
    # frappe.msgprint(_("Update Rate and Availability completed successfully."), alert=True)
    # # doc.save()


#  ************ ===============  ****************

#  ===============   END update_stock_entry_items  ====================




# ========================================================================
# ========================================================================


# -----------------------------------------------------
# -----------------------------------------------------

@frappe.whitelist(allow_guest=True)
def move_data_from_production_items_table_to_scrap_items(doc, method=None):
    try:
        # Parse the JSON string
        doc_dict = frappe.parse_json(doc) if isinstance(doc, str) else doc
        production_items = doc_dict.get('production_items_a_001')

        if not production_items:
            return

        # Clear existing scrap_items before adding new data
        doc.scrap_items = []

        for item in production_items:
            scrap_item_data = {
                'item_code': item.get('item_code'),
                'item_name': item.get('item_name'),
                'stock_qty': item.get('stock_qty'),
                'rate': item.get('rate'),
                'amount': item.get('amount'),
                'stock_uom': item.get('stock_uom'),
                'base_rate': item.get('base_rate'),
                'base_amount': item.get('base_amount'),
                'standard_deviation_a_010': item.get('standard_deviation_a_010')
            }
            doc.append('scrap_items', scrap_item_data)

        # Set the 'scrap_items' field in the 'BOM' document
        frappe.db.set_value("BOM", doc.name, 'scrap_items', doc.scrap_items, update_modified=False)
        frappe.db.commit()
        doc.reload()
        frappe.msgprint("Production Items have been created successfully!", alert=True)
    except frappe.ValidationError as e:
        frappe.msgprint(str(e), alert=True)
    except Exception as ex:
        pass
        # frappe.msgprint(f"Error: {str(ex)}", alert=True)

# -----------------------------------------------------

# ========================================================================
# ========================================================================





# ========================================================================
# ========================================================================

@frappe.whitelist(allow_guest=True)
def calc_qty(doc_name, method=None):
    try:
        # Fetch the BOM document
        doc = frappe.get_doc("BOM", doc_name)

        # FG_Item = doc.quantity
        # doc.calc_qty_a_001 = FG_Item

        # bom_no = doc.name
        # if not bom_no:
        #     frappe.msgprint("BOM No is missing in the Stock Entry.", alert=True)
        #     return
        #
        # # # BOM document
        # # bom_scrap_items = frappe.get_all(
        # #     "BOM Scrap Item",
        # #     filters={"parent": bom_no},
        # #     fields=["item_code", "stock_qty"]
        # # )
        # #
        # # # Create a dictionary to map item_code to total quantity in BOM Scrap Items
        # # bom_scrap_dict = {}
        # # for item in bom_scrap_items:
        # #     if item["item_code"] in bom_scrap_dict:
        # #         bom_scrap_dict[item["item_code"]] += item["stock_qty"]
        # #     else:
        # #         bom_scrap_dict[item["item_code"]] = item["stock_qty"]
        # #
        # # total_scrap_qty = sum(bom_scrap_dict.values())
        # # # doc.total_scrap_qty = total_scrap_qty

        # doc.total_production_qty = total_production_qty


        # # doc.calc_qty_a_001 = FG_Item + doc.total_scrap_qty
        # doc.calc_qty_a_001 = FG_Item + total_production_qty
        # # # Calculate and update calc_qty_a_001
        # # total_calc_a = FG_Item + doc.total_scrap_qty

        # =========================================
        FG_Item = doc.quantity
        bom_no = doc.name

        # BOM document
        bom_production_items = frappe.get_all(
            "BOM Production Items",
            filters={"parent": bom_no},
            fields=["item_code", "stock_qty"]
        )

        # Create a dictionary to map item_code
        bom_production_dict = {}
        for item in bom_production_items:
            if item["item_code"] in bom_production_dict:
                bom_production_dict[item["item_code"]] += item["stock_qty"]
            else:
                bom_production_dict[item["item_code"]] = item["stock_qty"]

        total_production_qty = sum(bom_production_dict.values())


        total_calc = FG_Item + total_production_qty
        doc.calc_qty_a_001 = total_calc

        # frappe.msgprint("Calculate Qty (Finished Good & Production Items)!", alert=True)

        # # frappe.db.set_value("BOM", doc.name, "calc_qty_a_001", total_calc_a)
        # frappe.db.set_value("BOM", doc.name, "calc_qty_a_001", total_calc)

        # # # Update calc_qty_a_001 field in BOM
        frappe.db.sql("""
                    UPDATE `tabBOM`
                    SET calc_qty_a_001 = %s
                    WHERE name = %s
                """, (total_calc, doc.name))

        # Commit the transaction
        frappe.db.commit()

        # frappe.msgprint(str(total_calc), alert=True)
        frappe.msgprint("Calculate Qty (Finished Good & Production Items)!", alert=True)
    except frappe.ValidationError as e:
        frappe.msgprint(str(e), alert=True)
    except Exception as ex:
        pass



# ========================================================================
# ========================================================================



# ========================================================================
# ========================================================================

@frappe.whitelist(allow_guest=True)
def changed_the_doc_name(doc_name, method=None):
    try:
        # Fetch the BOM document
        doc = frappe.get_doc("BOM", doc_name)


        # ======================================

        bom_no_data = doc.name
        # BOM bom_description_data
        bom_description_data = frappe.get_all(
            "BOM",
            filters={"name": bom_no_data},
            fields=["bom_description_a_001", "name"]
        )

        # # Select in BOM
        # bom_description_data = frappe.db.sql("""
        #     SELECT bom_description_a_001 FROM `tabBOM`
        #     WHERE name = %s
        # """, (doc.name,), as_dict=True)
        #
        # # Check if the result is not empty
        # if bom_description_data:
        #     bom_description = bom_description_data[0].get('bom_description_a_001')
        #     frappe.msgprint(msg=bom_description, alert=True)
        # else:
        #     frappe.msgprint(msg="No BOM found with the given name.", alert=True)
        #
        # # # Commit the transaction
        # # frappe.db.commit()

        # Ensure that at least one record is found
        if bom_description_data:
            bom_description_data_info = bom_description_data[0].get("bom_description_a_001")
        else:
            pass

        # # # Optionally set a value in the BOM document if needed
        # frappe.db.set_value("BOM", bom_no_data, "name", bom_description_data_info)

        # # Rename the BOM document
        # frappe.rename_doc(doctype, old_name, new_name, merge=False)
        frappe.rename_doc("BOM", bom_no_data, bom_description_data_info, merge=False)

        # Display the bom_description in an alert
        frappe.msgprint(str(bom_description_data_info), alert=True)

        # # Update the name in BOM
        # frappe.db.sql("""
        #     UPDATE `tabBOM`
        #     SET name = %s
        #     WHERE name = %s
        # """, (bom_description_data_info, doc.name))
        #
        # # Commit the transaction
        # frappe.db.commit()

        # Display a success message
        frappe.msgprint(msg="Changed the Doc Name", alert=True)


    except frappe.ValidationError as e:
        frappe.msgprint(str(e), alert=True)
    except Exception as ex:
        pass



# ========================================================================
# ========================================================================





# # ========================================================================
# # ========================================================================







# # ========================================================================
# # ========================================================================


# # ========================================================================
# # ========================================================================


# ========================================================================
# ========================================================================

@frappe.whitelist(allow_guest=True)
def mod_qty(doc, method=None):
    try:
        bom_no = doc.bom_no
        # frappe.msgprint(str(bom_no))
        if not bom_no:
            frappe.msgprint("BOM No is missing in the Work Order.", alert=True)
            return

        bom_work_order = frappe.get_all(
            "BOM Item",
            filters={"parent": bom_no},
            fields=["item_code", "qty"]
        )

        for item in bom_work_order:
            item_code_bom = item["item_code"]
            item_qty_bom = item["qty"]

            # frappe.msgprint(_("Item Code: {0}, Quantity: {1}").format(item_code_bom, item_qty_bom))
            # frappe.msgprint("========")

        doc_name = doc.name
        bom_no = doc.get("bom_no")

        if not bom_no:
            frappe.msgprint(_("BOM No is missing in the document."), alert=True)
            return

        # Fetch the required items for the work order
        bom_required_items = frappe.get_all(
            "Work Order Item",
            filters={"parent": doc_name},
            fields=["item_code", "required_qty", "name"]
        )

        if not bom_required_items:
            frappe.msgprint(_("No Work Order Items found for Work Order: {0}").format(doc_name), alert=True)
            return

        # Fetch BOM items related to the BOM number
        bom_work_order = frappe.get_all(
            "BOM Item",
            filters={"parent": bom_no},
            fields=["item_code", "qty"]
        )

        if not bom_work_order:
            frappe.msgprint(_("No BOM Items found for BOM No: {0}").format(bom_no), alert=True)
            return

        # Create a dictionary for quick lookup
        bom_items_dict = {item["item_code"]: item["qty"] for item in bom_work_order}

        # Iterate through work order items and update the required quantity
        for work_order_item in bom_required_items:
            item_code = work_order_item["item_code"]
            required_qty = work_order_item["required_qty"]
            name_data = work_order_item["name"]

            if item_code in bom_items_dict:
                item_qty_bom = bom_items_dict[item_code]
                new_required_qty = item_qty_bom * doc.qty

                # Update the required_qty field in Work Order Item
                frappe.db.set_value(
                    "Work Order Item",
                    doc.name,
                    "required_qty",
                    new_required_qty
                )

                frappe.msgprint(
                    f"Updated: Item Code: {item_code}, New Required Quantity: {new_required_qty}",
                    alert=True
                )

                required_qty = new_required_qty

                # # Attempt to update using set_value
                # frappe.db.set_value(
                #     "Work Order Item",
                #     {"parent": doc_name, "item_code": item_code},
                #     'required_qty',
                #     new_required_qty,
                #     update_modified=False
                # )
                # frappe.db.commit()
                # frappe.msgprint(f"Updated: Item Code: {item_code}, New Required Quantity: {new_required_qty}",
                #                 alert=True)
                #
                # # frappe.db.sql("""
                # #             UPDATE `tabWork Order Item`
                # #             SET required_qty = %s
                # #             WHERE parent = %s AND item_code = %s
                # #         """, (new_required_qty, doc_name, item_code))

                # # Using frappe.db.sql
                # query = f"""
                #     UPDATE `tabWork Order Item`
                #     SET required_qty = {new_required_qty}
                #     WHERE parent = '{doc_name}' AND item_code = '{item_code}';
                # """

                # # Using frappe.db.sql
                # query = f"""
                #                     UPDATE `tabWork Order Item`
                #                     SET data_qty_a_001 = {new_required_qty}
                #                     WHERE parent = '{doc_name}' AND item_code = '{item_code}';
                #                 """

                # Using frappe.db.sql
                query = f"""
                    UPDATE `tabWork Order Item`
                    SET data_qty_a_001 = '{new_required_qty}'
                    WHERE name = '{name_data}' AND parent = '{doc_name}' AND item_code = '{item_code}';
                """

                # frappe.db.set_value("Work Order Item", doc.name, "data_qty_a_001", new_required_qty)

                frappe.db.set_value("Work Order Item", doc.name, "data_qty_a_001", 44)

                # # Update using frappe.db.set_value
                # frappe.db.set_value(
                #     "Work Order Item",
                #     {"name": name_data, "parent": doc_name, "item_code": item_code},
                #     "data_qty_a_001",
                #     new_required_qty
                # )
                frappe.db.commit()

                try:
                    frappe.db.sql(query)
                    frappe.db.commit()

                    frappe.msgprint(f"Updated: Item Code: {item_code}, New Required Quantity: {new_required_qty}",
                                    alert=True)
                    frappe.msgprint(f"{query}",alert=True)
                except Exception as e:
                    frappe.msgprint(f"Error updating database: {e}", alert=True)


    #         # # # # Commit changes to the database
    #         # # frappe.db.commit()
    #         # # # doc.save(ignore_permissions=True)
    #         #
    #         # frappe.db.delete("tabWork Order Item", {"parent": doc.name, "item_code": item_code})
    #
    #     # Fetch updated Work Order to ensure it reflects the changes
    #     updated_doc = frappe.get_doc("Work Order", doc_name)
    #     updated_doc.reload()
    #
    #     # frappe.msgprint(_("Updated required quantities for Work Order: {0}").format(doc_name))
    # #
    # #     # ==========================================================================
    # #     # ==========================================================================
    # #     # ==========================================================================
    #
    # try:
    #     bom_no = doc.bom_no
    #     # frappe.msgprint(str(bom_no))
    #     if not bom_no:
    #         frappe.msgprint("BOM No is missing in the Work Order.", alert=True)
    #         return
    #
    #     bom_work_order = frappe.get_all(
    #         "BOM Item",
    #         filters={"parent": bom_no},
    #         fields=["item_code", "qty"]
    #     )
    #
    #     for item in bom_work_order:
    #         item_code_bom = item["item_code"]
    #         item_qty_bom = item["qty"]
    #
    #         # frappe.msgprint(_("Item Code: {0}, Quantity: {1}").format(item_code_bom, item_qty_bom))
    #         # frappe.msgprint("========")
    #
    #     doc_name = doc.name
    #     bom_no = doc.get("bom_no")
    #
    #     if not bom_no:
    #         frappe.msgprint(_("BOM No is missing in the document."), alert=True)
    #         return
    #
    #     # Fetch the required items for the work order
    #     bom_required_items = frappe.get_all(
    #         "Work Order Item",
    #         filters={"parent": doc_name},
    #         fields=["item_code", "required_qty"]
    #     )
    #
    #     if not bom_required_items:
    #         frappe.msgprint(_("No Work Order Items found for Work Order: {0}").format(doc_name), alert=True)
    #         return
    #
    #     # Fetch BOM items related to the BOM number
    #     bom_work_order = frappe.get_all(
    #         "BOM Item",
    #         filters={"parent": bom_no},
    #         fields=["item_code", "qty"]
    #     )
    #
    #     if not bom_work_order:
    #         frappe.msgprint(_("No BOM Items found for BOM No: {0}").format(bom_no), alert=True)
    #         return
    #
    #     # Create a dictionary for quick lookup
    #     bom_items_dict = {item["item_code"]: item["qty"] for item in bom_work_order}
    #
    #     # # Iterate through work order items and update the required quantity
    #     # for work_order_item in bom_required_items:
    #     #     item_code = work_order_item["item_code"]
    #     #     if item_code in bom_items_dict:
    #     #         item_qty_bom = bom_items_dict[item_code]
    #     #         new_required_qty = item_qty_bom * doc.qty
    #     #
    #     #         # Attempt to update using set_value
    #     #         frappe.db.set_value(
    #     #             "Work Order Item",
    #     #             {"parent": doc_name, "item_code": item_code},
    #     #             'required_qty',
    #     #             new_required_qty,
    #     #             update_modified=False
    #     #         )
    #     #         frappe.db.commit()
    #     #         frappe.msgprint(f"Updated: Item Code: {item_code}, New Required Quantity: {new_required_qty}",
    #     #                         alert=True)
    #     #
    #     #         frappe.db.sql("""
    #     #                     UPDATE `tabWork Order Item`
    #     #                     SET required_qty = %s
    #     #                     WHERE parent = %s AND item_code = %s
    #     #                 """, (new_required_qty, doc_name, item_code))
    #     #         frappe.db.commit()
    #     #         frappe.msgprint(f"Fallback Updated: Item Code: {item_code}, New Required Quantity: {new_required_qty}",
    #     #                         alert=True)
    #
    #     # # # Perform the delete operation
    #     # frappe.db.delete("Work Order Item", {"parent": doc_name})
    #     # frappe.msgprint(_("Deleted existing Work Order Items for Work Order: {0}").format(doc_name), alert=True)
    #     #
    #     # frappe.db.commit()
    #
    #
    #     # # # Add or Update items based on BOM
    #     # try:
    #     #     for bom_item in bom_work_order:
    #     #         item_code = bom_item["item_code"]
    #     #         item_qty_bom = bom_item["qty"]
    #     #         new_required_qty = item_qty_bom * doc.qty
    #     #
    #     #         # Insert new record into Work Order Item
    #     #         new_item = frappe.get_doc({
    #     #             "doctype": "Work Order Item",
    #     #             "parent": doc_name,
    #     #             "parentfield": "required_items",
    #     #             "parenttype": "Work Order",
    #     #             "item_code": item_code,
    #     #             "required_qty": new_required_qty
    #     #         })
    #     #         new_item.insert(ignore_permissions=True)
    #     #
    #     #
    #     #         # Print item code and updated required quantity
    #     #         frappe.msgprint(f"Item Code: {item_code}, New Required Quantity: {new_required_qty}", alert=True)
    #     #
    #     #     # Commit the changes
    #     #     frappe.db.commit()
    #     # except Exception as e:
    #     #     frappe.throw(_("Failed to add or update items for Work Order: {0}. Error: {1}").format(doc_name, str(e)))
    #
    #
    #
    #         # # # # Commit changes to the database
    #         # # frappe.db.commit()
    #         # # # doc.save(ignore_permissions=True)
    #         #
    #         # frappe.db.delete("tabWork Order Item", {"parent": doc.name, "item_code": item_code})
    #
    #     # Fetch updated Work Order to ensure it reflects the changes
    #     updated_doc = frappe.get_doc("Work Order", doc_name)
    #     updated_doc.reload()
    #
    #     # frappe.msgprint(_("Updated required quantities for Work Order: {0}").format(doc_name))
    #
    #     # ==========================================================================
    #     # ==========================================================================
    #     # ==========================================================================


    except frappe.ValidationError as e:
        frappe.msgprint(str(e), alert=True)
    except Exception as ex:
        pass



# ========================================================================
# ========================================================================
# ========================================================================
# ========================================================================






# ========================================================================
# ========================================================================

#  ==== Fetch data from items table - Function to select batch and serial number ====


@frappe.whitelist()
def get_batch_data(item_code=None, warehouse=None, batch_id=None):
    conditions = []

    # Check if columns exist in the Batch table
    columns = frappe.db.sql("SHOW COLUMNS FROM `tabBatch`", as_dict=True)
    column_names = [col['Field'] for col in columns]

    if batch_id:
        conditions.append(f"batch_id = '{batch_id}'")

    if item_code and 'item_code' in column_names:
        conditions.append(f"item_code = '{item_code}'")

    if warehouse and 'warehouse' in column_names:
        conditions.append(f"warehouse = '{warehouse}'")

    condition_str = " AND ".join(conditions) if conditions else "1=1"

    # Query the Batch table
    query = f"""
        SELECT
            name AS batch_name,
            batch_id,
            batch_qty
        FROM `tabBatch`
        WHERE {condition_str}
    """

    result = frappe.db.sql(query, as_dict=True)
    return result
# =======================================

@frappe.whitelist()
def fetch_batch_numbers(item_code):
    filters = {'item': item_code}

    batches = frappe.get_all('Batch',
                             filters=filters,
                             fields=['batch_id', 'batch_qty'])
    return batches



# ========================================================================
# ========================================================================





# ========================================================================
# ========================================================================



# ===========================================================
# ===========================================================
# ======= Validation Qty in BOM (Standard Deviation) ==================


@frappe.whitelist()
def validate_qty_in_bom_standard_deviation(bom_items, selected_item_code=None, selected_idx=None):
    """
    Validate the quantity in BOM (Bill of Materials) based on standard deviation.

    Parameters:
    bom_items (str): JSON string representing the list of items in the BOM. Each item
                     should be a dictionary with 'item_code', 'qty', and 'standard_deviation_a_020'.
    selected_item_code (str, optional): Item code to filter BOM items.
    selected_idx (int, optional): Index to filter BOM items.

    Returns:
    dict: A dictionary with item indices as keys and a boolean indicating if the quantity
          is within the allowable range based on standard deviation percentage.
    """
    import json
    import frappe

    try:
        # Parse JSON strings
        bom_items = json.loads(bom_items)
        selected_idx = int(selected_idx) if selected_idx else None
        selected_item_code = json.loads(selected_item_code) if selected_item_code else None

        # Validation result dictionary
        validation_result = {}

        # Get new_qty from the form dict and convert it to float
        new_qty = float(frappe.form_dict.get('new_qty', 0))

        # Validate each item
        for item in bom_items:
            idx = item.get('idx')
            item_code = item.get('item_code')
            if selected_idx is not None and selected_item_code:
                if idx != selected_idx or item_code != selected_item_code:
                    continue
            elif selected_idx is not None:
                if idx != selected_idx:
                    continue
            elif selected_item_code:
                if item_code != selected_item_code:
                    continue

            qty = float(item.get('qty', 0))
            std_dev_percentage = float(item.get('standard_deviation_a_020', 0))

            # Calculate allowable range
            std_dev_value = qty * (std_dev_percentage / 100)
            lower_bound = qty - std_dev_value
            upper_bound = qty + std_dev_value

            # Validate if the new quantity is within the allowable range
            is_valid = lower_bound <= new_qty <= upper_bound
            validation_result[idx] = is_valid

            # If the new quantity is outside the allowable range, print a message
            if not is_valid:
                frappe.msgprint(
                    f"Quantity for item with idx {idx} and item_code {item_code} exceeds allowable range. Allowed: {lower_bound} - {upper_bound}, Provided: {new_qty}",alert=True
                )

        # Optionally, display selected BOM item in JSON format
        if selected_idx is not None and selected_item_code:
            selected_item = next((item for item in bom_items if item.get('idx') == selected_idx and item.get('item_code') == selected_item_code), None)
        elif selected_idx is not None:
            selected_item = next((item for item in bom_items if item.get('idx') == selected_idx), None)
        elif selected_item_code:
            selected_item = next((item for item in bom_items if item.get('item_code') == selected_item_code), None)
        else:
            selected_item = None

        if selected_item:
            selected_item_json = json.dumps(selected_item, indent=2)
            # frappe.msgprint(f"<pre>{selected_item_json}</pre>")
        else:
            frappe.msgprint(f"No selected item index or item code provided or item not found.", alert=True)

    except (json.JSONDecodeError, TypeError, ValueError) as e:
        frappe.msgprint(f"Error parsing JSON data: {e}", alert=True)
        return {}

    return validation_result



# # ====================================



# #  ======  updates the quantity of a specific item in a Stock Entry  ========
#
#
# @frappe.whitelist()
# def update_item_qty(stock_entry_name, item_code, idx, new_qty):
#     stock_entry = frappe.get_doc("Stock Entry", stock_entry_name)
#
#     for item in stock_entry.items:
#         if item.item_code == item_code and item.idx == idx:
#             item.qty = new_qty
#             stock_entry.save()
#             return True
#
#     return False






# ===========================================================
# ===========================================================










# ===========================================================
# ===========================================================
# ===== Check if stock entry type is Manufacture or Material Transfer for Manufacture =========
# ===== Check if either serial_and_batch_bundle or batch_no is not empty =========



# @frappe.whitelist()
# def check_batch_bundle_and_batch_no(doc, method):
#     # Check if stock entry type is Manufacture or Material Transfer for Manufacture
#     # if doc.stock_entry_type in ['Manufacture', 'Material Transfer for Manufacture']:
#     if doc.stock_entry_type in ['Material Transfer for Manufacture']:
#         for item in doc.items:
#             # Check if serial_and_batch_bundle is empty or batch_no is empty
#             if not item.serial_and_batch_bundle and not item.batch_no:
#                 frappe.msgprint(
#                     _("Row {0}: Either ( Batch Bundle or Batch No ) must be provided.").format(item.idx),
#                     indicator='red',
#                     alert=True
#                 )
#                 raise frappe.ValidationError(_("Validation Error"))





# =========== Ignore this Error =================
@frappe.whitelist()
def check_batch_bundle_and_batch_no(doc, method):
    # # Check if stock entry type is Manufacture or Material Transfer for Manufacture
    # # if doc.stock_entry_type in ['Manufacture', 'Material Transfer for Manufacture']:

    if doc.stock_entry_type in ['Material Transfer for Manufacture']:
        for item in doc.items:
            pass

            # # Check if serial_and_batch_bundle is empty or batch_no is empty
            # if not item.serial_and_batch_bundle and not item.batch_no:
            #     frappe.msgprint(
            #         _("Row {0}: Either ( Batch Bundle or Batch No ) must be provided.").format(item.idx),
            #         indicator='red',
            #         alert=True
            #     )
            #     raise frappe.ValidationError(_("Validation Error"))









# ======== START create_serial_and_batch_bundles  ========








@frappe.whitelist(allow_guest=False)
def create_serial_and_batch_bundles(doc_name, method=None):
    doc = frappe.get_doc("Stock Entry", doc_name)
    bundle_map = {}

    # # check_update_create_batch_bundles = frappe.get_all(
    # #     "Stock Entry",
    # #     filters={"name": doc.name},
    # #     fields=["update_create_batch_bundles"]
    # # )
    #
    # # Query to check the column value
    # query = """
    #         SELECT update_create_batch_bundles
    #         FROM `tabStock Entry`
    #         WHERE name = %s
    #     """
    # check_update_create_batch_bundles = frappe.db.sql(query, (doc_name,), as_dict=True)
    #
    # # if not check_update_create_batch_bundles:
    # #     frappe.throw(f'No Stock Entry found with name: {doc_name}')
    #
    # update_create_batch_bundles_info = check_update_create_batch_bundles[0].get('update_create_batch_bundles', 0)
    #
    # frappe.msgprint(str(update_create_batch_bundles_info), alert=True)

    # # frappe.msgprint(str(update_create_batch_bundles_info), alert=True)
    #
    # if update_create_batch_bundles_info != 1:

    if doc.stock_entry_type == 'Material Transfer for Manufacture':
        for item in doc.items:
            # warehouse = item.get('t_warehouse')
            warehouse = item.get('s_warehouse')
            if warehouse:
                batch_no = get_fifo_batch_no(item.item_code)
                next_serial_number = generate_next_serial_number()

                bundle = frappe.get_doc({
                    'doctype': 'Serial and Batch Bundle',
                    'item_code': item.item_code,
                    'qty': item.qty,
                    'name': next_serial_number,
                    'status': 'Draft',
                    'type_of_transaction': 'Outward',
                    'voucher_type': 'Stock Entry',
                    'voucher_no': doc.name,
                    'item_name': item.item_name,
                    'warehouse': warehouse
                })

                bundle.append('entries', {
                    'batch_no': batch_no,
                    'qty': item.qty
                })

                try:
                    bundle.insert()
                    frappe.msgprint(f'Serial and Batch Bundle created for Item Code: {item.item_code}', alert=True)

                    # existing_bundle = frappe.get_doc('Serial and Batch Bundle', next_serial_number)
                    # if not existing_bundle:
                    #     frappe.throw(f'Serial and Batch Bundle {next_serial_number} not found.')

                    # # Validate Bundle Creation
                    # if not frappe.db.exists('Serial and Batch Bundle', next_serial_number):
                    #     frappe.throw(f'Serial and Batch Bundle {next_serial_number} not found after creation.')

                    # Map the created bundle number to the item code
                    bundle_map[item.item_code] = next_serial_number

                    # Update the Stock Entry items table
                    for se_item in doc.items:
                        if se_item.item_code == item.item_code:
                            if hasattr(se_item, 'serial_and_batch_bundle'):
                                se_item.serial_and_batch_bundle = next_serial_number
                            else:
                                frappe.throw(
                                    f'Stock Entry does not have field `serial_and_batch_bundle` for Item Code: {item.item_code}'
                                )
                    # doc.save()

                    # if update_create_batch_bundles_info != 1:
                    #     frappe.db.set_value("Stock Entry", doc.name, "update_create_batch_bundles_info", 1)

                except frappe.ValidationError as e:
                    frappe.throw(f'Error creating Serial and Batch Bundle for Item Code: {item.item_code}. '
                                 f'Please ensure all required fields are filled. Error details: {str(e)}')

            else:
                frappe.throw(f'Warehouse is missing for item {item.item_code}')

    return bundle_map
def get_fifo_batch_no(item_code):
    batch_no = frappe.db.get_value('Batch',
                                   {'item': item_code},
                                   'name', order_by='creation asc')

    if not batch_no:
        frappe.throw(f'No available batch number for item {item_code}')
    return batch_no


def generate_next_serial_number():
    last_bundle = frappe.get_all('Serial and Batch Bundle', fields=['name'],
                                 order_by='name desc', limit=1)
    if last_bundle:
        last_serial = last_bundle[0]['name']
        return increment_serial_number(last_serial)
    else:
        return 'SABB-00000001'


def increment_serial_number(serial_number):
    prefix = 'SABB-'
    number_part = int(serial_number.replace(prefix, ''), 10)
    next_number = number_part + 1
    return prefix + str(next_number).zfill(8)










# ======== END create_serial_and_batch_bundles  ========








# ===========================================================
# ===========================================================






# ========================================================================
# ========================================================================
# ========  Update the qty of a specific Stock Entry Detail row  ========


# @frappe.whitelist()
# def update_stock_entry_detail(docname, item_code, new_qty):
#     """
#     Update the qty of a specific Stock Entry Detail row.
#
#     Args:
#         docname (str): The name of the Stock Entry document.
#         item_code (str): The item code to update.
#         new_qty (float): The new quantity to set.
#     """
#     stock_entry = frappe.get_doc("Stock Entry", docname)
#
#     try:
#         frappe.db.sql("""
#                 UPDATE `tabStock Entry Detail`
#                 SET qty = %s, transfer_qty = %s
#                 WHERE parent = %s AND item_code = %s
#             """, (new_qty, new_qty, docname, item_code), as_dict=False)
#
#         frappe.db.commit()
#         return _("Quantity updated successfully")
#     except Exception as e:
#         frappe.db.rollback()
#         frappe.throw(_("Error updating quantities: {0}").format(str(e)))




@frappe.whitelist()
def update_stock_entry_detail(docname, item_code, idx, new_qty):
    """
    Update the qty of a specific Stock Entry Detail row.

    Args:
        docname (str): The name of the Stock Entry document.
        item_code (str): The item code to update.
        idx (int): The idx of the item to update.
        new_qty (float): The new quantity to set.
    """
    try:
        frappe.db.sql("""
                    UPDATE `tabStock Entry Detail`
                    SET qty = %s, transfer_qty = %s, change_qty_a_010 = %s
                    WHERE parent = %s AND item_code = %s AND idx = %s
                """, (new_qty, new_qty, 1, docname, item_code, idx), as_dict=False)

        frappe.db.commit()

        # frappe.db.set_value("Stock Entry Detail", docname, "change_qty_a_010", 1)
        # return _("Quantity updated successfully")
    except Exception as e:
        frappe.db.rollback()
        frappe.throw(_("Error updating quantities: {0}").format(str(e)))





# ========================================================================
# ========================================================================






# ========================================================================
# ========================================================================
# ========= Update the qty of a specific Stock Entry Detail row and transfer_qty ===========



@frappe.whitelist()
def update_qty_stock_entry_detail_from_transfer_qty(docname):
    """
    Update the qty of Stock Entry Detail rows where is_finished_item is 1 based on transfer_qty.

    Args:
        docname (str): The name of the Stock Entry document.
    """
    try:
        # Fetch the Stock Entry Detail rows with is_finished_item = 1
        details = frappe.get_all(
            "Stock Entry Detail",
            filters={"parent": docname, "is_finished_item": 1},
            fields=["name", "transfer_qty"]
        )

        if not details:
            frappe.msgprint(
                _("No matching Stock Entry Detail found or is_finished_item is not 1."),
                indicator='red',
                alert=True
            )
            return

        for detail in details:
            # Update qty field to be the same as transfer_qty
            frappe.db.sql("""
                UPDATE `tabStock Entry Detail`
                SET qty = %s
                WHERE name = %s
            """, (detail.transfer_qty, detail.name))

        frappe.db.commit()
        # frappe.msgprint(_("Quantities updated successfully"))

    except Exception as e:
        frappe.db.rollback()
        frappe.throw(_("Error updating quantities: {0}").format(str(e)))






# @frappe.whitelist()
# def update_qty_stock_entry_detail_from_transfer_qty(docname):
#     """
#     Update the qty, basic_rate, valuation_rate, basic_amount, and amount of Stock Entry Detail rows
#     where is_finished_item is 1 based on transfer_qty and standard_valuation_rate.
#
#     Args:
#         docname (str): The name of the Stock Entry document.
#     """
#     try:
#         # Fetch the Stock Entry Detail rows with is_finished_item = 1
#         details = frappe.get_all(
#             "Stock Entry Detail",
#             filters={"parent": docname, "is_finished_item": 1},
#             fields=["name", "transfer_qty", "standard_valuation_rate", "qty",
#                     "basic_rate", "valuation_rate", "basic_amount", "amount"]
#         )
#
#         if not details:
#             frappe.msgprint(
#                 _("No matching Stock Entry Detail found or is_finished_item is not 1."),
#                 indicator='red',
#                 alert=True
#             )
#             return
#
#         for detail in details:
#             # Calculate the basic_rate and valuation_rate
#             standard_valuation_rate = detail.standard_valuation_rate
#             basic_rate = detail.basic_rate
#             valuation_rate = detail.valuation_rate
#
#             # # Calculate the basic_amount and amount
#             # basic_amount = standard_valuation_rate * detail.qty
#             basic_amount = standard_valuation_rate * detail.transfer_qty
#             amount = standard_valuation_rate * detail.transfer_qty
#
#             # # Update the fields in the database
#             # frappe.db.sql("""
#             #     UPDATE `tabStock Entry Detail`
#             #     SET qty = %s,
#             #         basic_rate = %s,
#             #         valuation_rate = %s,
#             #         basic_amount = %s,
#             #         amount = %s
#             #     WHERE name = %s
#             # """, (detail.transfer_qty, basic_rate, valuation_rate, basic_amount, amount, detail.name))
#
#             # Update the fields in the database
#             frappe.db.sql("""
#                             UPDATE `tabStock Entry Detail`
#                             SET qty = %s,
#                                 basic_rate = %s,
#                                 valuation_rate = %s,
#                                 basic_amount = %s,
#                                 amount = %s
#                             WHERE name = %s
#                         """, (detail.transfer_qty, basic_amount, basic_amount, basic_amount, amount, detail.name))
#
#         # for detail in details:
#         #     # frappe.msgprint(str(detail.transfer_qty))
#         #     # frappe.msgprint(str(detail.name))
#         #
#         #     # Update the fields in the database
#         #     frappe.db.sql("""
#         #                 UPDATE `tabStock Entry Detail`
#         #                 SET qty = %s
#         #                 WHERE name = %s
#         #             """, (detail.transfer_qty, detail.name))
#
#         frappe.db.commit()
#         # frappe.msgprint(_("Quantities and rates updated successfully"))
#
#     except Exception as e:
#         frappe.db.rollback()
#         frappe.throw(_("Error updating quantities and rates: {0}").format(str(e)))






# # ============= ** { Change Raw Material Cost } ** ===============
#
#
# @frappe.whitelist()
# def update_qty_stock_entry_detail_from_transfer_qty(docname):
#     """
#     Update the qty, basic_rate, valuation_rate, basic_amount, and amount of Stock Entry Detail rows
#     where is_finished_item is 1 based on transfer_qty and standard_valuation_rate.
#     Also recalculate total_outgoing_value, total_incoming_value, and value_difference.
#
#     Args:
#         docname (str): The name of the Stock Entry document.
#     """
#     try:
#         # Fetch the Stock Entry Detail rows with is_finished_item = 1
#         details = frappe.get_all(
#             "Stock Entry Detail",
#             filters={"parent": docname, "is_finished_item": 1},
#             fields=["name", "transfer_qty", "standard_valuation_rate", "qty",
#                     "basic_rate", "valuation_rate", "basic_amount", "amount"]
#         )
#
#         if not details:
#             frappe.msgprint(
#                 _("No matching Stock Entry Detail found or is_finished_item is not 1."),
#                 indicator='red',
#                 alert=True
#             )
#             return
#
#         total_incoming_value_is_finished_item = 0
#         total_incoming_value_is_scrap_item = 0
#
#         for detail in details:
#             standard_valuation_rate = detail.standard_valuation_rate
#             basic_rate_a = detail.basic_rate
#             valuation_rate = detail.valuation_rate
#             transfer_qty_a = detail.transfer_qty
#
#             basic_amount_a = standard_valuation_rate * detail.transfer_qty
#             amount_a = standard_valuation_rate * detail.transfer_qty
#
#
#             frappe.db.sql("""
#                 UPDATE `tabStock Entry Detail`
#                 SET qty = %s,
#                     basic_rate = %s,
#                     valuation_rate = %s,
#                     basic_amount = %s,
#                     amount = %s
#                 WHERE name = %s
#             """, (detail.transfer_qty, basic_amount_a, basic_amount_a, basic_amount_a, amount_a, detail.name))
#
#             frappe.db.commit()
#
#             # if detail.transfer_qty > 0:
#             #     total_incoming_value += amount
#             # else:
#             #     pass
#
#             amount_aa = amount_a * transfer_qty_a
#
#             total_incoming_value_is_finished_item += amount_aa
#
#
#         details_scrap = frappe.get_all(
#             "Stock Entry Detail",
#             filters={"parent": docname, "is_scrap_item": 1},
#             fields=["name", "transfer_qty", "standard_valuation_rate", "qty",
#                     "basic_rate", "valuation_rate", "basic_amount", "amount"]
#         )
#
#         for detail_b in details_scrap:
#             standard_valuation_rate = detail_b.standard_valuation_rate
#             total_qty = detail_b.qty
#             basic_rate_b = detail_b.basic_rate
#
#             basic_amount_b = standard_valuation_rate * detail_b.qty
#
#             amount_b = basic_rate_b * total_qty
#
#             total_incoming_value_is_scrap_item += amount_b
#
#         # Calculate total incoming value
#         total_incoming_value = total_incoming_value_is_finished_item + total_incoming_value_is_scrap_item
#
#         # # frappe.msgprint(str(total_incoming_value_is_finished_item))
#         # # frappe.msgprint(str(total_incoming_value_is_scrap_item))
#         # # frappe.msgprint(str(total_incoming_value))
#         #
#         # frappe.db.sql("""
#         #     UPDATE `tabStock Entry`
#         #     SET total_incoming_value = %s
#         #     WHERE name = %s
#         # """, (total_incoming_value, docname))
#
#         # Fetch current total_outgoing_value from tabStock Entry
#         total_outgoing_value = frappe.db.get_value(
#             "Stock Entry",
#             {"name": docname},
#             "total_outgoing_value"
#         ) or 0.0
#
#         # Calculate value_difference
#         value_difference = total_incoming_value - total_outgoing_value
#
#         # Update total_incoming_value and value_difference in Stock Entry
#         frappe.db.sql("""
#                     UPDATE `tabStock Entry`
#                     SET total_incoming_value = %s,
#                         value_difference = %s
#                     WHERE name = %s
#                 """, (total_incoming_value, value_difference, docname))
#
#         frappe.db.commit()
#         # frappe.msgprint(_("Quantities and rates updated successfully"))
#
#         # Fetch the Stock Entry
#         stock_entry = frappe.get_doc("Stock Entry", docname)
#         bom_no = stock_entry.bom_no
#
#         if not bom_no:
#             frappe.throw(_("No BOM linked to this Stock Entry."))
#
#         bom_item_detail = frappe.get_all(
#             "BOM Item",
#             filters={"parent": bom_no, },
#             fields=["item_code", "rate"],
#         )
#
#         bom_item_item_code = bom_item_detail[0].get('item_code')
#         bom_item_rate = bom_item_detail[0].get('rate')
#
#         frappe.db.sql("""
#                     UPDATE `tabStock Entry Detail`
#                     SET basic_rate = %s, valuation_rate = %s
#                     WHERE parent = %s AND item_code = %s
#                 """, (bom_item_rate, bom_item_rate, docname, bom_item_item_code))
#
#         frappe.db.commit()
#
#         # Execute the SQL update
#         frappe.db.sql("""
#             UPDATE `tabStock Entry Detail`
#             SET
#                 basic_rate = %s,
#                 valuation_rate = %s,
#                 basic_amount = qty * %s,
#                 amount = qty * %s
#             WHERE parent = %s AND item_code = %s
#         """, (
#             flt(bom_item_rate), flt(bom_item_rate), flt(bom_item_rate), flt(bom_item_rate), docname,
#             bom_item_item_code))
#
#         frappe.db.commit()
#
#         frappe.msgprint(" __ Valuation Rate updated successfully!", alert=True)
#
#
#
#     except Exception as e:
#         frappe.db.rollback()
#         frappe.throw(_("Error updating quantities and rates: {0}").format(str(e)))
#
# # ============= ** { Change Raw Material Cost } ** ===============







# ========================================================================
# ========================================================================









# ========================================================================
# ========================================================================
# ========= Fetch Qty (Finished Item) & UOM (ربطة) ===========








@frappe.whitelist()
def update_finished_item_qty_uom(doc, method=None):
    """
    Updates the Stock Entry items by splitting items into separate rows if:
    - is_finished_item is true
    - UOM is "ربطة"
    - qty > 1
    """

    doc = frappe.get_doc('Stock Entry', doc)

    stock_entry_items = frappe.get_all(
        "Stock Entry Detail",
        filters={"parent": doc.name},
        fields=["name", "item_code", "qty", "uom", "is_finished_item", "is_scrap_item", "basic_rate", "bom_no", "item_name",
                "standard_deviation_a_020", "t_warehouse"]
    )

    # ======== START Fetch total_cost From BOM ==============
    if isinstance(doc, str):
        stock_entry = frappe.get_doc("Stock Entry", doc)
    else:
        stock_entry = doc

    bom_no = stock_entry.bom_no

    bom_fetch_total_cost = frappe.get_all(
        "BOM",
        filters={"name": bom_no},
        fields=["total_cost"]
    )

    if not bom_fetch_total_cost:
        frappe.throw(_("BOM Total Cost not found."))

    bom_total_cost = bom_fetch_total_cost[0].get('total_cost')

    # ======== END Fetch total_cost From BOM ==============

    try:
        for item in stock_entry_items:
            if item["is_finished_item"] == 1 and item["uom"] == "ربطة" and item["qty"] > 1:
                total_qty = item["qty"]

                # Get the whole part and the decimal part
                whole_qty = int(total_qty)
                decimal_qty = round(total_qty - whole_qty, 2)

                # # Update the original item to have quantity 1
                # frappe.db.set_value("Stock Entry Detail", item["name"], "qty", 1)

                # Update the original item
                frappe.db.set_value("Stock Entry Detail", item["name"], {
                    "qty": 1,
                    "basic_rate": bom_total_cost,
                    "valuation_rate": bom_total_cost,
                    "basic_amount": bom_total_cost,
                    "amount": bom_total_cost,
                })


                # Insert rows for the whole quantity
                for i in range(1, whole_qty):
                    query = """
                            INSERT INTO `tabStock Entry Detail`
                            (idx, parent, item_code, name, qty, basic_rate, valuation_rate, basic_amount, amount, uom, stock_uom, parenttype, parentfield, is_finished_item, is_scrap_item, bom_no, conversion_factor, item_name, standard_deviation_a_020, t_warehouse)
                            SELECT
                                IFNULL(MAX(idx), 0) + 1 AS new_idx,
                                %(parent)s,
                                %(item_code)s,
                                CONCAT('djsr', SUBSTRING(MD5(RAND()), 1, 5), SUBSTRING(MD5(RAND()), 1, 1)),
                                %(qty)s,
                                %(basic_rate)s,
                                %(valuation_rate)s,
                                %(basic_amount)s,
                                %(amount)s,
                                %(uom)s,
                                %(stock_uom)s,
                                'Stock Entry',
                                'items',
                                0,
                                1,
                                %(bom_no)s,
                                1,
                                %(item_name)s,
                                %(standard_deviation_a_020)s,
                                %(t_warehouse)s
                            FROM
                                `tabStock Entry Detail`
                            WHERE parent = %(parent)s;
                            """
                    params = {
                        "parent": doc.name,
                        "item_code": item["item_code"],
                        "qty": 1,
                        "basic_rate": bom_total_cost,
                        "valuation_rate": bom_total_cost,
                        "basic_amount": bom_total_cost,
                        "amount": bom_total_cost,
                        "uom": item["uom"],
                        "stock_uom": item["uom"],
                        "bom_no": item["bom_no"],
                        "item_name": item["item_name"],
                        "standard_deviation_a_020": item["standard_deviation_a_020"],
                        "t_warehouse": item["t_warehouse"]
                    }
                    frappe.db.sql(query, params)

                # Insert row for the decimal quantity if it exists
                if decimal_qty > 0:
                    query = """
                            INSERT INTO `tabStock Entry Detail`
                            (idx, parent, item_code, name, qty, basic_rate, valuation_rate, basic_amount, amount, uom, stock_uom, parenttype, parentfield, is_finished_item, is_scrap_item, bom_no, conversion_factor, item_name, standard_deviation_a_020, t_warehouse)
                            SELECT
                                IFNULL(MAX(idx), 0) + 1 AS new_idx,
                                %(parent)s,
                                %(item_code)s,
                                CONCAT('djsr', SUBSTRING(MD5(RAND()), 1, 5), SUBSTRING(MD5(RAND()), 1, 1)),
                                %(qty)s,
                                %(basic_rate)s,
                                %(valuation_rate)s,
                                %(basic_amount)s,
                                %(amount)s,
                                %(uom)s,
                                %(stock_uom)s,
                                'Stock Entry',
                                'items',
                                0,
                                1,
                                %(bom_no)s,
                                1,
                                %(item_name)s,
                                %(standard_deviation_a_020)s,
                                %(t_warehouse)s
                            FROM
                                `tabStock Entry Detail`
                            WHERE parent = %(parent)s;
                            """
                    params = {
                        "parent": doc.name,
                        "item_code": item["item_code"],
                        "qty": decimal_qty,
                        "basic_rate": bom_total_cost,
                        "valuation_rate": bom_total_cost,
                        "basic_amount": bom_total_cost * decimal_qty,
                        "amount": bom_total_cost * decimal_qty,
                        "uom": item["uom"],
                        "stock_uom": item["uom"],
                        "bom_no": item["bom_no"],
                        "item_name": item["item_name"],
                        "standard_deviation_a_020": item["standard_deviation_a_020"],
                        "t_warehouse": item["t_warehouse"]
                    }
                    frappe.db.sql(query, params)

        frappe.db.commit()
        frappe.msgprint(_("Stock Entry items updated successfully."), alert=True)
        doc.reload()

        frappe.db.set_value("Stock Entry", doc, "update_valuation_rate_a_010", 1)

    except Exception as e:
        frappe.throw(_("An error occurred: {0}").format(str(e)))





# ========================================================================
# ========================================================================







# ========================================================================
# ========================================================================
# ========= Set the scrap_material_cost and base_scrap_material_cost to 0 ===========




# @frappe.whitelist()
# def update_bom_cost(doc, method=None):
#     frappe.db.sql("""
#         UPDATE `tabBOM`
#         SET scrap_material_cost = 0, base_scrap_material_cost = 0
#         WHERE name = %s
#     """, (doc,))
#
#     frappe.db.commit()
#
#     bom_doc = frappe.get_doc('BOM', doc)
#     return bom_doc







# ========================================================================
# ========================================================================









# ========================================================================
# ========================================================================
# ========  Update the Cost (Valuation Rate) ========


# @frappe.whitelist()
# def update_stock_entry_valuation_rate(docname, item_code):
#     """
#     Update the Cost (Valuation Rate)
#
#     Args:
#         docname (str): The name of the Stock Entry document.
#         item_code (str): The item code to update.
#     """
#     try:
#         # stock_entry = frappe.get_doc("Stock Entry", docname)
#         # bom_no = stock_entry.bom_no
#         bom_no = docname.bom_no
#
#         bom_item_detail = frappe.get_all(
#             "BOM Item",
#             filters={"parent": bom_no},
#             fields=["item_code", "rate"],
#         )
#
#         bom_item_code = bom_item_detail[0].get('item_code')
#         bom_item_rate = bom_item_detail[0].get('rate')
#
#
#         frappe.db.sql("""
#                     UPDATE `tabStock Entry Detail`
#                     SET basic_rate = %s, valuation_rate = %s
#                     WHERE parent = %s AND item_code = %s
#                 """, (bom_item_rate, bom_item_rate, docname, item_code), as_dict=False)
#
#         frappe.db.commit()
#
#     except Exception as e:
#         frappe.db.rollback()
#         frappe.throw(_("Error updating cost: {0}").format(str(e)))




# # # ============= ** { Change Raw Material Cost } ** ===============
# @frappe.whitelist()
# def update_stock_entry_valuation_rate(docname, item_code):
#     """
#     Update the Cost (Valuation Rate) for a specific item in a Stock Entry.
#
#     Args:
#         docname (str): The name of the Stock Entry document.
#         item_code (str): The item code to update.
#     """
#     try:
#         stock_entry = frappe.get_doc("Stock Entry", docname)
#         bom_no = stock_entry.bom_no
#
#         bom_item_detail = frappe.get_all(
#             "BOM Item",
#             filters={"parent": bom_no, "item_code": item_code},
#             fields=["rate"],
#             limit=1
#         )
#
#         if not bom_item_detail:
#             frappe.throw(_("BOM Item with item code {0} not found.").format(item_code))
#
#         bom_item_rate = bom_item_detail[0].get('rate')
#
#         frappe.db.sql("""
#             UPDATE `tabStock Entry Detail`
#             SET basic_rate = %s, valuation_rate = %s
#             WHERE parent = %s AND item_code = %s
#         """, (bom_item_rate, bom_item_rate, docname, item_code))
#
#         frappe.db.commit()
#
#         # # stock_entry.set_work_order_details()
#         # # stock_entry.set_transfer_qty()
#         # # stock_entry.set_actual_qty()
#         # stock_entry.calculate_rate_and_amount()
#         # stock_entry.save()
#
#
#         # # Fetch the Stock Entry Detail document and calculate basic_amount
#         # stock_entry_detail = frappe.get_doc("Stock Entry Detail", {"parent": docname, "item_code": item_code})
#         #
#         # # Calculate and update the basic_amount
#         # stock_entry_detail.basic_rate = flt(bom_item_rate)
#         # stock_entry_detail.basic_amount = flt(stock_entry_detail.qty) * flt(bom_item_rate)
#         # stock_entry_detail.amount = flt(stock_entry_detail.qty) * flt(bom_item_rate)
#         #
#         # stock_entry_detail.save()
#
#         frappe.db.sql("""
#             UPDATE `tabStock Entry Detail`
#             SET
#                 basic_rate = %s,
#                 basic_amount = qty * %s,
#                 amount = qty * %s
#             WHERE parent = %s AND item_code = %s
#         """, (flt(bom_item_rate), flt(bom_item_rate), flt(bom_item_rate), docname, item_code))
#
#         frappe.db.commit()
#
#         # # Recalculate total incoming and outgoing values
#         # stock_entry.set_total_incoming_outgoing_value()
#         # stock_entry.save()
#
#         # # `stock_entry`
#         # stock_entry.set_total_incoming_outgoing_value()
#         # stock_entry.save(ignore_permissions=True)
#
#         # # Retrieve the Stock Entry document
#         # stock_entry = frappe.get_doc('Stock Entry', docname)
#         #
#         # if not isinstance(stock_entry, frappe.model.document.Document):
#         #     raise ValueError("The retrieved stock_entry is not a valid document.")
#         #
#         # stock_entry.set_total_incoming_outgoing_value()
#         # stock_entry.save(ignore_permissions=True)
#
#
#     except Exception as e:
#         frappe.db.rollback()
#         frappe.throw(_("Error updating cost for item code {0}: {1}").format(item_code, str(e)))
#
# # # ============= ** { Change Raw Material Cost } ** ===============






# ========================================================================
# ========================================================================








# ========================================================================
# ========================================================================
# =======  START Calc Valuation Rate IN Material Transfer for Manufacture  ========





@frappe.whitelist(allow_guest=True)
def update_valuation_rate_in_material_transfer_for_manufacture(doc, item_code, method=None):
    """
    Updates Calc Valuation Rate IN Material Transfer for Manufacture

    Args:
        doc (Document): The Stock Entry document.
    """

    if isinstance(doc, str):
        stock_entry = frappe.get_doc("Stock Entry", doc)
    else:
        stock_entry = doc

    # Check if the Stock Entry type is 'Material Transfer for Manufacture'
    if stock_entry.stock_entry_type != "Material Transfer for Manufacture":
        # frappe.msgprint("This script only works for 'Material Transfer for Manufacture' type Stock Entries.", alert=True)
        return

    try:

        frappe.msgprint("START This script 'Material Transfer for Manufacture' ", alert=True)

        bom_no = stock_entry.bom_no

        bom_item_detail = frappe.get_all(
            "BOM Item",
            filters={"parent": bom_no, "item_code": item_code},
            fields=["rate"],
            limit=1
        )

        if not bom_item_detail:
            frappe.throw(_("BOM Item with item code {0} not found.").format(item_code))

        bom_item_rate = bom_item_detail[0].get('rate')

        # stock_entry.calculate_rate_and_amount()

        frappe.db.sql("""
            UPDATE `tabStock Entry Detail`
            SET basic_rate = %s, valuation_rate = %s, basic_amount = qty * %s, amount = qty * %s
            WHERE parent = %s AND item_code = %s
        """, (bom_item_rate, bom_item_rate, bom_item_rate, bom_item_rate, stock_entry.name,
              item_code))

        frappe.db.commit()

        # frappe.msgprint(str(bom_item_rate), alert=True)

        # stock_entry.set_work_order_details()
        # stock_entry.set_transfer_qty()
        # stock_entry.set_actual_qty()
        # stock_entry.calculate_rate_and_amount()
        # stock_entry.save(ignore_permissions=True)

        # stock_entry.set_total_incoming_outgoing_value()
        # stock_entry.set_total_amount()

        # # stock_entry.calculate_rate_and_amount()
        # stock_entry.save(ignore_permissions=True)




        frappe.msgprint("END This script 'Material Transfer for Manufacture' ", alert=True)
    except Exception as e:
        frappe.throw(_("Error Updating Valuation Rate for Item Code {0}: {1}").format(item_code, str(e)))







    # # ======== START IF Condition Check  =============
    # # if doc.bom_check == 1:
    #
    # bom_check_detail = frappe.get_all(
    #     "Stock Entry",
    #     filters={"name": doc.name},
    #     fields=["bom_check",],
    # )
    # bom_check_info = bom_check_detail[0].get('bom_check')








# =======  END Calc Valuation Rate IN Material Transfer for Manufacture  ========
# ========================================================================
# ========================================================================








# ========================================================================
# ========================================================================
# =======  START  Custom override for get_items_for_mr (Production Plan)  ========



# @frappe.whitelist(allow_guest=True)
# def get_items_for_material_requests_a(doc, warehouses=None, method=None):
#     """
#     Production Plan
#
#     Args:
#         doc (Document): The Production Plan document.
#     """
#     if isinstance(doc, str):
#         production_plan = frappe.get_doc("Production Plan", doc)
#     else:
#         production_plan = doc
#     if warehouses:
#         frappe.msgprint(str(warehouses))
#
#     return warehouses









# # -------------------------------------------
# @frappe.whitelist(allow_guest=True)
# def get_items_for_material_requests_a(doc, warehouses=None, method=None):
#     """
#     Fetch items for the material request in a Production Plan and add them to the `mr_items` table.
#
#     Args:
#         doc (Document or str): The Production Plan document.
#         warehouses (list): List of warehouses (optional).
#         method (str, optional): Optional method argument.
#     """
#
#     if isinstance(doc, str):
#         production_plan = frappe.get_doc("Production Plan", doc)
#     else:
#         production_plan = doc
#
#     if not production_plan:
#         frappe.throw(_("Invalid Production Plan Document"))
#
#     # Clear existing mr_items
#     production_plan.set("mr_items", [])
#
#     po_items = production_plan.get("po_items") if production_plan.get("po_items") else production_plan.get("items")
#
#     if not po_items or not any(row.get("item_code") for row in po_items):
#         frappe.throw(_("Items to Manufacture are required to pull the Raw Materials."), title=_("Items Required"))
#
#     mr_items = []
#
#     for data in po_items:
#         item_code = data.get("item_code")
#         if not item_code:
#             continue
#
#         planned_qty = data.get("required_qty") or data.get("planned_qty")
#         warehouse = production_plan.get("for_warehouse") or data.get("warehouse")
#
#         if not planned_qty:
#             frappe.throw(_("For item {0}: Enter Planned Qty").format(item_code))
#
#         mr_item = frappe._dict({
#             "item_code": item_code,
#             "warehouse": warehouse,
#             "item_name": data.get("item_name"),
#             "quantity": planned_qty,
#             "uom": data.get("uom"),
#             "description": data.get("description"),
#             "schedule_date": data.get("schedule_date"),
#             "material_request_type": data.get("material_request_type") or "Purchase",
#             "conversion_factor": data.get("conversion_factor") or 1.0,
#             "min_order_qty": data.get("min_order_qty") or 1,
#             "requested_qty": data.get("requested_qty") or 0,
#             "projected_qty": data.get("projected_qty") or 0,
#             "actual_qty": data.get("actual_qty") or 0,
#             "reserved_qty_for_production": data.get("reserved_qty_for_production") or 0,
#             "ordered_qty": data.get("ordered_qty") or 0,
#             "safety_stock": data.get("safety_stock") or 0,
#         })
#
#         mr_items.append(mr_item)
#
#     if warehouses:
#         mr_items = [item for item in mr_items if item.get("warehouse") in warehouses]
#
#     for mr_item in mr_items:
#         production_plan.append("mr_items", mr_item)
#
#     production_plan.save()
#
#     # frappe.msgprint(f"{len(mr_items)} items added to the Material Request.")
#
#     return production_plan.mr_items
# # -------------------------------------------












#
# # # -------------------------------------------
# @frappe.whitelist(allow_guest=True)
# def get_items_for_material_requests_a(doc, warehouses=None, method=None):
#     """
#     Fetch raw materials from BOM for the material request in a Production Plan
#     and add them to the `mr_items` table.
#
#     Args:
#         doc (Document or str): The Production Plan document.
#         warehouses (list): List of warehouses (optional).
#         method (str, optional): Optional method argument.
#     """
#
#     if isinstance(doc, str):
#         production_plan = frappe.get_doc("Production Plan", doc)
#     else:
#         production_plan = doc
#
#     if not production_plan:
#         frappe.throw(_("Invalid Production Plan Document"))
#
#     # Clear existing mr_items
#     production_plan.set("mr_items", [])
#
#     mr_items = []
#
#     po_items = production_plan.get("po_items") if production_plan.get("po_items") else production_plan.get("items")
#
#     if not po_items or not any(row.get("item_code") for row in po_items):
#         frappe.throw(_("Items to Manufacture are required to pull the Raw Materials."), title=_("Items Required"))
#
#     for data in po_items:
#         item_code = data.get("item_code")
#         planned_qty = data.get("planned_qty")
#         if not item_code:
#             continue
#
#         bom_name = frappe.db.get_value("BOM", {"item": item_code, "is_active": 1, "is_default": 1}, "name")
#         if not bom_name:
#             frappe.throw(_("No active BOM found for item {0}").format(item_code))
#
#         bom_doc = frappe.get_doc("BOM", bom_name)
#
#         bom_item_detail = frappe.get_all(
#             "BOM Item",
#             filters={"parent": bom_name},
#             fields=["item_code", "item_name", "qty", "uom", "description", "conversion_factor"],
#         )
#
#         frappe.msgprint(str(po_items))
#         frappe.msgprint("=================")
#         frappe.msgprint(str(item_code))
#         frappe.msgprint("=================")
#         frappe.msgprint(str(bom_name))
#         frappe.msgprint("=================")
#         frappe.msgprint(str(bom_doc))
#         frappe.msgprint("=================")
#         frappe.msgprint(str(bom_item_detail))
#         frappe.msgprint("=================")
#
#         for bom_item in bom_item_detail:
#             raw_material_code = bom_item["item_code"]
#             raw_material_qty = bom_item["qty"]
#             warehouse = production_plan.get("for_warehouse") or data.get("warehouse")
#
#             frappe.msgprint("-------------")
#             frappe.msgprint("-------------")
#             frappe.msgprint(str(bom_item_detail))
#             frappe.msgprint("-------------")
#             frappe.msgprint(str(raw_material_code))
#             frappe.msgprint(str(raw_material_qty))
#             frappe.msgprint(str(warehouse))
#             frappe.msgprint("-------------")
#
#             mr_item = frappe._dict({
#                 "item_code": raw_material_code,
#                 "warehouse": warehouse,
#                 "item_name": bom_item["item_name"],
#                 # "quantity": raw_material_qty * (data.get("required_qty") or 1),
#                 "quantity": raw_material_qty * (data.get("planned_qty") or 1),
#                 "uom": bom_item["uom"],
#                 "description": bom_item["description"],
#                 "schedule_date": data.get("schedule_date"),
#                 "material_request_type": data.get("material_request_type") or "Purchase",
#                 "conversion_factor": bom_item["conversion_factor"] or 1.0,
#                 # "min_order_qty": bom_item["min_order_qty"] or 1,
#                 "requested_qty": 0,
#                 "projected_qty": 0,
#                 "actual_qty": 0,
#                 "reserved_qty_for_production": 0,
#                 "ordered_qty": 0,
#                 "safety_stock": 0,
#             })
#
#             mr_items.append(mr_item)
#
#             frappe.msgprint("*****************")
#             frappe.msgprint(str(mr_items))
#             frappe.msgprint("*****************")
#
#     if warehouses:
#         mr_items = [item for item in mr_items if item.get("warehouse") in warehouses]
#
#     for mr_item in mr_items:
#         production_plan.append("mr_items", mr_item)
#
#     production_plan.save()
#
#     return production_plan.mr_items
# # # -------------------------------------------













# # # -------------------------------------------
# # # -------------------------------------------
#
# @frappe.whitelist(allow_guest=True)
# def get_items_for_material_requests_a(doc, warehouses=None, method=None):
#     """
#     Fetch raw materials from BOM for the material request in a Production Plan
#     and add them to the `mr_items` table.
#
#     Args:
#         doc (Document or str): The Production Plan document.
#         warehouses (list): List of warehouses (optional).
#         method (str, optional): Optional method argument.
#     """
#
#     if isinstance(doc, str):
#         production_plan = frappe.get_doc("Production Plan", doc)
#     else:
#         production_plan = doc
#
#     if not production_plan:
#         frappe.throw(_("Invalid Production Plan Document"))
#
#     # Clear existing mr_items
#     production_plan.set("mr_items", [])
#
#     mr_items = []
#
#     po_items = production_plan.get("po_items") if production_plan.get("po_items") else production_plan.get("items")
#
#     if not po_items or not any(row.get("item_code") for row in po_items):
#         frappe.throw(_("Items to Manufacture are required to pull the Raw Materials."), title=_("Items Required"))
#
#     for data in po_items:
#         item_code = data.get("item_code")
#         planned_qty = data.get("planned_qty")
#         if not item_code:
#             continue
#
#         bom_name = frappe.db.get_value("BOM", {"item": item_code, "is_active": 1, "is_default": 1}, "name")
#         if not bom_name:
#             frappe.throw(_("No active BOM found for item {0}").format(item_code))
#
#         bom_doc = frappe.get_doc("BOM", bom_name)
#
#         bom_item_detail = frappe.get_all(
#             "BOM Item",
#             filters={"parent": bom_name},
#             fields=["item_code", "item_name", "qty", "uom", "description", "conversion_factor"],
#         )
#
#         for bom_item in bom_item_detail:
#             raw_material_code = bom_item["item_code"]
#             raw_material_qty = bom_item["qty"]
#             warehouse = production_plan.get("for_warehouse") or data.get("warehouse")
#
#             acute_qty = frappe.db.sql("""
#                 SELECT SUM(actual_qty) AS acute_qty
#                 FROM `tabBin`
#                 WHERE item_code = %s
#             """, raw_material_code, as_dict=True)
#
#             acute_qty = acute_qty[0].get("acute_qty", 0) if acute_qty else 0
#
#             mr_item = frappe._dict({
#                 "item_code": raw_material_code,
#                 "warehouse": warehouse,
#                 "item_name": bom_item["item_name"],
#                 "quantity": raw_material_qty * (data.get("planned_qty") or 1),
#                 "uom": bom_item["uom"],
#                 "description": bom_item["description"],
#                 "schedule_date": data.get("schedule_date"),
#                 "material_request_type": data.get("material_request_type") or "Purchase",
#                 "conversion_factor": bom_item["conversion_factor"] or 1.0,
#                 "requested_qty": 0,
#                 "projected_qty": 0,
#                 "actual_qty": acute_qty,
#                 "reserved_qty_for_production": 0,
#                 "ordered_qty": 0,
#                 "safety_stock": 0,
#             })
#
#             mr_items.append(mr_item)
#
#     if warehouses:
#         mr_items = [item for item in mr_items if item.get("warehouse") in warehouses]
#
#     for mr_item in mr_items:
#         production_plan.append("mr_items", mr_item)
#
#     production_plan.save()
#
#     return production_plan.mr_items
#
#
#
# # # -------------------------------------------
# # # -------------------------------------------












# # -------------------------------------------
# # -------------------------------------------


@frappe.whitelist(allow_guest=True)
def get_items_for_material_requests_a(doc, warehouses=None, method=None):
    """
    Fetch raw materials from BOM for the material request in a Production Plan
    and add them to the `mr_items` table.

    Args:
        doc (Document or str): The Production Plan document.
        warehouses (list): List of warehouses (optional).
        method (str, optional): Optional method argument.
    """

    if isinstance(doc, str):
        production_plan = frappe.get_doc("Production Plan", doc)
    else:
        production_plan = doc

    if not production_plan:
        frappe.throw(_("Invalid Production Plan Document"))

    # Clear existing mr_items
    production_plan.set("mr_items", [])

    mr_items = []

    po_items = production_plan.get("po_items") if production_plan.get("po_items") else production_plan.get("items")

    if not po_items or not any(row.get("item_code") for row in po_items):
        frappe.throw(_("Items to Manufacture are required to pull the Raw Materials."), title=_("Items Required"))

    for data in po_items:
        item_code = data.get("item_code")
        planned_qty = data.get("planned_qty")
        bom_no = data.get("bom_no")
        if not item_code:
            continue

        # # bom_name = frappe.db.get_value("BOM", {"item": item_code, "is_active": 1, "is_default": 1}, "name")
        bom_name = frappe.db.get_value("BOM", {"item": item_code, "is_active": 1, "name": bom_no}, "name")
        if not bom_name:
            frappe.throw(_("No active BOM found for item {0}").format(item_code))

        # frappe.msgprint(str(bom_name), alert=True)


        bom_doc = frappe.get_doc("BOM", bom_name)

        bom_item_detail = frappe.get_all(
            "BOM Item",
            # filters={"parent": bom_name, "bom_no": bom_no},
            filters={"parent": bom_name},
            fields=["item_code", "item_name", "qty", "uom", "description", "conversion_factor"],
        )

        # frappe.msgprint(str("==================="), alert=True)
        # frappe.msgprint(str(bom_item_detail), alert=True)
        # frappe.msgprint(str(bom_item_detail))

        for bom_item in bom_item_detail:
            raw_material_code = bom_item["item_code"]
            raw_material_qty = bom_item["qty"]
            warehouse = production_plan.get("for_warehouse") or data.get("warehouse")

            # Fetch acute_qty for the raw material from tabBin
            acute_qty = frappe.db.sql("""
                SELECT SUM(actual_qty) AS acute_qty
                FROM `tabBin`
                WHERE item_code = %s
            """, raw_material_code, as_dict=True)

            # acute_qty = acute_qty[0].get("acute_qty", 0) if acute_qty else 0

            acute_qty = acute_qty[0].get("acute_qty") if acute_qty else 0
            acute_qty = acute_qty if acute_qty is not None else 0


            # frappe.msgprint(str("*****************"), alert=True)
            # frappe.msgprint(str(acute_qty), alert=True)
            # frappe.msgprint(str(acute_qty))

            required_qty = raw_material_qty * (data.get("planned_qty") or 1)
            ignore_existing_ordered_qty = production_plan.get("ignore_existing_ordered_qty", False)


            if required_qty > acute_qty and not ignore_existing_ordered_qty:
                last_qty = required_qty - acute_qty
            else:
                last_qty = required_qty



            if acute_qty < required_qty or ignore_existing_ordered_qty:
                mr_item = frappe._dict({
                    "item_code": raw_material_code,
                    "warehouse": warehouse,
                    "item_name": bom_item["item_name"],
                    "quantity": last_qty,
                    "uom": bom_item["uom"],
                    "description": bom_item["description"],
                    "schedule_date": data.get("schedule_date"),
                    "material_request_type": data.get("material_request_type") or "Purchase",
                    "conversion_factor": bom_item["conversion_factor"] or 1.0,
                    "requested_qty": 0,
                    "projected_qty": 0,
                    "actual_qty": acute_qty,
                    "reserved_qty_for_production": 0,
                    "ordered_qty": 0,
                    "safety_stock": 0,
                })

                mr_items.append(mr_item)

    if warehouses:
        mr_items = [item for item in mr_items if item.get("warehouse") in warehouses]

    for mr_item in mr_items:
        production_plan.append("mr_items", mr_item)

    production_plan.save()

    return production_plan.mr_items




# # -------------------------------------------
# # -------------------------------------------





























# =======  END  Custom override for get_items_for_mr (Production Plan)  ========
# ========================================================================
# ========================================================================









# ========================================================================
# ========================================================================









# ========================================================================
# ========================================================================
# =======  START  Search for the voucher_no in the Serial and Batch Bundle DocType based on the given Batch No.  ========




@frappe.whitelist(allow_guest=True)
def get_voucher_no_by_batch(batch_no):
    """
    Search for the voucher_no in the Serial and Batch Bundle DocType based on the given Batch No,
    and only return entries where the Stock Entry's docstatus is '0' (Draft).
    """
    voucher_nos = frappe.db.sql("""
        SELECT DISTINCT sab.voucher_no
        FROM `tabSerial and Batch Bundle` sab
        JOIN `tabSerial and Batch Entry` sbe ON sab.name = sbe.parent
        JOIN `tabStock Entry` se ON sab.voucher_no = se.name
        WHERE sbe.batch_no = %s AND se.docstatus = 0  -- Use docstatus for Draft
    """, (batch_no), as_dict=True)

    voucher_no_list = [voucher['voucher_no'] for voucher in voucher_nos]

    return voucher_no_list




# ------------------------------------------------

# @frappe.whitelist(allow_guest=True)
# def get_voucher_no_by_batch(batch_no):
#     """
#     Search for the voucher_no in the Serial and Batch Bundle DocType based on the given Batch No.
#     """
#     voucher_nos = frappe.db.sql("""
#         SELECT DISTINCT sab.voucher_no
#         FROM `tabSerial and Batch Bundle` sab
#         JOIN `tabSerial and Batch Entry` sbe ON sab.name = sbe.parent
#         WHERE sbe.batch_no = %s
#     """, (batch_no), as_dict=True)
#
#     voucher_no_list = [voucher['voucher_no'] for voucher in voucher_nos]
#
#     return voucher_no_list




# =======  END  Search for the voucher_no in the Serial and Batch Bundle DocType based on the given Batch No.  ========
# ========================================================================
# ========================================================================
















# ========================================================================
# ========================================================================
# ========= START Fetch Qty (Finished Item) & UOM (حبة) tie_the_bundle_a_010 ===========





@frappe.whitelist()
def update_finished_item_qty_uom_piece(doc, method=None):
    """
    Updates the Stock Entry items by splitting items into separate rows if:
    - is_finished_item is true
    - UOM is "حبة"
    - qty > tie_the_bundle_a_010
    """

    doc = frappe.get_doc('Stock Entry', doc)

    stock_entry_items = frappe.get_all(
        "Stock Entry Detail",
        filters={"parent": doc.name},
        fields=["name", "item_code", "qty", "uom", "is_finished_item", "is_scrap_item", "basic_rate", "bom_no", "item_name",
                "standard_deviation_a_020", "t_warehouse"]
    )

    # ======== START Fetch total_cost From BOM ==============
    if isinstance(doc, str):
        stock_entry = frappe.get_doc("Stock Entry", doc)
    else:
        stock_entry = doc

    bom_no = stock_entry.bom_no

    bom_fetch_total_cost = frappe.get_all(
        "BOM",
        filters={"name": bom_no},
        fields=["total_cost"]
    )

    if not bom_fetch_total_cost:
        frappe.throw(_("BOM Total Cost not found."))

    bom_total_cost = bom_fetch_total_cost[0].get('total_cost')


    # # tie_the_bundle_a_010
    # # ==================================================

    # Loop to finished item code
    for item_a in stock_entry_items:
        # if item_a["is_finished_item"] == 1 and item_a["uom"] == "حبة" and item_a["qty"] > 100:
        if item_a["is_finished_item"] == 1 and item_a["uom"] == "حبة":
            item_code_is_finished_item = item_a["item_code"]
            # frappe.msgprint("OK")
            # frappe.msgprint(str(item_code_is_finished_item))
            break

    if not item_code_is_finished_item:
        frappe.msgprint("No finished item found with the specified criteria.")


    # if not item_code_is_finished_item:
    #     frappe.throw("No finished item found that meets the criteria.")

    # Fetch items
    item_tie_the_bundle = frappe.get_all(
        "Item",
        filters={
            "item_code": item_code_is_finished_item
        },
        fields=["name", "item_code", "tie_the_bundle_a_010"]
    )

    # if item_tie_the_bundle:
    #     for item_test in item_tie_the_bundle:
    #         frappe.msgprint(
    #             f"Item Name: {item_test['name']}, Item Code: {item_test['item_code']}, Tie The Bundle: {item_test['tie_the_bundle_a_010']}")
    # else:
    #     frappe.msgprint("No items found with the specified filters.")
    #
    # # frappe.msgprint(str(item_code_is_finished_item))
    # # frappe.msgprint(str(item_tie_the_bundle))


    if item_tie_the_bundle:
        for item_test in item_tie_the_bundle:
            info_item_tie_the_bundle = item_test["tie_the_bundle_a_010"]
            # frappe.msgprint(str(info_item_tie_the_bundle))


    for item_aa in stock_entry_items:
        if item_aa["is_finished_item"] == 1 and item_aa["uom"] == "حبة":
            total_qty = item_aa["qty"]

            if total_qty <= 0:
                frappe.throw("The total quantity must be greater than zero.")

            whole_qty = int(total_qty)
            decimal_qty = round(total_qty - whole_qty, 2)

            # if decimal_qty > 0:
            #     full_rows = int(total_qty // decimal_qty)
            #     remaining_qty = total_qty % decimal_qty
            # else:
            #     full_rows = 0
            #     remaining_qty = 0


            # frappe.msgprint(f"Total Quantity: {total_qty}")
            # frappe.msgprint(f"Whole Quantity: {whole_qty}")
            # frappe.msgprint(f"Decimal Quantity: {decimal_qty}")
            # # frappe.msgprint(f"Full Rows: {full_rows}")
            # # frappe.msgprint(f"Remaining Quantity: {remaining_qty}")


    # # ======== END Fetch total_cost From BOM ==============

    try:
        for item in stock_entry_items:
            if item["is_finished_item"] == 1 and item["uom"] == "حبة":
                total_qty = item["qty"]

                # Get the whole part and the decimal part
                whole_qty = int(total_qty)
                decimal_qty = round(total_qty - whole_qty, 2)


                # # Update the original item to have quantity 1
                # frappe.db.set_value("Stock Entry Detail", item["name"], "qty", 1)

                # Update the original item
                frappe.db.set_value("Stock Entry Detail", item["name"], {
                    # "qty": 1,
                    "qty": info_item_tie_the_bundle,
                    "basic_rate": bom_total_cost,
                    "valuation_rate": bom_total_cost,
                    "basic_amount": bom_total_cost,
                    "amount": bom_total_cost,
                })

                full_rows_count = whole_qty // info_item_tie_the_bundle
                remaining_qty = whole_qty % info_item_tie_the_bundle

                # # # # Insert rows for the whole quantity
                # # # for i in range(1, whole_qty):
                # for i in range(1, full_rows_count + 1):
                for i in range(1, full_rows_count):
                    query = """
                            INSERT INTO `tabStock Entry Detail`
                            (idx, parent, item_code, name, qty, basic_rate, valuation_rate, basic_amount, amount, uom, stock_uom, parenttype, parentfield, is_finished_item, is_scrap_item, bom_no, conversion_factor, item_name, standard_deviation_a_020, t_warehouse)
                            SELECT
                                IFNULL(MAX(idx), 0) + 1 AS new_idx,
                                %(parent)s,
                                %(item_code)s,
                                CONCAT('djsr', SUBSTRING(MD5(RAND()), 1, 5), SUBSTRING(MD5(RAND()), 1, 1)),
                                %(qty)s,
                                %(basic_rate)s,
                                %(valuation_rate)s,
                                %(basic_amount)s,
                                %(amount)s,
                                %(uom)s,
                                %(stock_uom)s,
                                'Stock Entry',
                                'items',
                                0,
                                1,
                                %(bom_no)s,
                                1,
                                %(item_name)s,
                                %(standard_deviation_a_020)s,
                                %(t_warehouse)s
                            FROM
                                `tabStock Entry Detail`
                            WHERE parent = %(parent)s;
                            """
                    params = {
                        "parent": doc.name,
                        "item_code": item["item_code"],
                        # "qty": 1,
                        "qty": info_item_tie_the_bundle,
                        "basic_rate": bom_total_cost,
                        "valuation_rate": bom_total_cost,
                        "basic_amount": bom_total_cost,
                        "amount": bom_total_cost,
                        "uom": item["uom"],
                        "stock_uom": item["uom"],
                        "bom_no": item["bom_no"],
                        "item_name": item["item_name"],
                        "standard_deviation_a_020": item["standard_deviation_a_020"],
                        "t_warehouse": item["t_warehouse"]
                    }
                    frappe.db.sql(query, params)

                # # Insert row for the decimal quantity if it exists
                # if decimal_qty > 0:

                if remaining_qty > 0 or decimal_qty > 0:
                    last_qty = remaining_qty + decimal_qty
                    query = """
                            INSERT INTO `tabStock Entry Detail`
                            (idx, parent, item_code, name, qty, basic_rate, valuation_rate, basic_amount, amount, uom, stock_uom, parenttype, parentfield, is_finished_item, is_scrap_item, bom_no, conversion_factor, item_name, standard_deviation_a_020, t_warehouse)
                            SELECT
                                IFNULL(MAX(idx), 0) + 1 AS new_idx,
                                %(parent)s,
                                %(item_code)s,
                                CONCAT('djsr', SUBSTRING(MD5(RAND()), 1, 5), SUBSTRING(MD5(RAND()), 1, 1)),
                                %(qty)s,
                                %(basic_rate)s,
                                %(valuation_rate)s,
                                %(basic_amount)s,
                                %(amount)s,
                                %(uom)s,
                                %(stock_uom)s,
                                'Stock Entry',
                                'items',
                                0,
                                1,
                                %(bom_no)s,
                                1,
                                %(item_name)s,
                                %(standard_deviation_a_020)s,
                                %(t_warehouse)s
                            FROM
                                `tabStock Entry Detail`
                            WHERE parent = %(parent)s;
                            """
                    params = {
                        "parent": doc.name,
                        "item_code": item["item_code"],
                        # "qty": decimal_qty,
                        "qty": last_qty,
                        "basic_rate": bom_total_cost,
                        "valuation_rate": bom_total_cost,
                        "basic_amount": bom_total_cost * decimal_qty,
                        "amount": bom_total_cost * decimal_qty,
                        "uom": item["uom"],
                        "stock_uom": item["uom"],
                        "bom_no": item["bom_no"],
                        "item_name": item["item_name"],
                        "standard_deviation_a_020": item["standard_deviation_a_020"],
                        "t_warehouse": item["t_warehouse"]
                    }
                    frappe.db.sql(query, params)

        frappe.db.commit()
        frappe.msgprint(_("Stock Entry items updated successfully."), alert=True)
        doc.reload()

        frappe.db.set_value("Stock Entry", doc, "update_valuation_rate_a_010", 1)

    except Exception as e:
        frappe.throw(_("An error occurred: {0}").format(str(e)))





# =======  END Fetch Qty (Finished Item) & UOM (حبة)  tie_the_bundle_a_010  ========
# ========================================================================
# ========================================================================




# ========================================================================
# ========================================================================












# ========================================================================
# ========================================================================
# ========= START Fetch Qty (Scrap Item) (Production Items Table) & UOM (حبة) tie_the_bundle_a_010 ===========





@frappe.whitelist()
def update_production_items_qty_uom_piece(doc, method=None):
    """
    Updates the Stock Entry items by splitting items into separate rows if:
    - is_scrap_item is true
    - UOM is "حبة"
    - qty > tie_the_bundle_a_010
    """

    # Fetch the Stock Entry document
    doc = frappe.get_doc('Stock Entry', doc)

    # Fetch the Stock Entry Detail items for this stock entry
    stock_entry_items = frappe.get_all(
        "Stock Entry Detail",
        filters={"parent": doc.name},
        fields=[
            "name", "item_code", "qty", "uom", "is_scrap_item",
            "basic_rate", "bom_no", "item_name", "standard_deviation_a_020",
            "t_warehouse", "stock_uom", "conversion_factor"
        ]
    )

    # Fetch BOM Total Cost
    bom_total_cost = frappe.db.get_value("BOM", doc.bom_no, "total_cost")
    if not bom_total_cost:
        frappe.throw(_("BOM Total Cost not found for BOM: {0}".format(doc.bom_no)))

    try:
        for scrap_item in stock_entry_items:
            if scrap_item["is_scrap_item"] and scrap_item["uom"] == "حبة":
                item_code = scrap_item["item_code"]
                qty = scrap_item["qty"]

                # Fetch tie_the_bundle_a_010 value for the item
                tie_the_bundle = frappe.db.get_value("Item", item_code, "tie_the_bundle_a_010")
                if not tie_the_bundle:
                    frappe.throw(_(f"Bundle size not defined for item {item_code}"))

                # Validate required fields
                if not scrap_item["stock_uom"]:
                    frappe.throw(_(f"Stock UOM missing for item {item_code}"))
                if not scrap_item["conversion_factor"]:
                    frappe.throw(_(f"Conversion Factor missing for item {item_code}"))

                # Calculate whole rows and remaining quantity
                full_rows_count = int(qty // tie_the_bundle)
                remaining_qty = qty % tie_the_bundle

                # Update the original item with one bundle quantity
                frappe.db.set_value("Stock Entry Detail", scrap_item["name"], {
                    "qty": tie_the_bundle,
                    "basic_rate": bom_total_cost,
                    "valuation_rate": bom_total_cost,
                    "basic_amount": bom_total_cost * tie_the_bundle,
                    "amount": bom_total_cost * tie_the_bundle,
                })

                # Insert the full rows for the bundle quantity
                for i in range(1, full_rows_count):
                    query = """
                            INSERT INTO `tabStock Entry Detail`
                            (idx, parent, item_code, name, qty, basic_rate, valuation_rate, basic_amount, amount, uom, stock_uom, parenttype, parentfield, is_scrap_item, bom_no, conversion_factor, item_name, standard_deviation_a_020, t_warehouse)
                            SELECT
                                IFNULL(MAX(idx), 0) + 1 AS new_idx,
                                %(parent)s,
                                %(item_code)s,
                                CONCAT('djsr', SUBSTRING(MD5(RAND()), 1, 5), SUBSTRING(MD5(RAND()), 1, 1)),
                                %(qty)s,
                                %(basic_rate)s,
                                %(valuation_rate)s,
                                %(basic_amount)s,
                                %(amount)s,
                                %(uom)s,
                                %(stock_uom)s,
                                'Stock Entry',
                                'items',
                                1,
                                %(bom_no)s,
                                1,
                                %(item_name)s,
                                %(standard_deviation_a_020)s,
                                %(t_warehouse)s
                            FROM
                                `tabStock Entry Detail`
                            WHERE parent = %(parent)s;
                            """
                    params = {
                        "parent": doc.name,
                        "item_code": scrap_item["item_code"],
                        "qty": tie_the_bundle,
                        "basic_rate": bom_total_cost,
                        "valuation_rate": bom_total_cost,
                        "basic_amount": bom_total_cost * tie_the_bundle,
                        "amount": bom_total_cost * tie_the_bundle,
                        "uom": scrap_item["uom"],
                        "stock_uom": scrap_item["uom"],
                        "bom_no": scrap_item["bom_no"],
                        "item_name": scrap_item["item_name"],
                        "standard_deviation_a_020": scrap_item["standard_deviation_a_020"],
                        "t_warehouse": scrap_item["t_warehouse"]
                    }
                    frappe.db.sql(query, params)

                # Insert the remaining quantity as a new entry if necessary
                if remaining_qty > 0:
                    query = """
                            INSERT INTO `tabStock Entry Detail`
                            (idx, parent, item_code, name, qty, basic_rate, valuation_rate, basic_amount, amount, uom, stock_uom, parenttype, parentfield, is_scrap_item, bom_no, conversion_factor, item_name, standard_deviation_a_020, t_warehouse)
                            SELECT
                                IFNULL(MAX(idx), 0) + 1 AS new_idx,
                                %(parent)s,
                                %(item_code)s,
                                CONCAT('djsr', SUBSTRING(MD5(RAND()), 1, 5), SUBSTRING(MD5(RAND()), 1, 1)),
                                %(qty)s,
                                %(basic_rate)s,
                                %(valuation_rate)s,
                                %(basic_amount)s,
                                %(amount)s,
                                %(uom)s,
                                %(stock_uom)s,
                                'Stock Entry',
                                'items',
                                1,
                                %(bom_no)s,
                                1,
                                %(item_name)s,
                                %(standard_deviation_a_020)s,
                                %(t_warehouse)s
                            FROM
                                `tabStock Entry Detail`
                            WHERE parent = %(parent)s;
                            """
                    params = {
                        "parent": doc.name,
                        "item_code": scrap_item["item_code"],
                        "qty": remaining_qty,
                        "basic_rate": bom_total_cost,
                        "valuation_rate": bom_total_cost,
                        "basic_amount": bom_total_cost * remaining_qty,
                        "amount": bom_total_cost * remaining_qty,
                        "uom": scrap_item["uom"],
                        "stock_uom": scrap_item["uom"],
                        "bom_no": scrap_item["bom_no"],
                        "item_name": scrap_item["item_name"],
                        "standard_deviation_a_020": scrap_item["standard_deviation_a_020"],
                        "t_warehouse": scrap_item["t_warehouse"]
                    }
                    frappe.db.sql(query, params)

        # Commit changes and refresh document
        frappe.db.commit()
        frappe.msgprint(_("Stock Entry items updated successfully."), alert=True)
        doc.reload()

        frappe.db.set_value("Stock Entry", doc.name, "update_valuation_rate_a_010", 1)

    except Exception as e:
        frappe.throw(_("An error occurred: {0}").format(str(e)))









# # *************************************************
#
# @frappe.whitelist()
# def update_production_items_qty_uom_piece(doc, method=None):
#     """
#     Updates the Stock Entry items by splitting items into separate rows if:
#     - is_scrap_item is true
#     - UOM is "حبة"
#     - qty > tie_the_bundle_a_010
#     """
#
#     doc = frappe.get_doc('Stock Entry', doc)
#
#     stock_entry_items = frappe.get_all(
#         "Stock Entry Detail",
#         filters={"parent": doc.name},
#         fields=[
#             "name", "item_code", "qty", "uom", "is_scrap_item",
#             "basic_rate", "bom_no", "item_name", "standard_deviation_a_020",
#             "t_warehouse", "stock_uom", "conversion_factor"
#         ]
#     )
#
#     # Fetch BOM Total Cost
#     bom_total_cost = frappe.db.get_value("BOM", doc.bom_no, "total_cost")
#     if not bom_total_cost:
#         frappe.throw(_("BOM Total Cost not found for BOM: {0}".format(doc.bom_no)))
#
#     try:
#         for scrap_item in stock_entry_items:
#             if scrap_item["is_scrap_item"] and scrap_item["uom"] == "حبة":
#                 item_code = scrap_item["item_code"]
#                 qty = scrap_item["qty"]
#
#                 # Fetch tie_the_bundle_a_010 value for the item
#                 tie_the_bundle = frappe.db.get_value("Item", item_code, "tie_the_bundle_a_010")
#                 if not tie_the_bundle:
#                     frappe.throw(_(f"Bundle size not defined for item {item_code}"))
#
#                 # Validate required fields
#                 if not scrap_item["stock_uom"]:
#                     frappe.throw(_(f"Stock UOM missing for item {item_code}"))
#                 if not scrap_item["conversion_factor"]:
#                     frappe.throw(_(f"Conversion Factor missing for item {item_code}"))
#
#                 # Calculate whole rows and remaining quantity
#                 full_rows_count = int(qty // tie_the_bundle)
#                 remaining_qty = qty % tie_the_bundle
#
#                 # Update the original item with one bundle quantity
#                 frappe.db.set_value("Stock Entry Detail", scrap_item["name"], {
#                     "qty": tie_the_bundle,
#                     "basic_rate": bom_total_cost,
#                     "valuation_rate": bom_total_cost,
#                     "basic_amount": bom_total_cost * tie_the_bundle,
#                     "amount": bom_total_cost * tie_the_bundle,
#                 })
#
#                 # # Add rows for the rest of the bundles
#                 # for _ in range(full_rows_count - 1):
#                 #     frappe.get_doc({
#                 #         "doctype": "Stock Entry Detail",
#                 #         "parent": doc.name,
#                 #         "parentfield": "items",
#                 #         "parenttype": "Stock Entry",
#                 #         "item_code": item_code,
#                 #         "qty": tie_the_bundle,
#                 #         "uom": scrap_item["uom"],
#                 #         "stock_uom": scrap_item["stock_uom"],
#                 #         "conversion_factor": scrap_item["conversion_factor"],
#                 #         "basic_rate": bom_total_cost,
#                 #         "valuation_rate": bom_total_cost,
#                 #         "basic_amount": bom_total_cost * tie_the_bundle,
#                 #         "amount": bom_total_cost * tie_the_bundle,
#                 #         "t_warehouse": scrap_item["t_warehouse"]
#                 #     }).insert(ignore_permissions=True)
#                 #
#                 # # Add a row for the remaining quantity if applicable
#                 # if remaining_qty > 0:
#                 #     frappe.get_doc({
#                 #         "doctype": "Stock Entry Detail",
#                 #         "parent": doc.name,
#                 #         "parentfield": "items",
#                 #         "parenttype": "Stock Entry",
#                 #         "item_code": item_code,
#                 #         "qty": remaining_qty,
#                 #         "uom": scrap_item["uom"],
#                 #         "stock_uom": scrap_item["stock_uom"],
#                 #         "conversion_factor": scrap_item["conversion_factor"],
#                 #         "basic_rate": bom_total_cost,
#                 #         "valuation_rate": bom_total_cost,
#                 #         "basic_amount": bom_total_cost * remaining_qty,
#                 #         "amount": bom_total_cost * remaining_qty,
#                 #         "t_warehouse": scrap_item["t_warehouse"]
#                 #     }).insert(ignore_permissions=True)
#
#         frappe.db.commit()
#         frappe.msgprint(_("Stock Entry items updated successfully."), alert=True)
#         doc.reload()
#
#     except Exception as e:
#         frappe.throw(_(f"An error occurred: {str(e)}"))
#
# # ***********************************************








# # ------------------------------------------------------------------------------------
#
#
# @frappe.whitelist()
# def update_production_items_qty_uom_piece(doc, method=None):
#     """
#     Updates the Stock Entry items by splitting items into separate rows if:
#     - is_scrap_item is true
#     - UOM is "حبة"
#     - qty > tie_the_bundle_a_010
#     """
#
#     doc = frappe.get_doc('Stock Entry', doc)
#
#     stock_entry_items_a = frappe.get_all(
#         "Stock Entry Detail",
#         filters={"parent": doc.name},
#         fields=["name", "item_code", "qty", "uom", "is_finished_item", "is_scrap_item", "basic_rate", "bom_no", "item_name",
#                 "standard_deviation_a_020", "t_warehouse"]
#     )
#
#     # ======== START Fetch total_cost From BOM ==============
#     if isinstance(doc, str):
#         stock_entry = frappe.get_doc("Stock Entry", doc)
#     else:
#         stock_entry = doc
#
#     bom_no = stock_entry.bom_no
#
#     bom_fetch_total_cost = frappe.get_all(
#         "BOM",
#         filters={"name": bom_no},
#         fields=["total_cost"]
#     )
#
#     if not bom_fetch_total_cost:
#         frappe.throw(_("BOM Total Cost not found."))
#
#     bom_total_cost = bom_fetch_total_cost[0].get('total_cost')
#
#
#     # # tie_the_bundle_a_010
#     # # ==================================================
#
#     # Loop to finished item code
#     for item_a_a in stock_entry_items_a:
#         # if item_a["is_finished_item"] == 1 and item_a["uom"] == "حبة" and item_a["qty"] > 100:
#         if item_a_a["is_scrap_item"] == 1 and item_a_a["uom"] == "حبة":
#             item_code_is_scrap_item= item_a_a["item_code"]
#             # frappe.msgprint("OK")
#             # frappe.msgprint(str(item_code_is_finished_item))
#             break
#
#     if not item_code_is_scrap_item:
#         frappe.msgprint("No Scrap item item found with the specified criteria.")
#
#     # Fetch items
#     item_tie_the_bundle_a = frappe.get_all(
#         "Item",
#         filters={
#             "item_code": item_code_is_scrap_item
#         },
#         fields=["name", "item_code", "tie_the_bundle_a_010"]
#     )
#
#     if item_tie_the_bundle_a:
#         for item_test_a in item_tie_the_bundle_a:
#             info_item_tie_the_bundle_a = item_test_a["tie_the_bundle_a_010"]
#             # frappe.msgprint(str(info_item_tie_the_bundle))
#
#
#     for item_aa_a in stock_entry_items_a:
#         if item_aa_a["is_scrap_item"] == 1 and item_aa_a["uom"] == "حبة":
#             total_qty_a = item_aa_a["qty"]
#
#             if total_qty_a <= 0:
#                 frappe.throw("The total quantity must be greater than zero.")
#
#             whole_qty_a = int(total_qty_a)
#             decimal_qty_a = round(total_qty_a - whole_qty_a, 2)
#
#             # frappe.msgprint(f"Total Quantity: {total_qty}")
#             # frappe.msgprint(f"Whole Quantity: {whole_qty}")
#             # frappe.msgprint(f"Decimal Quantity: {decimal_qty}")
#             # # frappe.msgprint(f"Full Rows: {full_rows}")
#             # # frappe.msgprint(f"Remaining Quantity: {remaining_qty}")
#
#
#     # # ======== END Fetch total_cost From BOM ==============
#
#     try:
#         for item_a in stock_entry_items_a:
#             if item_a["is_scrap_item"] == 1 and item_a["uom"] == "حبة":
#                 total_qty_b = item_a["qty"]
#
#                 # Get the whole part and the decimal part
#                 whole_qty_b = int(total_qty_b)
#                 decimal_qty_b = round(total_qty_b - whole_qty_b, 2)
#
#
#                 # Update the original item
#                 frappe.db.set_value("Stock Entry Detail", item_a["name"], {
#                     # "qty": 1,
#                     "qty": info_item_tie_the_bundle_a,
#                     "basic_rate": bom_total_cost,
#                     "valuation_rate": bom_total_cost,
#                     "basic_amount": bom_total_cost,
#                     "amount": bom_total_cost,
#                 })
#
#                 full_rows_count = whole_qty_b // info_item_tie_the_bundle_a
#                 remaining_qty = whole_qty_b % info_item_tie_the_bundle_a
#
#                 for i in range(1, full_rows_count):
#                     query = """
#                             INSERT INTO `tabStock Entry Detail`
#                             (idx, parent, item_code, name, qty, basic_rate, valuation_rate, basic_amount, amount, uom, stock_uom, parenttype, parentfield, is_finished_item, is_scrap_item, bom_no, conversion_factor, item_name, standard_deviation_a_020, t_warehouse)
#                             SELECT
#                                 IFNULL(MAX(idx), 0) + 1 AS new_idx,
#                                 %(parent)s,
#                                 %(item_code)s,
#                                 CONCAT('djsr', SUBSTRING(MD5(RAND()), 1, 5), SUBSTRING(MD5(RAND()), 1, 1)),
#                                 %(qty)s,
#                                 %(basic_rate)s,
#                                 %(valuation_rate)s,
#                                 %(basic_amount)s,
#                                 %(amount)s,
#                                 %(uom)s,
#                                 %(stock_uom)s,
#                                 'Stock Entry',
#                                 'items',
#                                 1,
#                                 0,
#                                 %(bom_no)s,
#                                 1,
#                                 %(item_name)s,
#                                 %(standard_deviation_a_020)s,
#                                 %(t_warehouse)s
#                             FROM
#                                 `tabStock Entry Detail`
#                             WHERE parent = %(parent)s;
#                             """
#                     params = {
#                         "parent": doc.name,
#                         "item_code": item_a["item_code"],
#                         # "qty": 1,
#                         "qty": info_item_tie_the_bundle_a,
#                         "basic_rate": bom_total_cost,
#                         "valuation_rate": bom_total_cost,
#                         "basic_amount": bom_total_cost,
#                         "amount": bom_total_cost,
#                         "uom": item_a["uom"],
#                         "stock_uom": item_a["uom"],
#                         "bom_no": item_a["bom_no"],
#                         "item_name": item_a["item_name"],
#                         "standard_deviation_a_020": item_a["standard_deviation_a_020"],
#                         "t_warehouse": item_a["t_warehouse"]
#                     }
#                     frappe.db.sql(query, params)
#
#
#                 if remaining_qty > 0 or decimal_qty_b > 0:
#                     last_qty = remaining_qty + decimal_qty_b
#                     query = """
#                             INSERT INTO `tabStock Entry Detail`
#                             (idx, parent, item_code, name, qty, basic_rate, valuation_rate, basic_amount, amount, uom, stock_uom, parenttype, parentfield, is_finished_item, is_scrap_item, bom_no, conversion_factor, item_name, standard_deviation_a_020, t_warehouse)
#                             SELECT
#                                 IFNULL(MAX(idx), 0) + 1 AS new_idx,
#                                 %(parent)s,
#                                 %(item_code)s,
#                                 CONCAT('djsr', SUBSTRING(MD5(RAND()), 1, 5), SUBSTRING(MD5(RAND()), 1, 1)),
#                                 %(qty)s,
#                                 %(basic_rate)s,
#                                 %(valuation_rate)s,
#                                 %(basic_amount)s,
#                                 %(amount)s,
#                                 %(uom)s,
#                                 %(stock_uom)s,
#                                 'Stock Entry',
#                                 'items',
#                                 1,
#                                 0,
#                                 %(bom_no)s,
#                                 1,
#                                 %(item_name)s,
#                                 %(standard_deviation_a_020)s,
#                                 %(t_warehouse)s
#                             FROM
#                                 `tabStock Entry Detail`
#                             WHERE parent = %(parent)s;
#                             """
#                     params = {
#                         "parent": doc.name,
#                         "item_code": item_a["item_code"],
#                         # "qty": decimal_qty,
#                         "qty": last_qty,
#                         "basic_rate": bom_total_cost,
#                         "valuation_rate": bom_total_cost,
#                         "basic_amount": bom_total_cost * decimal_qty_b,
#                         "amount": bom_total_cost * decimal_qty_b,
#                         "uom": item_a["uom"],
#                         "stock_uom": item_a["uom"],
#                         "bom_no": item_a["bom_no"],
#                         "item_name": item_a["item_name"],
#                         "standard_deviation_a_020": item_a["standard_deviation_a_020"],
#                         "t_warehouse": item_a["t_warehouse"]
#                     }
#                     frappe.db.sql(query, params)
#
#         frappe.db.commit()
#         frappe.msgprint(_("Stock Entry items updated successfully."), alert=True)
#         doc.reload()
#
#         frappe.db.set_value("Stock Entry", doc, "update_valuation_rate_a_010", 1)
#
#     except Exception as e:
#         frappe.throw(_("An error occurred: {0}").format(str(e)))
#
# # ------------------------------------------------------------------------------------



# =======  END Fetch Qty (Scrap Item) (Production Items Table) & UOM (حبة)  tie_the_bundle_a_010  ========
# ========================================================================
# ========================================================================










# ========================================================================
# ========================================================================












# ========================================================================
# ========================================================================















# ========================================================================
# ========================================================================












# ========================================================================
# ========================================================================



















# ========================================================================
# ========================================================================









# ========================================================================
# ========================================================================
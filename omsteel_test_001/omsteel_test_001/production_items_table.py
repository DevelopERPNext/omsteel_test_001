# Copyright (c) 2024, Mahmoud Khattab
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe import _

import json



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
        fields=["item", "quantity", ],
    )

    bom_production_item_check_info = bom_production_item_check_detail[0].get('quantity')
    bom_production_item_code = bom_production_item_check_detail[0].get('item')
    # frappe.msgprint(f"Item Code: {bom_production_item_code} , Qty {bom_production_item_check_info}")

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

    # Check if a result is returned and extract the value
    # if bom_check_info == 0:
    if bom_check_info == 1:
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
            fields=["parent", "parentfield", "item_code", "item_name", "rate", "stock_qty", "stock_uom"]
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
                    frappe.db.delete("Stock Entry Detail", {"parent": doc.name, "item_code": item_code})

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
            key = (item["item_code"], item["item_name"], item["stock_qty"], item["rate"], item["stock_uom"])
            if key in item_count:
                item_count[key] += 1
            else:
                item_count[key] = 1

        # frappe.msgprint(str(item_count), alert=True)
        # frappe.msgprint(str(item_count))

        # Loop through item_count to handle items with count > 1
        for key, count in item_count.items():
            item_code, item_name, stock_qty, rate, stock_uom = key
            # frappe.msgprint(str(type(count)))
            # frappe.msgprint(str(count))

            calc_stock_qty = stock_qty / calc_a_test

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
                                (idx, parent, item_code, name, qty, basic_rate, uom, stock_uom, parenttype, parentfield, is_scrap_item, bom_no, conversion_factor, item_name, t_warehouse)
                                SELECT
                                    IFNULL(MAX(idx), 0) + 1 AS new_idx,
                                    %(parent)s,
                                    %(item_code)s,
                                    CONCAT('djsr', SUBSTRING(MD5(RAND()), 1, 5), SUBSTRING(MD5(RAND()), 1, 1)),
                                    %(qty)s,
                                    %(basic_rate)s,
                                    %(uom)s,
                                    %(stock_uom)s,
                                    'Stock Entry',
                                    'items',
                                    1,
                                    %(bom_no)s,
                                    1,
                                    %(item_name)s,
                                    %(t_warehouse)s
                                FROM
                                    `tabStock Entry Detail`
                                WHERE parent = %(parent)s;
                            """

                        params = {
                            "parent": doc.name,
                            "item_code": item_code,
                            "qty": calc_stock_qty,
                            "basic_rate": basic_rate,
                            "uom": stock_uom,
                            "stock_uom": stock_uom,
                            "bom_no": bom_no,
                            "item_name": item_name,
                            "t_warehouse": scrap_warehouse_value
                        }

                        frappe.db.sql(query, params)
                        # frappe.msgprint("Record inserted successfully", alert=True)
                    except Exception as e:
                        frappe.msgprint(f"Error occurred: {e}")

        frappe.db.set_value("Stock Entry", doc.name, "bom_check", 1)

        # doc.save(ignore_permissions=True)
        # frappe.db.commit()
        doc.reload()
        frappe.msgprint(_("Stock Entry items updated successfully."), alert=True)

        # ======== END IF Condition Check  =============
    else:
        pass

#  ************ ===============  ****************

#  ===============   END update_stock_entry_items  ====================




# ========================================================================
# ========================================================================


# @frappe.whitelist(allow_guest=True)
# def move_data_from_production_items_table_to_scrap_items(doc, method=None):
#
#
#     doc_dict = frappe.parse_json(doc) if isinstance(doc, str) else doc
#     production_items = doc_dict.get('production_items_a_001')
#
#     if not production_items:
#         pass
#     else:
#         doc.scrap_items = []
#
#     if production_items:
#         for item in production_items:
#             scrap_item_data = {
#                 'item_code': item.item_code,
#                 'item_name': item.item_name,
#                 'stock_qty': item.stock_qty,
#                 'rate': item.rate,
#                 'amount': item.amount,
#                 'stock_uom': item.stock_uom,
#                 'base_rate': item.base_rate,
#                 'base_amount': item.base_amount,
#             }
#             doc.append('scrap_items', scrap_item_data)
#
#         try:
#             doc.save(ignore_permissions=True)
#             frappe.db.commit()
#             doc.reload()
#             frappe.msgprint("Production Items have been created successfully!", alert=True)
#         except frappe.ValidationError as e:
#             frappe.msgprint(str(e), alert=True)


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
                'base_amount': item.get('base_amount')
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
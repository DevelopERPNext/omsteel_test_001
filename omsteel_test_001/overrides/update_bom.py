from erpnext.manufacturing.doctype.bom.bom import BOM
import frappe
from frappe.utils import flt


class CustomBOM(BOM):
    def calculate_cost(self, save_updates=False, update_hour_rate=False):
        # """Calculate BOM totals"""
        # frappe.db.sql("""
        #     UPDATE `tabBOM`
        #     SET scrap_material_cost = 0, base_scrap_material_cost = 0
        #     WHERE name = %s
        # """, (self.name,))
        #
        # frappe.db.commit()

        self.calculate_op_cost(update_hour_rate)
        self.calculate_rm_cost(save=save_updates)
        self.calculate_sm_cost(save=save_updates)

        if save_updates:
            self.calculate_exploded_cost()

        old_cost = self.total_cost

        # self.total_cost = self.operating_cost + self.raw_material_cost - self.scrap_material_cost
        self.total_cost = self.operating_cost + self.raw_material_cost
        # self.base_total_cost = (
        #     self.base_operating_cost + self.base_raw_material_cost - self.base_scrap_material_cost
        # )
        self.base_total_cost = (
                self.base_operating_cost + self.base_raw_material_cost
        )

        self.scrap_material_cost = 0
        self.base_scrap_material_cost = 0

        if self.total_cost != old_cost:
            self.flags.cost_updated = True





    # # ============= ** { Change Raw Material Cost } ** ===============

    def get_rm_rate(self, args):
        """Get raw material rate as per valuation rate, last purchase rate, or price list rate"""

        rate = 0
        item_code = args.get("item_code")


        if args.get("bom_no"):
            # rate = frappe.db.get_value("BOM", args.get("bom_no"), "total_cost") / args.get("qty")
            rate = frappe.db.get_value("BOM", args.get("bom_no"), "total_cost")

        else:
            """Get Purchase rate as per valuation rate, last purchase rate, or price list rate"""
            rate = self.get_average_purchase_rate(item_code)


        return rate

    # # -------------------------

    def get_average_purchase_rate(self, item_code):
        """Fetch the average purchase rate for the given item code."""
        purchase_invoices = frappe.get_all(
            "Purchase Invoice Item",
            filters={"item_code": item_code},
            fields=["rate"]
        )

        if not purchase_invoices:
            purchase_invoices = frappe.get_all(
                "Purchase Receipt Item",
                filters={"item_code": item_code},
                fields=["rate"]
            )

        if purchase_invoices:
            total_rate = sum(flt(purchase['rate']) for purchase in purchase_invoices)
            average_rate = total_rate / len(purchase_invoices)
            return average_rate

        return 0

    # # -------------------------



    # def get_rm_rate(self, args):
    #     """Get raw material rate as per valuation rate, last purchase rate, or price list rate"""
    #
    #     rate = 0
    #     if args.get("bom_no"):
    #         # rate = frappe.db.get_value("BOM", args.get("bom_no"), "total_cost") / args.get("qty")
    #         rate = frappe.db.get_value("BOM", args.get("bom_no"), "total_cost")
    #     else:
    #         pass
    #
    #     return rate



    # #  -----------------------------------

    # #  -----------------------------------


    # def get_rm_rate(self, args):
    #     rate = 0
    #     stock_qty_scrap = 0
    #
    #     bom_no = args.get("bom_no")
    #     item_code = args.get("item_code")
    #     selected_item_code = item_code
    #
    #     # if bom_no:
    #     if bom_no and item_code:
    #         bom_items = frappe.get_all(
    #             "BOM Item",
    #             filters={"parent": bom_no},
    #             fields=["item_code" , "qty"]
    #         )
    #         bom_item_codes = [item.get('item_code') for item in bom_items]
    #
    #
    #         """Fetch the finished item and quantity from the BOM document."""
    #
    #         bom_doc = frappe.get_doc("BOM", bom_no)
    #
    #         finished_item_code = bom_doc.item
    #         finished_item_qty = bom_doc.quantity
    #
    #         frappe.msgprint(str("============"))
    #         frappe.msgprint(f"Finished Item Code: {finished_item_code}")
    #         frappe.msgprint(f"Finished Item Quantity: {finished_item_qty}")
    #         frappe.msgprint(str("============"))
    #
    #         # Check if the finished item code matches the selected item code
    #         if finished_item_code == selected_item_code:
    #             frappe.msgprint(f"Selected Item Code matches with BOM item code: {finished_item_code}")
    #             frappe.msgprint(f"Finished Item Quantity: {finished_item_qty}")
    #
    #             scrap_items_all = frappe.get_all(
    #                 "BOM Scrap Item",
    #                 filters={"parent": args.get("bom_no"), "item_code": item_code},
    #                 fields=["stock_qty"]
    #             )
    #
    #             stock_qty_scrap = sum([flt(scrap.get('stock_qty', 0)) for scrap in scrap_items_all])
    #
    #             # total_qty_bom =  finished_item_qty + stock_qty_scrap
    #
    #             frappe.msgprint(f"Scrap items fetched: {scrap_items_all}")
    #             frappe.msgprint(str(bom_items))
    #             frappe.msgprint(str("-------------"))
    #             # frappe.msgprint(str(finish_item))
    #             frappe.msgprint(str("-------------"))
    #             frappe.msgprint(str(bom_item_codes))
    #             frappe.msgprint(str("-------------"))
    #
    #
    #             total_cost = frappe.db.get_value("BOM", bom_no, "total_cost")
    #             # qty = args.get("qty", 1)
    #             total_qty = finished_item_qty + stock_qty_scrap
    #
    #             if total_qty > 0:
    #                 # rate = total_cost / total_qty
    #                 rate = total_cost * total_qty
    #
    #             frappe.msgprint(str("-------------"))
    #             frappe.msgprint(str(total_cost))
    #             frappe.msgprint(str(stock_qty_scrap))
    #             frappe.msgprint(str(finished_item_qty))
    #             frappe.msgprint(str(total_qty))
    #             frappe.msgprint(str("-------------"))
    #             frappe.msgprint(str(rate))
    #
    #
    #         else:
    #             """Get Purchase rate as per valuation rate, last purchase rate, or price list rate"""
    #
    #             rate = self.get_average_purchase_rate(item_code)
    #
    #     return rate
    #
    # def get_average_purchase_rate(self, item_code):
    #     """Fetch the last purchase rate for the given item code."""
    #     last_purchase = frappe.get_all(
    #         "Purchase Invoice Item",
    #         filters={"item_code": item_code},
    #         fields=["rate"],
    #         order_by="creation desc",
    #         limit=1
    #     )
    #
    #     if not last_purchase:
    #         last_purchase = frappe.get_all(
    #             "Purchase Receipt Item",
    #             filters={"item_code": item_code},
    #             fields=["rate"],
    #             order_by="creation desc",
    #             limit=1
    #         )
    #
    #     if last_purchase:
    #         return flt(last_purchase[0].rate)
    #
    #     return 0




    # #  -----------------------------------
    # #  -----------------------------------
    # #  -----------------------------------

    # # ============= ** { Change Raw Material Cost } ** ===============
    #
    # def get_rm_rate(self, args):
    #     """Get raw material rate as per valuation rate, last purchase rate, or price list rate"""
    #
    #     rate = 0
    #     bom_no = args.get("bom_no")
    #     item_code = args.get("item_code")
    #
    #     if bom_no and item_code:
    #         bom_items = frappe.get_all(
    #             "BOM Item",
    #             filters={"parent": bom_no},
    #             fields=["item_code", "qty"]
    #         )
    #         bom_item_codes = [item.get('item_code') for item in bom_items]
    #
    #         bom_doc = frappe.get_doc("BOM", bom_no)
    #         finished_item_code = bom_doc.item
    #         finished_item_qty = bom_doc.quantity
    #
    #         # frappe.msgprint("============")
    #         # frappe.msgprint(f"Finished Item Code: {finished_item_code}")
    #         # frappe.msgprint(f"Finished Item Quantity: {finished_item_qty}")
    #         # frappe.msgprint("============")
    #
    #         if finished_item_code == item_code:
    #             # frappe.msgprint(f"Selected Item Code matches with BOM item code: {finished_item_code}")
    #             # frappe.msgprint(f"Finished Item Quantity: {finished_item_qty}")
    #
    #             scrap_items_all = frappe.get_all(
    #                 "BOM Scrap Item",
    #                 filters={"parent": bom_no, "item_code": item_code},
    #                 fields=["stock_qty"]
    #             )
    #
    #             stock_qty_scrap = sum([flt(scrap.get('stock_qty', 0)) for scrap in scrap_items_all])
    #
    #             total_cost = frappe.db.get_value("BOM", bom_no, "total_cost")
    #             total_qty = finished_item_qty + stock_qty_scrap
    #
    #             if total_qty > 0:
    #                 # rate = total_cost / total_qty
    #                 rate = total_cost * total_qty
    #             else:
    #                 rate = 0
    #
    #             # frappe.msgprint("-------------")
    #             # frappe.msgprint(str(total_cost))
    #             # frappe.msgprint(str(stock_qty_scrap))
    #             # frappe.msgprint(str(finished_item_qty))
    #             # frappe.msgprint(str(total_qty))
    #             # frappe.msgprint("-------------")
    #             # frappe.msgprint(str(rate))
    #         else:
    #             rate = self.get_average_purchase_rate(item_code)
    #     else:
    #         """Get Purchase rate as per valuation rate, last purchase rate, or price list rate"""
    #         rate = self.get_average_purchase_rate(item_code)
    #
    #     return rate
    #
    # # -------------------------
    #
    # def get_average_purchase_rate(self, item_code):
    #     """Fetch the average purchase rate for the given item code."""
    #     purchase_invoices = frappe.get_all(
    #         "Purchase Invoice Item",
    #         filters={"item_code": item_code},
    #         fields=["rate"]
    #     )
    #
    #     if not purchase_invoices:
    #         purchase_invoices = frappe.get_all(
    #             "Purchase Receipt Item",
    #             filters={"item_code": item_code},
    #             fields=["rate"]
    #         )
    #
    #     if purchase_invoices:
    #         total_rate = sum(flt(purchase['rate']) for purchase in purchase_invoices)
    #         average_rate = total_rate / len(purchase_invoices)
    #         return average_rate
    #
    #     return 0
    #
    # # -------------------------






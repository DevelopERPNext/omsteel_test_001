import frappe
from erpnext.manufacturing.doctype.production_plan.production_plan import ProductionPlan as BaseProductionPlan

from frappe import _
import json






class CustomProductionPlan(BaseProductionPlan):

    pass

    # @frappe.whitelist()
    # def get_items_for_material_requests_a(self, doc, warehouses=None, get_parent_warehouse_data=None):
    #     if isinstance(doc, str):
    #         doc = frappe._dict(json.loads(doc))
    #
    #     if warehouses:
    #         warehouses = list(set(self.get_warehouse_list(warehouses)))
    #         if doc.get("for_warehouse") and not get_parent_warehouse_data:
    #             if doc.get("for_warehouse") in warehouses:
    #                 warehouses.remove(doc.get("for_warehouse"))
    #
    #     frappe.msgprint("Custom override triggered")
    #     return "Success"
    #
    # def get_warehouse_list(self, warehouses):
    #     """Method to get a list of warehouses"""
    #     warehouse_list = []
    #
    #     if isinstance(warehouses, str):
    #         warehouses = json.loads(warehouses)
    #
    #     for row in warehouses:
    #         child_warehouses = frappe.db.get_descendants("Warehouse", row.get("warehouse"))
    #         if child_warehouses:
    #             warehouse_list.extend(child_warehouses)
    #         else:
    #             warehouse_list.append(row.get("warehouse"))
    #
    #     return warehouse_list
    #
    #
    #
    # def get_raw_materials_of_sub_assembly_items(
    #     self, item_details, company, bom_no, include_non_stock_items, sub_assembly_items, planned_qty=1
    # ):
    #     """Custom override for get_raw_materials_of_sub_assembly_items"""
    #     frappe.msgprint("Test -------------------")
    #
    #     # return super().get_raw_materials_of_sub_assembly_items(
    #     #     item_details, company, bom_no, include_non_stock_items, sub_assembly_items, planned_qty
    #     # )


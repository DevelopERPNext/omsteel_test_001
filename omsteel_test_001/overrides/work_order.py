import frappe
from erpnext.manufacturing.doctype.work_order.work_order import WorkOrder as BaseWorkOrder
from erpnext.manufacturing.doctype.work_order_item.work_order_item import WorkOrderItem

from frappe import _



# class CustomWorkOrder(BaseWorkOrder):
#     def set_required_items(self, reset_only_qty=False):
#         bom_required_items = self.get_bom_items()
#         bom_items_dict = {item['item_code']: item['qty'] for item in bom_required_items}
#
#
#         # # Clear existing required_items and add new ones from BOM
#         # self.required_items = []
#         #
#         # for bom_item in bom_required_items:
#         #     item_code = bom_item['item_code']
#         #     required_qty = bom_item['qty']
#         #
#         #     # Create a new WorkOrderItem instance
#         #     work_order_item = WorkOrderItem(
#         #         item_code=item_code,
#         #         qty=required_qty,
#         #         parent=self.name,
#         #         parenttype='Work Order',
#         #         parentfield='required_items'
#         #     )
#         #
#         #     # Append the WorkOrderItem instance to required_items
#         #     self.required_items.append(work_order_item)
#         #
#         # frappe.msgprint("BOM items added to Work Order items successfully.", alert=True)
#
#
#         # =====================================================
#
#         # # # Add or Update items based on BOM
#         try:
#             for bom_item in bom_required_items:
#                 item_code = bom_item["item_code"]
#                 item_qty_bom = bom_item["qty"]
#                 # new_required_qty = item_qty_bom * self.required_items.qty
#                 new_required_qty = item_qty_bom * self.required_items.qty
#
#                 # Check if the item already exists in required_items
#                 existing_item = self.get_existing_work_order_item(item_code)
#                 if existing_item:
#                     existing_item.required_qty = new_required_qty
#                     existing_item.save(ignore_permissions=True)
#                 else:
#                     # Create a new WorkOrderItem instance
#                     new_item = frappe.get_doc({
#                         "doctype": "Work Order Item",
#                         "parent": self.name,
#                         "parentfield": "required_items",
#                         "parenttype": "Work Order",
#                         "item_code": item_code,
#                         "required_qty": new_required_qty
#                     })
#                     new_item.insert(ignore_permissions=True)
#
#                 # Print item code and updated required quantity
#                 frappe.msgprint(f"Item Code: {item_code}, New Required Quantity: {new_required_qty}", alert=True)
#
#                 # Commit the changes
#                 frappe.db.commit()
#         except Exception as e:
#             frappe.throw(_("Failed to add or update items for Work Order: {0}. Error: {1}").format(self.name, str(e)))
#
#
#         # =====================================================
#
#
#         for work_order_item in self.required_items:
#             item_code = work_order_item.item_code
#
#             if item_code in bom_items_dict:
#                 item_qty_bom = bom_items_dict[item_code]
#                 new_required_qty = item_qty_bom * self.qty
#
#                 work_order_item.required_qty = new_required_qty
#
#         frappe.msgprint("Updated Successfully.", alert=True)
#
#     def get_bom_items(self):
#         bom_no = self.bom_no
#         bom_doc = frappe.get_doc("BOM", bom_no)
#         bom_items = bom_doc.items
#
#         bom_required_items = []
#         for item in bom_items:
#             bom_required_items.append({
#                 "item_code": item.item_code,
#                 "qty": item.qty
#             })
#
#         return bom_required_items
#
#
# # ===================================================================











# ============ Start  Working ==================
# class CustomWorkOrder(BaseWorkOrder):
#     def set_required_items(self, reset_only_qty=False):
#         """set required_items for production to keep track of reserved qty"""
#         # if not reset_only_qty:
#         #     self.required_items = []
#
#         # # Delete existing required_items
#         # frappe.db.delete("Work Order Item", {"parent": self.name})
#
#         bom_required_items = self.get_bom_items()
#         # bom_items_dict = {item['item_code']: item['qty'] for item in bom_required_items}
#
#         # if reset_only_qty:
#         #     self.required_items = []
#         #     # reset_only_qty = False
#
#         try:
#             for bom_item in bom_required_items:
#                 item_code = bom_item["item_code"]
#                 item_qty_bom = bom_item["qty"]
#                 item_name = bom_item["item_name"]
#                 rate = bom_item["rate"]
#                 include_item_in_manufacturing = bom_item["include_item_in_manufacturing"]
#
#                 # # Retrieve source warehouse from item master
#                 # item_doc = frappe.get_doc("Item", item_code)
#                 # source_warehouse = item_doc.item_defaults.default_warehouse
#
#                 # Retrieve source warehouse from item master
#                 source_warehouse = self.get_item_default_warehouse(item_code)
#
#                 # Calculate new required quantity based on BOM quantity and Work Order quantity
#                 new_required_qty = item_qty_bom * self.qty
#
#                 frappe.db.set_value("Work Order Item", self.name, "required_qty", new_required_qty)
#                 frappe.db.commit()
#
#                 # frappe.msgprint(str(new_required_qty))
#
#                 # # # Check if the item already exists in required_items
#                 # existing_item = self.get_existing_work_order_item(item_code)
#                 # if existing_item:
#                 #     # Update required_qty using frappe.db.set_value
#                 #     frappe.db.set_value("Work Order Item", existing_item.name, "required_qty", new_required_qty)
#                 #     frappe.db.commit()
#                 #
#                 #     frappe.msgprint(f"Item Code: {item_code}, New Required Quantity: {new_required_qty}", alert=True)
#                 #     # existing_item.required_qty = new_required_qty
#                 #     # existing_item.save(ignore_permissions=True)
#                 # else:
#
#                 # if not reset_only_qty:
#                 # Create a new WorkOrderItem instance
#                 new_item = frappe.get_doc({
#                     "doctype": "Work Order Item",
#                     "parent": self.name,
#                     "parentfield": "required_items",
#                     "parenttype": "Work Order",
#                     "item_code": item_code,
#                     "required_qty": new_required_qty,
#                     "item_name": item_name,
#                     "rate": rate,
#                     "source_warehouse": source_warehouse,
#                     "include_item_in_manufacturing": include_item_in_manufacturing,
#                 })
#                 new_item.insert(ignore_permissions=True)
#                 frappe.db.commit()
#
#                 # Print item code and updated required quantity
#                 frappe.msgprint(f"Item Code: {item_code}, New Required Quantity: {new_required_qty}", alert=True)
#
#                 # reset_only_qty = True
#                 # else:
#                 #
#                 #     pass
#                 #     # self.required_items = []
#                 #
#                 #     # # # Using frappe.db.sql
#                 #     # query = f"""
#                 #     #             UPDATE `tabWork Order Item`
#                 #     #             SET required_qty = '{new_required_qty}'
#                 #     #             WHERE parent = '{self.name}' AND item_code = '{item_code}';
#                 #     #         """
#                 #     #
#                 #     # frappe.db.sql(query)
#                 #     #
#                 #     # frappe.db.set_value("Work Order Item", self.name, "required_qty", new_required_qty)
#                 #     # frappe.db.commit()
#
#             # Commit the changes
#             frappe.db.commit()
#         except Exception as e:
#             frappe.throw(_("Failed to add or update items for Work Order: {0}. Error: {1}").format(self.name, str(e)))
#
#     def get_existing_work_order_item(self, item_code):
#         """Retrieve existing Work Order Item by item_code."""
#         for work_order_item in self.required_items:
#             if work_order_item.item_code == item_code:
#                 return work_order_item
#         return None
#
#     def get_bom_items(self):
#         bom_no = self.bom_no
#         bom_doc = frappe.get_doc("BOM", bom_no)
#         bom_items = bom_doc.items
#
#         bom_required_items = []
#         for item in bom_items:
#             bom_required_items.append({
#                 "item_code": item.item_code,
#                 "qty": item.qty,
#                 "item_name": item.item_name,
#                 "rate": item.rate,
#                 "include_item_in_manufacturing": item.include_item_in_manufacturing
#             })
#
#         return bom_required_items
#
#     def get_item_default_warehouse(self, item_code):
#         """Retrieve default warehouse for an item."""
#         item_defaults = frappe.get_all("Item Default", filters={"parent": item_code}, fields=["default_warehouse"])
#         if item_defaults:
#             return item_defaults[0].default_warehouse
#         return None
# ============ End  Working ==================
# ==============================================================





#  ============================================================





class CustomWorkOrder(BaseWorkOrder):
    def set_required_items(self, reset_only_qty=False):
        """Set required_items for production to keep track of reserved qty"""

        if not self.name:
            self.save()
            frappe.msgprint(_("Work Order saved with name: {0}").format(self.name), alert=True)

        bom_required_items = self.get_bom_items()

        try:
            for bom_item in bom_required_items:
                item_code = bom_item["item_code"]
                if not item_code:
                    continue

                item_qty_bom = bom_item["qty"]
                item_name = bom_item["item_name"]
                rate = bom_item["rate"]
                include_item_in_manufacturing = bom_item["include_item_in_manufacturing"]

                source_warehouse = self.get_item_default_warehouse(item_code)
                new_required_qty = item_qty_bom * self.qty

                existing_item = self.get_existing_work_order_item(item_code)
                if existing_item:
                    # Update existing item
                    frappe.db.set_value("Work Order Item", existing_item.name, "required_qty", new_required_qty)
                    frappe.msgprint(f"Item Code: {item_code}, Updated Required Quantity: {new_required_qty}", alert=True)
                else:
                    # Add new item
                    new_item = frappe.get_doc({
                        "doctype": "Work Order Item",
                        "parent": self.name,
                        "parentfield": "required_items",
                        "parenttype": "Work Order",
                        "item_code": item_code,
                        "required_qty": new_required_qty,
                        "item_name": item_name,
                        "rate": rate,
                        "source_warehouse": source_warehouse,
                        "include_item_in_manufacturing": include_item_in_manufacturing,
                    })
                    new_item.insert(ignore_permissions=True)
                    frappe.msgprint(f"Item Code: {item_code}, New Required Quantity: {new_required_qty}", alert=True)

            frappe.db.commit()

        except Exception as e:
            frappe.throw(_("Failed to add or update items for Work Order: {0}. Error: {1}").format(self.name, str(e)))

    def get_existing_work_order_item(self, item_code):
        """Retrieve existing Work Order Item by item_code."""
        return frappe.db.get_value("Work Order Item", {"parent": self.name, "item_code": item_code}, "*")

    def get_bom_items(self):
        """Retrieve BOM items."""
        bom_doc = frappe.get_doc("BOM", self.bom_no)
        return [
            {
                "item_code": item.item_code,
                "qty": item.qty,
                "item_name": item.item_name,
                "rate": item.rate,
                "include_item_in_manufacturing": item.include_item_in_manufacturing
            }
            for item in bom_doc.items
        ]

    def get_item_default_warehouse(self, item_code):
        """Retrieve default warehouse for an item."""
        return frappe.db.get_value("Item Default", {"parent": item_code}, "default_warehouse")


















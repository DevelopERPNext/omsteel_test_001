import frappe
from erpnext.stock.doctype.stock_entry.stock_entry import StockEntry as BaseStockEntry

from frappe import _
from frappe.utils import flt



# from erpnext.stock.stock_ledger import NegativeStockError, get_previous_sle, get_valuation_rate
import erpnext



class CustomStockEntry(BaseStockEntry):
    # pass
    def validate_finished_goods(self):
        pass

    def update_transferred_qty(self):
        pass

    # def calculate_rate_and_amount(self, reset_outgoing_rate=True, raise_error_if_no_rate=True):
    #     pass
    #     # self.set_basic_rate(reset_outgoing_rate, raise_error_if_no_rate)
    #     # self.distribute_additional_costs()
    #     # self.update_valuation_rate()
    #     # self.set_total_incoming_outgoing_value()
    #     # self.set_total_amount()




    # def update_work_order(self):
    #     pass


    # def set_basic_rate(self, reset_outgoing_rate=True, raise_error_if_no_rate=True):
    #     """
    #     Set rate for outgoing, scrapped, and finished items based on BOM rates.
    #     """
    #     outgoing_items_cost = self.set_rate_for_outgoing_items(reset_outgoing_rate, raise_error_if_no_rate)
    #     finished_item_qty = sum(d.transfer_qty for d in self.items if d.is_finished_item)
    #
    #     items = []
    #     bom_no = self.bom_no
    #
    #     bom_item_detail = frappe.get_all(
    #         "BOM Item",
    #         filters={"parent": bom_no},
    #         fields=["item_code", "rate"],
    #     )
    #
    #     bom_rates = {item['item_code']: item['rate'] for item in bom_item_detail}
    #
    #     for d in self.get("items"):
    #         if d.s_warehouse or d.set_basic_rate_manually:
    #             continue
    #
    #         if d.allow_zero_valuation_rate:
    #             d.basic_rate = 0.0
    #             items.append(d.item_code)
    #
    #         elif d.is_finished_item:
    #             if self.purpose == "Manufacture":
    #                 d.basic_rate = self.get_basic_rate_for_manufactured_item(
    #                     finished_item_qty, outgoing_items_cost
    #                 )
    #             elif self.purpose == "Repack":
    #                 d.basic_rate = self.get_basic_rate_for_repacked_items(d.transfer_qty, outgoing_items_cost)
    #
    #         if d.item_code in bom_rates:
    #             d.basic_rate = bom_rates[d.item_code]
    #
    #         if not d.basic_rate and not d.allow_zero_valuation_rate:
    #             if self.is_new():
    #                 raise_error_if_no_rate = False
    #
    #             d.basic_rate = get_valuation_rate(
    #                 d.item_code,
    #                 d.t_warehouse,
    #                 self.doctype,
    #                 self.name,
    #                 d.allow_zero_valuation_rate,
    #                 currency=erpnext.get_company_currency(self.company),
    #                 company=self.company,
    #                 raise_error_if_no_rate=raise_error_if_no_rate,
    #                 batch_no=d.batch_no,
    #                 serial_and_batch_bundle=d.serial_and_batch_bundle,
    #             )
    #
    #         d.basic_rate = flt(d.basic_rate)
    #         d.basic_amount = flt(flt(d.transfer_qty) * flt(d.basic_rate), d.precision("basic_amount"))
    #
    #     if items:
    #         message = ""
    #
    #         if len(items) > 1:
    #             message = _(
    #                 "Items rate has been updated to zero as Allow Zero Valuation Rate is checked for the following items: {0}"
    #             ).format(", ".join(frappe.bold(item) for item in items))
    #         else:
    #             message = _(
    #                 "Item rate has been updated to zero as Allow Zero Valuation Rate is checked for item {0}"
    #             ).format(frappe.bold(items[0]))
    #
    #         frappe.msgprint(message, alert=True)


    #  ==============================================================
    #  ==============================================================

    def update_valuation_rate(self):
        pass
    #     # for d in self.get("items"):
    #     #     if d.transfer_qty:
    #     #         d.amount = flt(flt(d.basic_amount) + flt(d.additional_cost), d.precision("amount"))
    #     #         # Do not round off valuation rate to avoid precision loss
    #     #         d.valuation_rate = flt(d.basic_rate) + (flt(d.additional_cost) / flt(d.transfer_qty))


    # def set_basic_rate(self, reset_outgoing_rate=True, raise_error_if_no_rate=True):
    #     """
    #     Set rate for outgoing, scrapped and finished items
    #     """
    #     pass
    #     # # Set rate for outgoing items
    #     # outgoing_items_cost = self.set_rate_for_outgoing_items(reset_outgoing_rate, raise_error_if_no_rate)
    #     # finished_item_qty = sum(d.transfer_qty for d in self.items if d.is_finished_item)
    #     #
    #     # items = []
    #     # # Set basic rate for incoming items
    #     # for d in self.get("items"):
    #     #     if d.s_warehouse or d.set_basic_rate_manually:
    #     #         continue
    #     #
    #     #     if d.allow_zero_valuation_rate:
    #     #         d.basic_rate = 0.0
    #     #         items.append(d.item_code)
    #     #
    #     #     elif d.is_finished_item:
    #     #         if self.purpose == "Manufacture":
    #     #             d.basic_rate = self.get_basic_rate_for_manufactured_item(
    #     #                 finished_item_qty, outgoing_items_cost
    #     #             )
    #     #         elif self.purpose == "Repack":
    #     #             d.basic_rate = self.get_basic_rate_for_repacked_items(d.transfer_qty, outgoing_items_cost)
    #     #
    #     #     if not d.basic_rate and not d.allow_zero_valuation_rate:
    #     #         if self.is_new():
    #     #             raise_error_if_no_rate = False
    #     #
    #     #         d.basic_rate = get_valuation_rate(
    #     #             d.item_code,
    #     #             d.t_warehouse,
    #     #             self.doctype,
    #     #             self.name,
    #     #             d.allow_zero_valuation_rate,
    #     #             currency=erpnext.get_company_currency(self.company),
    #     #             company=self.company,
    #     #             raise_error_if_no_rate=raise_error_if_no_rate,
    #     #             batch_no=d.batch_no,
    #     #             serial_and_batch_bundle=d.serial_and_batch_bundle,
    #     #         )
    #     #
    #     #     # do not round off basic rate to avoid precision loss
    #     #     d.basic_rate = flt(d.basic_rate)
    #     #     d.basic_amount = flt(flt(d.transfer_qty) * flt(d.basic_rate), d.precision("basic_amount"))
    #     #
    #     # if items:
    #     #     message = ""
    #     #
    #     #     if len(items) > 1:
    #     #         message = _(
    #     #             "Items rate has been updated to zero as Allow Zero Valuation Rate is checked for the following items: {0}"
    #     #         ).format(", ".join(frappe.bold(item) for item in items))
    #     #     else:
    #     #         message = _(
    #     #             "Item rate has been updated to zero as Allow Zero Valuation Rate is checked for item {0}"
    #     #         ).format(frappe.bold(items[0]))
    #     #
    #     #     frappe.msgprint(message, alert=True)



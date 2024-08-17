import frappe
from erpnext.stock.doctype.stock_entry.stock_entry import StockEntry as BaseStockEntry

from frappe import _




class CustomStockEntry(BaseStockEntry):
    # pass
    def validate_finished_goods(self):
        pass

    def update_transferred_qty(self):
        pass

    # def update_work_order(self):
    #     pass







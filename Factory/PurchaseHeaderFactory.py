import Model.PurchaseHeaderModel as PurchaseHeaderModel
from uuid import uuid1


class PurchaseHeaderFactory:
    def CreatePurchaseHeader(supplier_id, shop_id, transaction_date_time, transaction_price_change, payment_status):
        purchase_id = uuid1()
        purchase_header = PurchaseHeaderModel.PurchaseHeader(
            purchase_id, supplier_id, shop_id, transaction_date_time, transaction_price_change, payment_status, "A")
        return purchase_header

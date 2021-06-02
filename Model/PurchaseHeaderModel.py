class PurchaseHeader:
    def __init__(self, purchase_id, supplier_id, shop_id, transaction_date_time, transaction_price_change, payment_status, purchase_status):
        self.purchase_id = purchase_id
        self.supplier_id = supplier_id
        self.shop_id = shop_id
        self.transaction_date_time = transaction_date_time
        self.transaction_price_change = transaction_price_change
        self.payment_status = payment_status
        self.purchase_status = purchase_status

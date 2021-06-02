class SalesHeader:
    def __init__(self, sales_id, account_id, shop_id, transaction_date_time, transaction_price_change, payment_status, sales_status):
        self.sales_id = sales_id
        self.account_id = account_id
        self.shop_id = shop_id
        self.transaction_date_time = transaction_date_time
        self.transaction_price_change = transaction_price_change
        self.payment_status = payment_status
        self.sales_status = sales_status

import Model.SalesHeaderModel as SalesHeaderModel
from uuid import uuid1


class SalesHeaderFactory:
    def CreateSalesHeader(account_id, shop_id, transaction_date_time, transaction_price_change, payment_status):
        sales_id = uuid1()
        sales_header = SalesHeaderModel.SalesHeader(sales_id, account_id, shop_id,
                                                    transaction_date_time, transaction_price_change, payment_status, "A")
        return sales_header

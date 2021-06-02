import Model.SalesDetailModel as SalesDetailModel


class SalesDetailFactory:
    def CreateSalesDetail(sales_id, product_detail_id, product_sale_price, amount):
        sales_detail = SalesDetailModel.SalesDetail(
            sales_id, product_detail_id, product_sale_price, amount, "A")
        return sales_detail

import Repository.ProductDetailRepository as ProductDetailRepository
import Repository.SalesDetailRepository as SalesDetailRepository

import Factory.SalesDetailFactory as SalesDetailFactory


class SalesDetailHandler:
    def RegisterSalesDetail(json_data):
        sales_id = json_data['sales_id']
        product_id = json_data['product_id']
        product_sale_price = json_data['product_sale_price']
        amount = json_data['amount']

        product_detail_list = ProductDetailRepository.ProductDetailRepository.GetProductDetailWithStockByProduct(
            product_id)

        i = 0

        reponse = []

        while amount > 0:
            current_detail_id = product_detail_list[i]['product_detail_id']
            current_stock = product_detail_list[i]['stock']

            if current_stock >= amount:
                current_stock = current_stock - amount
                current_amount = amount
                amount = 0

            else:
                amount = amount - current_stock
                current_amount = current_stock
                current_stock = 0

            ProductDetailRepository.ProductDetailRepository.UpdateProductDetailStock(
                current_detail_id, current_stock)

            sales_detail = SalesDetailFactory.SalesDetailFactory.CreateSalesDetail(
                sales_id, current_detail_id, product_sale_price, current_amount)

            SalesDetailRepository.SalesDetailRepository.AddSalesDetail(
                sales_detail)

            sales_detail = {"sales_id": str(sales_detail.sales_id),  "product_detail_id": str(sales_detail.product_detail_id),
                            "product_sale_price": str(sales_detail.product_sale_price), "amount": str(sales_detail.amount),
                            "sales_detail_status": str(sales_detail.sales_detail_status)}

            reponse.append(sales_detail)

            i = i + 1

        return reponse

    def GetSalesDetailBySales(json_data):
        sales_id = json_data['sales_id']

        sales_detail_list = SalesDetailRepository.SalesDetailRepository.GetSalesDetailBySales(
            sales_id)

        if sales_detail_list:
            Data = {}
            Data["Data"] = sales_detail_list

            return Data

        else:
            return {"status": "Error No Such Sales's Detail"}

    def GetUniqueSalesDetail(json_data):
        sales_id = json_data['sales_id']
        product_detail_id = json_data['product_detail_id']

        sales_detail_list = SalesDetailRepository.SalesDetailRepository.GetUniqueSalesDetail(
            sales_id, product_detail_id)

        if sales_detail_list:
            Data = {}
            Data["Data"] = sales_detail_list

            return Data

        else:
            return {"status": "Error No Such Sales's Detail"}

    def DeleteUniqueSalesDetail(json_data):
        sales_id = json_data['sales_id']
        product_detail_id = json_data['product_detail_id']

        sales_detail_list = SalesDetailRepository.SalesDetailRepository.GetUniqueSalesDetail(
            sales_id, product_detail_id)

        if sales_detail_list:
            result = SalesDetailRepository.SalesDetailRepository.DeleteSalesDetail(
                sales_id, product_detail_id)

            if result == "success":
                return {"status": "Success"}

        else:
            return {"status": "Error Sales's Detail Not Found"}

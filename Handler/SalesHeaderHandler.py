from datetime import datetime

import Repository.SalesHeaderRepository as SalesHeaderRepository
import Repository.SalesDetailRepository as SalesDetailRepository
import Repository.ProductDetailRepository as ProductDetailRepository
import Repository.AccountRepository as AccountRepository

import Factory.SalesHeaderFactory as SalesHeaderFactory


class SalesHeaderHandler:
    def RegisterSalesHeader(json_data):
        account_id = json_data['account_id']
        shop_id = json_data['shop_id']
        transaction_date_time = datetime.now().strftime("%Y-%m-%d")
        transaction_price_change = json_data['transaction_price_change']
        payment_status = json_data['payment_status']

        sales_header = SalesHeaderFactory.SalesHeaderFactory.CreateSalesHeader(
            account_id, shop_id, transaction_date_time, transaction_price_change, payment_status)

        result = SalesHeaderRepository.SalesHeaderRepository.AddSalesHeader(
            sales_header)

        if result == "success":

            sales_header = {"sales_id": str(sales_header.sales_id), "account_id": str(sales_header.account_id),
                            "shop_id": str(sales_header.shop_id), "transaction_date_time": str(sales_header.transaction_date_time),
                            "transaction_price_change": sales_header.transaction_price_change,
                            "payment_status": str(sales_header.payment_status),
                            "sales_status": str(sales_header.sales_status)}

            return sales_header
        else:
            return {"status": "Error Registering Sales's Header"}

    def GetSalesHeaderByShop(json_data):
        shop_id = json_data['shop_id']

        sales_header_list = SalesHeaderRepository.SalesHeaderRepository.GetSalesHeaderByShop(
            shop_id)

        if sales_header_list:
            Data = {}
            result = []

            for sales_header in sales_header_list:
                account_id = sales_header['account_id']
                account = AccountRepository.AccountRepository.GetAccountById(
                    account_id)

                if account:
                    tempResult = {"Sales Header": sales_header,
                                  "Account": account[0]}
                else:
                    tempResult = {"Sales Header": sales_header}
                result.append(tempResult)

            Data["Data"] = result

            return Data

        else:
            return {"status": "Error No Such Sales's Header"}

    def SetPaymentToPaid(json_data):
        sales_id = json_data['sales_id']

        sales_header_list = SalesHeaderRepository.SalesHeaderRepository.GetSalesHeaderById(
            sales_id)

        if sales_header_list:
            result = SalesHeaderRepository.SalesHeaderRepository.SetPaymentToPaid(
                sales_id)

            if result == "success":
                return {"status": "Success"}

            else:
                return {"status": "Error Updating Sales's Header"}
        else:
            return {"status": "Error Sales's Header Not Found"}

    def DeleteSalesHeader(json_data):
        sales_id = json_data['sales_id']

        sales_header_list = SalesHeaderRepository.SalesHeaderRepository.GetSalesHeaderById(
            sales_id)

        if sales_header_list:
            sales_detail_list = SalesDetailRepository.SalesDetailRepository.GetSalesDetailBySales(
                sales_id)

            if sales_detail_list:
                for sales_detail in sales_detail_list:
                    amount = sales_detail[0]['amount']
                    product_detail_id = sales_detail[0]['product_detail_id']

                    product_detail = ProductDetailRepository.ProductDetailRepository.GetProductDetailById(
                        product_detail_id)[0]

                    newStock = product_detail['stock'] + amount

                    result = ProductDetailRepository.ProductDetailRepository.UpdateProductDetailStock(
                        product_detail_id, newStock)

            result = SalesHeaderRepository.SalesHeaderRepository.DeleteSalesHeader(
                sales_id)

            if result == "success":
                return {"status": "Success"}

            else:
                return {"status": "Error Deleting Sales's Header"}
        else:
            return {"status": "Error Sales's Header Not Found"}

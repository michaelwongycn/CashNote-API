from datetime import datetime

import Repository.PurchaseHeaderRepository as PurchaseHeaderRepository
import Repository.PurchaseDetailRepository as PurchaseDetailRepository
import Repository.SupplierRepository as SupplierRepository

import Factory.PurchaseHeaderFactory as PurchaseHeaderFactory


class PurchaseHeaderHandler:
    def RegisterPurhcaseHeader(json_data):
        supplier_id = json_data['supplier_id']
        shop_id = json_data['shop_id']
        transaction_date_time = datetime.now().strftime("%Y-%m-%d")
        transaction_price_change = json_data['transaction_price_change']
        payment_status = json_data['payment_status']

        purchase_header = PurchaseHeaderFactory.PurchaseHeaderFactory.CreatePurchaseHeader(
            supplier_id, shop_id, transaction_date_time, transaction_price_change, payment_status)

        result = PurchaseHeaderRepository.PurchaseHeaderRepository.AddPurchaseHeader(
            purchase_header)

        if result == "success":

            purchase_header = {"purchase_id": str(purchase_header.purchase_id), "supplier_id": str(purchase_header.supplier_id),
                               "shop_id": str(purchase_header.shop_id), "transaction_date_time": str(purchase_header.transaction_date_time),
                               "transaction_price_change": purchase_header.transaction_price_change,
                               "payment_status": str(purchase_header.payment_status),
                               "purchase_status": str(purchase_header.purchase_status)}

            return purchase_header
        else:
            return {"status": "Error Registering Purchase's Header"}

    def GetPurchaseHeaderByShop(json_data):
        shop_id = json_data['shop_id']

        purchase_header_list = PurchaseHeaderRepository.PurchaseHeaderRepository.GetPurchaseHeaderByShop(
            shop_id)

        if purchase_header_list:
            Data = {}
            result = []

            for purchase_header in purchase_header_list:
                supplier_id = purchase_header['supplier_id']
                supplier = SupplierRepository.SupplierRepository.GetSupplierById(
                    supplier_id)

                if supplier:
                    tempResult = {"Purchase Header": purchase_header,
                                  "Supplier": supplier[0]}
                else:
                    tempResult = {"Purchase Header": purchase_header}

                result.append(tempResult)

            Data["Data"] = result

            return Data

        else:
            return {"status": "Error No Such Purchase's Header"}

    def SetPaymentToPaid(json_data):
        purchase_id = json_data['purchase_id']

        purchase_header_list = PurchaseHeaderRepository.PurchaseHeaderRepository.GetPurchaseHeaderById(
            purchase_id)

        if purchase_header_list:
            result = PurchaseHeaderRepository.PurchaseHeaderRepository.SetPaymentToPaid(
                purchase_id)

            if result == "success":
                return {"status": "Success"}

            else:
                return {"status": "Error Updating Purchase's Header"}
        else:
            return {"status": "Error Purchase's Header Not Found"}

    def DeletePurchaseHeader(json_data):
        purchase_id = json_data['purchase_id']

        purchase_header_list = PurchaseHeaderRepository.PurchaseHeaderRepository.GetPurchaseHeaderById(
            purchase_id)

        if purchase_header_list:
            purchase_detail_list = PurchaseDetailRepository.PurchaseDetailRepository.GetPurchaseDetailByPurchase(
                purchase_id)

            if not purchase_detail_list:
                result = PurchaseHeaderRepository.PurchaseHeaderRepository.DeletePurchaseHeader(
                    purchase_id)

                if result == "success":
                    return {"status": "Success"}

                else:
                    return {"status": "Error Deleting Purchase's Header"}
            else:
                return {"status": "Please Delete Purchase's Detail First"}
        else:
            return {"status": "Error Purchase's Header Not Found"}

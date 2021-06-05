import Repository.ProductDetailRepository as ProductDetailRepository
import Repository.PurchaseDetailRepository as PurchaseDetailRepository

import Factory.ProductDetailFactory as ProductDetailFactory
import Factory.PurchaseDetailFactory as PurchaseDetailFactory


class PurchaseDetailHandler:
    def RegisterPurchaseDetail(json_data):
        purchase_id = json_data['purchase_id']
        product_id = json_data['product_id']
        product_purchase_price = json_data['product_purchase_price']
        product_expired_date = json_data['product_expired_date']
        amount = json_data['amount']

        product_detail_list = ProductDetailRepository.ProductDetailRepository.GetProductDetailWithPriceAndExpiredDateByProduct(
            product_id, product_expired_date, product_purchase_price)

        if product_detail_list:
            product_detail_id = product_detail_list[0]['product_detail_id']
            product_old_stock = product_detail_list[0]['stock']
            product_new_stock = product_old_stock + amount

            ProductDetailRepository.ProductDetailRepository.UpdateProductDetailStock(
                product_detail_id, product_new_stock)

            purchase_detail = PurchaseDetailFactory.PurchaseDetailFactory.CreatePurchaseDetail(
                purchase_id, product_detail_id, amount)

            PurchaseDetailRepository.PurchaseDetailRepository.AddPurchaseDetail(
                purchase_detail)

            return product_detail_list[0]

        else:
            product_detail = ProductDetailFactory.ProductDetailFactory.CreateProductDetail(
                product_id, product_purchase_price, amount, product_expired_date)

            ProductDetailRepository.ProductDetailRepository.AddProductDetail(
                product_detail)

            purchase_detail = PurchaseDetailFactory.PurchaseDetailFactory.CreatePurchaseDetail(
                purchase_id, product_detail.product_detail_id, amount)

            PurchaseDetailRepository.PurchaseDetailRepository.AddPurchaseDetail(
                purchase_detail)

            purchase_detail = {"purchase_id": str(purchase_detail.purchase_id),  "product_detail_id": str(purchase_detail.product_detail_id),
                               "amount": str(purchase_detail.amount), "purchase_detail_status": str(purchase_detail.purchase_detail_status)}

            return purchase_detail

    def GetPurchaseDetailByPurchase(json_data):
        purchase_id = json_data['purchase_id']

        purchase_detail_list = PurchaseDetailRepository.PurchaseDetailRepository.GetPurchaseDetailByPurchase(
            purchase_id)

        Data = {}
        Data["Data"] = purchase_detail_list

        return Data

    def GetUniquePurchaseDetail(json_data):
        purchase_id = json_data['purchase_id']
        product_detail_id = json_data['product_detail_id']

        purchase_detail_list = PurchaseDetailRepository.PurchaseDetailRepository.GetUniquePurchaseDetail(
            purchase_id, product_detail_id)

        return purchase_detail_list

    def DeleteUniquePurchaseDetail(json_data):
        purchase_id = json_data['purchase_id']
        product_detail_id = json_data['product_detail_id']

        result = PurchaseDetailRepository.PurchaseDetailRepository.DeletePurchaseDetail(
            purchase_id, product_detail_id)

        if result == "success":
            return {"status": "Success"}
        else:
            return {"status": "Error"}

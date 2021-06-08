import Repository.ProductDetailRepository as ProductDetailRepository
import Repository.ProductRepository as ProductRepository
import Repository.PurchaseDetailRepository as PurchaseDetailRepository

import Factory.ProductDetailFactory as ProductDetailFactory
import Factory.PurchaseDetailFactory as PurchaseDetailFactory


class PurchaseDetailHandler:
    def RegisterPurchaseDetail(json_data):
        purchase_id = json_data['purchase_id']
        product_id = json_data['product_id']
        supplier_id = json_data['supplier_id']
        product_purchase_price = json_data['product_purchase_price']
        product_expired_date = json_data['product_expired_date']
        amount = json_data['amount']

        product_detail_list = ProductDetailRepository.ProductDetailRepository.GetProductDetailWithSupplierPriceAndExpiredDateByProduct(
            product_id, supplier_id, product_expired_date, product_purchase_price)

        if product_detail_list:
            product_detail_id = product_detail_list[0]['product_detail_id']
            product_old_stock = product_detail_list[0]['stock']
            product_new_stock = product_old_stock + amount

            result = ProductDetailRepository.ProductDetailRepository.UpdateProductDetailStock(
                product_detail_id, product_new_stock)

            if result == "success":
                purchase_detail = PurchaseDetailFactory.PurchaseDetailFactory.CreatePurchaseDetail(
                    purchase_id, product_detail_id, amount)

                result = PurchaseDetailRepository.PurchaseDetailRepository.AddPurchaseDetail(
                    purchase_detail)

                if result == "success":
                    return product_detail_list[0]

                else:
                    result = ProductDetailRepository.ProductDetailRepository.UpdateProductDetailStock(
                        product_detail_id, product_old_stock)
                    return {"status": "Error Registering Purchase's Detail"}
            else:
                return {"status": "Error Registering Purchase's Detail"}

        else:
            product_detail = ProductDetailFactory.ProductDetailFactory.CreateProductDetail(
                product_id, supplier_id, product_purchase_price, amount, product_expired_date)

            result = ProductDetailRepository.ProductDetailRepository.AddProductDetail(
                product_detail)

            if result == "success":
                purchase_detail = PurchaseDetailFactory.PurchaseDetailFactory.CreatePurchaseDetail(
                    purchase_id, product_detail.product_detail_id, amount)

                result = PurchaseDetailRepository.PurchaseDetailRepository.AddPurchaseDetail(
                    purchase_detail)

                if result == "success":
                    purchase_detail = {"purchase_id": str(purchase_detail.purchase_id),  "product_detail_id": str(purchase_detail.product_detail_id),
                                       "amount": str(purchase_detail.amount), "purchase_detail_status": str(purchase_detail.purchase_detail_status)}

                    return purchase_detail

                else:
                    ProductDetailRepository.ProductDetailRepository.DeleteProductDetail(
                        product_detail.product_detail_id)
                    return {"status": "Error Registering Purchase's Detail"}
            else:
                return {"status": "Error Registering Purchase's Detail"}

    def GetPurchaseDetailByPurchase(json_data):
        purchase_id = json_data['purchase_id']

        purchase_detail_list = PurchaseDetailRepository.PurchaseDetailRepository.GetPurchaseDetailByPurchase(
            purchase_id)

        if purchase_detail_list:
            Data = {}
            result = []

            for purchase_detail in purchase_detail_list:
                product_detail_id = purchase_detail['product_detail_id']
                product_detail = ProductDetailRepository.ProductDetailRepository.GetProductDetailById(
                    product_detail_id)

                if product_detail:
                    product_id = product_detail[0]['product_id']
                    product = ProductRepository.ProductRepository.get(
                        product_id)

                    if product:
                        tempResult = {"Purchase Detail": purchase_detail,
                                      "Product": product[0]}
                    else:
                        tempResult = {"Purchase Detail": purchase_detail}
                else:
                    tempResult = {"Purchase Detail": purchase_detail}

                tempResult = {"Purchase Detail": purchase_detail,
                              "Product": product[0]}

                result.append(tempResult)

            Data["Data"] = result

            return Data

        else:
            return {"status": "Error No Such Purchase's Detail"}

    def GetUniquePurchaseDetail(json_data):
        purchase_id = json_data['purchase_id']
        product_detail_id = json_data['product_detail_id']

        purchase_detail_list = PurchaseDetailRepository.PurchaseDetailRepository.GetUniquePurchaseDetail(
            purchase_id, product_detail_id)

        if purchase_detail_list:
            Data = {}
            Data["Data"] = purchase_detail_list

            return Data

        else:
            return {"status": "Error No Such Purchase's Detail"}

    def DeleteUniquePurchaseDetail(json_data):
        purchase_id = json_data['purchase_id']
        product_detail_id = json_data['product_detail_id']

        purchase_detail_list = PurchaseDetailRepository.PurchaseDetailRepository.GetUniquePurchaseDetail(
            purchase_id, product_detail_id)

        if purchase_detail_list:
            result = PurchaseDetailRepository.PurchaseDetailRepository.DeletePurchaseDetail(
                purchase_id, product_detail_id)

            if result == "success":
                return {"status": "Success"}

        else:
            return {"status": "Error Purchase's Detail Not Found"}

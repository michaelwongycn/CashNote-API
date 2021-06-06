import Repository.SupplierRepository as SupplierRepository
import Repository.ProductDetailRepository as ProductDetailRepository
import Repository.PurchaseDetailRepository as PurchaseDetailRepository
import Repository.SalesDetailRepository as SalesDetailRepository

import Factory.ProductDetailFactory as ProductDetailFactory


class ProductDetailHandler:
    def AddProductDetail(json_data):
        product_id = json_data['product_id']
        supplier_id = json_data['supplier_id']
        product_purchase_price = json_data['product_purchase_price']
        stock = json_data['stock']
        product_expired_date = json_data['product_expired_date']

        product_detail = ProductDetailFactory.ProductDetailFactory.CreateProductDetail(
            product_id, supplier_id, product_purchase_price, stock, product_expired_date)

        result = ProductDetailRepository.ProductDetailRepository.AddProductDetail(
            product_detail)

        if result == "success":

            product_detail = {"product_detail_id": str(product_detail.product_detail_id),
                              "product_id": str(product_detail.product_id),
                              "supplier_id": str(product_detail.supplier_id),
                              "product_purchase_price": str(product_detail.product_purchase_price),
                              "stock": str(product_detail.stock),
                              "product_expired_date": str(product_detail.product_expired_date),
                              "product_detail_status": str(product_detail.product_detail_status)}

            return product_detail

        else:
            return {"status": "Error Registering Product's Detail"}

    def GetProductDetailByProduct(json_data):
        product_id = json_data['product_id']
        result = []

        product_detail_list = ProductDetailRepository.ProductDetailRepository.GetProductDetailByProduct(
            product_id)

        for product_detail in product_detail_list:

            supplier_id = product_detail['supplier_id']

            supplier = SupplierRepository.SupplierRepository.GetSupplierById(
                supplier_id)

            tempResult = {"Product Detail": product_detail,
                          "Supplier": supplier[0]}

            result.append(tempResult)

        if result:
            Data = {}
            Data["Data"] = result

            return Data

        else:
            return {"status": "Error No Such Product's Detail"}

    def UpdateProductDetail(json_data):
        product_detail_id = json_data['product_detail_id']
        product_expired_date = json_data['product_expired_date']
        product_purchase_price = json_data['product_purchase_price']
        stock = json_data['stock']

        product_detail_list = ProductDetailRepository.ProductDetailRepository.GetProductDetailById(
            product_detail_id)

        if product_detail_list:
            result = ProductDetailRepository.ProductDetailRepository.UpdateProductDetail(
                product_detail_id, product_expired_date, product_purchase_price, stock)

            if result == "success":
                return {"status": "Success"}

            else:
                return {"status": "Error Updating Product's Detail"}
        else:
            return {"status": "Error Product's Detail Not Found"}

    def DeleteProductDetail(json_data):
        product_detail_id = json_data['product_detail_id']

        product_detail_list = ProductDetailRepository.ProductDetailRepository.GetProductDetailById(
            product_detail_id)

        if product_detail_list:
            purchase_detail_list = PurchaseDetailRepository.PurchaseDetailRepository.GetPurchaseDetailByProductDetail(
                product_detail_id)

            if not purchase_detail_list:
                sales_detail_list = SalesDetailRepository.SalesDetailRepository.GetSalesDetailByProductDetail(
                    product_detail_id)

                if not sales_detail_list:
                    result = ProductDetailRepository.ProductDetailRepository.DeleteProductDetail(
                        product_detail_id)

                    if result == "success":
                        return {"status": "Success"}

                    else:
                        return {"status": "Error Deleting Product's Detail"}
                else:
                    return {"status": "Please Delete Product's Detail's Sales First"}
            else:
                return {"status": "Please Delete Product's Detail's Purchase First"}
        else:
            return {"status": "Error Product's Detail Not Found"}

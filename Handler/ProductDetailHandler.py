import Repository.ProductDetailRepository as ProductDetailRepository

import Factory.ProductDetailFactory as ProductDetailFactory


class ProductDetailHandler:
    def AddProductDetail(json_data):
        product_id = json_data['product_id']
        product_purchase_price = json_data['product_purchase_price']
        stock = json_data['stock']
        product_expired_date = json_data['product_expired_date']

        product_detail = ProductDetailFactory.ProductDetailFactory.CreateProductDetail(
            product_id, product_purchase_price, stock, product_expired_date)

        result = ProductDetailRepository.ProductDetailRepository.AddProductDetail(
            product_detail)

        if result == "success":

            product_detail = {"product_detail_id": str(product_detail.product_detail_id),
                              "product_id": str(product_detail.product_id),
                              "product_purchase_price": str(product_detail.product_purchase_price),
                              "stock": str(product_detail.stock),
                              "product_expired_date": str(product_detail.product_expired_date),
                              "product_detail_status": str(product_detail.product_detail_status)}

            return product_detail

        else:
            return {"status": "Error"}

    def GetProductDetailByProduct(json_data):
        product_id = json_data['product_id']

        product_detail_list = ProductDetailRepository.ProductDetailRepository.GetProductDetailByProduct(
            product_id)

        return product_detail_list

    def UpdateProductDetail(json_data):
        product_detail_id = json_data['product_detail_id']
        product_expired_date = json_data['product_expired_date']
        product_purchase_price = json_data['product_purchase_price']

        result = ProductDetailRepository.ProductDetailRepository.UpdateProductDetail(
            product_detail_id, product_expired_date, product_purchase_price)

        if result == "success":
            return {"status": "Success"}
        else:
            return {"status": "Error"}

    def DeleteProductDetail(json_data):
        product_detail_id = json_data['product_detail_id']

        result = ProductDetailRepository.ProductDetailRepository.DeleteProductDetail(
            product_detail_id)

        if result == "success":
            return {"status": "Success"}
        else:
            return {"status": "Error"}

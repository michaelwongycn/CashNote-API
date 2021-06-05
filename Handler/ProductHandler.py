import Repository.ProductRepository as ProductRepository

import Factory.ProductFactory as ProductFactory


class ProductHandler:
    def AddProduct(json_data):
        shop_id = json_data['shop_id']
        product_name = json_data['product_name']
        product_sale_price = json_data['product_sale_price']

        product = ProductFactory.ProductFactory.CreateProduct(
            shop_id, product_name, product_sale_price)

        result = ProductRepository.ProductRepository.AddProduct(
            product)

        if result == "success":

            product = {"product_id": str(product.product_id),  "shop_id": str(product.shop_id),
                       "product_name": str(product.product_name), "product_sale_price": product.product_sale_price,
                       "product_status": str(product.product_status)}

            return product
        else:
            return {"status": "Error"}

    def GetProductByShop(json_data):
        shop_id = json_data['shop_id']

        product_list = ProductRepository.ProductRepository.GetProductByShop(
            shop_id)

        Data = {}
        Data["Data"] = product_list

        return Data

    def GetProductById(json_data):
        product_id = json_data['product_id']

        product_list = ProductRepository.ProductRepository.GetProductById(
            product_id)

        return product_list

    def UpdateProduct(json_data):
        product_id = json_data['product_id']
        product_name = json_data['product_name']
        product_sale_price = json_data['product_sale_price']

        result = ProductRepository.ProductRepository.UpdateProduct(
            product_id, product_name, product_sale_price)

        if result == "success":
            return {"status": "Success"}
        else:
            return {"status": "Error"}

    def DeleteProduct(json_data):
        product_id = json_data['product_id']

        result = ProductRepository.ProductRepository.DeleteProduct(product_id)

        if result == "success":
            return {"status": "Success"}
        else:
            return {"status": "Error"}

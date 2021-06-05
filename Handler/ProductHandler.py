import Repository.ProductRepository as ProductRepository
import Repository.ProductDetailRepository as ProductDetailRepository

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
            return {"status": "Error Registering Product"}

    def GetProductByShop(json_data):
        shop_id = json_data['shop_id']

        product_list = ProductRepository.ProductRepository.GetProductByShop(
            shop_id)

        if product_list:
            Data = {}
            Data["Data"] = product_list

            return Data

        else:
            return {"status": "Error No Such Shop's Product"}

    def GetProductById(json_data):
        product_id = json_data['product_id']

        product_list = ProductRepository.ProductRepository.GetProductById(
            product_id)

        if product_list:
            Data = {}
            Data["Data"] = product_list

            return Data

        else:
            return {"status": "Error No Such Product"}

    def UpdateProduct(json_data):
        product_id = json_data['product_id']
        product_name = json_data['product_name']
        product_sale_price = json_data['product_sale_price']

        product_list = ProductRepository.ProductRepository.GetProductById(
            product_id)

        if product_list:
            result = ProductRepository.ProductRepository.UpdateProduct(
                product_id, product_name, product_sale_price)

            if result == "success":
                return {"status": "Success"}
            
            else:
                return {"status": "Error Updating Product"}
        else:
            return {"status": "Error Product Not Found"}

    def DeleteProduct(json_data):
        product_id = json_data['product_id']

        product_list = ProductRepository.ProductRepository.GetProductById(
            product_id)

        if product_list:
            product_detail_list = ProductDetailRepository.ProductDetailRepository.GetProductDetailByProduct(
                product_id)

            if not product_detail_list:
                result = ProductRepository.ProductRepository.DeleteProduct(
                    product_id)

                if result == "success":
                    return {"status": "Success"}

                else:
                    return {"status": "Error Deleting Product"}
            else:
                return {"status": "Please Delete Product's Detail First"}
        else:
            return {"status": "Error Product Not Found"}

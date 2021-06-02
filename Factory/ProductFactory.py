import Model.ProductModel as ProductModel
from uuid import uuid1


class ProductFactory:
    def CreateProduct(shop_id, product_name, product_sale_price):
        product_id = uuid1()
        product = ProductModel.Product(product_id, shop_id, product_name,
                                       product_sale_price, "A")
        return product

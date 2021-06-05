import Model.ProductDetailModel as ProductDetailModel
from uuid import uuid1


class ProductDetailFactory:
    def CreateProductDetail(product_id, supplier_id, product_purchase_price, stock, product_expired_date):
        product_detail_id = uuid1()
        product_detail = ProductDetailModel.ProductDetail(
            product_detail_id, product_id, supplier_id, product_purchase_price, stock, product_expired_date, "A")
        return product_detail

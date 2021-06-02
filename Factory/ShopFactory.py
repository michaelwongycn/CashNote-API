import Model.ShopModel as ShopModel
from uuid import uuid1


class ShopFactory:
    def CreateShop(shop_name):
        shop_id = uuid1()
        shop = ShopModel.Shop(shop_id, shop_name, "A")
        return shop

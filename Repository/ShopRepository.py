import Utility


class ShopRepository:
    def AddShop(shop):
        connection = Utility.get_connection()
        cursor = connection.cursor()

        query = "INSERT INTO shop (shop_id, shop_name, shop_status) VALUES (?, ?, ?)"
        params = [str(shop.shop_id), str(
            shop.shop_name), str(shop.shop_status)]
        cursor.execute(query, params)

        connection.commit()
        cursor.close()
        connection.close()

        return "success"

    def GetShops():
        connection = Utility.get_connection()
        cursor = connection.cursor()

        query = "SELECT * FROM shop WHERE shop_status = 'A'"
        cursor.execute(query)

        shops = cursor.fetchall()
        shop_list = []

        for shop in shops:
            dictionary = {
                "shop_id": shop[0],  "shop_name": shop[1], "shop_status": shop[2]}
            shop_list.append(dictionary)

        cursor.close()
        connection.close()

        return shop_list

    def GetShopById(shop_id):
        connection = Utility.get_connection()
        cursor = connection.cursor()

        query = "SELECT * FROM shop WHERE shop_id = ? AND shop_status = 'A'"
        params = [shop_id]
        cursor.execute(query, params)

        shops = cursor.fetchall()
        shop_list = []

        for shop in shops:
            dictionary = {
                "shop_id": shop[0],  "shop_name": shop[1], "shop_status": shop[2]}
            shop_list.append(dictionary)

        cursor.close()
        connection.close()

        return shop_list

    def DeleteShop(shop_id):
        connection = Utility.get_connection()
        cursor = connection.cursor()

        query = "UPDATE shop SET shop_status = 'D' WHERE shop_id = ? AND shop_status = 'A'"
        params = [shop_id]
        cursor.execute(query, params)

        connection.commit()
        cursor.close()
        connection.close()

        return "success"

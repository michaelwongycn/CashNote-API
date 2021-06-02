import Utility


class ProductRepository:
    def AddProduct(product):
        connection = Utility.get_connection()
        cursor = connection.cursor()

        query = "INSERT INTO product (product_id, shop_id, product_name, product_sale_price, product_status) VALUES (?, ?, ?, ?, ?)"
        params = [str(product.product_id), str(product.shop_id), str(product.product_name),
                  product.product_sale_price, str(product.product_status)]
        cursor.execute(query, params)

        connection.commit()
        cursor.close()
        connection.close()

        return "success"

    def GetProducts():
        connection = Utility.get_connection()
        cursor = connection.cursor()

        query = "SELECT * FROM product WHERE product_status = 'A'"
        cursor.execute(query)

        products = cursor.fetchall()
        product_list = []

        for product in products:
            dictionary = {"product_id": product[0],  "shop_id": product[1], "product_name": product[2],
                          "product_sale_price": product[3], "product_status": product[4]}
            product_list.append(dictionary)

        cursor.close()
        connection.close()

        return product_list

    def GetProductByShop(shop_id):
        connection = Utility.get_connection()
        cursor = connection.cursor()

        query = "SELECT * FROM product WHERE shop_id = ? AND product_status = 'A'"
        params = [shop_id]
        cursor.execute(query, params)

        products = cursor.fetchall()
        product_list = []

        for product in products:
            dictionary = {"product_id": product[0],  "shop_id": product[1], "product_name": product[2],
                          "product_sale_price": product[3], "product_status": product[4]}
            product_list.append(dictionary)

        cursor.close()
        connection.close()

        return product_list

    def GetProductById(product_id):
        connection = Utility.get_connection()
        cursor = connection.cursor()

        query = "SELECT * FROM product WHERE product_id = ? AND product_status = 'A'"
        params = [product_id]
        cursor.execute(query, params)

        products = cursor.fetchall()
        product_list = []

        for product in products:
            dictionary = {"product_id": product[0],  "shop_id": product[1], "product_name": product[2],
                          "product_sale_price": product[3], "product_status": product[4]}
            product_list.append(dictionary)

        cursor.close()
        connection.close()

        return product_list

    def UpdateProduct(product_id, product_name, product_sale_price):
        connection = Utility.get_connection()
        cursor = connection.cursor()

        query = "UPDATE product SET product_name = ? WHERE product_id = ? AND product_status = 'A'"
        params = [product_name, product_id]
        cursor.execute(query, params)

        query = "UPDATE product SET product_sale_price = ? WHERE product_id = ? AND product_status = 'A'"
        params = [product_sale_price, product_id]
        cursor.execute(query, params)

        connection.commit()
        cursor.close()
        connection.close()

        return "success"

    def DeleteProduct(product_id):
        connection = Utility.get_connection()
        cursor = connection.cursor()

        query = "UPDATE product SET product_status = 'D' WHERE product_id = ? AND product_status = 'A'"
        params = [product_id]
        cursor.execute(query, params)

        query = "UPDATE product_detail SET product_detail_status = 'D' WHERE product_id = ? AND product_detail_status = 'A'"
        params = [product_id]
        cursor.execute(query, params)

        connection.commit()
        cursor.close()
        connection.close()

        return "success"

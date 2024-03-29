import Utility


class ProductDetailRepository:
    def AddProductDetail(product_detail):
        connection = Utility.get_connection()
        cursor = connection.cursor()

        query = "INSERT INTO product_detail (product_detail_id, product_id, supplier_id, product_purchase_price, stock, product_expired_date, product_detail_status) VALUES (?, ?, ?, ?, ?, ?, ?)"
        params = [str(product_detail.product_detail_id), str(product_detail.product_id),  str(product_detail.supplier_id),
                  product_detail.product_purchase_price, product_detail.stock, str(
                      product_detail.product_expired_date),
                  str(product_detail.product_detail_status)]
        cursor.execute(query, params)

        connection.commit()
        cursor.close()
        connection.close()

        return "success"

    def GetProductsDetail():
        connection = Utility.get_connection()
        cursor = connection.cursor()

        query = "SELECT * FROM product_detail WHERE product_detail_status = 'A'"
        cursor.execute(query)

        products_detail = cursor.fetchall()
        product_detail_list = []

        for product_detail in products_detail:
            dictionary = {"product_detail_id": product_detail[0],  "product_id": product_detail[1], "supplier_id": product_detail[2],
                          "product_purchase_price": product_detail[3], "stock": product_detail[4],
                          "product_expired_date": product_detail[5], "product_detail_status": product_detail[6]}
            product_detail_list.append(dictionary)

        cursor.close()
        connection.close()

        return product_detail_list

    def GetProductDetailByProduct(product_id):
        connection = Utility.get_connection()
        cursor = connection.cursor()

        query = "SELECT * FROM product_detail WHERE product_id = ? AND product_detail_status = 'A'"
        params = [product_id]
        cursor.execute(query, params)

        products_detail = cursor.fetchall()
        product_detail_list = []

        for product_detail in products_detail:
            dictionary = {"product_detail_id": product_detail[0],  "product_id": product_detail[1], "supplier_id": product_detail[2],
                          "product_purchase_price": product_detail[3], "stock": product_detail[4],
                          "product_expired_date": product_detail[5], "product_detail_status": product_detail[6]}
            product_detail_list.append(dictionary)

        cursor.close()
        connection.close()

        return product_detail_list

    def GetProductDetailBySupplier(supplier_id):
        connection = Utility.get_connection()
        cursor = connection.cursor()

        query = "SELECT * FROM product_detail WHERE supplier_id = ? AND product_detail_status = 'A'"
        params = [supplier_id]
        cursor.execute(query, params)

        products_detail = cursor.fetchall()
        product_detail_list = []

        for product_detail in products_detail:
            dictionary = {"product_detail_id": product_detail[0],  "product_id": product_detail[1], "supplier_id": product_detail[2],
                          "product_purchase_price": product_detail[3], "stock": product_detail[4],
                          "product_expired_date": product_detail[5], "product_detail_status": product_detail[6]}
            product_detail_list.append(dictionary)

        cursor.close()
        connection.close()

        return product_detail_list

    def GetProductDetailWithStockByProduct(product_id):
        connection = Utility.get_connection()
        cursor = connection.cursor()

        query = "SELECT * FROM product_detail WHERE product_id = ? AND stock > 0 AND product_detail_status = 'A'"
        params = [product_id]
        cursor.execute(query, params)

        products_detail = cursor.fetchall()
        product_detail_list = []

        for product_detail in products_detail:
            dictionary = {"product_detail_id": product_detail[0],  "product_id": product_detail[1], "supplier_id": product_detail[2],
                          "product_purchase_price": product_detail[3], "stock": product_detail[4],
                          "product_expired_date": product_detail[5], "product_detail_status": product_detail[6]}
            product_detail_list.append(dictionary)

        cursor.close()
        connection.close()

        return product_detail_list

    def GetProductDetailWithSupplierPriceAndExpiredDateByProduct(product_id, supplier_id, product_expired_date, product_purchase_price):
        connection = Utility.get_connection()
        cursor = connection.cursor()

        query = "SELECT * FROM product_detail WHERE supplier_id = ? AND product_purchase_price = ? AND product_expired_date = ? AND product_id = ?AND product_detail_status = 'A'"
        params = [supplier_id, product_purchase_price,
                  product_expired_date, product_id]
        cursor.execute(query, params)

        products_detail = cursor.fetchall()
        product_detail_list = []

        for product_detail in products_detail:
            dictionary = {"product_detail_id": product_detail[0],  "product_id": product_detail[1], "supplier_id": product_detail[2],
                          "product_purchase_price": product_detail[3], "stock": product_detail[4],
                          "product_expired_date": product_detail[5], "product_detail_status": product_detail[6]}
            product_detail_list.append(dictionary)

        cursor.close()
        connection.close()

        return product_detail_list

    def GetProductDetailById(product_detail_id):
        connection = Utility.get_connection()
        cursor = connection.cursor()

        query = "SELECT * FROM product_detail WHERE product_detail_id = ? AND product_detail_status = 'A'"
        params = [product_detail_id]
        cursor.execute(query, params)

        products_detail = cursor.fetchall()
        product_detail_list = []

        for product_detail in products_detail:
            dictionary = {"product_detail_id": product_detail[0],  "product_id": product_detail[1], "supplier_id": product_detail[2],
                          "product_purchase_price": product_detail[3], "stock": product_detail[4],
                          "product_expired_date": product_detail[5], "product_detail_status": product_detail[6]}
            product_detail_list.append(dictionary)

        cursor.close()
        connection.close()

        return product_detail_list

    def GetProductDetailAndNonActiveById(product_detail_id):
        connection = Utility.get_connection()
        cursor = connection.cursor()

        query = "SELECT * FROM product_detail WHERE product_detail_id = ? AND (product_detail_status = 'A' OR product_detail_status = 'N')"
        params = [product_detail_id]
        cursor.execute(query, params)

        products_detail = cursor.fetchall()
        product_detail_list = []

        for product_detail in products_detail:
            dictionary = {"product_detail_id": product_detail[0],  "product_id": product_detail[1], "supplier_id": product_detail[2],
                          "product_purchase_price": product_detail[3], "stock": product_detail[4],
                          "product_expired_date": product_detail[5], "product_detail_status": product_detail[6]}
            product_detail_list.append(dictionary)

        cursor.close()
        connection.close()

        return product_detail_list

    def UpdateProductDetail(product_detail_id, product_expired_date, product_purchase_price, stock):
        connection = Utility.get_connection()
        cursor = connection.cursor()

        query = "UPDATE product_detail SET product_purchase_price = ? WHERE product_detail_id = ? AND product_detail_status = 'A'"
        params = [product_purchase_price, product_detail_id]
        cursor.execute(query, params)

        query = "UPDATE product_detail SET product_expired_date = ? WHERE product_detail_id = ? AND product_detail_status = 'A'"
        params = [product_expired_date, product_detail_id]
        cursor.execute(query, params)

        query = "UPDATE product_detail SET stock = ? WHERE product_detail_id = ? AND product_detail_status = 'A'"
        params = [stock, product_detail_id]
        cursor.execute(query, params)

        connection.commit()
        cursor.close()
        connection.close()

        return "success"

    def UpdateProductDetailStock(product_detail_id, stock):
        connection = Utility.get_connection()
        cursor = connection.cursor()

        query = "UPDATE product_detail SET stock = ? WHERE product_detail_id = ? AND product_detail_status = 'A'"
        params = [stock, product_detail_id]
        cursor.execute(query, params)

        connection.commit()
        cursor.close()
        connection.close()

        return "success"

    def DeleteProductDetail(product_detail_id):
        connection = Utility.get_connection()
        cursor = connection.cursor()

        query = "UPDATE product_detail SET product_detail_status = 'D' WHERE product_detail_id = ? AND product_detail_status = 'A'"
        params = [product_detail_id]
        cursor.execute(query, params)

        connection.commit()
        cursor.close()
        connection.close()

        return "success"

    def NonActiveProductDetail(product_detail_id):
        connection = Utility.get_connection()
        cursor = connection.cursor()

        query = "UPDATE product_detail SET product_detail_status = 'N' WHERE product_detail_id = ? AND product_detail_status = 'A'"
        params = [product_detail_id]
        cursor.execute(query, params)

        connection.commit()
        cursor.close()
        connection.close()

        return "success"

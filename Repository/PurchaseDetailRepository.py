import Utility


class PurchaseDetailRepository:
    def AddPurchaseDetail(purchase_detail):
        connection = Utility.get_connection()
        cursor = connection.cursor()

        query = "INSERT INTO purchase_detail (purchase_id, product_detail_id, amount, purchase_detail_status) VALUES (?, ?, ?, ?)"
        params = [str(purchase_detail.purchase_id), str(purchase_detail.product_detail_id), purchase_detail.amount,
                  str(purchase_detail.purchase_detail_status)]
        cursor.execute(query, params)

        connection.commit()
        cursor.close()
        connection.close()

        return "success"

    def GetPurchasesDetail():
        connection = Utility.get_connection()
        cursor = connection.cursor()

        query = "SELECT * FROM purchase_detail WHERE purchase_detail_status = 'A'"
        cursor.execute(query)

        purchases_detail = cursor.fetchall()
        purchase_detail_list = []

        for purchase_detail in purchases_detail:
            dictionary = {"purchase_id": purchase_detail[0],  "product_detail_id": purchase_detail[1],
                          "amount": purchase_detail[2], "purchase_detail_status": purchase_detail[3]}
            purchase_detail_list.append(dictionary)

        cursor.close()
        connection.close()

        return purchase_detail_list

    def GetPurchaseDetailByPurchase(purchase_id):
        connection = Utility.get_connection()
        cursor = connection.cursor()

        query = "SELECT * FROM purchase_detail WHERE purchase_id = ? AND purchase_detail_status = 'A'"
        params = [purchase_id]
        cursor.execute(query, params)

        purchases_detail = cursor.fetchall()
        purchase_detail_list = []

        for purchase_detail in purchases_detail:
            dictionary = {"purchase_id": purchase_detail[0],  "product_detail_id": purchase_detail[1],
                          "amount": purchase_detail[2], "purchase_detail_status": purchase_detail[3]}
            purchase_detail_list.append(dictionary)

        cursor.close()
        connection.close()

        return purchase_detail_list

    def GetPurchaseDetailByProductDetail(product_detail_id):
        connection = Utility.get_connection()
        cursor = connection.cursor()

        query = "SELECT * FROM purchase_detail WHERE product_detail_id = ? AND purchase_detail_status = 'A'"
        params = [product_detail_id]
        cursor.execute(query, params)

        purchases_detail = cursor.fetchall()
        purchase_detail_list = []

        for purchase_detail in purchases_detail:
            dictionary = {"purchase_id": purchase_detail[0],  "product_detail_id": purchase_detail[1],
                          "amount": purchase_detail[2], "purchase_detail_status": purchase_detail[3]}
            purchase_detail_list.append(dictionary)

        cursor.close()
        connection.close()

        return purchase_detail_list

    def GetUniquePurchaseDetail(purchase_id, product_detail_id):
        connection = Utility.get_connection()
        cursor = connection.cursor()

        query = "SELECT * FROM purchase_detail WHERE purchase_id = ? AND product_detail_id = ? AND purchase_detail_status = 'A'"
        params = [purchase_id, product_detail_id]
        cursor.execute(query, params)

        purchases_detail = cursor.fetchall()
        purchase_detail_list = []

        for purchase_detail in purchases_detail:
            dictionary = {"purchase_id": purchase_detail[0],  "product_detail_id": purchase_detail[1],
                          "amount": purchase_detail[2], "purchase_detail_status": purchase_detail[3]}
            purchase_detail_list.append(dictionary)

        cursor.close()
        connection.close()

        return purchase_detail_list

    def DeletePurchaseDetail(purchase_id, product_detail_id):
        connection = Utility.get_connection()
        cursor = connection.cursor()

        query = "UPDATE purchase_detail SET purchase_detail_status = 'D' WHERE purchase_id = ? AND product_detail_id = ? AND purchase_detail_status = 'A'"
        params = [purchase_id, product_detail_id]
        cursor.execute(query, params)

        connection.commit()
        cursor.close()
        connection.close()

        return "success"

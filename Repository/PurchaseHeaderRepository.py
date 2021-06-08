import Utility


class PurchaseHeaderRepository:
    def AddPurchaseHeader(purchase_header):
        connection = Utility.get_connection()
        cursor = connection.cursor()

        query = "INSERT INTO purchase_header (purchase_id, supplier_id, shop_id, transaction_date_time, transaction_price_change, payment_status, purchase_status) VALUES (?, ?, ?, ?, ?, ?, ?)"
        params = [str(purchase_header.purchase_id), str(purchase_header.supplier_id), str(purchase_header.shop_id),
                  str(purchase_header.transaction_date_time), purchase_header.transaction_price_change, str(purchase_header.payment_status), str(purchase_header.purchase_status)]
        cursor.execute(query, params)

        connection.commit()
        cursor.close()
        connection.close()

        return "success"

    def GetPurchasesHeader():
        connection = Utility.get_connection()
        cursor = connection.cursor()

        query = "SELECT * FROM purchase_header WHERE purchase_status = 'A'"
        cursor.execute(query)

        purchases_header = cursor.fetchall()
        purchase_header_list = []

        for purchase_header in purchases_header:
            dictionary = {"purchase_id": purchase_header[0],  "supplier_id": purchase_header[1], "shop_id": purchase_header[2],
                          "transaction_date_time": purchase_header[3], "transaction_price_change": purchase_header[4], "payment_status": purchase_header[5], "purchase_status": purchase_header[6]}
            purchase_header_list.append(dictionary)

        cursor.close()
        connection.close()

        return purchase_header_list

    def GetPurchaseHeaderByShop(shop_id):
        connection = Utility.get_connection()
        cursor = connection.cursor()

        query = "SELECT * FROM purchase_header WHERE shop_id = ? AND purchase_status = 'A'"
        params = [shop_id]
        cursor.execute(query, params)

        purchases_header = cursor.fetchall()
        purchase_header_list = []

        for purchase_header in purchases_header:
            dictionary = {"purchase_id": purchase_header[0],  "supplier_id": purchase_header[1], "shop_id": purchase_header[2],
                          "transaction_date_time": purchase_header[3], "transaction_price_change": purchase_header[4], "payment_status": purchase_header[5], "purchase_status": purchase_header[6]}
            purchase_header_list.append(dictionary)

        cursor.close()
        connection.close()

        return purchase_header_list

    def GetPurchaseHeaderBySupplier(supplier_id):
        connection = Utility.get_connection()
        cursor = connection.cursor()

        query = "SELECT * FROM purchase_header WHERE supplier_id = ? AND purchase_status = 'A'"
        params = [supplier_id]
        cursor.execute(query, params)

        purchases_header = cursor.fetchall()
        purchase_header_list = []

        for purchase_header in purchases_header:
            dictionary = {"purchase_id": purchase_header[0],  "supplier_id": purchase_header[1], "shop_id": purchase_header[2],
                          "transaction_date_time": purchase_header[3], "transaction_price_change": purchase_header[4], "payment_status": purchase_header[5], "purchase_status": purchase_header[6]}
            purchase_header_list.append(dictionary)

        cursor.close()
        connection.close()

        return purchase_header_list

    def GetPurchaseHeaderById(purchase_id):
        connection = Utility.get_connection()
        cursor = connection.cursor()

        query = "SELECT * FROM purchase_header WHERE purchase_id = ? AND purchase_status = 'A'"
        params = [purchase_id]
        cursor.execute(query, params)

        purchases_header = cursor.fetchall()
        purchase_header_list = []

        for purchase_header in purchases_header:
            dictionary = {"purchase_id": purchase_header[0],  "supplier_id": purchase_header[1], "shop_id": purchase_header[2],
                          "transaction_date_time": purchase_header[3], "transaction_price_change": purchase_header[4], "payment_status": purchase_header[5], "purchase_status": purchase_header[6]}
            purchase_header_list.append(dictionary)

        cursor.close()
        connection.close()

        return purchase_header_list

    def GetPurchaseHeaderByYearMonthDate(date, shop_id):
        connection = Utility.get_connection()
        cursor = connection.cursor()

        query = "SELECT * FROM purchase_header WHERE strftime('%Y-%m-%d', transaction_date_time) = ? AND shop_id = ? AND purchase_status = 'A'"
        params = [date, shop_id]
        cursor.execute(query, params)

        purchases_header = cursor.fetchall()
        purchase_header_list = []

        for purchase_header in purchases_header:
            dictionary = {"purchase_id": purchase_header[0],  "supplier_id": purchase_header[1], "shop_id": purchase_header[2],
                          "transaction_date_time": purchase_header[3], "transaction_price_change": purchase_header[4], "payment_status": purchase_header[5], "purchase_status": purchase_header[6]}
            purchase_header_list.append(dictionary)

        cursor.close()
        connection.close()

        return purchase_header_list

    def GetPurchaseHeaderByYearMonth(date, shop_id):
        connection = Utility.get_connection()
        cursor = connection.cursor()

        query = "SELECT * FROM purchase_header WHERE strftime('%Y-%m', transaction_date_time) = ? AND shop_id = ? AND purchase_status = 'A'"
        params = [date, shop_id]
        cursor.execute(query, params)

        purchases_header = cursor.fetchall()
        purchase_header_list = []

        for purchase_header in purchases_header:
            dictionary = {"purchase_id": purchase_header[0],  "supplier_id": purchase_header[1], "shop_id": purchase_header[2],
                          "transaction_date_time": purchase_header[3], "transaction_price_change": purchase_header[4], "payment_status": purchase_header[5], "purchase_status": purchase_header[6]}
            purchase_header_list.append(dictionary)

        cursor.close()
        connection.close()

        return purchase_header_list

    def GetPurchaseHeaderByYear(date, shop_id):
        connection = Utility.get_connection()
        cursor = connection.cursor()

        query = "SELECT * FROM purchase_header WHERE strftime('%Y', transaction_date_time) = ? AND shop_id = ? AND purchase_status = 'A'"
        params = [date, shop_id]
        cursor.execute(query, params)

        purchases_header = cursor.fetchall()
        purchase_header_list = []

        for purchase_header in purchases_header:
            dictionary = {"purchase_id": purchase_header[0],  "supplier_id": purchase_header[1], "shop_id": purchase_header[2],
                          "transaction_date_time": purchase_header[3], "transaction_price_change": purchase_header[4], "payment_status": purchase_header[5], "purchase_status": purchase_header[6]}
            purchase_header_list.append(dictionary)

        cursor.close()
        connection.close()

        return purchase_header_list

    def SetPaymentToPaid(purchase_id):
        connection = Utility.get_connection()
        cursor = connection.cursor()

        query = "UPDATE purchase_header SET Payment_status = 'Paid' WHERE purchase_id = ? AND purchase_status = 'A'"
        params = [purchase_id]
        cursor.execute(query, params)

        connection.commit()
        cursor.close()
        connection.close()

        return "success"

    def DeletePurchaseHeader(purchase_id):
        connection = Utility.get_connection()
        cursor = connection.cursor()

        query = "UPDATE purchase_header SET purchase_status = 'D' WHERE purchase_id = ? AND purchase_status = 'A'"
        params = [purchase_id]
        cursor.execute(query, params)

        query = "UPDATE purchase_detail SET purchase_detail_status = 'D' WHERE purchase_id = ? AND purchase_detail_status = 'A'"
        params = [purchase_id]
        cursor.execute(query, params)

        connection.commit()
        cursor.close()
        connection.close()

        return "success"

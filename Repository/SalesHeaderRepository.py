import Utility


class SalesHeaderRepository:
    def AddSalesHeader(sales_header):
        connection = Utility.get_connection()
        cursor = connection.cursor()

        query = "INSERT INTO sales_header (sales_id, account_id, shop_id, transaction_date_time, transaction_price_change, payment_status, sales_status) VALUES (?, ?, ?, ?, ?, ?, ?)"
        params = [str(sales_header.sales_id), str(sales_header.account_id), str(sales_header.shop_id),
                  str(sales_header.transaction_date_time), sales_header.transaction_price_change,
                  str(sales_header.payment_status), str(sales_header.sales_status)]
        cursor.execute(query, params)

        connection.commit()
        cursor.close()
        connection.close()

        return "success"

    def GetSalesHeader():
        connection = Utility.get_connection()
        cursor = connection.cursor()

        query = "SELECT * FROM sales_header WHERE sales_status = 'A'"
        cursor.execute(query)

        sales_header = cursor.fetchall()
        sales_header_list = []

        for sales_item in sales_header:
            dictionary = {"sales_id": sales_item[0],  "account_id": sales_item[1], "shop_id": sales_item[2],
                          "transaction_date_time": sales_item[3], "transaction_price_change": sales_item[4],
                          "payment_status": sales_item[5], "sales_status": sales_item[6]}
            sales_header_list.append(dictionary)

        cursor.close()
        connection.close()

        return sales_header_list

    def GetSalesHeaderByShop(shop_id):
        connection = Utility.get_connection()
        cursor = connection.cursor()

        query = "SELECT * FROM sales_header WHERE shop_id = ? AND sales_status = 'A'"
        params = [shop_id]
        cursor.execute(query, params)

        sales_header = cursor.fetchall()
        sales_header_list = []

        for sales_item in sales_header:
            dictionary = {"sales_id": sales_item[0],  "account_id": sales_item[1], "shop_id": sales_item[2],
                          "transaction_date_time": sales_item[3], "transaction_price_change": sales_item[4],
                          "payment_status": sales_item[5], "sales_status": sales_item[6]}
            sales_header_list.append(dictionary)

        cursor.close()
        connection.close()

        return sales_header_list

    def GetSalesHeaderByAccount(account_id):
        connection = Utility.get_connection()
        cursor = connection.cursor()

        query = "SELECT * FROM sales_header WHERE account_id = ? AND sales_status = 'A'"
        params = [account_id]
        cursor.execute(query, params)

        sales_header = cursor.fetchall()
        sales_header_list = []

        for sales_item in sales_header:
            dictionary = {"sales_id": sales_item[0],  "account_id": sales_item[1], "shop_id": sales_item[2],
                          "transaction_date_time": sales_item[3], "transaction_price_change": sales_item[4],
                          "payment_status": sales_item[5], "sales_status": sales_item[6]}
            sales_header_list.append(dictionary)

        cursor.close()
        connection.close()

        return sales_header_list

    def GetSalesHeaderById(sales_id):
        connection = Utility.get_connection()
        cursor = connection.cursor()

        query = "SELECT * FROM sales_header WHERE sales_id = ? AND sales_status = 'A'"
        params = [sales_id]
        cursor.execute(query, params)

        sales_header = cursor.fetchall()
        sales_header_list = []

        for sales_item in sales_header:
            dictionary = {"sales_id": sales_item[0],  "account_id": sales_item[1], "shop_id": sales_item[2],
                          "transaction_date_time": sales_item[3], "transaction_price_change": sales_item[4],
                          "payment_status": sales_item[5], "sales_status": sales_item[6]}
            sales_header_list.append(dictionary)

        cursor.close()
        connection.close()

        return sales_header_list

    def GetSalesHeaderByYearMonthDate(date, shop_id):
        connection = Utility.get_connection()
        cursor = connection.cursor()

        query = "SELECT * FROM sales_header WHERE strftime('%Y-%m-%d', transaction_date_time) = ? AND shop_id = ? AND sales_status = 'A'"
        params = [date, shop_id]
        cursor.execute(query, params)

        sales_header = cursor.fetchall()
        sales_header_list = []

        for sales_item in sales_header:
            dictionary = {"sales_id": sales_item[0],  "account_id": sales_item[1], "shop_id": sales_item[2],
                          "transaction_date_time": sales_item[3], "transaction_price_change": sales_item[4],
                          "payment_status": sales_item[5], "sales_status": sales_item[6]}
            sales_header_list.append(dictionary)

        cursor.close()
        connection.close()

        return sales_header_list

    def GetSalesHeaderByYearMonth(date, shop_id):
        connection = Utility.get_connection()
        cursor = connection.cursor()

        query = "SELECT * FROM sales_header WHERE strftime('%Y-%m', transaction_date_time) = ? AND shop_id = ? AND sales_status = 'A'"
        params = [date, shop_id]
        cursor.execute(query, params)

        sales_header = cursor.fetchall()
        sales_header_list = []

        for sales_item in sales_header:
            dictionary = {"sales_id": sales_item[0],  "account_id": sales_item[1], "shop_id": sales_item[2],
                          "transaction_date_time": sales_item[3], "transaction_price_change": sales_item[4],
                          "payment_status": sales_item[5], "sales_status": sales_item[6]}
            sales_header_list.append(dictionary)

        cursor.close()
        connection.close()

        return sales_header_list

    def GetSalesHeaderByYear(date, shop_id):
        connection = Utility.get_connection()
        cursor = connection.cursor()

        query = "SELECT * FROM sales_header WHERE strftime('%Y', transaction_date_time) = ? AND shop_id = ? AND sales_status = 'A'"
        params = [date, shop_id]
        cursor.execute(query, params)

        sales_header = cursor.fetchall()
        sales_header_list = []

        for sales_item in sales_header:
            dictionary = {"sales_id": sales_item[0],  "account_id": sales_item[1], "shop_id": sales_item[2],
                          "transaction_date_time": sales_item[3], "transaction_price_change": sales_item[4],
                          "payment_status": sales_item[5], "sales_status": sales_item[6]}
            sales_header_list.append(dictionary)

        cursor.close()
        connection.close()

        return sales_header_list

    def SetPaymentToPaid(sales_id):
        connection = Utility.get_connection()
        cursor = connection.cursor()

        query = "UPDATE sales_header SET Payment_status = 'Paid' WHERE sales_id = ? AND sales_status = 'A'"
        params = [sales_id]
        cursor.execute(query, params)

        connection.commit()
        cursor.close()
        connection.close()

        return "success"

    def DeleteSalesHeader(sales_id):
        connection = Utility.get_connection()
        cursor = connection.cursor()

        query = "UPDATE sales_header SET sales_status = 'D' WHERE sales_id = ? AND sales_status = 'A'"
        params = [sales_id]
        cursor.execute(query, params)

        query = "UPDATE sales_detail SET sales_detail_status = 'D' WHERE sales_id = ? AND sales_detail_status = 'A'"
        params = [sales_id]
        cursor.execute(query, params)

        connection.commit()
        cursor.close()
        connection.close()

        return "success"

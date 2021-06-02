import Utility


class SalesDetailRepository:
    def AddSalesDetail(sales_detail):
        connection = Utility.get_connection()
        cursor = connection.cursor()

        query = "INSERT INTO sales_detail (sales_id, product_detail_id, product_sale_price, amount, sales_detail_status) VALUES (?, ?, ?, ?, ?)"
        params = [str(sales_detail.sales_id), str(sales_detail.product_detail_id), sales_detail.product_sale_price,
                  sales_detail.amount, str(sales_detail.sales_detail_status)]
        cursor.execute(query, params)

        connection.commit()
        cursor.close()
        connection.close()

        return "success"

    def GetSalesDetail():
        connection = Utility.get_connection()
        cursor = connection.cursor()

        query = "SELECT * FROM sales_detail WHERE sales_detail_status = 'A'"
        cursor.execute(query)

        sales_detail = cursor.fetchall()
        sales_detail_list = []

        for sales_detail in sales_detail:
            dictionary = {"sales_id": sales_detail[0],  "product_detail_id": sales_detail[1], "product_sale_price": sales_detail[2],
                          "amount": sales_detail[3], "sales_detail_status": sales_detail[4]}
            sales_detail_list.append(dictionary)

        cursor.close()
        connection.close()

        return sales_detail_list

    def GetSalesDetailBySales(sales_id):
        connection = Utility.get_connection()
        cursor = connection.cursor()

        query = "SELECT * FROM sales_detail WHERE sales_id = ? AND sales_detail_status = 'A'"
        params = [sales_id]
        cursor.execute(query, params)

        sales_detail = cursor.fetchall()
        sales_detail_list = []

        for sales_detail in sales_detail:
            dictionary = {"sales_id": sales_detail[0],  "product_detail_id": sales_detail[1], "product_sale_price": sales_detail[2],
                          "amount": sales_detail[3], "sales_detail_status": sales_detail[4]}
            sales_detail_list.append(dictionary)

        cursor.close()
        connection.close()

        return sales_detail_list

    def GetUniqueSalesDetail(sales_id, product_detail_id):
        connection = Utility.get_connection()
        cursor = connection.cursor()

        query = "SELECT * FROM sales_detail WHERE sales_id = ? AND product_detail_id = ? AND sales_detail_status = 'A'"
        params = [sales_id, product_detail_id]
        cursor.execute(query, params)

        sales_detail = cursor.fetchall()
        sales_detail_list = []

        for sales_detail in sales_detail:
            dictionary = {"sales_id": sales_detail[0],  "product_detail_id": sales_detail[1], "product_sale_price": sales_detail[2],
                          "amount": sales_detail[3], "sales_detail_status": sales_detail[4]}
            sales_detail_list.append(dictionary)

        cursor.close()
        connection.close()

        return sales_detail_list

    def DeleteSalesDetail(sales_id, product_detail_id):
        connection = Utility.get_connection()
        cursor = connection.cursor()

        query = "UPDATE sales_detail SET sales_detail_status = 'D' WHERE sales_id = ? AND product_detail_id = ? AND sales_detail_status = 'A'"
        params = [sales_id, product_detail_id]
        cursor.execute(query, params)

        connection.commit()
        cursor.close()
        connection.close()

        return "success"

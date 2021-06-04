import Utility


class SupplierRepository:
    def AddSupplier(supplier):
        connection = Utility.get_connection()
        cursor = connection.cursor()

        query = "INSERT INTO supplier (supplier_id, shop_id, supplier_name, supplier_address, supplier_phone, supplier_status) VALUES (?, ?, ?, ?, ?, ?)"
        params = [str(supplier.supplier_id), str(supplier.shop_id), str(supplier.supplier_name),
                  str(supplier.supplier_address), str(supplier.supplier_phone), str(supplier.supplier_status)]
        cursor.execute(query, params)

        connection.commit()
        cursor.close()
        connection.close()

        return "success"

    def GetSuppliers():
        connection = Utility.get_connection()
        cursor = connection.cursor()

        query = "SELECT * FROM supplier WHERE supplier_status = 'A'"
        cursor.execute(query)

        suppliers = cursor.fetchall()
        supplier_list = []

        for supplier in suppliers:
            dictionary = {"supplier_id": supplier[0],  "shop_id": supplier[1], "supplier_name": supplier[2],
                          "supplier_address": supplier[3], "supplier_phone": supplier[4], "supplier_status": supplier[5]}
            supplier_list.append(dictionary)

        cursor.close()
        connection.close()

        return supplier_list

    def GetSupplierByShop(shop_id):
        connection = Utility.get_connection()
        cursor = connection.cursor()

        query = "SELECT * FROM supplier WHERE shop_id = ? AND supplier_status = 'A'"
        params = [shop_id]
        cursor.execute(query, params)

        suppliers = cursor.fetchall()
        supplier_list = []

        for supplier in suppliers:
            dictionary = {"supplier_id": supplier[0],  "shop_id": supplier[1], "supplier_name": supplier[2],
                          "supplier_address": supplier[3], "supplier_phone": supplier[4], "supplier_status": supplier[5]}
            supplier_list.append(dictionary)

        cursor.close()
        connection.close()

        result = {"Data": supplier_list}

        return result

    def GetSupplierById(supplier_id):
        connection = Utility.get_connection()
        cursor = connection.cursor()

        query = "SELECT * FROM supplier WHERE supplier_id = ? AND supplier_status = 'A'"
        params = [supplier_id]
        cursor.execute(query, params)

        suppliers = cursor.fetchall()
        supplier_list = []

        for supplier in suppliers:
            dictionary = {"supplier_id": supplier[0],  "shop_id": supplier[1], "supplier_name": supplier[2],
                          "supplier_address": supplier[3], "supplier_phone": supplier[4], "supplier_status": supplier[5]}
            supplier_list.append(dictionary)

        cursor.close()
        connection.close()

        return supplier_list

    def UpdateSupplier(supplier_id, supplier_name, supplier_address, supplier_phone):
        connection = Utility.get_connection()
        cursor = connection.cursor()

        query = "UPDATE supplier SET supplier_name = ? WHERE supplier_id = ? AND supplier_status = 'A'"
        params = [supplier_name, supplier_id]
        cursor.execute(query, params)

        query = "UPDATE supplier SET supplier_address = ? WHERE supplier_id = ? AND supplier_status = 'A'"
        params = [supplier_address, supplier_id]
        cursor.execute(query, params)

        query = "UPDATE supplier SET supplier_phone = ? WHERE supplier_id = ? AND supplier_status = 'A'"
        params = [supplier_phone, supplier_id]
        cursor.execute(query, params)

        connection.commit()
        cursor.close()
        connection.close()

        return "success"

    def DeleteSupplier(supplier_id):
        connection = Utility.get_connection()
        cursor = connection.cursor()

        query = "UPDATE supplier SET supplier_status = 'D' WHERE supplier_id = ? AND supplier_status = 'A'"
        params = [supplier_id]
        cursor.execute(query, params)

        connection.commit()
        cursor.close()
        connection.close()

        return "success"

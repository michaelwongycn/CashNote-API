import Utility


class AccountRepository:
    def AddAccount(account):
        connection = Utility.get_connection()
        cursor = connection.cursor()

        query = "INSERT INTO account (account_id, shop_id, account_name, account_password, account_previlege, account_status) VALUES (?, ?, ?, ?, ?, ?)"
        params = [str(account.account_id), str(account.shop_id), str(account.account_name),
                  str(account.account_password), str(account.account_previlege), str(account.account_status)]
        cursor.execute(query, params)

        connection.commit()
        cursor.close()
        connection.close()

        return "success"

    def GetAccounts():
        connection = Utility.get_connection()
        cursor = connection.cursor()

        query = "SELECT * FROM account WHERE account_status = 'A'"
        cursor.execute(query)

        accounts = cursor.fetchall()
        account_list = []

        for account in accounts:
            dictionary = {"account_id": account[0],  "shop_id": account[1], "account_name": account[2],
                          "account_password": account[3], "account_previlege": account[4], "account_status": account[5]}
            account_list.append(dictionary)

        cursor.close()
        connection.close()

        return account_list

    def GetAccountByShop(shop_id):
        connection = Utility.get_connection()
        cursor = connection.cursor()

        query = "SELECT * FROM account WHERE shop_id = ? AND account_status = 'A'"
        params = [shop_id]
        cursor.execute(query, params)

        accounts = cursor.fetchall()
        account_list = []

        for account in accounts:
            dictionary = {"account_id": account[0],  "shop_id": account[1], "account_name": account[2],
                          "account_password": account[3], "account_previlege": account[4], "account_status": account[5]}
            account_list.append(dictionary)

        cursor.close()
        connection.close()

        return account_list

    def GetAccountById(account_id):
        connection = Utility.get_connection()
        cursor = connection.cursor()

        query = "SELECT * FROM account WHERE account_id = ? AND account_status = 'A'"
        params = [account_id]
        cursor.execute(query, params)

        accounts = cursor.fetchall()
        account_list = []

        for account in accounts:
            dictionary = {"account_id": account[0],  "shop_id": account[1], "account_name": account[2],
                          "account_password": account[3], "account_previlege": account[4], "account_status": account[5]}
            account_list.append(dictionary)

        cursor.close()
        connection.close()

        return account_list

    def GetAccountByName(account_name):
        connection = Utility.get_connection()
        cursor = connection.cursor()

        query = "SELECT * FROM account WHERE account_name = ? AND account_status = 'A'"
        params = [account_name]
        cursor.execute(query, params)

        accounts = cursor.fetchall()
        account_list = []

        for account in accounts:
            dictionary = {"account_id": account[0],  "shop_id": account[1], "account_name": account[2],
                          "account_password": account[3], "account_previlege": account[4], "account_status": account[5]}
            account_list.append(dictionary)

        cursor.close()
        connection.close()

        return account_list

    def GetAccountByNameAndPassword(account_name, account_password):
        connection = Utility.get_connection()
        cursor = connection.cursor()

        query = "SELECT * FROM account WHERE account_name = ? AND account_password = ? AND account_status = 'A'"
        params = [account_name, account_password]
        cursor.execute(query, params)

        accounts = cursor.fetchall()
        account_list = []

        for account in accounts:
            dictionary = {"account_id": account[0],  "shop_id": account[1], "account_name": account[2],
                          "account_password": account[3], "account_previlege": account[4], "account_status": account[5]}
            account_list.append(dictionary)

        cursor.close()
        connection.close()

        return account_list

    def DeleteAccount(account_id):
        connection = Utility.get_connection()
        cursor = connection.cursor()

        query = "UPDATE account SET account_status = 'D' WHERE account_id = ? AND account_status = 'A'"
        params = [account_id]
        cursor.execute(query, params)

        connection.commit()
        cursor.close()
        connection.close()

        return "success"

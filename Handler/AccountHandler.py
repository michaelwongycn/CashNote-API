import Repository.AccountRepository as AccountRepository
import Repository.ShopRepository as ShopRepository
import Repository.SalesHeaderRepository as SalesHeaderRepository


import Factory.AccountFactory as AccountFactory


class AccountHandler:
    def RegisterNewAdmin(json_data):
        shop_id = json_data['shop_id']
        account_name = json_data['account_name']
        account_password = json_data['account_password']

        account_list = AccountRepository.AccountRepository.GetAccountByName(
            account_name)

        if not account_list:
            account = AccountFactory.AccountFactory.CreateAccount(
                str(shop_id), account_name, account_password, "Admin")

            result = AccountRepository.AccountRepository.AddAccount(
                account)

            if result == "success":
                account = {"account_id": str(account.account_id),  "shop_id": str(account.shop_id),
                           "account_name": str(account.account_name), "account_password": str(account.account_password),
                           "account_previlege": str(account.account_previlege), "account_status": str(account.account_status)}

                return account
            else:
                return {"status": "Error Registering Admin"}

        else:
            return {"status": "Username Already Taken"}

    def GetAccountByShop(json_data):
        shop_id = json_data['shop_id']

        account_list = AccountRepository.AccountRepository.GetAccountByShop(
            shop_id)

        if account_list:
            Data = {}
            Data["Data"] = account_list

            return Data

        else:
            return {"status": "Error No Such Shop's Admin"}

    def RemoveAdmin(json_data):
        account_id = json_data['account_id']

        account_list = AccountRepository.AccountRepository.GetAccountById(
            account_id)

        if account_list:
            if account_list[0]['account_previlege'] == "Admin":

                account_id = account_list[0]['account_id']

                sales_header_list = SalesHeaderRepository.SalesHeaderRepository.GetSalesHeaderByAccount(
                    account_id)

                if not sales_header_list:
                    AccountRepository.AccountRepository.DeleteAccount(
                        account_id)
                    return {"status": "Success"}

                else:
                    return {"status": "Please Delete Admin's Sales First"}
            else:
                return {"status": "Error Can't Remove Owner"}
        else:
            return {"status": "Error Admin Not Found"}

    def Login(json_data):
        account_name = json_data['account_name']
        account_password = json_data['account_password']

        account_list = AccountRepository.AccountRepository.GetAccountByNameAndPassword(
            account_name, account_password)

        if account_list:
            shop = ShopRepository.ShopRepository.GetShopById(
                account_list[0]['shop_id'])

            respond = {"account": account_list[0],  "shop": shop[0]}

            return respond
        else:
            return {"status": "Wrong Credential"}

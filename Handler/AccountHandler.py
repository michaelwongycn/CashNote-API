import Repository.AccountRepository as AccountRepository

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
                           "account_name": str(account.account_name), "account_password": str(account.account_password), "account_previlege": str(account.account_previlege), "account_status": str(account.account_status)}

                return account
            else:
                return {"status": "Error"}

        else:
            return {"status": "Username Already Taken"}

    def GetAccountByShop(json_data):
        shop_id = json_data['shop_id']

        account_list = AccountRepository.AccountRepository.GetAccountByShop(
            shop_id)

        return account_list

    def RemoveAdmin(json_data):
        account_id = json_data['account_id']

        account_list = AccountRepository.AccountRepository.GetAccountById(
            account_id)

        if account_list:
            if account_list[0]['account_previlege'] == "Admin":
                AccountRepository.AccountRepository.DeleteAccount(
                    account_id)
                return {"status": "Success"}
            else:
                return {"status": "Error"}

        else:
            return {"status": "Error"}

    def Login(json_data):
        account_name = json_data['account_name']
        account_password = json_data['account_password']

        account_list = AccountRepository.AccountRepository.GetAccountByNameAndPassword(
            account_name, account_password)

        if account_list:
            return account_list[0]
        else:
            return {"status": "Wrong Credential"}

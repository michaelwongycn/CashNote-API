import Repository.ShopRepository as ShopRepository
import Repository.AccountRepository as AccountRepository

import Factory.ShopFactory as ShopFactory
import Factory.AccountFactory as AccountFactory


class ShopHandler:
    def RegisterNewShop(json_data):
        shop_name = json_data['shop_name']
        account_name = json_data['account_name']
        account_password = json_data['account_password']

        account_list = AccountRepository.AccountRepository.GetAccountByName(
            account_name)

        if not account_list:
            shop = ShopFactory.ShopFactory.CreateShop(shop_name)
            account = AccountFactory.AccountFactory.CreateAccount(
                str(shop.shop_id), account_name, account_password, "Owner")

            ShopRepository.ShopRepository.AddShop(shop)
            AccountRepository.AccountRepository.AddAccount(account)

            account = {"account_id": str(account.account_id),  "shop_id": str(account.shop_id),
                       "account_name": str(account.account_name), "account_password": str(account.account_password), "account_previlege": str(account.account_previlege), "account_status": str(account.account_status)}

            return account

        else:
            return {"status": "Username Already Taken"}

import Model.AccountModel as AccountModel
from uuid import uuid1


class AccountFactory:
    def CreateAccount(shop_id, account_name, account_password, account_previlege):
        account_id = uuid1()
        account = AccountModel.Account(account_id, shop_id, account_name,
                                       account_password, account_previlege, "A")
        return account

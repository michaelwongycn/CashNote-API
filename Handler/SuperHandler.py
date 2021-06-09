import Repository.AccountRepository as AccountRepository


def GetAllAccount():
    account_list = AccountRepository.AccountRepository.GetAccounts()

    if account_list:
        Data = {}
        Data["Data"] = account_list

        return Data

    else:
        return {"status": "Error No Such Shop's Admin"}

import Repository.ProductDetailRepository as ProductDetailRepository
import Repository.PurchaseHeaderRepository as PurchaseHeaderRepository
import Repository.PurchaseDetailRepository as PurchaseDetailRepository
import Repository.SalesHeaderRepository as SalesHeaderRepository
import Repository.SalesDetailRepository as SalesDetailRepository


class AnalyticHandler:
    def GetIncomeByYearMonthDate(json_data):
        shop_id = json_data['shop_id']
        date = json_data['date']

        Data = {}
        total_income = 0

        sales_header_list = SalesHeaderRepository.SalesHeaderRepository.GetSalesHeaderByYearMonthDate(
            date, shop_id)

        if sales_header_list:
            for sales_header in sales_header_list:
                sales_id = sales_header['sales_id']
                price_change = sales_header['transaction_price_change']
                payment_status = sales_header['payment_status']
                header_income = 0

                if payment_status == "Paid":
                    sales_detail_list = SalesDetailRepository.SalesDetailRepository.GetSalesDetailBySales(
                        sales_id)

                    for sales_detail in sales_detail_list:
                        detail_income = 0

                        sale_price = sales_detail['product_sale_price']
                        amount = sales_detail['amount']
                        detail_income = int(sale_price) * int(amount)
                        header_income = int(
                            header_income) + int(detail_income)

                    header_income = int(
                        header_income) + int(price_change)

                    total_income = int(
                        total_income) + int(header_income)

            result = {"Income": total_income}
            Data["Data"] = result

            return Data
        else:
            return {"status": "Error No Such Sales's Header For the Date"}

    def GetIncomeByYearMonth(json_data):
        shop_id = json_data['shop_id']
        date = json_data['date']

        Data = {}
        total_income = 0

        sales_header_list = SalesHeaderRepository.SalesHeaderRepository.GetSalesHeaderByYearMonth(
            date, shop_id)

        if sales_header_list:
            for sales_header in sales_header_list:
                sales_id = sales_header['sales_id']
                price_change = sales_header['transaction_price_change']
                payment_status = sales_header['payment_status']
                header_income = 0

                if payment_status == "Paid":
                    sales_detail_list = SalesDetailRepository.SalesDetailRepository.GetSalesDetailBySales(
                        sales_id)

                    for sales_detail in sales_detail_list:
                        detail_income = 0

                        sale_price = sales_detail['product_sale_price']
                        amount = sales_detail['amount']
                        detail_income = int(sale_price) * int(amount)
                        header_income = int(
                            header_income) + int(detail_income)

                    header_income = int(
                        header_income) + int(price_change)

                    total_income = int(
                        total_income) + int(header_income)

            result = {"Income": total_income}
            Data["Data"] = result

            return Data
        else:
            return {"status": "Error No Such Sales's Header For the Month"}

    def GetIncomeByYear(json_data):
        shop_id = json_data['shop_id']
        date = json_data['date']

        Data = {}
        total_income = 0

        sales_header_list = SalesHeaderRepository.SalesHeaderRepository.GetSalesHeaderByYear(
            date, shop_id)

        if sales_header_list:
            for sales_header in sales_header_list:
                sales_id = sales_header['sales_id']
                price_change = sales_header['transaction_price_change']
                payment_status = sales_header['payment_status']
                header_income = 0

                if payment_status == "Paid":
                    sales_detail_list = SalesDetailRepository.SalesDetailRepository.GetSalesDetailBySales(
                        sales_id)

                    for sales_detail in sales_detail_list:
                        detail_income = 0

                        sale_price = sales_detail['product_sale_price']
                        amount = sales_detail['amount']
                        detail_income = int(sale_price) * int(amount)
                        header_income = int(
                            header_income) + int(detail_income)

                    header_income = int(
                        header_income) + int(price_change)

                    total_income = int(
                        total_income) + int(header_income)

            result = {"Income": total_income}
            Data["Data"] = result

            return Data
        else:
            return {"status": "Error No Such Sales's Header For the Year"}

    def GetProfitByYearMonthDate(json_data):
        shop_id = json_data['shop_id']
        date = json_data['date']

        Data = {}
        total_profit = 0

        sales_header_list = SalesHeaderRepository.SalesHeaderRepository.GetSalesHeaderByYearMonthDate(
            date, shop_id)

        if sales_header_list:
            for sales_header in sales_header_list:
                sales_id = sales_header['sales_id']
                price_change = sales_header['transaction_price_change']
                payment_status = sales_header['payment_status']
                header_profit = 0

                if payment_status == "Paid":
                    sales_detail_list = SalesDetailRepository.SalesDetailRepository.GetSalesDetailBySales(
                        sales_id)

                    for sales_detail in sales_detail_list:
                        product_detail_id = sales_detail['product_detail_id']
                        detail_profit = 0

                        product_detail = ProductDetailRepository.ProductDetailRepository.GetProductDetailById(
                            product_detail_id)

                        product_price = product_detail[0]['product_purchase_price']
                        sale_price = sales_detail['product_sale_price']
                        amount = sales_detail['amount']
                        detail_profit = (int(sale_price) -
                                         int(product_price)) * int(amount)
                        header_profit = int(
                            header_profit) + int(detail_profit)

                    header_profit = int(
                        header_profit) + int(price_change)

                    total_profit = int(
                        total_profit) + int(header_profit)

            result = {"Profit": total_profit}
            Data["Data"] = result

            return Data
        else:
            return {"status": "Error No Such Sales's Header For the Date"}

    def GetProfitByYearMonth(json_data):
        shop_id = json_data['shop_id']
        date = json_data['date']

        Data = {}
        total_profit = 0

        sales_header_list = SalesHeaderRepository.SalesHeaderRepository.GetSalesHeaderByYearMonth(
            date, shop_id)

        if sales_header_list:
            for sales_header in sales_header_list:
                sales_id = sales_header['sales_id']
                price_change = sales_header['transaction_price_change']
                payment_status = sales_header['payment_status']
                header_profit = 0

                if payment_status == "Paid":
                    sales_detail_list = SalesDetailRepository.SalesDetailRepository.GetSalesDetailBySales(
                        sales_id)

                    for sales_detail in sales_detail_list:
                        product_detail_id = sales_detail['product_detail_id']
                        detail_profit = 0

                        product_detail = ProductDetailRepository.ProductDetailRepository.GetProductDetailById(
                            product_detail_id)

                        product_price = product_detail[0]['product_purchase_price']
                        sale_price = sales_detail['product_sale_price']
                        amount = sales_detail['amount']
                        detail_profit = (int(sale_price) -
                                         int(product_price)) * int(amount)
                        header_profit = int(
                            header_profit) + int(detail_profit)

                    header_profit = int(
                        header_profit) + int(price_change)

                    total_profit = int(
                        total_profit) + int(header_profit)

            result = {"Profit": total_profit}
            Data["Data"] = result

            return Data
        else:
            return {"status": "Error No Such Sales's Header For the Month"}

    def GetProfitByYear(json_data):
        shop_id = json_data['shop_id']
        date = json_data['date']

        Data = {}
        total_profit = 0

        sales_header_list = SalesHeaderRepository.SalesHeaderRepository.GetSalesHeaderByYear(
            date, shop_id)

        if sales_header_list:
            for sales_header in sales_header_list:
                sales_id = sales_header['sales_id']
                price_change = sales_header['transaction_price_change']
                payment_status = sales_header['payment_status']
                header_profit = 0

                if payment_status == "Paid":
                    sales_detail_list = SalesDetailRepository.SalesDetailRepository.GetSalesDetailBySales(
                        sales_id)

                    for sales_detail in sales_detail_list:
                        product_detail_id = sales_detail['product_detail_id']
                        detail_profit = 0

                        product_detail = ProductDetailRepository.ProductDetailRepository.GetProductDetailById(
                            product_detail_id)

                        product_price = product_detail[0]['product_purchase_price']
                        sale_price = sales_detail['product_sale_price']
                        amount = sales_detail['amount']
                        detail_profit = (int(sale_price) -
                                         int(product_price)) * int(amount)
                        header_profit = int(
                            header_profit) + int(detail_profit)

                    header_profit = int(
                        header_profit) + int(price_change)

                    total_profit = int(
                        total_profit) + int(header_profit)

            result = {"Profit": total_profit}
            Data["Data"] = result

            return Data
        else:
            return {"status": "Error No Such Sales's Header For the Year"}

    def GetDebtByYearMonthDate(json_data):
        shop_id = json_data['shop_id']
        date = json_data['date']

        Data = {}
        total_debt = 0

        purchase_header_list = PurchaseHeaderRepository.PurchaseHeaderRepository.GetPurchaseHeaderByYearMonthDate(
            date, shop_id)

        if purchase_header_list:
            for purchase_header in purchase_header_list:
                purchase_id = purchase_header['purchase_id']
                price_change = purchase_header['transaction_price_change']
                payment_status = purchase_header['payment_status']
                header_debt = 0

                if payment_status == "Unpaid":
                    purchase_detail_list = PurchaseDetailRepository.PurchaseDetailRepository.GetPurchaseDetailByPurchase(
                        purchase_id)

                    for purchase_detail in purchase_detail_list:
                        product_detail_id = purchase_detail['product_detail_id']
                        detail_debt = 0

                        product_detail = ProductDetailRepository.ProductDetailRepository.GetProductDetailById(
                            product_detail_id)

                        product_price = product_detail[0]['product_purchase_price']
                        amount = purchase_detail['amount']
                        detail_debt = int(product_price) * int(amount)
                        header_debt = int(header_debt) + int(detail_debt)

                    header_debt = int(header_debt) + int(price_change)

                    total_debt = int(total_debt) + int(header_debt)

            result = {"Debt": total_debt}
            Data["Data"] = result

            return Data
        else:
            return {"status": "Error No Such Purchase's Header For the Date"}

    def GetDebtByYearMonth(json_data):
        shop_id = json_data['shop_id']
        date = json_data['date']

        Data = {}
        total_debt = 0

        purchase_header_list = PurchaseHeaderRepository.PurchaseHeaderRepository.GetPurchaseHeaderByYearMonth(
            date, shop_id)

        if purchase_header_list:
            for purchase_header in purchase_header_list:
                purchase_id = purchase_header['purchase_id']
                price_change = purchase_header['transaction_price_change']
                payment_status = purchase_header['payment_status']
                header_debt = 0

                if payment_status == "Unpaid":
                    purchase_detail_list = PurchaseDetailRepository.PurchaseDetailRepository.GetPurchaseDetailByPurchase(
                        purchase_id)

                    for purchase_detail in purchase_detail_list:
                        product_detail_id = purchase_detail['product_detail_id']
                        detail_debt = 0

                        product_detail = ProductDetailRepository.ProductDetailRepository.GetProductDetailById(
                            product_detail_id)

                        product_price = product_detail[0]['product_purchase_price']
                        amount = purchase_detail['amount']
                        detail_debt = int(product_price) * int(amount)
                        header_debt = int(header_debt) + int(detail_debt)

                    header_debt = int(header_debt) + int(price_change)

                    total_debt = int(total_debt) + int(header_debt)

            result = {"Debt": total_debt}
            Data["Data"] = result

            return Data
        else:
            return {"status": "Error No Such Purchase's Header For the Month"}

    def GetDebtByYear(json_data):
        shop_id = json_data['shop_id']
        date = json_data['date']

        Data = {}
        total_debt = 0

        purchase_header_list = PurchaseHeaderRepository.PurchaseHeaderRepository.GetPurchaseHeaderByYear(
            date, shop_id)

        if purchase_header_list:
            for purchase_header in purchase_header_list:
                purchase_id = purchase_header['purchase_id']
                price_change = purchase_header['transaction_price_change']
                payment_status = purchase_header['payment_status']
                header_debt = 0

                if payment_status == "Unpaid":
                    purchase_detail_list = PurchaseDetailRepository.PurchaseDetailRepository.GetPurchaseDetailByPurchase(
                        purchase_id)

                    for purchase_detail in purchase_detail_list:
                        product_detail_id = purchase_detail['product_detail_id']
                        detail_debt = 0

                        product_detail = ProductDetailRepository.ProductDetailRepository.GetProductDetailById(
                            product_detail_id)

                        product_price = product_detail[0]['product_purchase_price']
                        amount = purchase_detail['amount']
                        detail_debt = int(product_price) * int(amount)
                        header_debt = int(header_debt) + int(detail_debt)

                    header_debt = int(header_debt) + int(price_change)

                    total_debt = int(total_debt) + int(header_debt)

            result = {"Debt": total_debt}
            Data["Data"] = result

            return Data
        else:
            return {"status": "Error No Such Purchase's Header For the Year"}

    def GetRecievableByYearMonthDate(json_data):
        shop_id = json_data['shop_id']
        date = json_data['date']

        Data = {}
        total_recievable = 0

        sales_header_list = SalesHeaderRepository.SalesHeaderRepository.GetSalesHeaderByYearMonthDate(
            date, shop_id)

        if sales_header_list:
            for sales_header in sales_header_list:
                sales_id = sales_header['sales_id']
                price_change = sales_header['transaction_price_change']
                payment_status = sales_header['payment_status']
                header_recievable = 0

                if payment_status == "Unpaid":
                    sales_detail_list = SalesDetailRepository.SalesDetailRepository.GetSalesDetailBySales(
                        sales_id)

                    for sales_detail in sales_detail_list:
                        detail_recievable = 0

                        sale_price = sales_detail['product_sale_price']
                        amount = sales_detail['amount']
                        detail_recievable = int(sale_price) * int(amount)
                        header_recievable = int(
                            header_recievable) + int(detail_recievable)

                    header_recievable = int(
                        header_recievable) + int(price_change)

                    total_recievable = int(
                        total_recievable) + int(header_recievable)

            result = {"Recievable": total_recievable}
            Data["Data"] = result

            return Data
        else:
            return {"status": "Error No Such Sales's Header For the Date"}

    def GetRecievableByYearMonth(json_data):
        shop_id = json_data['shop_id']
        date = json_data['date']

        Data = {}
        total_recievable = 0

        sales_header_list = SalesHeaderRepository.SalesHeaderRepository.GetSalesHeaderByYearMonth(
            date, shop_id)

        if sales_header_list:
            for sales_header in sales_header_list:
                sales_id = sales_header['sales_id']
                price_change = sales_header['transaction_price_change']
                payment_status = sales_header['payment_status']
                header_recievable = 0

                if payment_status == "Unpaid":
                    sales_detail_list = SalesDetailRepository.SalesDetailRepository.GetSalesDetailBySales(
                        sales_id)

                    for sales_detail in sales_detail_list:
                        detail_recievable = 0

                        sale_price = sales_detail['product_sale_price']
                        amount = sales_detail['amount']
                        detail_recievable = int(sale_price) * int(amount)
                        header_recievable = int(
                            header_recievable) + int(detail_recievable)

                    header_recievable = int(
                        header_recievable) + int(price_change)

                    total_recievable = int(
                        total_recievable) + int(header_recievable)

            result = {"Recievable": total_recievable}
            Data["Data"] = result

            return Data
        else:
            return {"status": "Error No Such Sales's Header For the Month"}

    def GetRecievableByYear(json_data):
        shop_id = json_data['shop_id']
        date = json_data['date']

        Data = {}
        total_recievable = 0

        sales_header_list = SalesHeaderRepository.SalesHeaderRepository.GetSalesHeaderByYear(
            date, shop_id)

        if sales_header_list:
            for sales_header in sales_header_list:
                sales_id = sales_header['sales_id']
                price_change = sales_header['transaction_price_change']
                payment_status = sales_header['payment_status']
                header_recievable = 0

                if payment_status == "Unpaid":
                    sales_detail_list = SalesDetailRepository.SalesDetailRepository.GetSalesDetailBySales(
                        sales_id)

                    for sales_detail in sales_detail_list:
                        detail_recievable = 0

                        sale_price = sales_detail['product_sale_price']
                        amount = sales_detail['amount']
                        detail_recievable = int(sale_price) * int(amount)
                        header_recievable = int(
                            header_recievable) + int(detail_recievable)

                    header_recievable = int(
                        header_recievable) + int(price_change)

                    total_recievable = int(
                        total_recievable) + int(header_recievable)

            result = {"Recievable": total_recievable}
            Data["Data"] = result

            return Data
        else:
            return {"status": "Error No Such Sales's Header For the Year"}

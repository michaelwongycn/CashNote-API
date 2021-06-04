import json
from flask import Flask, request

import Handler.AccountHandler as AccountHandler
import Handler.ShopHandler as ShopHandler
import Handler.ProductHandler as ProductHandler
import Handler.ProductDetailHandler as ProductDetailHandler
import Handler.SupplierHandler as SupplierHandler
import Handler.PurchaseHeaderHandler as PurchaseHeaderHandler
import Handler.PurchaseDetailHandler as PurchaseDetailHandler
import Handler.SalesHeaderHandler as SalesHeaderHandler
import Handler.SalesDetailHandler as SalesDetailHandler


app = Flask(__name__)


@app.route('/', methods=['POST'])
def Home():
    return "CashNote API"


@app.route('/ShopRegister', methods=['POST'])
def ShopRegister():
    json_data = request.get_json()

    response = ShopHandler.ShopHandler.RegisterNewShop(json_data)

    if response:
        return json.dumps(response)
    else:
        return "Username Already Taken"


@app.route('/Login', methods=['POST'])
def Login():
    json_data = request.get_json()

    response = AccountHandler.AccountHandler.Login(json_data)

    if response:
        return json.dumps(response)
    else:
        return "Wrong Credential"


@app.route('/CreateSales', methods=['POST'])
def CreateSales():
    json_data = request.get_json()

    response = SalesHeaderHandler.SalesHeaderHandler.RegisterSalesHeader(
        json_data)

    if response:
        return json.dumps(response)
    else:
        return "Error Creating Sales"


@app.route('/CreateSalesDetail', methods=['POST'])
def CreateSalesDetail():
    json_data = request.get_json()

    response = SalesDetailHandler.SalesDetailHandler.RegisterSalesDetail(
        json_data)

    if response:
        return json.dumps(response)
    else:
        return "Error Creating Sales Detail"


@app.route('/CreatePurchase', methods=['POST'])
def CreatePurchase():
    json_data = request.get_json()

    response = PurchaseHeaderHandler.PurchaseHeaderHandler.RegisterPurhcaseHeader(
        json_data)

    if response:
        return json.dumps(response)
    else:
        return "Error Creating Purchase"


@app.route('/CreatePurchaseDetail', methods=['POST'])
def CreatePurchaseDetail():
    json_data = request.get_json()

    response = PurchaseDetailHandler.PurchaseDetailHandler.RegisterPurchaseDetail(
        json_data)

    if response:
        return json.dumps(response)
    else:
        return "Error Creating Purchase Detail"


@app.route('/ChangeSalesToPaid', methods=['POST'])
def ChangeSalesToPaid():
    json_data = request.get_json()

    response = SalesHeaderHandler.SalesHeaderHandler.SetPaymentToPaid(
        json_data)

    if response:
        return json.dumps(response)
    else:
        return "Error Changing Payment Status"


@app.route('/GetSalesHeader', methods=['POST'])
def GetSalesHeader():
    json_data = request.get_json()

    response = SalesHeaderHandler.SalesHeaderHandler.GetSalesHeaderByShop(
        json_data)

    if response:
        return json.dumps(response)
    else:
        return "Error Fetching Sales"


@app.route('/GetSalesDetail', methods=['POST'])
def GetSalesDetail():
    json_data = request.get_json()

    response = SalesDetailHandler.SalesDetailHandler.GetSalesDetailBySales(
        json_data)

    if response:
        return json.dumps(response)
    else:
        return "Error Fetching Sales Detail"


@app.route('/DeleteSales', methods=['POST'])
def DeleteSales():
    json_data = request.get_json()

    response = SalesHeaderHandler.SalesHeaderHandler.DeleteSalesHeader(
        json_data)

    if response:
        return json.dumps(response)
    else:
        return "Error Deleting Sales"


@app.route('/DeleteSalesDetail', methods=['POST'])
def DeleteSalesDetail():
    json_data = request.get_json()

    response = SalesDetailHandler.SalesDetailHandler.DeleteUniqueSalesDetail(
        json_data)

    if response:
        return json.dumps(response)
    else:
        return "Error Deleting Sales Detail"


@app.route('/ChangePurchaseToPaid', methods=['POST'])
def ChangePurchaseToPaid():
    json_data = request.get_json()

    response = PurchaseHeaderHandler.PurchaseHeaderHandler.SetPaymentToPaid(
        json_data)

    if response:
        return json.dumps(response)
    else:
        return "Error Changing Payment Status"


@app.route('/GetPurchaseHeader', methods=['POST'])
def GetPurchaseHeader():
    json_data = request.get_json()

    response = PurchaseHeaderHandler.PurchaseHeaderHandler.GetPurchaseHeaderByShop(
        json_data)

    if response:
        return json.dumps(response)
    else:
        return "Error Fetching Purchase"


@app.route('/GetPurchaseDetail', methods=['POST'])
def GetPurchaseDetail():
    json_data = request.get_json()

    response = PurchaseDetailHandler.PurchaseDetailHandler.GetPurchaseDetailByPurchase(
        json_data)

    if response:
        return json.dumps(response)
    else:
        return "Error Fetching Purchase Detail"


@app.route('/DeletePurchase', methods=['POST'])
def DeletePurchase():
    json_data = request.get_json()

    response = PurchaseHeaderHandler.PurchaseHeaderHandler.DeletePurchaseHeader(
        json_data)

    if response:
        return json.dumps(response)
    else:
        return "Error Deleting Purchase"


@app.route('/DeletePurchaseDetail', methods=['POST'])
def DeletePurchaseDetail():
    json_data = request.get_json()

    response = PurchaseDetailHandler.PurchaseDetailHandler.DeleteUniquePurchaseDetail(
        json_data)

    if response:
        return json.dumps(response)
    else:
        return "Error Deleting Purchase Detail"


@app.route('/CreateSupplier', methods=['POST'])
def CreateSupplier():
    json_data = request.get_json()

    response = SupplierHandler.SupplierHandler.AddSupplier(json_data)

    if response:
        return json.dumps(response)
    else:
        return "Error Adding Supplier"


@app.route('/GetSupplier', methods=['POST'])
def GetSupplier():
    json_data = request.get_json()

    response = SupplierHandler.SupplierHandler.GetSupplierByShop(json_data)

    if response:
        return json.dumps(response)
    else:
        return "Error Fetching Supplier"


@app.route('/DeleteSupplier', methods=['POST'])
def DeleteSupplier():
    json_data = request.get_json()

    response = SupplierHandler.SupplierHandler.DeleteSupplier(json_data)

    if response:
        return json.dumps(response)
    else:
        return "Error Deleting Supplier"


@app.route('/CreateAdmin', methods=['POST'])
def CreateAdmin():
    json_data = request.get_json()

    response = AccountHandler.AccountHandler.RegisterNewAdmin(json_data)

    if response:
        return json.dumps(response)
    else:
        return "Error Adding Admin"


@app.route('/GetAdmin', methods=['POST'])
def GetAdmin():
    json_data = request.get_json()

    response = AccountHandler.AccountHandler.GetAccountByShop(json_data)

    if response:
        return json.dumps(response)
    else:
        return "Error Fetching Admin"


@app.route('/DeleteAdmin', methods=['POST'])
def DeleteAdmin():
    json_data = request.get_json()

    response = AccountHandler.AccountHandler.RemoveAdmin(json_data)

    if response:
        return json.dumps(response)
    else:
        return "Error Deleting Admin"


@app.route('/CreateProduct', methods=['POST'])
def CreateProduct():
    json_data = request.get_json()

    response = ProductHandler.ProductHandler.AddProduct(json_data)

    if response:
        return json.dumps(response)
    else:
        return "Error Adding Product"


@app.route('/CreateProductDetail', methods=['POST'])
def CreateProductDetail():
    json_data = request.get_json()

    response = ProductDetailHandler.ProductDetailHandler.AddProduct(json_data)

    if response:
        return json.dumps(response)
    else:
        return "Error Adding Product"


@app.route('/GetProduct', methods=['POST'])
def GetProduct():
    json_data = request.get_json()

    response = ProductHandler.ProductHandler.GetProductByShop(json_data)

    if response:
        return json.dumps(response)
    else:
        return "Error Fetching Product"


@app.route('/GetProductDetail', methods=['POST'])
def GetProducDetail():
    json_data = request.get_json()

    response = ProductDetailHandler.ProductDetailHandler.GetProductDetailByProduct(
        json_data)

    if response:
        return json.dumps(response)
    else:
        return "Error Fetching Product Detail"


@app.route('/UpdateProduct', methods=['POST'])
def UpdateProduct():
    json_data = request.get_json()

    response = ProductHandler.ProductHandler.UpdateProduct(json_data)

    if response:
        return json.dumps(response)
    else:
        return "Error Updating Product"


@app.route('/UpdateProductDetail', methods=['POST'])
def UpdateProductDetail():
    json_data = request.get_json()

    response = ProductDetailHandler.ProductDetailHandler.UpdateProductDetail(
        json_data)

    if response:
        return json.dumps(response)
    else:
        return "Error Updating Product Detail"


@app.route('/DeleteProduct', methods=['POST'])
def DeleteProduct():
    json_data = request.get_json()

    response = ProductHandler.ProductHandler.DeleteProduct(json_data)

    if response:
        return json.dumps(response)
    else:
        return "Error Deleting Product"


@app.route('/DeleteProductDetail', methods=['POST'])
def DeleteProductDetail():
    json_data = request.get_json()

    response = ProductDetailHandler.ProductDetailHandler.DeleteProductDetail(
        json_data)

    if response:
        return json.dumps(response)
    else:
        return "Error Deleting Product Detail"

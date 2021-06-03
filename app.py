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


@app.route('/', methods=['GET'])
def Home():
    return "CashNote API"


@app.route('/ShopRegister', methods=['GET'])
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


@app.route('/CreateSales', methods=['GET'])
def CreateSales():
    json_data = request.get_json()

    response = SalesHeaderHandler.SalesHeaderHandler.RegisterSalesHeader(
        json_data)

    if response:
        return json.dumps(response)
    else:
        return "Error Creating Sales"


@app.route('/CreateSalesDetail', methods=['GET'])
def CreateSalesDetail():
    json_data = request.get_json()

    response = SalesDetailHandler.SalesDetailHandler.RegisterSalesDetail(
        json_data)

    if response:
        return json.dumps(response)
    else:
        return "Error Creating Sales Detail"


@app.route('/CreatePurchase', methods=['GET'])
def CreatePurchase():
    json_data = request.get_json()

    response = PurchaseHeaderHandler.PurchaseHeaderHandler.RegisterPurhcaseHeader(
        json_data)

    if response:
        return json.dumps(response)
    else:
        return "Error Creating Purchase"


@app.route('/CreatePurchaseDetail', methods=['GET'])
def CreatePurchaseDetail():
    json_data = request.get_json()

    response = PurchaseDetailHandler.PurchaseDetailHandler.RegisterPurchaseDetail(
        json_data)

    if response:
        return json.dumps(response)
    else:
        return "Error Creating Purchase Detail"


@app.route('/ChangeSalesToPaid', methods=['GET'])
def ChangeSalesToPaid():
    json_data = request.get_json()

    response = SalesHeaderHandler.SalesHeaderHandler.SetPaymentToPaid(
        json_data)

    if response:
        return json.dumps(response)
    else:
        return "Error Changing Payment Status"


@app.route('/GetSalesHeader', methods=['GET'])
def GetSalesHeader():
    json_data = request.get_json()

    response = SalesHeaderHandler.SalesHeaderHandler.GetSalesHeaderByShop(
        json_data)

    if response:
        return json.dumps(response)
    else:
        return "Error Fetching Sales"


@app.route('/GetSalesDetail', methods=['GET'])
def GetSalesDetail():
    json_data = request.get_json()

    response = SalesDetailHandler.SalesDetailHandler.GetSalesDetailBySales(
        json_data)

    if response:
        return json.dumps(response)
    else:
        return "Error Fetching Sales Detail"


@app.route('/DeleteSales', methods=['GET'])
def DeleteSales():
    json_data = request.get_json()

    response = SalesHeaderHandler.SalesHeaderHandler.DeleteSalesHeader(
        json_data)

    if response:
        return json.dumps(response)
    else:
        return "Error Deleting Sales"


@app.route('/DeleteSalesDetail', methods=['GET'])
def DeleteSalesDetail():
    json_data = request.get_json()

    response = SalesDetailHandler.SalesDetailHandler.DeleteUniqueSalesDetail(
        json_data)

    if response:
        return json.dumps(response)
    else:
        return "Error Deleting Sales Detail"


@app.route('/ChangePurchaseToPaid', methods=['GET'])
def ChangePurchaseToPaid():
    json_data = request.get_json()

    response = PurchaseHeaderHandler.PurchaseHeaderHandler.SetPaymentToPaid(
        json_data)

    if response:
        return json.dumps(response)
    else:
        return "Error Changing Payment Status"


@app.route('/GetPurchaseHeader', methods=['GET'])
def GetPurchaseHeader():
    json_data = request.get_json()

    response = PurchaseHeaderHandler.PurchaseHeaderHandler.GetPurchaseHeaderByShop(
        json_data)

    if response:
        return json.dumps(response)
    else:
        return "Error Fetching Purchase"


@app.route('/GetPurchaseDetail', methods=['GET'])
def GetPurchaseDetail():
    json_data = request.get_json()

    response = PurchaseDetailHandler.PurchaseDetailHandler.GetPurchaseDetailByPurchase(
        json_data)

    if response:
        return json.dumps(response)
    else:
        return "Error Fetching Purchase Detail"


@app.route('/DeletePurchase', methods=['GET'])
def DeletePurchase():
    json_data = request.get_json()

    response = PurchaseHeaderHandler.PurchaseHeaderHandler.DeletePurchaseHeader(
        json_data)

    if response:
        return json.dumps(response)
    else:
        return "Error Deleting Purchase"


@app.route('/DeletePurchaseDetail', methods=['GET'])
def DeletePurchaseDetail():
    json_data = request.get_json()

    response = PurchaseDetailHandler.PurchaseDetailHandler.DeleteUniquePurchaseDetail(
        json_data)

    if response:
        return json.dumps(response)
    else:
        return "Error Deleting Purchase Detail"


@app.route('/CreateSupplier', methods=['GET'])
def CreateSupplier():
    json_data = request.get_json()

    response = SupplierHandler.SupplierHandler.AddSupplier(json_data)

    if response:
        return json.dumps(response)
    else:
        return "Error Adding Supplier"


@app.route('/GetSupplier', methods=['GET'])
def GetSupplier():
    json_data = request.get_json()

    response = SupplierHandler.SupplierHandler.GetSupplierByShop(json_data)

    if response:
        return json.dumps(response)
    else:
        return "Error Fetching Supplier"


@app.route('/DeleteSupplier', methods=['GET'])
def DeleteSupplier():
    json_data = request.get_json()

    response = SupplierHandler.SupplierHandler.DeleteSupplier(json_data)

    if response:
        return json.dumps(response)
    else:
        return "Error Deleting Supplier"


@app.route('/CreateAdmin', methods=['GET'])
def CreateAdmin():
    json_data = request.get_json()

    response = AccountHandler.AccountHandler.RegisterNewAdmin(json_data)

    if response:
        return json.dumps(response)
    else:
        return "Error Adding Admin"


@app.route('/GetAdmin', methods=['GET'])
def GetAdmin():
    json_data = request.get_json()

    response = AccountHandler.AccountHandler.GetAccountByShop(json_data)

    if response:
        return json.dumps(response)
    else:
        return "Error Fetching Admin"


@app.route('/DeleteAdmin', methods=['GET'])
def DeleteAdmin():
    json_data = request.get_json()

    response = AccountHandler.AccountHandler.RemoveAdmin(json_data)

    if response:
        return json.dumps(response)
    else:
        return "Error Deleting Admin"


@app.route('/CreateProduct', methods=['GET'])
def CreateProduct():
    json_data = request.get_json()

    response = ProductHandler.ProductHandler.AddProduct(json_data)

    if response:
        return json.dumps(response)
    else:
        return "Error Adding Product"


@app.route('/GetProduct', methods=['GET'])
def GetProduct():
    json_data = request.get_json()

    response = ProductHandler.ProductHandler.GetProductByShop(json_data)

    if response:
        return json.dumps(response)
    else:
        return "Error Fetching Product"


@app.route('/GetProductDetail', methods=['GET'])
def GetProducDetail():
    json_data = request.get_json()

    response = ProductDetailHandler.ProductDetailHandler.GetProductDetailByProduct(
        json_data)

    if response:
        return json.dumps(response)
    else:
        return "Error Fetching Product Detail"


@app.route('/UpdateProduct', methods=['GET'])
def UpdateProduct():
    json_data = request.get_json()

    response = ProductHandler.ProductHandler.UpdateProduct(json_data)

    if response:
        return json.dumps(response)
    else:
        return "Error Updating Product"


@app.route('/UpdateProductDetail', methods=['GET'])
def UpdateProductDetail():
    json_data = request.get_json()

    response = ProductDetailHandler.ProductDetailHandler.UpdateProductDetail(
        json_data)

    if response:
        return json.dumps(response)
    else:
        return "Error Updating Product Detail"


@app.route('/DeleteProduct', methods=['GET'])
def DeleteProduct():
    json_data = request.get_json()

    response = ProductHandler.ProductHandler.DeleteProduct(json_data)

    if response:
        return json.dumps(response)
    else:
        return "Error Deleting Product"


@app.route('/DeleteProductDetail', methods=['GET'])
def DeleteProductDetail():
    json_data = request.get_json()

    response = ProductDetailHandler.ProductDetailHandler.DeleteProductDetail(
        json_data)

    if response:
        return json.dumps(response)
    else:
        return "Error Deleting Product Detail"

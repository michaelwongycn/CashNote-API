import Repository.SupplierRepository as SupplierRepository
import Repository.PurchaseHeaderRepository as PurchaseHeaderRepository
import Repository.ProductDetailRepository as ProductDetailRepository

import Factory.SupplierFactory as SupplierFactory


class SupplierHandler:
    def AddSupplier(json_data):
        shop_id = json_data['shop_id']
        supplier_name = json_data['supplier_name']
        supplier_address = json_data['supplier_address']
        supplier_phone = json_data['supplier_phone']

        supplier = SupplierFactory.SupplierFactory.CreateSupplier(
            shop_id, supplier_name, supplier_address, supplier_phone)

        result = SupplierRepository.SupplierRepository.AddSupplier(supplier)

        if result == "success":

            supplier = {"supplier_id": str(supplier.supplier_id),  "shop_id": str(supplier.shop_id),
                        "supplier_name": str(supplier.supplier_name), "supplier_address": str(supplier.supplier_address),
                        "supplier_phone": str(supplier.supplier_phone), "supplier_status": str(supplier.supplier_status)}

            return supplier
        else:
            return {"status": "Error Registering Supplier"}

    def GetSupplierByShop(json_data):
        shop_id = json_data['shop_id']

        supplier_list = SupplierRepository.SupplierRepository.GetSupplierByShop(
            shop_id)

        if supplier_list:
            Data = {}
            Data["Data"] = supplier_list

            return Data

        else:
            return {"status": "Error No Such Supplier"}

    def GetSupplierById(json_data):
        supplier_id = json_data['supplier_id']

        supplier_list = SupplierRepository.SupplierRepository.GetSupplierById(
            supplier_id)

        if supplier_list:
            Data = {}
            Data["Data"] = supplier_list

            return Data

        else:
            return {"status": "Error No Such Supplier"}

    def UpdateSupplier(json_data):
        supplier_id = json_data['supplier_id']
        supplier_name = json_data['supplier_name']
        supplier_address = json_data['supplier_address']
        supplier_phone = json_data['supplier_phone']

        supplier_list = SupplierRepository.SupplierRepository.GetSupplierById(
            supplier_id)

        if supplier_list:
            result = SupplierRepository.SupplierRepository.UpdateSupplier(
                supplier_id, supplier_name, supplier_address, supplier_phone)

            if result == "success":
                return {"status": "Success"}

            else:
                return {"status": "Error Updating Supplier"}
        else:
            return {"status": "Error Supplier Not Found"}

    def DeleteSupplier(json_data):
        supplier_id = json_data['supplier_id']

        supplier_list = SupplierRepository.SupplierRepository.GetSupplierById(
            supplier_id)

        if supplier_list:
            purchase_header_list = PurchaseHeaderRepository.PurchaseHeaderRepository.GetPurchaseHeaderBySupplier(
                supplier_id)

            if not purchase_header_list:
                product_detail_list = ProductDetailRepository.ProductDetailRepository.GetProductDetailBySupplier(
                    supplier_id)

                if not product_detail_list:
                    result = SupplierRepository.SupplierRepository.DeleteSupplier(
                        supplier_id)

                    if result == "success":
                        return {"status": "Success"}

                    else:
                        return {"status": "Error Deleting Supplier"}
                else:
                    return {"status": "Please Delete Supplier's Product's Detail First"}
            else:
                return {"status": "Please Delete Supplier's Purchase's Header First"}
        else:
            return {"status": "Error Supplier Not Found"}

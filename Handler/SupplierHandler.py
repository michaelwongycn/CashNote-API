import Repository.SupplierRepository as SupplierRepository

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
            return {"status": "Error"}

    def GetSupplierByShop(json_data):
        shop_id = json_data['shop_id']

        supplier_list = SupplierRepository.SupplierRepository.GetSupplierByShop(
            shop_id)

        return supplier_list

    def GetSupplierById(json_data):
        supplier_id = json_data['supplier_id']

        supplier_list = SupplierRepository.SupplierRepository.GetSupplierById(
            supplier_id)

        return supplier_list

    def UpdateSupplier(json_data):
        supplier_id = json_data['supplier_id']
        supplier_name = json_data['supplier_name']
        supplier_address = json_data['supplier_address']
        supplier_phone = json_data['supplier_phone']

        result = SupplierRepository.SupplierRepository.UpdateSupplier(
            supplier_id, supplier_name, supplier_address, supplier_phone)

        if result == "success":
            return {"status": "Success"}
        else:
            return {"status": "Error"}

    def DeleteSupplier(json_data):
        supplier_id = json_data['supplier_id']

        result = SupplierRepository.SupplierRepository.DeleteSupplier(
            supplier_id)

        if result == "success":
            return {"status": "Success"}
        else:
            return {"status": "Error"}

import Model.SupplierModel as SupplierModel
from uuid import uuid1


class SupplierFactory:
    def CreateSupplier(shop_id, supplier_name, supplier_address, supplier_phone):
        suplier_id = uuid1()
        supplier = SupplierModel.Supplier(suplier_id, shop_id, supplier_name,
                                          supplier_address, supplier_phone, "A")
        return supplier

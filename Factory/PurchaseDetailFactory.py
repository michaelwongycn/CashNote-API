import Model.PurchaseDetailModel as PurchaseDetailModel


class PurchaseDetailFactory:
    def CreatePurchaseDetail(purchase_id, product_detail_id, amount):
        purchase_detail = PurchaseDetailModel.PurchaseDetail(
            purchase_id, product_detail_id, amount, "A")
        return purchase_detail

from config import Config, get_config
user_config=get_config()
#так вызыыаем ___init______
cfg=Config(*user_config)
rint=RInt(cfg)
pprint(rint.update_co_ecom_status("142", "18909834227", "PickingDownloaded"))



@fixture(scope="function")
def smth(argument):
    return argument    
@mark.Sveta
@mark.paramatrize('argument', [1, 3])
def test_fixture(argument, smth):
    print(smth)
    assert argument == smth


#с моего файла теста
from pprint import pprint
from pytest import mark, fixture
from api.tsc import TSC
from api.rint import RInt
from api.oms import OMS


@mark.update
@mark.parametrize(
    "target_ecom_status,expected_mfc_status",
    [("PickingDownloaded", "new"), ("CustomerCancelled", "cancelled")],
)
def test_update_to_picking_downloaded(
    cfg, draft_order_with_mixed_reg_items, target_ecom_status, expected_mfc_status
):
    pprint(draft_order_with_mixed_reg_items)
    tsc = TSC(cfg)
    rint = RInt(cfg)
    oms = OMS(cfg)
    order_id = draft_order_with_mixed_reg_items["order-id"]
    location_code_retailer = tsc.get_location_code("location-code-retailer")
   
    co_updated_by_user_answer = input(f"Type 1 if you want to update to PickingDownloaded, "
                                             "type 2 if you want to update to CustomerCancelled: ")
    if co_updated_by_user_answer == "1":
        rint.update_co_ecom_status(location_code_retailer, order_id, "PickingDownloaded")
        order_status = oms.get_co(order_id)["response"]["status"]
        assert order_status == "new"
    if co_updated_by_user_answer == "2":
        rint.update_co_ecom_status(location_code_retailer, order_id, "CustomerCancelled")
        order_status = oms.get_co(order_id)["response"]["status"]
        assert order_status == "cancelled"


#c RINT file
        def update_co_ecom_status(self, location_code_retailer:str, order_id: str, target_status:str ):
        url = self.base_url + "v4/common/update-customer-order-ecom-status"
        body = {
            "mfc-id": location_code_retailer,
            "ecom-order-id": order_id,
            "ecom-order-status": target_status,
            "ecom-payment-status": ""
                }
        response = requests.post(
            url=url,
            json=body,
            headers=self.default_headers
        )
        pprint(response.json())
        response.raise_for_status()
        return response.json()



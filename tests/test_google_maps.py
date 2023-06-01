from requests import Response
import json
from utils.checking import Checking
from utils.api import Google_maps_api
import allure

@allure.epic("Test create new location")
class Test_create_place():
    @allure.description("Test create,update,delete new location")
    def test_create_new_place(self):
        print("method post")
        result_post = Google_maps_api.create_new_place()  # вызываем экземпляр класса и внутри него вызываем метод
        check_post = result_post.json()
        place_id = check_post.get("place_id")        # return value place_id from post body
        Checking.check_status_code(result_post, 200)
        # Checking.check_json_value(result_post, 'status','OK')
        # token = json.loads(result_post.text)
        # Checking.check_json_token(result_post, ['status', 'place_id', 'scope', 'reference', 'id'])
        print(result_post.status_code)

        print("method get post")
        result_get = Google_maps_api.get_new_place(place_id)
        Checking.check_status_code(result_get, 200)
        #token = json.loads(result_get.text)
        #Checking.check_json_token(result_get,
        # ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])
        Checking.check_json_value(result_get, 'address', '29, side layout, cohen 09')

        print("method put")
        result_put = Google_maps_api.put_new_place(place_id)
        Checking.check_status_code(result_put, 200)
        Checking.check_json_token(result_put,["msg"]) # msg - show what we should get in response from server

        print("method get put")
        result_get = Google_maps_api.get_new_place(place_id)
        Checking.check_status_code(result_get, 200)
        Checking.check_json_value(result_put, 'msg', 'Address successfully updated')
        Checking.check_json_value(result_get, 'address','100 Lenina street, RU')

        print("method delete")
        result_delete = Google_maps_api.delete_new_place(place_id)
        Checking.check_status_code(result_delete, 200)
        Checking.check_json_token(result_delete, ["status"])
        Checking.check_json_value(result_delete, 'status', 'OK')

        print("method get delete")
        result_get = Google_maps_api.get_new_place(place_id)
        Checking.check_status_code(result_get, 404)
        Checking.check_json_token(result_get, ["msg"])
        Checking.check_json_value(result_delete, 'status', 'OK')
        #Checking.check_json_search_word_in_value(result_get, 'msg',"failed")
        Checking.check_json_value(result_get,'msg', "Get operation failed, looks like place_id  doesn't exists")

        print("Testing is finished succesfull")











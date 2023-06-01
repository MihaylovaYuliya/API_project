import requests
import json
"""Methods for checking answers from server"""
class Checking():
    """Method for checking status code"""
    @staticmethod
    def check_status_code(result, status_code):
       assert status_code == result.status_code
       print("Sucess!!! Status code = " + str(result.status_code))

    """Method for checking mandatory fields"""

    @staticmethod
    def check_json_token(result, expected_value):
        token = json.loads(result.text)      # распарсить
        assert list(token) == expected_value # get all values for all mandatory fields
        print("all fields are represented")

    @staticmethod
    def check_json_value(result, field_name, expected_value):
        check = result.json()
        check_info = check.get(field_name)
        assert check_info == expected_value
        print(field_name + " correct !!!")

    """Метод для проверки значений обязательных полей в ответе запроса по заданному слову"""

    @staticmethod
    def check_json_search_word_in_value(result, field_name, search_word):
        check = result.json()
        check_info = check.get(field_name)
        if search_word in check_info:
            print(f'Word {search_word} exist!!!')
        else:
            print(f'Word {search_word} not founded')
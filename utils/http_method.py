import allure
import requests
from utils.logger import Logger

"""Lists HTTP methods"""
class Http_methods:
    headers = { 'Content-Type': 'applications/json'}
    cookie = ""

    @staticmethod   # метод не привязан к классу можем вызывать где угодно
    def get(url):
        with allure.step("GET"):
            Logger.add_request(url, method= 'GET')
            result = requests.get(url,headers=Http_methods.headers,cookies=Http_methods.cookie)
            Logger.add_response(result)
            return result

    @staticmethod  # метод не привязан к классу можем вызывать где угодно
    def post(url, body):
        with allure.step("POST"):
            Logger.add_request(url, method='POST')
            result = requests.post(url,json=body, headers=Http_methods.headers, cookies=Http_methods.cookie)
            Logger.add_response(result)
            return result

    @staticmethod  # метод не привязан к классу можем вызывать где угодно
    def put(url, body):
        with allure.step("PUT"):
            Logger.add_request(url, method='PUT')
            result = requests.put(url, json=body, headers=Http_methods.headers, cookies=Http_methods.cookie)
            Logger.add_response(result)
            return result

    @staticmethod  # метод не привязан к классу можем вызывать где угодно
    def delete(url,body):
        with allure.step("DELETE"):
            Logger.add_request(url, method='DELETE')
            result = requests.delete(url, json=body, headers=Http_methods.headers, cookies=Http_methods.cookie)
            Logger.add_response(result)
            return result

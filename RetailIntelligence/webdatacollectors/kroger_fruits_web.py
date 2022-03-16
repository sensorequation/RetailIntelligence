import os
import requests
import json
from addict import Dict
from extract import json_extract
from datetime import date
from kroger_curl_details import *


def fetch_data_page1():

    response_page1 = requests.get('https://www.kroger.com/atlas/v1/product/v2/products', headers=headers, params=params_page1)

    data_fetched_page1 = response_page1.json()

    # print(data_fetched_page1)

    return data_fetched_page1


def fetch_data_page2():

    response_page2 = requests.get('https://www.kroger.com/atlas/v1/product/v2/products', headers=headers, params=params_page2)

    data_fetched_page2 = response_page2.json()

    # print(data_fetched_page2)

    return data_fetched_page2


def fetch_data_page3():
    response_page3 = requests.get('https://www.kroger.com/atlas/v1/product/v2/products', headers=headers, params=params_page3)

    data_fetched_page3 = response_page3.json()

    # print(data_fetched_page3)

    return data_fetched_page3


def fetch_data_page4():

    response_page4 = requests.get('https://www.kroger.com/atlas/v1/product/v2/products', headers=headers, params=params_page4)

    data_fetched_page4 = response_page4.json()

    # print(data_fetched_page4)

    return data_fetched_page4


def fetch_data_page5():

    response_page5 = requests.get('https://www.kroger.com/atlas/v1/product/v2/products', headers=headers, params=params_page5)

    data_fetched_page5 = response_page5.json()

    # print(data_fetched_page5)

    return data_fetched_page5


def store_data():

    today = str(date.today())

    json_dump_first_page = json.dumps(fetch_data_page1())
    with open("data/kroger/kroger_fruits/"+today+".json", "w") as outfile:
        outfile.write(json_dump_first_page)

    json_dump_second_page = json.dumps(fetch_data_page2())
    with open("data/kroger/kroger_fruits/"+today+".json", "a") as outfile:
        outfile.write(json_dump_second_page)

    json_dump_third_page = json.dumps(fetch_data_page3())
    with open("data/kroger/kroger_fruits/"+today+".json", "a") as outfile:
        outfile.write(json_dump_third_page)

    json_dump_forth_page = json.dumps(fetch_data_page4())
    with open("data/kroger/kroger_fruits/"+today+".json", "a") as outfile:
        outfile.write(json_dump_forth_page)

    json_dump_fifth_page = json.dumps(fetch_data_page5())
    with open("data/kroger/kroger_fruits/"+today+".json", "a") as outfile:
        outfile.write(json_dump_fifth_page)

    print('### '+today+'- All Data Stored ###')


store_data()


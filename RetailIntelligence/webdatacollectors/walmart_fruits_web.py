from addict import Dict
from extract import json_extract
import requests
import json
from walmart_curl_details import *
from datetime import date


def fetch_data_first_products():

    response_first_products = requests.post('https://www.walmart.ca/api/bsp/carousel/spr', headers=headers, params=params_first_products, cookies=cookies_first_products, json=json_data_first_products)

    fetch_first_products_json = response_first_products.json()

    # print(fetch_first_products_json)

    return fetch_first_products_json


def fetch_data_product():

    response_fetch_product = requests.post('https://www.walmart.ca/api/bsp/fetch-products', headers=headers, cookies=cookies_fetch_products, json=json_data_fetch_products)

    fetch_product_json = response_fetch_product.json()

    # print(fetch_product_json)

    return fetch_product_json


def fetch_data_price():

    response_fetch_price = requests.post('https://www.walmart.ca/api/bsp/v2/price-offer', headers=headers, cookies=cookies_fetch_price, json=json_data_fetch_price)

    fetch_price_json = response_fetch_price.json()

    # print(fetch_price_json)

    return fetch_price_json


def store_data():

    today = str(date.today())

    json_dump_first_products = json.dumps(fetch_data_first_products())
    with open("data/walmart/walmart_fruits/"+today+"_fp"+".json", "w") as outfile:
        outfile.write(json_dump_first_products)

    json_dump_products = json.dumps(fetch_data_product())
    with open("data/walmart/walmart_fruits/"+today+"_product"+".json", "w") as outfile:
        outfile.write(json_dump_products)

    json_dump_price = json.dumps(fetch_data_price())
    with open("data/walmart/walmart_fruits/"+today+"_price"+".json", "w") as outfile:
        outfile.write(json_dump_price)

    print('### '+today+'- All Data Stored ###')


store_data()

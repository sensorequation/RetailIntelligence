import json
import requests
from extract import json_extract
from addict import Dict
from datetime import date


for i in range(0, 6):
    def fetch_data():

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:97.0) Gecko/20100101 Firefox/97.0',
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'Origin': 'https://www.meijer.com',
            'Connection': 'keep-alive',
            'Referer': 'https://www.meijer.com/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'cross-site',
            'TE': 'trailers',
        }

        params = (
            ('c', 'ciojs-client-2.15.0'),
            ('key', 'key_GdYuTcnduTUtsZd6'),
            ('i', '2799e664-7630-4157-a8a7-1c66b8722d79'),
            ('s', '2'),
            ('us', 'web'),
            ('page', i+1),
            ('filters[availableInStores]', '20'),
            ('sort_by', 'relevance'),
            ('sort_order', 'descending'),
            ('fmt_options[groups_max_depth]', '3'),
            ('fmt_options[groups_start]', 'current'),
            ('_dt', '1645543509718'),
        )

        response = requests.get('https://ac.cnstrc.com/browse/group_id/L3-3197', headers=headers, params=params)
        data_fetched = response.json()
        return data_fetched


    def store_data():

        today = str(date.today())
        page_number = str(i+1)
        json_dump = json.dumps(fetch_data())
        with open("data/meijer/meijer_fruits/" + today + "_" + page_number + ".json", "w") as outfile:
            outfile.write(json_dump)


    store_data()

date = str(date.today())
print('### ' + date + '- All Data Stored ###')

import requests
import json
import csv
import re
import pandas as pd
import time 
HEADERS = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}

def get_cat():
    
    product_per_page_link = f"https://tiki.vn/api/personalish/v1/blocks/listings?limit=40&include=advertisement&aggregations=2&trackity_id=369db117-5d0a-53e7-8e3e-1f0f27aec791&category=316&page=1&urlKey=sach-truyen-tieng-viet"
    response  = requests.get(product_per_page_link, headers=HEADERS)
    categories = json.loads(response.text)['filters'][0]['values']
    categories_list = []
    for i in range(1, len(categories)):
        categories_list.append({'name':categories[i]['display_value'], 'id':categories[i]['query_value']})
        

       
    return categories_list



def main():
    print(get_cat())
if __name__ == "__main__":
    main()

    
   
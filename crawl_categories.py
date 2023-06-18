import requests
import json
import csv
import re
import pandas as pd
CAT_LINK = "https://api.tiki.vn/raiden/v2/menu-config?platform=desktop"
HEADERS = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}

def get_categories(cat_link):
    response  = requests.get(cat_link, headers=HEADERS)
    categories = json.loads(response.text)["menu_block"]["items"]
    categories_str = json.dumps(categories,indent=4)


    df = pd.read_json(categories_str)
    df['cat_id'] = df['link'].apply(get_categories_id)
    df = df.drop(columns=['icon_url'])
    df.to_csv('categories.csv')

    return categories_str

def get_categories_id(url_str):
    id_str = url_str.split('/')[-1][1:]
    return id_str


def main():
    get_categories(CAT_LINK)

if __name__ == "__main__":
    main()

    
   
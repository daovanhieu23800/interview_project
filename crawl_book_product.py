import requests
import json
import csv
import re
import pandas as pd
import time 
from book_cat import get_cat
HEADERS = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}
LIMIT = 40
TOTAL_PAGE = 20
BOOK_CAT = 8322
def get_product_per_page(book_cat, page):
    product_list_per_page = [] 
    product_per_page_link = f"https://tiki.vn/api/v2/products?category={book_cat}&limit={LIMIT}&page={page}"
    response  = requests.get(product_per_page_link, headers=HEADERS)
    products = json.loads(response.text)['data']
    for product in (products):
        product_data = (get_product(product['id']))
        #print(product_data['name'])
        print(product_data['id'],page)#,'-----',response.text)
        if 'authors'in product_data and ("categories" in product_data) and ("all_time_quantity_sold" in product_data):
            product_list_per_page.append({
                "id":product_data['id'],
                "name":product_data['name'],
                "price":product_data['price'],
                "original_price":product_data["original_price"],
                "discount": product_data["discount"],
                "discount_rate": product_data["discount_rate"],
                "rating_average": product_data["rating_average"],
                "review_count": product_data["review_count"],
                "short_description":product_data["short_description"],
                #"has_ebook": product_data["has_ebook"],
                "all_time_quantity_sold": product_data["all_time_quantity_sold"],
                #"warranty_policy": product_data["warranty_policy"],
                "authors":  [auth["name"] for auth in  product_data['authors']],
                "specifications": product_data["specifications"],
                #"current_seller": product_data["current_seller"],
                # #"other_sellers": product_data["other_sellers"],
                # "publisher_vn":product_data["specifications"][0]["attributes"][0]['value'],
                # "publication_date":product_data["specifications"][0]["attributes"][1]['value'],
                # "dimensions":product_data["specifications"][0]["attributes"][2]['value'],
                # "book_cover":product_data["specifications"][0]["attributes"][3]['value'],
                # "number_of_page":product_data["specifications"][0]["attributes"][4]['value'],
                # "manufacturer":product_data["specifications"][0]["attributes"][5]['value'],
                "categories":product_data["categories"]['name'],

            })
       # print(product_list_per_page)
    return product_list_per_page

def get_product(product_id):
    time.sleep(1)
    product_info_link = f"https://tiki.vn/api/v2/products/{product_id}"
    response  = requests.get(product_info_link, headers=HEADERS)
    #print(response.status_code,response.text)
    product_info = json.loads(response.text)
    
    return product_info


def main():
    product_list = []
    cat_list = get_cat()
    #print(cat_list)
    for i in range(13,23):
    #for item in cat_list:
        print(cat_list[i])
        for page in range(1,11):
            #time.sleep(10)
            if get_product_per_page(cat_list[i]['id'],page)== []:
                time.sleep(12)
                break
            product_list += (get_product_per_page(cat_list[i]['id'],page))
            time.sleep(12)
           
            
    #print(product_list)

    df = df = pd.DataFrame(product_list)
    df.to_csv('test2.csv')

if __name__ == "__main__":
    main()

    
   
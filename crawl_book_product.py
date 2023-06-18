import requests
import json
import csv
import re
import pandas as pd
HEADERS = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}
LIMIT = 2
TOTAL_PAGE = 3
BOOK_CAT = 8322
def get_product_per_page(page):
    product_list_per_page = [] 
    product_per_page_link = f"https://tiki.vn/api/v2/products?category={BOOK_CAT}&limit={LIMIT}&page={page}"
    response  = requests.get(product_per_page_link, headers=HEADERS)
    products = json.loads(response.text)['data']
    
    for product in (products):
        product_data = (get_product(product['id']))
        #print(product_data['name'])
        product_list_per_page.append({
            "id":product_data['id'],
            "name":product_data['name'],
            "price":product_data['price'],
            "original_price":product_data["original_price"],
            "discount": product_data["discount"],
            "discount_rate": product_data["discount_rate"],
            "rating_average": product_data["rating_average"],
            "review_count": product_data["review_count"],
            "has_ebook": product_data["has_ebook"],
            "all_time_quantity_sold": product_data["all_time_quantity_sold"],
            "warranty_policy": product_data["warranty_policy"],
            "authors":product_data["authors"],
            "current_seller": product_data["current_seller"],
            "other_sellers": product_data["other_sellers"],
            # "publisher_vn":product_data["rating_average"],
            # "publication_date":product_data["rating_average"],
            # "dimensions":product_data["rating_average"],
            # "book_cover":product_data["rating_average"],
            # "number_of_page":product_data["rating_average"],
            # "manufacturer":product_data["rating_average"],
            "categories":product_data["categories"],

        })

    return product_list_per_page

def get_product(product_id):
    product_info_link = f"https://tiki.vn/api/v2/products/{product_id}"
    response  = requests.get(product_info_link, headers=HEADERS)
    product_info = json.loads(response.text)
    return product_info


def main():
    product_list = []
    for page in range(1,TOTAL_PAGE+1):
        product_list += (get_product_per_page(page))
    print(product_list)

    df = df = pd.DataFrame(product_list)
    df.to_csv('book_product.csv')

if __name__ == "__main__":
    main()

    
   
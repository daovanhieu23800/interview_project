import pandas as pd
import requests
import time
import json
import os
folder_path = 'images'
os.makedirs(folder_path, exist_ok=True)
HEADERS = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}

book_df = pd.read_csv("book.csv")
def download_image(url, category):
    # Create the category folder if it doesn't exist
    if not os.path.exists(category):
        os.makedirs(category)
    
    # Extract the image filename from the URL
    filename = os.path.basename(url)
    
    # Build the path to save the image
    save_path = os.path.join(category, filename)
    
    # Download the image and save it
    response = requests.get(url)
    if response.status_code == 200:
        with open(save_path, 'wb') as f:
            f.write(response.content)
        print(f"Downloaded: {url} -> {save_path}")
    else:
        print(f"Failed to download: {url}")

for item in book_df.iloc:
    time.sleep(1)
    print(item)
    book_id = item['id']

    book_cat = item['categories']

    product_info_link = f"https://tiki.vn/api/v2/products/{book_id}"
    response  = requests.get(product_info_link, headers=HEADERS)
    #print(response.status_code,response.text)
    product_info = json.loads(response.text)
    image_link = product_info["images"][0]["small_url"]
    image_cat = book_cat
    image_cat =image_cat.replace(' ','_')
    
    print(image_cat)
    download_image(image_link, image_cat)
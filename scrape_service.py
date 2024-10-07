from fastapi import FastAPI, HTTPException
from .db_connection import insert_data_into_mongo_db
import requests
from bs4 import BeautifulSoup
import time
from pydantic import BaseModel
from typing import List

# # Pydantic model for scraped article data
# class Article(BaseModel):
#     title: str
#     date: str
#     category: str
#     description: str
#     image_url: str

# Function to scrape a single page
async def scrape_page(url):
    response = requests.get(url, timeout=10)

    if response.status_code == 200:
        html_content = response.content
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        return

    soup = BeautifulSoup(html_content, "html.parser")
    articles = soup.find_all('article', class_="article")

    # List to hold all scraped articles for a page
    scraped_data = []

    for article in articles:
        title = article.select('div > div.txtContBlock > header > h1 > a > span')[0].text
        date = article.select('div > div.txtContBlock > p.article-date > time')[0].text
        category_elem = article.select('div > div.txtContBlock > ul > li > span > a')
        category = category_elem[0].text if category_elem else "Unknown"
        description = article.select('div > div.txtContBlock > p.article-descript')[0].text
        image_url = article.select('div > div.thumbImg > a > img')[0].get('src')

        # Append scraped data to the list
        scraped_data.append({
            "title": title,
            "date": date,
            "category": category,
            "description": description,
            "image_url": image_url
        })

    # Insert the scraped data into MongoDB
    # await insert_data_into_mongo_db(scraped_data)

    return scraped_data


# # API Endpoint to trigger the scraping process and store in MongoDB
# @app.get("/scrape")
# async def start_scraping():
#     base_url = "https://kabochan.blog.jp"

#     # First, scrape the base URL
#     print(f"Scraping the base page: {base_url}")
#     await scrape_page(base_url)

#     # Then scrape the other pages (from page 2 onwards)
#     for page_num in range(2, 237):  # Loop over multiple pages
#         page_url = f"{base_url}/?p={page_num}"
#         await scrape_page(page_url)
#         print(f"Scraping page {page_num}: {page_url}")
#         time.sleep(2)  # Pause to avoid overwhelming the server

#     return {"status": "Scraping completed"}


# # API Endpoint to get all articles from MongoDB
# @app.get("/articles/", response_model=List[Article])
# async def get_articles():
#     articles = await collection.find().to_list(1000)
#     if articles:
#         return articles
#     raise HTTPException(status_code=404, detail="No articles found")

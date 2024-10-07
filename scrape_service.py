import requests
from bs4 import BeautifulSoup


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



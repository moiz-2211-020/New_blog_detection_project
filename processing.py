from hashing_and_redis_service import *
from scrape_service import scrape_page
from db_connection import insert_data_into_mongo_db
from New_blog_detection_project.email_notification import send_email_notification
import asyncio  # Import asyncio for asynchronous handling

url = "https://kabochan.blog.jp/"

async def main():
    # Scrape the page (awaiting the asynchronous function)
    article_data = await scrape_page(url)
    print(f'{article_data} is scraped completely')

    # Process the article
    result = await process_article(article_data)  # Awaiting process_article
    print(result)


async def process_article(article_data):
    # Generate hash for the article
    article_hashes = generate_article_hash(article_data)
    for article_hash in article_hashes:
        print(f'article hashed{article_hash}')
        
        # Check if the article is new using Redis
        if is_new_article(article_hash):
            # Save new article hash in Redis
            save_article_hash(article_hash)
            print("article save successfully")
            
            # Save the article in MongoDB
            await insert_data_into_mongo_db(article_data)
            print("article inserted successfully")
            if isinstance(article_data, list):
                for data in article_data:
                    print(data)

                # Send notification for the new article
                    send_email_notification(data.get('title'), data.get('description'))
            return ("Email notification sended successfully!")
        else:
            return "Article already exist!"



if __name__ == "__main__":
    try:
        asyncio.run(main())  # This should be the entry point
    except Exception as e:
        print(f"An error occurred: {e}")
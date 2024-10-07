import hashlib
import redis
from db_connection import insert_data_into_mongo_db
from New_blog_detection_project.email_notification import send_email_notification

def generate_article_hash(article_data):
    """
    Generate a hash for the given article data.
    Uses a combination of title, content, and URL as the basis for the hash.
    """
    if isinstance(article_data, list):
        hashes = []
        for article in article_data:
            # Ensure each article is a dictionary
            if isinstance(article, dict):
                # Create a string representation of relevant fields
                article_string = f"{article.get('title', '')}{article.get('discription', '')}"
                hash_object = hashlib.md5(article_string.encode('utf-8'))
                hashes.append(hash_object.hexdigest())
            else:
                raise ValueError("Each item in article_data should be a dictionary.")
        return hashes  # Return a list of hashes for each article
    else:
        raise ValueError("article_data should be a list of dictionaries.")
 



# Connect to Redis (modify host and port if necessary)
r = redis.Redis(host='redis_container', port=6379, db=0)

def is_new_article(article_hash):
    """
    Check if the article hash already exists in Redis.
    Returns True if it's a new article, False if it's already stored.
    """
    return not r.sismember('article_hashes', article_hash)

def save_article_hash(article_hash):
    """
    Save the article hash to Redis.
    """
    r.sadd('article_hashes', article_hash)



# async def process_article(article_data):
#     # Generate hash for the article
#     article_hash = generate_article_hash(article_data)
    
#     # Check if the article is new using Redis
#     if is_new_article(article_hash):
#         # Save new article hash in Redis
#         save_article_hash(article_hash)
        
#         # Save the article in MongoDB
#         await insert_data_into_mongo_db(article_data)
        
#         # Send notification for the new article
#         send_email_notification(article_data['title'], article_data['image_url'])


from motor.motor_asyncio import AsyncIOMotorClient

# MongoDB configuration
MONGO_DETAILS = "mongodb://mongo_container:27017"  # Connect to MongoDB running in Docker

# Create a new client and connect to the MongoDB instance
client = AsyncIOMotorClient(MONGO_DETAILS)

# Select the database (create if it doesn't exist)
database = client["scrape_database"]  # Replace with your preferred database name

# Select the collection (create if it doesn't exist)
collection = database["scrape_collection"] 

# Asynchronous function to insert data into MongoDB
async def insert_data_into_mongo_db(hash_data):
    if isinstance(hash_data, list):
        result = await collection.insert_many(hash_data)
        return result
    else:
        # If hash_data is a single document, use insert_one
        result = await collection.insert_one(hash_data)
        return result
    


# async def insert_data_into_mongo_db(article_data):
#     if isinstance(article_data, list):
#         for article in article_data:
#             # Insert each article into MongoDB
#             result = collection.insert_one(article)
#             print(f"Inserted article with ID: {result.inserted_id}")
#     else:
#         raise ValueError("Article data must be a list of dictionaries")

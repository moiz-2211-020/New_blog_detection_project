from motor.motor_asyncio import AsyncIOMotorClient

# MongoDB configuration
MONGO_DETAILS = "mongodb+srv://muhammadmoizkhan23:IY7QDq5fj5x6naIm@moizcluster.qkiu8.mongodb.net/"  # Replace with your MongoDB URI
client = AsyncIOMotorClient(MONGO_DETAILS)
database = client["scrape_database"]
collection = database["scrape_collection"]


def insert_data_into_mongo_db(hash_data):
    
    result = collection.insert_many(hash_data)
    return result.id

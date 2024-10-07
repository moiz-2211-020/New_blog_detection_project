import hashlib

def generate_article_hash(article_data):
    """
    Generate a hash for the given article data.
    You can use a combination of title, content, or URL as the basis for the hash.
    """
    hash_object = hashlib.md5(article_data.encode('utf-8'))
    return hash_object.hexdigest()

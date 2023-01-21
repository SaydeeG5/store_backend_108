import pymongo
import certifi

connection_str = "mongodb+srv://Saydee_G:Test12345@cluster0.q3dqtkv.mongodb.net/?retryWrites=true&w=majority"

client = pymongo.MongoClient(connection_str, tlsCAFile=certifi.where())
db = client.get_database("Boutique")
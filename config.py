import pymongo
import certifi

con_str = "mongodb+srv://a1271710:admin@fsdifranck.sht7qnk.mongodb.net/?retryWrites=true&w=majority"

client = pymongo.MongoClient(con_str, tlsCAFile=certifi.where())
db = client.get_database("onlinestore")
import pymongo
import pandas as pd

client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["sample_db"]
loc = db.page_table.find({})
res = list[db.page_table.aggregate([
    {"$match" : {"ocr_status" : 1}}
])]
print(res)
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017")

db = client["project_db"]
training_data = db.training_data.find({})

for obj in training_data:
    
import pymongo
import pandas as pd

client=pymongo.MongoClient("mongodb://localhost:27017")
db=client["sample_db"]

verified_bills = db.verified_bills.find({})

date = []
amount = []
invoice = []
vendor = []

for obj in verified_bills:
    if "Date" in obj['payload'].keys():
        print("date","true")
    else:
        print(obj)
        # obj['payload']['Date'] = 
        
    # print(obj['payload']['Date'])
    # date.append(obj['payload']['Date'])
    # amount.append(obj['payload']['Amount'])
    # invoice.append(obj['payload']['InvoiceNumber'])
    # vendor.append(obj['payload']['vendor'])

print(date)
        
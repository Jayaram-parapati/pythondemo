import pymongo
import pandas as pd

client=pymongo.MongoClient("mongodb://localhost:27017")
sample_db=client["sample_db"]
verified_bills=sample_db["verified_bills"]
page_table=sample_db["page_table"]
#print(page_table.find_one())
#print(verified_bills.find_one())
#print(type(page_table))
verified_bills_list=verified_bills.find()
for x in verified_bills_list:
    print(x["_id"],x["payload"]["InvoiceNumber"])
    





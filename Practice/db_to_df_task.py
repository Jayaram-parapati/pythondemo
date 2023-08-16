import pymongo
import pandas as pd
import numpy
import re
import json

client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["sample_db"]

date = []
amount = []
invoice = []
vendor = []
final_text = []


verified_bills = db.verified_bills.find({})

for obj in verified_bills:

    if 'page_id' in obj:
        ocr_list = list(db.page_table.aggregate([
            {
                '$match': {'_id': obj['page_id']}
            },
            {
                '$project': {'ocr_text': 1, '_id': 0}
            }
        ]))

        ocr_text_list = ocr_list[0]['ocr_text']

        print('----------------------------------------')

        if 'InvoiceNumber' in obj['payload']:
            search_string = obj["payload"]["InvoiceNumber"]
            start_index = ocr_text_list.find(search_string)
            end_index = start_index + len(search_string)

            if start_index != -1:
                final_text.append(search_string)
                # db.final_table.update_one({"text":search_string},{"$set":{"entities":[start_index, end_index, "InvoiceNumber"]}})
                # print(f"InvoiceNumber {start_index} to {end_index-1}")

        if 'Amount' in obj['payload']:
            search_string = obj["payload"]["Amount"]
            start_index = ocr_text_list.find(str(search_string))
            end_index = start_index + len(str(search_string))

            if start_index != -1:
                final_text.append(search_string)
                # db.final_table.update_one({"text":search_string},{"$set":{"entities":[start_index, end_index, "Amount"]}})
                # print(f"Amount, {start_index} to {end_index-1}")

        if 'vendor' in obj['payload']:
            search_string = obj["payload"]["vendor"]
            start_index = ocr_text_list.find(search_string)
            end_index = start_index + len(search_string)

            if start_index != -1:
                final_text.append(search_string)
                # db.final_table.update_one({"text":search_string},{"$set":{"entities":[start_index, end_index, "vendor"]}})
                 # print(f"Vendor {start_index} to {end_index-1}")

        print('----------------------------------------')

# for item in final_text:
#     db.final_table.insert_one({"text":item})
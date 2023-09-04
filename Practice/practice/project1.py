import pymongo, json,re

client = pymongo.MongoClient("mongodb://localhost:27017")

db = client["newproject_db"]
training_data = db.training_data.find({})
data_list = list(training_data)
output = list(db.output_data.find({}))
for obj in data_list:
    text = obj["data"]["Text"]

    result_arr = []

    for result in obj["annotations"][0]["result"]:
        start = result["value"]["start"]
        end = result["value"]["end"]
        label = result["value"]["labels"][0]
        result_arr.append([start, end, label])
    output.append({'text':text, 'entities':result_arr})

    db.output_data.insert_one({'text':text, 'entities':result_arr})


# final_output = []
# for op in output:
#     op['new_Text'] = (re.sub(r'\s+', ' ', op['text'])).strip()
#     result_arr = []
#     for ent in op['entities']:
#         start = ent[0]
#         end = ent[1]
#         actual_string = re.sub(r'\s+', ' ', op['text'][start:end])
#         match = re.search(pattern=actual_string,string=op['new_Text'])
#         if match is not None:
#             # print(start,end,actual_string)
#             # print(match.start(),match.end(),op['new_Text'][match.start():match.end()])
#             result_arr.append([match.start(),match.end(), ent[2]])
#             # result_arr.append([match.start(),match.end(), ent[2]])
#         else:
#             match1 = re.search(pattern=re.escape(actual_string),string=op['new_Text'])
#             if match1 is not None:
#                 # print(match1.start(),match1.end(),op['new_Text'][match1.start():match1.end()])
#                 result_arr.append([match1.start(),match1.end(), ent[2]])
#             else:print('match not found')
           
        

       
        
    
#     # final_output.append({'text':op['new_Text'], 'entities':result_arr})/
#     db.final_data.insert_one({'text':op['new_Text'], 'entities':result_arr})
        

        



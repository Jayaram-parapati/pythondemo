# import re
# story = "my name is Jayaram, and i work in hallmark at kakinada city. kakinada is a city in andhra pradesh. its famous for a sweet called kaja. kaja is sold at same street as hallmark."
# # search_list = []
# # inputs = input("enter elements by space ")
# # search_list = inputs.split()
# # print(search_list)
# person = {
#     "name" : "Jayaram",
#     "company" : "hallmark",
#     "city" : "kakinada",
#     "favorite" : "kaja",
# }

# final_list = []
# search_list = person.values()

# for x in search_list:
#   for m in re.finditer(x,story):
#     list = [x,m.start(),(m.end()-1)]
#     final_list.append(list)

# print(final_list)

story = "my name is Jayaram, and i work in hallmark at kakinada city. kakinada is a city in andhra pradesh. its famous for a sweet called kaja. kaja is sold at same street as hallmark."

person = {
    "name": "Jayaram",
    "company": "hallmark",
    "city": "kakinada",
    "favorite": "kaja",
}

search_list = person.values()
final_list = []

def check(sub_str):
    for x in range(len(story)):
        if story.startswith(sub_str,x):
            return [x , (x+(len(sub_str)-1)),sub_str]


for x in search_list:
    final_list.append((check(x)))
    
print(final_list)

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
#   for m in find(x,story):
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

def check(sub_str,story):
    # for x in range(len(story)):
    #     if story.startswith(sub_str,x): 
    #       return [x,((x)+len(sub_str)-1),sub_str]


      index = [index for index in range(len(story)) if story.startswith(sub_str, index)]
      if len(index) > 1:
          new_lists = [[x,len(sub_str)-1+x,sub_str] for x in index]
          return new_lists
      else:
          for x in index:
            y = [x,len(sub_str)-1+x,sub_str]
          return y

for sub_str in search_list:
  c = check(sub_str,story)
  final_list.append(c)

print(final_list)
  

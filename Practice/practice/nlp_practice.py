# import spacy  #>>>>>>>>>># Import spaCy

# nlp = spacy.blank("en")   #>>>>>>># Create a blank English nlp object

# doc = nlp("My name is Jayaram and I am from Srikakulam")  #>>>>>>>>>>>>>>>># Created  doc by processing a string of text with the nlp object

# for token in doc:  #>>>>># Iterate over tokens in a Doc
#     print(token)
# print("---------------------------")

# token = doc[3]  #>>>>>>>>>>>># Index into the Doc to get a single Token using index of specified token
# print(token) 
# print(token.text)   
# print("-----------------------------")

# span = doc[3:6]   #>>>>>>>>># A slice from the Doc is a Span object
# print(span)
# print(span.text)
# print("-----------------------------")

# doc = nlp("Jayaram 24 $100")
# print([token.i for token in doc])                 # .i
# print([token.text for token in doc])              # .text
# print([token.is_alpha for token in doc])          # .is_alpha 
# print([token.is_punct for token in doc])          # .is_num
# print([token.like_num for token in doc])          # .like_num
# print([token.like_email for token in doc])        # .like_emial all these are attruibutes and used to check the content of the token 
#                                                     # and many more attributes  are present
# print("-----------------------------")
                                              
# # # Process the text
# # doc = nlp("In 1990, more than 60% of people in East Asia were in extreme poverty. Now less than 4% are.")

# # Iterate over the tokens in the doc
# for token in doc:
#     # Check if the token resembles a number
#     if token.like_num:
#         # Get the next token in the document
#         next_token = doc[token.i + 1]
#         # Check if the next token's text equals "%"
#         if next_token.text == "%":
#             print("Percentage found:", token.text) 

# # print("-----------------------------")
# import spacy
# nlp = spacy.load("en_core_web_sm")   
# doc = nlp("she is doing garden work") 
# for token in doc:
#     print(token.text, token.pos_)
#     print(token.text, token.pos_, token.dep_, token.head.text)
#     print(spacy.explain(token.pos_))
#     print(spacy.explain(token.dep_))
#     print(">>>>>>>>>>>>>>")  

# print("-----------------------------")


# text = "It’s official: Apple is the first U.S. public company to reach a $1 trillion market value"

# # Process the text
# doc = nlp(text)

# for token in doc:
#     # Get the token text, part-of-speech tag and dependency label
#     token_text = token.text
#     token_pos = token.pos_
#     token_dep = token.dep_
#     # This is for formatting only
#     print(f"{token_text:<12}{token_pos:<10}{token_dep:<10}")

# import spacy

# # Import the Matcher
# from spacy.matcher import Matcher

# # Load a pipeline and create the nlp object
# nlp = spacy.load("en_core_web_sm")

# # Initialize the matcher with the shared vocab
# matcher = Matcher(nlp.vocab)

# # Add the pattern to the matcher
# pattern = [{"TEXT": "iPhone"}, {"TEXT": "X"}]
# matcher.add("IPHONE_PATTERN", [pattern])

# # Process some text
# doc = nlp("Upcoming iPhone X release date leaked")
# # doc1 = nlp("No Iphone x model is going to release in August")
# # Call the matcher on the doc
# matches = matcher(doc)
# # matches = matcher(doc1)
# print(matches) #giving o/p like [95284072(86733565721, 1, 3)]
# for match_id,start,end in matches:
#     matched_span = doc[start:end]
#     print(matched_span.text) # o/p as iPhone X
# print("-----------------------")
# pattern = [
#     {"IS_DIGIT": True},
#     {"IS_DIGIT": True},
#     {"LOWER": "fifa"},
#     {"LOWER": "world"},
#     {"LOWER": "cup"},
#     {"IS_PUNCT": True}
    
# ]
# matcher.add("winner pattern",[pattern])
# doc = nlp("2018 2020 FIFA World Cup: France won!")
# matches = matcher(doc)
# for match_id,start,end in matches:
#     print(doc[start:end])

# print("-----------------------")

# pattern = [
#     {"LEMMA": "love", "POS": "VERB"},
#     {"POS": "NOUN"}
# ]
# matcher.add("love pattern",[pattern])
# doc = nlp("I loved dogs but now I love cats more.")
# matches = matcher(doc)
# for match_id,start,end in matches:
#     print(doc[start:end])

# print("-----------------------")

# pattern = [
#     {"LEMMA": "buy"},
#     {"POS": "DET", "OP": "*"},  # optional: match 0 or 1 times
#     {"POS": "NOUN"}
# ]
# matcher.add("new",[pattern])
# doc = nlp("I bought a smartphone. Now I'm buying apps.")
# matches = matcher(doc)
# for match_id,start,end in matches:
#     print(doc[start:end])

# print("-----------------------")

# doc = nlp("I LOVE MY INDIA")
# hash_value = nlp.vocab.strings["INDIA"]
# print(hash_value)
# hash_string = nlp.vocab.strings[hash_value] #gives a hash_value for INDIA 7057732381406613485 by using nlp.vocab.strings
# print(hash_string) 
# print(nlp.vocab.strings[7057732381406613485])
# print(doc.vocab.strings["INDIA"])            # we can get hash_value by doc.vocab.strings also
# print(doc.vocab.strings[7057732381406613485])

# doc = nlp("I LOVE MY INDIA")
# lexeme = nlp.vocab["INDIA"]
# print(lexeme.text,lexeme.orth,lexeme.is_alpha)
# print("---------------------------------")

# import spacy
# nlp = spacy.blank("en")

# # Import the Doc class
# from spacy.tokens import Doc

# # The words and spaces to create the doc from
# words = ["Hello", "world", "!"]
# spaces = [True, False, False]

# # Create a doc manually
# doc = Doc(nlp.vocab, words=words, spaces=spaces)
# print(doc)
# print("-------------------------------")

# # Import the Doc and Span classes
# from spacy.tokens import Doc, Span

# # The words and spaces to create the doc from
# words = ["Hello", "world", "!"]
# spaces = [True, False, False]

# # Create a doc manually
# doc = Doc(nlp.vocab, words=words, spaces=spaces)

# # Create a span manually
# span = Span(doc, 0, 2)

# # Create a span with a label
# span_with_label = Span(doc, 0, 1, label="GREETING")

# # Add span to the doc.ents
# doc.ents = [span_with_label]
# for ent in doc.ents:
#     print(ent.text,ent.label_)

# print("-------------------------------")

# import spacy
# nlp = spacy.load("en_core_web_md")
# doc = nlp("I like Sports")
# doc1 = nlp("I like Cricket")
# print(doc.similarity(doc1))
# print(doc1.similarity(doc))
# token1 = doc[1]
# token2 = doc[2]
# print(token1.similarity(token2))
# print(token2.similarity(token1))
# print(doc[1].similarity(doc[2]))
# print(doc[2].similarity(doc[1]))

# import spacy
# nlp = spacy.load("en_core_web_md")
# doc = nlp("i love my Nation")
# print(doc[3].vector)
# print(doc[3].has_vector)
# print(doc[3].vector_norm)

# print("-------------------")

# import spacy
# nlp = spacy.load("en_core_web_md")
# doc = nlp("I love my Nation and name of my Country is INDIA")
# span1 = doc[1:4]
# span2 = doc[7:11]
# print(span1,"+",span2)
# print(span1.similarity(span2))
# print("--------------------")

# import spacy 
# from spacy.matcher import Matcher
# nlp = spacy.load("en_core_web_md")
# matcher = Matcher(nlp.vocab)
# pattern = [{"lower":"red"},{"lower":"roses"}]
# matcher.add("rose_pattern",[pattern])
# doc = nlp("i have bunch of RED ROSES")
# matched_doc = matcher(doc)
# for match_id,start,end in matched_doc:
#     span = doc[start:end]
#     print(span.text)
#     print(span.root.text)
#     print(span.root.head.text)

# import spacy
# from spacy.matcher import PhraseMatcher
# nlp = spacy.load("en_core_web_md")
# matcher = PhraseMatcher(nlp.vocab)
# pattern = nlp("RED ROSES")
# matcher.add("rose_pattern",[pattern])
# doc = nlp("I have bunch of RED ROSES")
# matched_doc = matcher(doc)
# for  match_id,start,end in matched_doc:
#     span = doc[start:end]
#     print(span.text)  
# print("--------------------")

# import spacy
# from spacy.matcher import Matcher
# nlp = spacy.load("en_core_web_md")
# matcher = Matcher(nlp.vocab)
# doc =nlp("Twitch Prime, the perks program for Amazon Prime Prime Prime members offering free "
#     "loot, games and other benefits, is ditching one of its best features: "
#     "ad-free viewing. According to an email sent out to Amazon Prime members "
#     "today, ad-free viewing will no longer be included as a part of Twitch "
#     "Prime for new members, beginning on September 14. However, members with "
#     "existing annual subscriptions will be able to continue to enjoy ad-free "
#     "viewing until their subscription comes up for renewal. Those with "
#     "monthly subscriptions will have access to ad-free viewing until October 15.")
# pattern1 = [{"LOWER":"amazon"},{"IS_TITLE":True,"POS":"PROPN","op":"!"}]
# pattern2 = [{"LOWER":"ad"},{"TEXT":"-"},{"LOWER":"free"}]
# matches = matcher.add("Pattern1",[pattern1])
# matches = matcher.add("Pattern2",[pattern2])
# matched_doc = matcher(doc)
# for match_id,start,end in matched_doc:
#     print(doc.vocab.strings[match_id],doc[start:end].text)
# print("-----------------------")

# import json
# import spacy
# from spacy.matcher import PhraseMatcher
# with open("json path here",encoding="utf8") as f:
#     COUNTRIES = json.loads(f.read())
# nlp = spacy.blank("en")
# doc = nlp("text goes here")
# matcher = PhraseMatcher(nlp.vocab)
# pattern = [nlp(country) for country in COUNTRIES]
# #otherwise above pattern can be written as:
# pattern = list(nlp.pipe(COUNTRIES))
# matcher.add("pattern",[pattern])
# matches = matcher(doc)
# for match_id,start,end in matches:
#     print(doc[start:end])

# import spacy
# nlp = spacy.load("en_core_web_md")
# from spacy.language import Language
# print(nlp.pipe_names)
# # print(nlp.pipeline)
# # print(nlp._pipe_configs)
# print("-----------------")
# @Language.component("custom_component")
# def length_function():
#     return
# nlp.add_pipe("custom_component")
# print(nlp.pipe_names)

# import spacy
# from spacy.language import Language
# nlp = spacy.load("en_core_web_md")

# @Language.component("custom_component")
# def len_function(doc):
#     print(doc,"the length of given doc is : " ,len(doc))
#     return doc
     

# nlp.add_pipe("custom_component")
# doc = nlp("I LOVE MY INDIA")
    
# print(nlp.pipe_names)

# import spacy
# from spacy.matcher import Matcher
# from spacy.matcher import PhraseMatcher
# from spacy.tokens import Span
# from spacy.language import Language

# nlp = spacy.load("en_core_web_sm")

# fruits = ["Apple","Banana","Cherry"]
# fruits_pattern = list(nlp.pipe(fruits))
# matcher = PhraseMatcher(nlp.vocab)

# fruit_pattern1 = [{"lower":"apple"}]
# fruit_pattern2 = [{"TEXT":"Banana"}]
# fruit_pattern3 = [{"lower":"cherry"}]

# matcher = Matcher(nlp.vocab)

# matcher.add("fruit_pattern1",[fruit_pattern1])
# matcher.add("fruit_pattern2",[fruit_pattern2])
# matcher.add("fruit_pattern3",[fruit_pattern3])

# @Language.component("custom_component")
# def fruit_function(doc):
#     matches = matcher(doc)
#     span = [Span(doc,start,end,label="FRUIT") for match_id,start,end in matches]
#     doc.ents = span
#     return doc

# nlp.add_pipe("custom_component",first = True)
# print(nlp.pipe_names)

# doc = nlp("In our garden we grow Apple,Pineapple,Brinjal, Banana and also cHerry.")

# print([(ent.text,ent.label_)for ent in doc.ents])

# import spacy
# from spacy.tokens import Doc,Span,Token
# nlp = spacy.load("en_core_web_md")
# doc = nlp("hi this is Jayaram")

# Doc.set_extension("title",default=None)
# print(doc._.title)
# doc._.title = "My_Name"
# print(doc._.title)

# Token.set_extension("is_name",default=False)
# print(doc[3]._.is_name)
# doc[3]._.is_name = True
# print(doc[3]._.is_name)  #Attribute extension

#using Property extension

# import spacy
# from spacy.tokens import doc,Span,Token

# nlp = spacy.load("en_core_web_md")
# # def get_is_color(token):
# #   colors = ["orange","blue","white","yellow","green","black"]
# #   return(token.text in colors)

# def get_has_color(span):
#     colors = ["orange","blue","white","yellow","green","black"]
#     # return any(token.text in colors for token in span)
#     list = []
#     for token in span:
#         if token.text in colors:
#             list.append(token.text)

#     return list

# # Token.set_extension("is_color",getter = get_is_color)
# Span.set_extension("has_color",getter = get_has_color )

# doc = nlp("I have three shirts of blue,black and white colors.")
# # print(doc[2]._.is_color,doc[2].text)
# print(doc[0:11]._.has_color,doc[0:11].text)

# print("-------------------------------------------------------------------------------------------")

# import spacy
# from spacy.tokens import Token,Span,Doc

# nlp = spacy.load("en_core_web_md")

# def given_is_present(doc,token_text):
#     return token_text in (token.text for token in doc)
    
# Doc.set_extension("check_is_present",method=given_is_present)

# doc = nlp("I have three shirts of blue,black and white colors.")
# print(doc._.check_is_present("crow"))

# import spacy
# from spacy.tokens import Token,Doc,Span
# nlp = spacy.load("en_core_web_md")
# def get_reversed(token):
#     return token.text[::-1]

# Token.set_extension("reverse_doc",getter=get_reversed)
# doc = nlp("I am a BTech Student.")
# for token in doc:
#     print(token._.reverse_doc)

# import spacy
# from spacy.tokens import Doc,Token,Span

# nlp = spacy.load("en_core_web_md")

# def get_has_num(doc):
#     return any(token.like_num for token in doc)
# Doc.set_extension("has_num",getter=get_has_num)
# doc = nlp("India got Independence in 1947")
# print(doc._.has_num)

import spacy
nlp = spacy.load("en_core_web_md")
doc = nlp("India has cricket board named BCCI and international cricket board name is ICC and it conducts ODI Cricket WorldCup for every Four years.")

for ent in doc.ents:
    print(ent.text,ent.label_,spacy.explain(ent.label_))
    



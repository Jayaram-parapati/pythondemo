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

import json
import spacy
from spacy.matcher import PhraseMatcher
json_path = r'C:\\Users\\anand.adapa\\Documents\\hii.json'
with open(json_path , 'r') as f:
    COUNTRIES = json.loads(f.read())

nlp = spacy.blank("en")
doc = nlp("ODI worldcup won by Australia 5 times ,India and WestIndies by 2 times,both Pakistan and Sri Lanka teams once each time")
matcher = PhraseMatcher(nlp.vocab)
# pattern = [nlp(country) for country in COUNTRIES]

pattern = list(nlp.pipe(COUNTRIES))
matcher.add("pattern",pattern)
matches = matcher(doc)
for match_id,start,end in matches:
    print(doc[start:end])

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

# using Property extension

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

# import spacy
# nlp = spacy.load("en_core_web_md")
# doc = nlp("India has cricket board named BCCI and international cricket board name is ICC and it conducts ODI Cricket WorldCup for every Four years.")

# for ent in doc.ents:
#     print(ent.text,ent.label_,spacy.explain(ent.label_))

# from spacy.lang.en import English
# from spacy.matcher import PhraseMatcher

# nlp = English()
# matcher = PhraseMatcher(nlp.vocab, attr="LOWER")
# patterns = [nlp.make_doc(name) for name in ["Angela Merkel", "Barack Obama"]]
# matcher.add("Names", patterns)

# doc = nlp("angela merkel and us president barack Obama")
# for match_id, start, end in matcher(doc):
#     print("Matched based on lowercase token text:", doc[start:end])

# from spacy.matcher import PhraseMatcher

# nlp = English()
# matcher = PhraseMatcher(nlp.vocab, attr="SHAPE")
# matcher.add("IP", [nlp("127.0.0.1"), nlp("127.127.0.0")])

# doc = nlp("Often the router will have an IP address such as 192.1.1.1 or 192.168.2.1.")
# for match_id, start, end in matcher(doc):
#     print("Matched based on token shape:", doc[start:end])
# print("------------------------------------------------")
# from spacy.lang.en import English

# nlp = English()
# ruler = nlp.add_pipe("entity_ruler")
# patterns = [{"label": "ORG", "pattern": "Apple"},
#             {"label": "GPE", "pattern": [{"LOWER": "san"}, {"LOWER": "francisco"}]}]
# ruler.add_patterns(patterns)

# doc = nlp("Apple is opening its first big office in San Francisco.")
# print([(ent.text, ent.label_) for ent in doc.ents])
# print(ruler.__doc__)
# print(nlp.pipe)
# print(nlp.pipe_labels)
# print(nlp.pipe_names)
# print(nlp.pipeline)
# print(nlp._pipe_configs)


# from spacy.tokens import Token, Span, Doc
# import json
# from spacy.matcher import PhraseMatcher
# from spacy.language import Language
# from spacy.lang.en import English
# import spacy
# print("--------------------------------------------------------")
# nlp = English()
# # nlp = spacy.load("en_core_web_sm")
# ruler = nlp.add_pipe("entity_ruler")
# patterns = [
#     {"label": "ORG", "pattern": [{"LOWER": "apple"}], "id": "San Francisco"},
#     {"label": "GPE", "pattern": [
#         {"LOWER": "san", "LOWER": "francisco"}], "id": "San Francisco"}
# ]
# ruler.add_patterns(patterns)


# doc = nlp("Apple is the biggest company in San Francisco")
# print([(ent.text, ent.label_, ent.id_) for ent in doc.ents])
# print("----------------------------------------------------------")


# nlp = English()
# # if we load nlp object with English then below procedure

# ruler = nlp.add_pipe("entity_ruler")
# print(nlp.pipe_names)
# patterns = [
#     {"label": "TOWN", "id": "HGT", "pattern": [{"LOWER": "srikakulam"}]},
#     {"label": "TOWN", "id": "HGT", "pattern": [{"LOWER": "kakinada"}]},
#     {"label": "IT COMPANY", "id": "HGT", "pattern": [
#         {"TEXT": "Hallmark"}, {"LOWER": "global"}, {"TEXT": "Technologies"}]}
# ]

# # ========= use above one or below one-------------

# nlp = spacy.load("en_core_web_sm")

# # if we load nlp with pipeline the below procedure

# # by using before = "ner" i am able to change entity label from default to my value like entity label of kakinada is GPE but by adding pipe before ner i changed it to TOWN as of my like
# ruler = nlp.add_pipe("entity_ruler", before="ner")
# print(nlp.pipe_names)
# patterns = [{"label": "IT COMPANY", "pattern": "Hallmark Global Technologies", "id": "HGT"},
#             {"label": "TOWN", "pattern": "Srikakulam", "id": "HGT"},
#             {"label": "TOWN", "pattern": "Kakinada", "id": "HGT"}
#             ]


# ruler.add_patterns(patterns)


# doc = nlp("my name is Jayaram.I am from Srikakulam.I work in Hallmark Global Technologies in Kakinada.")

# print([(ent.text, ent.label_, ent.id_)for ent in doc.ents])

# print("---------------------------------------")


# nlp = spacy.blank("en")
# COUNTRIES = ['Afghanistan', 'Åland Islands', 'Albania', 'Algeria', 'American Samoa', 'Andorra', 'Angola', 'Anguilla', 'Antarctica', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Aruba', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bolivia (Plurinational State of)', 'Bonaire, Sint Eustatius and Saba', 'Bosnia and Herzegovina', 'Botswana', 'Bouvet Island', 'Brazil', 'British Indian Ocean Territory', 'United States Minor Outlying Islands', 'Virgin Islands (British)', 'Virgin Islands (U.S.)', 'Brunei Darussalam', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cabo Verde', 'Cayman Islands', 'Central African Republic', 'Chad', 'Chile', 'China', 'Christmas Island', 'Cocos (Keeling) Islands', 'Colombia', 'Comoros', 'Congo', 'Congo (Democratic Republic of the)', 'Cook Islands', 'Costa Rica', 'Croatia', 'Cuba', 'Curaçao', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'Falkland Islands (Malvinas)', 'Faroe Islands', 'Fiji', 'Finland', 'France', 'French Guiana', 'French Polynesia', 'French Southern Territories', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Gibraltar', 'Greece', 'Greenland', 'Grenada', 'Guadeloupe', 'Guam', 'Guatemala', 'Guernsey', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Heard Island and McDonald Islands', 'Holy See', 'Honduras', 'Hong Kong', 'Hungary', 'Iceland', 'India', 'Indonesia', "Côte d'Ivoire", 'Iran (Islamic Republic of)', 'Iraq', 'Ireland', 'Isle of Man', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jersey', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Kuwait', 'Kyrgyzstan', "Lao People's Democratic Republic", 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macao', 'Macedonia (the former Yugoslav Republic of)',
#              'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Martinique', 'Mauritania', 'Mauritius', 'Mayotte', 'Mexico', 'Micronesia (Federated States of)', 'Moldova (Republic of)', 'Monaco', 'Mongolia', 'Montenegro', 'Montserrat', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Caledonia', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Niue', 'Norfolk Island', "Korea (Democratic People's Republic of)", 'Northern Mariana Islands', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Palestine, State of', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Pitcairn', 'Poland', 'Portugal', 'Puerto Rico', 'Qatar', 'Republic of Kosovo', 'Réunion', 'Romania', 'Russian Federation', 'Rwanda', 'Saint Barthélemy', 'Saint Helena, Ascension and Tristan da Cunha', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Martin (French part)', 'Saint Pierre and Miquelon', 'Saint Vincent and the Grenadines', 'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Sint Maarten (Dutch part)', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'South Georgia and the South Sandwich Islands', 'Korea (Republic of)', 'South Sudan', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'Svalbard and Jan Mayen', 'Swaziland', 'Sweden', 'Switzerland', 'Syrian Arab Republic', 'Taiwan', 'Tajikistan', 'Tanzania, United Republic of', 'Thailand', 'Timor-Leste', 'Togo', 'Tokelau', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Turks and Caicos Islands', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom of Great Britain and Northern Ireland', 'United States of America', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Venezuela (Bolivarian Republic of)', 'Viet Nam', 'Wallis and Futuna', 'Western Sahara', 'Yemen', 'Zambia', 'Zimbabwe']

# CAPITALS = {'Afghanistan': 'Kabul', 'Åland Islands': 'Mariehamn', 'Albania': 'Tirana', 'Algeria': 'Algiers', 'American Samoa': 'Pago Pago', 'Andorra': 'Andorra la Vella', 'Angola': 'Luanda', 'Anguilla': 'The Valley', 'Antarctica': '', 'Antigua and Barbuda': "Saint John's", 'Argentina': 'Buenos Aires', 'Armenia': 'Yerevan', 'Aruba': 'Oranjestad', 'Australia': 'Canberra', 'Austria': 'Vienna', 'Azerbaijan': 'Baku', 'Bahamas': 'Nassau', 'Bahrain': 'Manama', 'Bangladesh': 'Dhaka', 'Barbados': 'Bridgetown', 'Belarus': 'Minsk', 'Belgium': 'Brussels', 'Belize': 'Belmopan', 'Benin': 'Porto-Novo', 'Bermuda': 'Hamilton', 'Bhutan': 'Thimphu', 'Bolivia (Plurinational State of)': 'Sucre', 'Bonaire, Sint Eustatius and Saba': 'Kralendijk', 'Bosnia and Herzegovina': 'Sarajevo', 'Botswana': 'Gaborone', 'Bouvet Island': '', 'Brazil': 'Brasília', 'British Indian Ocean Territory': 'Diego Garcia', 'United States Minor Outlying Islands': '', 'Virgin Islands (British)': 'Road Town', 'Virgin Islands (U.S.)': 'Charlotte Amalie', 'Brunei Darussalam': 'Bandar Seri Begawan', 'Bulgaria': 'Sofia', 'Burkina Faso': 'Ouagadougou', 'Burundi': 'Bujumbura', 'Cambodia': 'Phnom Penh', 'Cameroon': 'Yaoundé', 'Canada': 'Ottawa', 'Cabo Verde': 'Praia', 'Cayman Islands': 'George Town', 'Central African Republic': 'Bangui', 'Chad': "N'Djamena", 'Chile': 'Santiago', 'China': 'Beijing', 'Christmas Island': 'Flying Fish Cove', 'Cocos (Keeling) Islands': 'West Island', 'Colombia': 'Bogotá', 'Comoros': 'Moroni', 'Congo': 'Brazzaville', 'Congo (Democratic Republic of the)': 'Kinshasa', 'Cook Islands': 'Avarua', 'Costa Rica': 'San José', 'Croatia': 'Zagreb', 'Cuba': 'Havana', 'Curaçao': 'Willemstad', 'Cyprus': 'Nicosia', 'Czech Republic': 'Prague', 'Denmark': 'Copenhagen', 'Djibouti': 'Djibouti', 'Dominica': 'Roseau', 'Dominican Republic': 'Santo Domingo', 'Ecuador': 'Quito', 'Egypt': 'Cairo', 'El Salvador': 'San Salvador', 'Equatorial Guinea': 'Malabo', 'Eritrea': 'Asmara', 'Estonia': 'Tallinn', 'Ethiopia': 'Addis Ababa', 'Falkland Islands (Malvinas)': 'Stanley', 'Faroe Islands': 'Tórshavn', 'Fiji': 'Suva', 'Finland': 'Helsinki', 'France': 'Paris', 'French Guiana': 'Cayenne', 'French Polynesia': 'Papeetē', 'French Southern Territories': 'Port-aux-Français', 'Gabon': 'Libreville', 'Gambia': 'Banjul', 'Georgia': 'Tbilisi', 'Germany': 'Berlin', 'Ghana': 'Accra', 'Gibraltar': 'Gibraltar', 'Greece': 'Athens', 'Greenland': 'Nuuk', 'Grenada': "St. George's", 'Guadeloupe': 'Basse-Terre', 'Guam': 'Hagåtña', 'Guatemala': 'Guatemala City', 'Guernsey': 'St. Peter Port', 'Guinea': 'Conakry', 'Guinea-Bissau': 'Bissau', 'Guyana': 'Georgetown', 'Haiti': 'Port-au-Prince', 'Heard Island and McDonald Islands': '', 'Holy See': 'Rome', 'Honduras': 'Tegucigalpa', 'Hong Kong': 'City of Victoria', 'Hungary': 'Budapest', 'Iceland': 'Reykjavík', 'India': 'New Delhi', 'Indonesia': 'Jakarta', "Côte d'Ivoire": 'Yamoussoukro', 'Iran (Islamic Republic of)': 'Tehran', 'Iraq': 'Baghdad', 'Ireland': 'Dublin', 'Isle of Man': 'Douglas', 'Israel': 'Jerusalem', 'Italy': 'Rome', 'Jamaica': 'Kingston', 'Japan': 'Tokyo', 'Jersey': 'Saint Helier', 'Jordan': 'Amman', 'Kazakhstan': 'Astana', 'Kenya': 'Nairobi', 'Kiribati': 'South Tarawa', 'Kuwait': 'Kuwait City', 'Kyrgyzstan': 'Bishkek', "Lao People's Democratic Republic": 'Vientiane', 'Latvia': 'Riga', 'Lebanon': 'Beirut', 'Lesotho': 'Maseru', 'Liberia': 'Monrovia', 'Libya': 'Tripoli', 'Liechtenstein': 'Vaduz',
#             'Lithuania': 'Vilnius', 'Luxembourg': 'Luxembourg', 'Macao': '', 'Macedonia (the former Yugoslav Republic of)': 'Skopje', 'Madagascar': 'Antananarivo', 'Malawi': 'Lilongwe', 'Malaysia': 'Kuala Lumpur', 'Maldives': 'Malé', 'Mali': 'Bamako', 'Malta': 'Valletta', 'Marshall Islands': 'Majuro', 'Martinique': 'Fort-de-France', 'Mauritania': 'Nouakchott', 'Mauritius': 'Port Louis', 'Mayotte': 'Mamoudzou', 'Mexico': 'Mexico City', 'Micronesia (Federated States of)': 'Palikir', 'Moldova (Republic of)': 'Chișinău', 'Monaco': 'Monaco', 'Mongolia': 'Ulan Bator', 'Montenegro': 'Podgorica', 'Montserrat': 'Plymouth', 'Morocco': 'Rabat', 'Mozambique': 'Maputo', 'Myanmar': 'Naypyidaw', 'Namibia': 'Windhoek', 'Nauru': 'Yaren', 'Nepal': 'Kathmandu', 'Netherlands': 'Amsterdam', 'New Caledonia': 'Nouméa', 'New Zealand': 'Wellington', 'Nicaragua': 'Managua', 'Niger': 'Niamey', 'Nigeria': 'Abuja', 'Niue': 'Alofi', 'Norfolk Island': 'Kingston', "Korea (Democratic People's Republic of)": 'Pyongyang', 'Northern Mariana Islands': 'Saipan', 'Norway': 'Oslo', 'Oman': 'Muscat', 'Pakistan': 'Islamabad', 'Palau': 'Ngerulmud', 'Palestine, State of': 'Ramallah', 'Panama': 'Panama City', 'Papua New Guinea': 'Port Moresby', 'Paraguay': 'Asunción', 'Peru': 'Lima', 'Philippines': 'Manila', 'Pitcairn': 'Adamstown', 'Poland': 'Warsaw', 'Portugal': 'Lisbon', 'Puerto Rico': 'San Juan', 'Qatar': 'Doha', 'Republic of Kosovo': 'Pristina', 'Réunion': 'Saint-Denis', 'Romania': 'Bucharest', 'Russian Federation': 'Moscow', 'Rwanda': 'Kigali', 'Saint Barthélemy': 'Gustavia', 'Saint Helena, Ascension and Tristan da Cunha': 'Jamestown', 'Saint Kitts and Nevis': 'Basseterre', 'Saint Lucia': 'Castries', 'Saint Martin (French part)': 'Marigot', 'Saint Pierre and Miquelon': 'Saint-Pierre', 'Saint Vincent and the Grenadines': 'Kingstown', 'Samoa': 'Apia', 'San Marino': 'City of San Marino', 'Sao Tome and Principe': 'São Tomé', 'Saudi Arabia': 'Riyadh', 'Senegal': 'Dakar', 'Serbia': 'Belgrade', 'Seychelles': 'Victoria', 'Sierra Leone': 'Freetown', 'Singapore': 'Singapore', 'Sint Maarten (Dutch part)': 'Philipsburg', 'Slovakia': 'Bratislava', 'Slovenia': 'Ljubljana', 'Solomon Islands': 'Honiara', 'Somalia': 'Mogadishu', 'South Africa': 'Pretoria', 'South Georgia and the South Sandwich Islands': 'King Edward Point', 'Korea (Republic of)': 'Seoul', 'South Sudan': 'Juba', 'Spain': 'Madrid', 'Sri Lanka': 'Colombo', 'Sudan': 'Khartoum', 'Suriname': 'Paramaribo', 'Svalbard and Jan Mayen': 'Longyearbyen', 'Swaziland': 'Lobamba', 'Sweden': 'Stockholm', 'Switzerland': 'Bern', 'Syrian Arab Republic': 'Damascus', 'Taiwan': 'Taipei', 'Tajikistan': 'Dushanbe', 'Tanzania, United Republic of': 'Dodoma', 'Thailand': 'Bangkok', 'Timor-Leste': 'Dili', 'Togo': 'Lomé', 'Tokelau': 'Fakaofo', 'Tonga': "Nuku'alofa", 'Trinidad and Tobago': 'Port of Spain', 'Tunisia': 'Tunis', 'Turkey': 'Ankara', 'Turkmenistan': 'Ashgabat', 'Turks and Caicos Islands': 'Cockburn Town', 'Tuvalu': 'Funafuti', 'Uganda': 'Kampala', 'Ukraine': 'Kiev', 'United Arab Emirates': 'Abu Dhabi', 'United Kingdom of Great Britain and Northern Ireland': 'London', 'United States of America': 'Washington, D.C.', 'Uruguay': 'Montevideo', 'Uzbekistan': 'Tashkent', 'Vanuatu': 'Port Vila', 'Venezuela (Bolivarian Republic of)': 'Caracas', 'Viet Nam': 'Hanoi', 'Wallis and Futuna': 'Mata-Utu', 'Western Sahara': 'El Aaiún', 'Yemen': "Sana'a", 'Zambia': 'Lusaka', 'Zimbabwe': 'Harare'}

# matcher = PhraseMatcher(nlp.vocab)
# matcher.add("COUNTRY", list(nlp.pipe(COUNTRIES)))


# @Language.component("countries_component")
# def countries_component_function(doc):
#     matches = matcher(doc)
#     print(matches)
#     doc.ents = [Span(doc, start, end, label="GPE")
#                 for match_id, start, end in matches]
#     return doc


# nlp.add_pipe("countries_component")

# print(nlp.pipe_names)


# def get_capital_function(span):
#     return CAPITALS.get(span.text)


# Span.set_extension("capitals", getter=get_capital_function)

# doc = nlp("ODI worldcup won by Australia 5 times ,India and WestIndies by 2 times,both Pakistan and Sri Lanka teams once each time")
# print([(ent.text, ent.label_, ent._.capitals) for ent in doc.ents])

# print("-------------------------------------------->>>>>>>>>>>>>>>>>>>>-------")

# nlp = spacy.load("en_core_web_sm")
# data = [
#     ("Hii my name is Ram", {"student_id": 101, "Hometown": "kakinada"}),
#     ("Hii my name is Syam", {"student_id": 102, "Hometown": "Sarpavaram"}),
#     ("hii my name is Deepak", {"student_id": 103, "Hometown": "Banugudi"})
# ]
# for doc, context in list(nlp.pipe(data, as_tuples=True)):
#     print(doc.text, context["student_id"])

# print([(doc.text, context["Hometown"])
#       for doc, context in list(nlp.pipe(data, as_tuples=True))])

# print('--------------------------------------')
import spacy
nlp = spacy.load("en_core_web_sm")
from spacy.tokens import Token,Span,Doc
data = [
    ("Hii my name is Ram", {"student_id": 101, "Hometown": "kakinada"}),
    ("Hii my name is Syam", {"student_id": 102, "Hometown": "Sarpavaram"}),
    ("hii my name is Deepak", {"student_id": 103, "Hometown": "Banugudi"})
]
Doc.set_extension("student_id", default=None)
Doc.set_extension("Hometown", default=None)

for doc, context in nlp.pipe(data,as_tuples=True):
    doc._.student_id = context["student_id"]
    doc._.Hometown = context["Hometown"]
    print(doc.text,doc._.student_id,doc._.Hometown)

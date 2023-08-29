# regex or regular expression(sequence of words to search) is nothing but a search pattern to check in a string
# to work with regular expresions we have to import a module named re
import re
txt = "ODI Worldcup is an event held by ICC for every 04 years and INDIA won twice this event in 1983 and 2011 ODI"
# #----------SETS[]-------------

print(re.findall("[a-h]",txt)) # [] set, [a-h] gives list of matched characters only between a-h in given txt string
print(re.findall("[bcdfW]",txt)) #gives list of specified matched characters only b,c,d,f,W in given txt
print(re.findall("[^bcdfW]",txt)) # gives list of matched characters except b,c,d,f,W in given txt
print(re.findall("[123]",txt)) #gives specified matched numbers from txt if no match returns empty list
print(re.findall("[01234]",txt)) #gives match
print(re.findall("[0-9]",txt)) #gives any match digit between 0-9
print(re.findall("[a-zA-Z0-9]",txt)) #gives matches between lower a-z and upper A-Z and also 0-9
print(re.findall("[2-2][0-9][0-9][0-9]",txt)) # here matches only between 2000-2999 not before 2000 thatswhy 1983 is not printed in op result

# #----------Metacharacters------------

print(re.findall("\AODI",txt)) #gives match if txt starts with given match---\A
print(re.findall("ODI\Z",txt)) #gives match if txt ends with given match---\A
print(re.findall("\AOdi",txt)) #gives no match and results empty list
print("-----------")
print(re.findall(r"\bent",txt)) # \bent gives match list if any word in string starts with ent else empty list
print(re.findall(r"ent\b",txt)) # ent\b gives match list if any word in string ends with ent else empty list
print(re.findall(r"\Bent",txt)) # \Bent gives match if ent present but doesn't start with ent 
print(re.findall(r"ent\B",txt)) # ent\B gives match if ent present but not in end position
print("-----------")
print(re.findall("\d",txt)) #Returns a match where the string contains digits (numbers from 0-9)
print(re.findall("\d\d",txt))
print(re.findall("\d[2-5]",txt))
print(re.findall("\d\d[0-5][0-5]",txt))
print("-----------")
print(re.findall("\D",txt)) #Returns a match where the string DOES NOT contain digits

print(re.findall("\s",txt)) #Returns a match where the string contains a white space character
print(re.findall("\S",txt)) #Returns a match where the string DOES NOT contain a white space character
print(re.findall("\w",txt)) #Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)
print(re.findall("\W",txt)) #Returns a match where the string DOES NOT contain any word characters

print(re.findall("^hello","hello world")) # ['hello'] gives match if start with ^hello 
print(re.findall("world$","hello world")) #['world'] gives match if ends with world$
print(re.findall("he..o","hello world"))  #['hello'] gives if match start with he..(any two characters) and ends with o -->hello
print(re.findall("he.*o","helllllllo world")) #zero or more occurances
print(re.findall("he.+o","helllllllo world")) #one or more occurance
print(re.findall("he.?o","hello world")) #zero or one occurance
print(re.findall("he.?o","helo world"))
print(re.findall("he.{6}o","hellllllo world")) #exact no of occurances mentioned {6}
print(re.findall("INDIA|PAKISTAN","there is a match between INDIA and AUSTRALIA tonight.")) #gives either one or Two matched values













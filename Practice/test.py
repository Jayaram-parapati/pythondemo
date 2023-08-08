#capitalizemethod()
txt = "india won worldcup in 1983"
print(txt.capitalize())
#casefold()
txt = "India Won WorldCup In 1983"
print(txt.casefold())
#center()
txt = "India"
print(txt.center(10,"$"))
#endswith()
txt = "india won worldcup in 1983"
print(txt.endswith("cup"))
#expandtabs()
txt="h\te\tl\tl\to"
print(txt.expandtabs(10))
#find()
txt = "india won worldcup in 1983"
print(txt.find("c"))
#format()
#named indexes:
txt1 = "My name is {fname}, I'm {age}"
print(txt1.format(fname = "John", age = 36))
#numbered indexes:
txt2 = "My name is {0}, I'm {1}"
print(txt2.format("John",36))
#empty placeholders:)
txt3 = "My name is {}, I'm {}"
print(txt3.format("John",36))
#isalnum()
txt = "Company12"
x = txt.isalnum()
print(x)
#ljust() 
txt = "banana"
x = txt.ljust(20, "O")
print(x)
#rjust()
txt = "banana"
x = txt.rjust(20, "O")
print(x)
#lstrp and rstrip
txt = "     banana     "
x = txt.lstrip()
print("of all fruits", x, "is my favorite")
#
txt = "     banana     "
x = txt.rstrip()
print("of all fruits", x, "is my favorite")
#
#
txt = ".,,.,.ghj...banana..,.,.,ghj     "
x = txt.lstrip(",.ghj")
print(x)
#
txt = ".,,.,.ghj...banana..,.,.,ghj"
x = txt.rstrip(",.ghj")
print(x)
#split()
txt = "apple#banana#cherry#orange"
x = txt.split("#")
print(x)
#split()
txt = "apple#banana#cherry#orange"
x = txt.split("#",2)
print(x)
#split()
txt = "apple#banana#cherry#orange"
x = txt.split("#",1)
print(x)
#swapcase()
txt = "Hello My Name Is PETER"
x = txt.swapcase()
print(x)
#loops

#
def myfun(*kids):
    print("younger one is" + kids[len(kids)-1])

    myfun("Emil", "Tobias", "Linus")
    
    
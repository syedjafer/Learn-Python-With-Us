# Let's learn more about string related methods.


mystring = "welcome"
total_amount=1000

# capitalize 
print("capitalized: ",mystring.capitalize())

# upper
print("upper cased: ",mystring.upper())


# lower
print("Lower cased: ","WelCome".lower())

# isalnum
print("Checking alphanumeric: ",mystring.isalnum())

# istitle
print("mystring is title: ",mystring.istitle())
print("TheWord is title: ","The Word".istitle())

# center
print("center my text to 20 char: ", mystring.center(10))
print("center my text to 20 char with fill char: ", mystring.center(20,"-"))

# count
print("count of e in word: ",mystring.count("e"))

# split
print("this is the split output: ","hi there paramesh".split("e"))

#print(dir("S"))
#print(len([item for item in dir("s") if "_" not in item]))

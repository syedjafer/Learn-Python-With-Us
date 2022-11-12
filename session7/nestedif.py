# Nested if can be used when we need to make decision after decision on a same criteria

#balu task 1
is_pass = int(input("You passed examination: "))

if is_pass:
    if int(input("Are you passed with distinction: ")):
        if int(input("Are you in top 2 students: ")): 
            print("Gold medal with First class distinction")
        else:
            print("First class with distinction")
    else:
        print("Degree graduate")
else:
    print("Soon to be graduate")

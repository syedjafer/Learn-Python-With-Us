# if else ladder can be used  if you have multiple decisions and multiple outcomes


mark = int(input("Enter your marks: "))

if mark<=45:
    print("Fail!!!")
elif mark >45 and mark <=60:
    print("Grade D")
elif mark >60 and mark <=70:
    print("Grade C")
elif mark >70 and mark <=80:
    print("Grade B")
elif mark >80 and mark <=90:
    print("Grade A")
elif mark >90 and mark <=100:
    print("Grade S")
else:
    print("Invalid Mark")

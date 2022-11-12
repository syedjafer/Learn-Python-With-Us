# If statements are good for checking only one condition


#score = int(input("Enter your score :"))
#Best_performer = int(input("Are you a best performer (1/0): "))
#
#if Best_performer:
#    print("ok best performer")
#    score+=100
#
#print("Your final score: ", score)
#

# if else statements are good when we have to do one if the condition pass and another task when condition not statisfied

is_puratasi = int(input("Is this month puratasi (1/0): "))

if is_puratasi:
    print("Only Veg meals my boy!!")
else:
    print("Biriyani")



# Slicing

# List[start:end:step]

# fruits = ['apple', 'papaya', 'banana', 'orange', 'pear', 'lemon']
        #    0        1         2          3       4        5
# print(id(fruits))
# fruits[2] = 'd'
# print(  id(fruits) , id(fruits[1:4]), fruits[1:4])

# print(fruits[:])
#
#
# name = "kanchilug"
# print(name[1], name[:])


fruits = ['apple', 'papaya', 'banana', 'orange', 'pear', 'lemon']
# print(fruits[0:5:1], fruits[0:5])
print(fruits[-1:-5:1], fruits[0:5])

print(fruits[::-1])
name = "kanchilug"
print(name[1], name[::-1])

### 1st Approach
# x = input("What's x? ")
# y = input("What's y? ")
# z = int(x) + int(y)
#
# print(z)



### 2nd Approach
# x = int(input("What's x? "))
# y = int(input("What's y? "))
#
# print(x+y)

### float
x = float(input("What's x? "))
y = float(input("What's y? "))
z = x / y
# z = round(x/y, 2)   # x = 2, y = 3, round to the nearest 2 decimal places


# print(f"{z:,}") # automatic formatting with commas
print(f"{z:.2f}")   # using f string to print 2 decimal places

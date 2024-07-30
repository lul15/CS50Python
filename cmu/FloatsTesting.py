"""
Parallel, aka Tuple Assignment
"""
x, y = 2, 3
print(x)
print(y)

x, y = y, x
print(x)
print(y)    # this only works bc values on right hand side are computed before varibles are assigne on the left in parallel assignment

## Floats
x = 0.1 + 0.2
print(x)    # 0.30000000000000004


print(0.1 + 0.2 == 0.3) # False, thus never use == with floats (they are approximations), instead use 'almostEqual' function

"""
Expressions vs Statements
variable = expression, expression is any value that can be assigned to a variable, function calls
statement is an action / command, assignment statement, or conditional statement, or function definition
Python program consists of statements, and statements generally use expressions
All expressions ARE statements, but most statements are NOT expressions
"""

n = 726
print(n % 2)
n += 1
print(n % 2)
print(n / 10)
n //= 10
print(n)


import math
# Hints:
# str(52) converts the integer 52 into the string '52'
# int('52') converts the string '52' into the integer 52

m = 42
n = m / 1
print(type(m) == int, type(n) == int)   # True, False (float)
x = int(2 * str(2 * int('2'))) + 2  #44 + 2 = 46
b = (x%2 == 1)  #False
print(x, b)     #4, False
print(int(b), int(not b))   #4, 1

# x = int(2 * str(2 * int('2'))) + 2
# y = int('44') + 2
# print(x, y)
# print(2 * '4')

print(1 * 2 // 1 + 4 - 3)   #1
print(2**4/10 + (3 + 2**3) // 10)   #2.6
print(round(8/3) + max(8/3, math.ceil(8/3)))  #3 + 3 = 6

print(float(1 * '4'))   #4.0
print(float('1' + '3')) #13.0
print(int('1' * 3))    #111
print(type(int('4') * '3'))  #3333 (type string)

def almostEqual(first, second):
    result = (abs(first - second) < 1e-9)
    return result

a = (0.3 * 3) + 0.1
b = 1
print(almostEqual(a,b))
print(1e-3)
print(round(2.5))

# i = 3
# while i != 0:
#     print("meow")
#     i = i -1

# i = 1
# while i <= 3:
#     print("meow")
#     i = i + 1

# for i in range(5):
#     print("meow")

# utilize the underscore _ for variable that exists only for counting
# and will not be used later
# for _ in range(6):
#     print("woof")

# print("meow\n" * 3, end="")

# while True:
#     n = int(input("What's n? "))
#     if n > 0:
#         break
#
# for _ in range(n):
#     print("meow")


def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            break
    return n

def meow(n):
    for _ in range(n):
        print("meow")

main()

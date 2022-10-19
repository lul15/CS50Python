# name = input("What's your name? ")

# open and close file
# file = open("names.txt", "a")
# file.write(f"{name}\n")
# file.close()

# pythonic approach, automatically open and close file
# with open("names.txt", "a") as file:
#     file.write(f"{name}\n")

# read from file
# with open("names.txt", "r") as file:
#     lines = file.readlines()
#
# for line in lines:
#     print("hello,", line.rstrip())

# condensed version of the block above, can read and print
# with open("names.txt", "r") as file:
#     for line in file:
#         print("hello,", line.rstrip())

names = []

### STRINGS
# Ask user for their name as input
name = input("What's your name? ")

# Remove whitespace from string and capitalize the user's name
name = name.strip().title()

# Split user's name into first name and last name
first, last = name.split(" ")

# Say hello to user, the options below all produce the same output
# print("hello, " + name)
# print("hello,", name)
# print("hello, ", end="") #overrode the default behavior end of line
# print(name)

# Newer way of printing - formatted string
print(f"hello, {first}")

#To print the quotations marks
# print('hello, "friend"')
# print("hello, \"friend\"")


# Ask user for their name as input
name = input("What's your name? ")

#Remove whitespace from string
name = name.strip()

# Say hello to user, the options below all produce the same output
print("hello, " + name)
print("hello,", name)
print("hello, ", end="") #overrode the default behavior end of line
print(name)

# Newer way of printing - formatted string
print(f"hello, {name}")

#To print the quotations marks
print('hello, "friend"')
print("hello, \"friend\"")

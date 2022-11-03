import re


email = input("What's your email? ").strip()

if re.search(r".+@.+\.edu", email):
    print("Valid")
else:
    print("Invalid")



# # 2nd iteration
# username, domain = email.split("@")
# if username and domain.endswith(".edu"):
#     print("Valid")
# else:
#     print("Invalid")


# # 1st iteration - rudimentary validation
# if "@" in email and "." in email:
#     print("Valid")
# else:
#     print("Invalid")

import re


email = input("What's your email? ").strip()




# 4th iteration - built in, utilizing the alphanumeric
# passed flag for case-insensitivity
# part of the substring optional  (?)
if re.search(r"^\w+@(\w+\.)?\w+\.(com|edu|gov|net|org)$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")


# # 3rd iteration - specify beginning and end
# # then specify the letters allowed
# if re.search(r"^[a-zA-Z-9_]+@[a-zA-Z-9_]+\.edu$", email):
#     print("Valid")
# else:
#     print("Invalid")


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

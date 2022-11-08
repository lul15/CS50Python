import re

name = input("What's your name? ").strip()

# capture groups (starts with index 1)
# matches = re.search(r"^(.+), *(.+)$", name)

# := walrus operator (assignment expression operator)
if matches := re.search(r"^(.+), *(.+)$", name):
    name = matches.group(2) + " " + matches.group(1)
print(f"hello, {name}")

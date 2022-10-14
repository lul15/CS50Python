import sys

#sys.argv = argument vector (list)

### Approach 1
# try:
#     print("hello, my name is", sys.argv[1])
# except IndexError:
#     print("Too few arguments")

### Approach 2
# if len(sys.argv) < 2:
#     print("Too few arguments")
# elif len(sys.argv) > 2:
#     print("Too many arguments")
# else:
#     print("hello, my name is", sys.argv[1])

### Approach 3
# if len(sys.argv) < 2:
#     sys.exit("Too few arguments")
# elif len(sys.argv) > 2:
#     sys.exit("Too many arguments")
#
# # By the time it gets here, can be assured that it would have exited for wrong cases
# print("hello, my name is", sys.argv[1])

### Approach 4
if len(sys.argv) < 2:
    sys.exit("Too few arguments")
# adding slicing
for arg in sys.argv[1:]:
    print("hello, my name is", arg)

#PyPI - pypi.org (python package index)

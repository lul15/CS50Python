# def countdown(i):
#     print(i)
#     if i <= 1:
#         return
#     else:
#         countdown(i-1)
#
# countdown(3)


def greet(name):
    print("hello, " + name + "!")
    greet2(name)
    print("getting ready to say bye...")
    bye()


def greet2(name):
    print("how are you, " + name + "?")

def bye():
    print("ok bye! ")

greet("maggie")

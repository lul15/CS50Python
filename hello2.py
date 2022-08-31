def main():
    hello() # print it with the default value
    name = input("What's your name? ")
    hello(name)

def hello(to="world"):  # custom function, with default value "world"
    print("hello,", to)

main()

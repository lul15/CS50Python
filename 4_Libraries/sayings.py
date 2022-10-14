def main():
    hello("world")
    goodbye("world")

def hello(name):
    print(f"Hello, {name}")

def goodbye(name):
    print(f"Goodbye, {name}")

# set the conditional for this to run only when called directly from commandline.
# Otherwise takes on the name of the module where it is imported
if __name__ == "__main__":
    main()

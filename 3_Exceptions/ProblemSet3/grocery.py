def main():
    grocery_list = get_items()
    pretty_print(grocery_list)

def get_items():
    groceries = {}
    while True:
        try:
            item = input().strip().upper()
            if item in groceries:
                groceries[item] = groceries.get(item) + 1
            else:
                groceries[item] = 1
        except EOFError:
            break
    return groceries

def pretty_print(items):
    #sort by alphabetical order and leave in dictionary
    sorted_items = dict(sorted(items.items()))

    #print the value, follow by keys
    for key, value in sorted_items.items():
        print(f"{value} {key}")

if __name__ == "__main__":
    main()

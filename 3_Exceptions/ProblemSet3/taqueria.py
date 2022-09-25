def main():
    item = get_cost("Item: ")

def get_cost(prompt):
    menu = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    total = 0
    while True:
        try:
            item = input(prompt).strip().title()
            cost = menu[item]
        except KeyError:
            pass
        except EOFError:
            break
        else:
            total = total + cost
            print(f"Total: ${total:.2f}")

if __name__ == "__main__":
    main()

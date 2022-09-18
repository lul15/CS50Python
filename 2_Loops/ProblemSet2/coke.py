def main():
    amt = 50
    print("Amount Due:", amt)
    amount_remaining(amt)

def amount_remaining(due):
    while due > 0:
        inserted = int(input("Insert Coin: "))
        match inserted:
            case 25 |10 | 5:
                due = due - inserted
            case _:
                due = due
        if due > 0:
            print("Amount Due:", due)
        else:
            print("Change owed:", abs(due))

main()

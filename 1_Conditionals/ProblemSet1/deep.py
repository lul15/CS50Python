def main():
    answer = input("What is the Answer to the Greatest Question of LIfe, the Universe, and Everything? ").lower().strip()

    match answer:
        case "42" | "forty-two" | "forty two":
            print("Yes")
        case _:
            print("No")

main()

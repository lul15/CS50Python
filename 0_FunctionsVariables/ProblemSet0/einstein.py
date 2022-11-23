def main():
    mass = int(input("m: "))
    print(f"E: {calculate_joules(mass)}")


def calculate_joules(m):
    return m * pow(300000000, 2)


if __name__ == "__main__":
    main()

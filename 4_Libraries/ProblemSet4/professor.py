import random


def main():
    level = get_level()
    total_correct = 0
    for i in range(10):
        numX = generate_integer(level)
        numY = generate_integer(level)
        ans = numX + numY
        response = int(input(f"{numX} + {numY} = "))
        count = 0
        if ans == response:
            total_correct = total_correct + 1
        else:
            while ans != response:
                print("EEE")
                count = count + 1
                if count == 3:
                    print(f"{numX} + {numY} = {ans}")
                    break
                response = int(input(f"{numX} + {numY} = "))
    print(f"Score: {total_correct}")


def get_level():
    while True:
        try:
            lvl = int(input("Level: "))
            if 1 <= lvl <= 3:
                return lvl
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        lower = 0
    else:
        lower = 10 ** (level - 1)

    upper = (10 ** level) - 1
    num = random.randint(lower, upper)
    return num


if __name__ == "__main__":
    main()

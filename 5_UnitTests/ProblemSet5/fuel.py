def main():
    while True:
        try:
            fraction = input("Fraction: ")
            percentage = convert(fraction)
            fuel = gauge(percentage)
            print(fuel)
            break
        except (ValueError, ZeroDivisionError):
            pass



def convert(fraction):
    x, y = fraction.split("/")
    fuel = int(x) / int(y)
    percentage = fuel * 100
    return percentage

def gauge(percentage):
    percentage_str = f"{round(percentage)}%"
    if 0 <= percentage <= 1:
        return "E"
    elif 99 <= percentage <= 100:
        return "F"
    elif 0 <= percentage <= 100:
        return percentage_str



if __name__ == "__main__":
    main()

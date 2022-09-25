def main():
    fuel = get_gauge("Fraction: ")
    print(f"{fuel}")

def get_gauge(prompt):
    while True:
        try:
            fraction = input(prompt)
            x, y = fraction.split('/')
            fuel = int(x) / int(y)
            percentage = fuel * 100
            percentage_str = f"{round(percentage)}%"
            if 0 <= percentage <= 1:
                return "E"
            elif 99 <= percentage <= 100:
                return "F"
            elif 0 <= percentage <= 100:
                return percentage_str
        except (ValueError, ZeroDivisionError):
            pass
main()

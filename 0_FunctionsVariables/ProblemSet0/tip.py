def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
    #remove leading '$'
    dollars = d[1:]
    #return element as float
    amt = float(dollars)
    return amt

def percent_to_float(p):
    #removing following '%'
    percent = p[:-1]
    per = float(percent) / 100
    return per

main()

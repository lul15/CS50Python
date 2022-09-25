def main():
    formatted_date = get_date("Date: ")
    print(formatted_date)

def get_date(prompt):
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]
    while True:
        try:
            standard_date, month, day, year = "", "", "", ""
            mid_endian = input(prompt).strip()
            #split into month, day, year
            if "/" in mid_endian:
                month, day, year = mid_endian.split("/")
            else:
                month, day, year = mid_endian.split(" ")
                #removing the comma
                day = day[:-1]
                #match the month actual month
                month = months.index(month) + 1

            month = int(month)
            day = int(day)

            if 1 <= month <= 12 and 1<= day <= 31:
                standard_date = f"{year}-{month:02d}-{day:02d}"
                return standard_date
            else:
                pass
        except ValueError:
            pass

if __name__ == "__main__":
    main()

import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches := re.search(
        r"^([0-1]?\d|[0-1]?\d:[0-5]\d) (AM|PM) to ([0-1]?\d|[0-1]?\d:[0-5]\d) (AM|PM)",
        s,
    ):
        start = reformat_time(matches.group(1), matches.group(2))
        end = reformat_time(matches.group(3), matches.group(4))
        return f"{start} to {end}"
    else:
        raise ValueError


def reformat_time(t, meridiem_indicator):
    if ":" in t:
        hour = t.split(":")[0]
        t_hr = int(hour)    #TODO - memory usage consideration, refactor
        if meridiem_indicator == "AM":
            if t_hr == 12:
                t_hr = 0
        else:
            if t_hr != 12:
                t_hr = t_hr + 12
        t_hr = "{:02d}".format(t_hr)
        t_min = t.split(":")[1]
    else:
        t = int(t)
        if meridiem_indicator == "AM":
            if t == 12:
                t_hr = 0
            else:
                t_hr = t
        else:
            if t == 12:
                t_hr = 12
            else:
                t_hr = t + 12
        t_hr = "{:02d}".format(t_hr)
        t_min = "00"
    return str(t_hr) + ":" + t_min


if __name__ == "__main__":
    main()

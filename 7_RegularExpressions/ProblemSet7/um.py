import re


def main():
    print(count(input("Text: ")))


def count(s):
    # findall - looks at all instances, and returns in a list
    if matches := re.findall(r"(^um)\W?| (\W?um\W+)", s.lower()):
        return len(matches)
    else:
        return 0


if __name__ == "__main__":
    main()

def main():
    tweet = input("Input: ").strip()
    result = shorten(tweet)
    print("Output:", result)


def shorten(word):
    result = ""
    for c in word:
        converted_char = c.lower()
        match converted_char:
            case "a" | "e" | "i" | "o" | "u":
                result = result + ""
            case _:
                result = result + c

    return result


if __name__ == "__main__":
    main()

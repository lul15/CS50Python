def main():
    tweet = input("Input: ").strip()
    result = remove_vowels(tweet)
    print("Output:", result)

def remove_vowels(input):
    result = ""
    for c in input:
        converted_char = c.lower()
        match converted_char:
            case "a" | "e" | "i" | "o" | "u":
                result = result + ""
            case _:
                result = result + c

    return result

main()

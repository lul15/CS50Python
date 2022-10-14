def main():
    names = get_names()
    print(print_lyrics(names))

def get_names():
    names = []
    while True:
        try:
            name = input("Name: ").strip()
            names.append(name)
        except EOFError:
            break
    return names

def print_lyrics(names):
    print("")
    lyric = "Adieu, adieu, to "
    result = ""
    if len(names) == 1:
        lyric = lyric + names[0]
    elif len(names) == 2:
        lyric = lyric + f"{names[0]} and {names[1]}"
    else:
        for name in names[:-1]:
            result = result + name + ", "
        result = result + f"and {names[-1]}"

    lyric = lyric + result
    return lyric

if __name__ == "__main__":
    main()

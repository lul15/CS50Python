import emoji

def main():
   alias = input("Input: ").strip()
   print("Output:", emoji.emojize(alias, language='alias'))

if __name__ == "__main__":
    main()

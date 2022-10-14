import random

def main():
    while True:
        try:
            level = int(input("Level: "))
            guess_game(level)
            break
        except ValueError:
            pass

def guess_game(n):
    num = random.randint(1, n)
    guess = 0
    while guess != num:
        guess = int(input("Guess: "))
        if guess < 0:
            continue
        elif guess < num:
            print("Too small!")
        elif guess > num:
            print("Too large!")
        else:
            break
    print("Just right!")

if __name__ == "__main__":
    main()

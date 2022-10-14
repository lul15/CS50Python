from pyfiglet import Figlet
import sys
import random

def main():
    if len(sys.argv) == 1:
        txt = input("Input: ").strip()
        random_text(txt)
    elif len(sys.argv) == 3 and (sys.argv[1] in ("-f", "--font")):
        print("sys.argv[1]:", sys.argv[1])
        figlet = Figlet()
        #retrieve the list of possible fonts
        fonts = figlet.getFonts()
        requested_font = sys.argv[2]
        if requested_font in fonts:
            txt = input("Input: ").strip()
            figlet.setFont(font=requested_font)
            print("Output:\n", figlet.renderText(txt))
        else:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")


def random_text(txt):
    figlet = Figlet()

    #retrieve the list of possible fonts
    fonts = figlet.getFonts()

    #randomly select a font
    random_font = random.choice(fonts)
    figlet.setFont(font=random_font)
    print("Output:", figlet.renderText(txt))


if __name__ == "__main__":
    main()

import sys
import os

from PIL import Image, ImageOps


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        # Right number of arguments, now check for wrong extensions
        ext1 = os.path.splitext(sys.argv[1])[-1].lower()
        ext2 = os.path.splitext(sys.argv[2])[-1].lower()
        extensions = [".jpg", ".jpeg", ".png"]
        if ext1 not in extensions:
            sys.exit("Invalid input")
        elif ext2 not in extensions:
            sys.exit("Invalid output")
        elif ext1 != ext2:
            sys.exit("Input and output have different extensions")
        else:
            # Extension validations complete, start overlay shirt
            overlay_shirt(sys.argv[1], sys.argv[2])


def overlay_shirt(file1, file2):
    try:
        shirt = Image.open("shirt.png")
        shirt_size = shirt.size
        img1 = Image.open(file1)
        fitted_img1 = ImageOps.fit(img1, size=shirt_size)
        fitted_img1.paste(shirt, mask=shirt)
        fitted_img1.save(file2)
    except FileNotFoundError:
        sys.exit("Input does not exist")


if __name__ == "__main__":
    main()

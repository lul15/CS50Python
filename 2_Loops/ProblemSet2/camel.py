def main():
    camelCase = input("camelCase: ").strip()
    convert_to_snake_case(camelCase)

def convert_to_snake_case(input):
    output = ""

    for c in input:
        if c.islower():
            output = output + c
        else:
            output = output + "_" + c.lower()
    print("snake_case:", output)

main()

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    #no periods, spaces, or punctuation marks allowed
    #max of 6 chars (letters or numbers) and min of 2 chars
    if 2 <= len(s) <= 6 and s.isalnum():
        # plates need start with at least two letters
        if s.isalpha():
            return True
        else:
            if s[0:2].isalpha():
             #numbers must be at the end, cannot start with 0
                #find first numeric digit
                first_digit = 0
                rem_str = s[2:]
                for i in range(len(rem_str)):
                    if rem_str[i].isnumeric():
                        # print("rem_str:", rem_str[i:])
                        first_digit = i
                        break
                # print("rem_str:", rem_str[first_digit])
                if rem_str[first_digit] != "0" and rem_str[first_digit:].isnumeric():
                    return True
    else:
        return False


main()

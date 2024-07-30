Given a mapping from digits to list of letters and a string of digits of arbitrary length determine all possible ways to replace the digits with letters.

Mapping = { '1' → ['A', 'B', 'C'], '2' → ['D', 'E', 'F'], ... } Input String = “12”

Expected Output = [“AD”, “AE”, “AF”, “BD”, “BE”, “BF”, “CD”, “CE”, “CF”]

output_1: [A, B, C], Input
output_2: [“AD”, “AE”, “AF”, “BD”, “BE”, “BF”, “CD”, “CE”, “CF”]
output_3: [ADA, ADB.., ], Input String = “121”


def digitsToLetters(mapping, input_str):
    output = []
    length_of_output = len(input_str)
    curr_output = ""

    # for each value in input_str, grab the corresponding list of characters
    for i in len(input_str):
        curr_digit = input_str(i)   #1
        list_of_chars = mapping.get(curr_digit) #[A,B,C]
        for j in len(list_of_chars):
            output.append(list_of_chars[j])

    # output.append(curr_output)

    # ex: 123 3--> ['X' , 'Y]
    #ADX, ADY, ...etc
    return output



----

Determine if any 3 integers in an array sum to 0.

[3, 5, 8, 10, -9, -11, 16, 2] => true // [3, 8, -11]

[3, 5, 4, 9, -16, -10] => false

[3, -3, 4, 8, -13] => false

#all unique values
#not sorted yet
#0 is possible

def sumToZero(inputs):
    # sort the inputs
    inputs.sort()
    #inputs = sorted(inputs)
    n = len(inputs)

    #Brute force approach: create combinations of 3 ints, take all their sums, if any is 0 --> True, otherwise False

    #if list of positives / list of all negatives --> false
    if input[0] > 0 and input[n-1] > 0:
        return false
    if input[0] < 0 and input[n-1] < 0:
        return false

    input_set = set(inputs)
    for i in inputs:
        curr = i #-11
        for j in range():
            elem1 = inputs[j]   #-9
            diff = curr + elem1 #-20
            elem2 = -1 * diff

            if elem2 in input_set:
                    return True

    return False


    #[-11, -9, 2, 3, 5, 8, 10, 16]


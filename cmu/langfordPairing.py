def is_langford_pairing(sequence):

    # helper function - find the number of digits in the input
    # convert sequence into a list
    num_list = []
    while sequence > 0:
        sequence, remainder = divmod(sequence, 10)
        num_list.insert(0, remainder)

    print(num_list)

    n = len(num_list) // 2
    # Get rid of the automatically False conditions
    if n % 4 == 1 or n % 4 == 2 or len(num_list) % 2 != 0:
        return False

    positions = [0] * (2 * n)

    for i in range(n):
        curr = num_list[i]
        # print("curr = ", curr)
        positions[i] = curr
        pair_position = i + (1 + curr)
        # print("pair_position = ", pair_position)
        if num_list[pair_position] == curr:
            positions[pair_position] = curr
        elif num_list[i - (1 + curr)] == curr:
            positions[i - (1 + curr)] = curr
        else:
            return False
        # print("positions = ", positions)

    return True


def main():
    print(is_langford_pairing(11))  # False
    print(is_langford_pairing(213142))  # False
    print(is_langford_pairing(231213))  # True
    print(is_langford_pairing(41312432))  # True


if __name__ == "__main__":
    main()

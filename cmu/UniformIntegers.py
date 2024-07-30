# Write any import statements here


def getUniformIntegerCountInInterval(A: int, B: int) -> int:

    # determine length of inputs
    i = A
    # end_length = len(str(B))
    res = 0

    while i <= B:
        # print("i = ", i)
        i_length = len(str(i))

        i_str = "1" * i_length
        i_num = int(i_str)
        # print("i_num = ", i_num)

        if i % i_num == 0:
            res += 1
            i = i + i_num
        else:
            rem = i % i_num
            diff = i_num - rem
            i += diff

    return res


def main():
    # test1 = getUniformIntegerCountInInterval(75, 300)
    # print("75, 300= ", test1)
    # test2 = getUniformIntegerCountInInterval(1, 9)
    # print("1, 9= ", test2)
    # test3 = getUniformIntegerCountInInterval(999999999999, 999999999999)
    # print("999999999999, 999999999999= ", test3)
    test4 = getUniformIntegerCountInInterval(1, 99999999999999999)
    print("1, 99999999999999999= ", test4)


if __name__ == "__main__":
    main()

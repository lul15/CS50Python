import math


def egpytianMultiplicaion(x, y):
    egyptMult = 0

    return egyptMult

# helper function
def getSumOfPowersOf2(n):
    if n <= 0:
        return f'{n} is not positive'
    powerOf2 = maxPowerOf2UpToN(n)
    if powerOf2 == n:
        return f'{n} is a power'
    if powerOf2 == n:
        sumSoFar = 0
    return result


def maxPowerOf2UpToN(n):
    result = 1
    while (2*result <= n):
        result *= 2
    return result

def testEgyptianMultiplication():
    assert egpytianMultiplicaion(11, 5) == 55


def main():
    testEgyptianMultiplication()


main()

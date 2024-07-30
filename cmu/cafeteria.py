from typing import List
import math

# Write any import statements here


def getMaxAdditionalDinersCount(N: int, K: int, M: int, S: List[int]) -> int:
    # Write your code here
    """
    N= Number of seats
    K = social distance
    M = current seated diners
    S = seated indices

    ex1:
    N= 10
    k = 1
    S = [2,6]
    """
    # Sort S
    S.sort()

    # from edge: 2k+1, remainder divide by k+1
    distance = (
        K + 1
    )  # social distance required, +1 (for the seat the diner is to occupy)
    S.append(N + distance)  # ensure it doesn't get OutofBounderror
    additional_diners = 0
    start = 1
    i = 0
    """
  while i < len(S): 
    r = S[i] - start - distance
    if r < 0: 
      start = S[i] + distance
      i += 1
    else: 
      additional_diners += 1
      start += distance
  """

    for s in S:
        r = s - start - distance
        print(r)
        if r >= 0:
            additional_diners += math.floor(r / distance) + 1
        start += distance

    return additional_diners


def main():
    test1 = getMaxAdditionalDinersCount(N=10, K=1, M=2, S=[2, 6])   #3
    print("test1=", test1)
    test2= getMaxAdditionalDinersCount(N=15, K=2, M=3, S=[11, 6, 14])   #1
    print("test2=", test2)


if __name__ == "__main__":
    main()

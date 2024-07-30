def binary_search(arr, item):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]

        if item == guess:
            return mid
        elif item < guess:
            high = mid -1
        else:
            low = mid + 1
    return None



#Test Cases
arr1 = [1,2,3,4,5]
item1 = 4
res1 = binary_search(arr1, item1)   #3
print(res1)

item2 = -1
res2 = binary_search(arr1, item2)   #None
print(res2)

item3 = 10
res3 = binary_search(arr1, item3)   #None
print(res3)

arr2 = [1,2,6,9,15]
item4 = 4
res4 = binary_search(arr2, item4)   #None
print(res4)

# Refactor test cases
print(binary_search(arr2, 15))  #4
print(2**30)

#selectionSort --> O(n^2)

#find the smallest element
def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

#selectionSort
def selectionSort(arr):
    newArr = []
    copiedArr = list(arr)   # coopy array before editing
    for i in range(len(copiedArr)):
        smallest = findSmallest(copiedArr)
        newArr.append(copiedArr.pop(smallest))
    return newArr

arr1 = [5,3,6,2,10]
print(selectionSort(arr1))

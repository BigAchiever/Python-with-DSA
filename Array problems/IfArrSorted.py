
def isSorted(arr, n):
    for i in range(1, n):
        if arr[i] < arr[i - 1]:  #if prev element sorted in whole arr than the arr is sorted
            return False
    return True

if __name__ == "__main__":
    N = 6
    arr = [1,2,3,4,5,0]

    isSorted(arr, N)

    print("True" if isSorted(arr, N) == True else "False")
    
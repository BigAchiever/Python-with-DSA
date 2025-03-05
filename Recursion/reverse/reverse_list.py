rev_arr = []
arr = [1,2,3,4,5]


def revArr(arr , n):
    for i in range( len(arr)-1, -1, -1):
        rev_arr.append(arr[i])
    return printArr(rev_arr, n)

def printArr(arr, n):  #iterating the arr elements one by one
    for i in range(n):
        print(rev_arr[i], end = " ")

if __name__ == "__main__":
    arr = [1,2,3,4,5]
    n = len(arr)
    revArr(arr, n)





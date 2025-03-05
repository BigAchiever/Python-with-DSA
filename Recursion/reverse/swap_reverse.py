
# using swapping logic

def revArr(arr , n):
    p1 = 0
    p2 = n-1

    while(p1<p2):
        arr[p1], arr[p2] = arr[p2], arr[p1]
        p1+=1
        p2-=1
    return PrintArr(arr, n)

def PrintArr(arr, n):
    for i in range(n):
        print(arr[i], end = "")

if __name__ == "__main__":
    arr = [5, 4, 3, 2, 1]
    n = len(arr)
    revArr(arr, n)
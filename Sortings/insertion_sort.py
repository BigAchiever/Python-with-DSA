N = 6
arr = [13,2,24,52,20,9]

for i in range(0, N-1):
    mini = i
    for j in range(i+1, N):

        if(arr[j] < arr[mini]):
            mini = j
            j += 1
    arr[mini], arr[i] = arr[i], arr[mini]

print(arr)

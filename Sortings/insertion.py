N = 6
arr = [31,2,24,52,20,9]
# We work in sub arrays in this sorting technique
for i in range(1,N):
    j = i
    while(j>0 and arr[j-1] > arr[j]):
        arr[j-1], arr[j] = arr[j], arr[j-1]
        j -= 1

print(arr)
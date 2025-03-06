N = 6
arr = [13,2,24,52,20,9, 24]

small = float('inf')
second_small = float('inf')
large = float('-inf')
second_large = float('-inf')
        

for i in range(N):
    large = max(large, arr[i])
    small = min(small, arr[i])

for i in range(N):
    if arr[i] < second_small and arr[i] != small:
        second_small = arr[i] 
    if arr[i] > second_large and arr[i] != large:
        second_large = arr[i]     

print(second_large)
N = 6
arr = [10, 12, 5, 8, 1, 2]
# we swap the adjecent elements of the arr based on which number is larger, 
# the largest number moves to its correct position 
# after all comparisions

for i in range(len(arr)):
# while(N >= 0):

    didSwap = 0
    for j in range(0, len(arr) - 1 -i):  # -i because after each pass, the last i elements are already sorted
        if arr[j] > arr[j + 1]:           # Compare adjacent elements
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            didSwap = 1
    if didSwap == 0: break    
    

print(arr)


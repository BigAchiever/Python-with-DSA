arr = [31,200,24,52,20,9]
largest = arr[0]   
for j in range(1, len(arr)):
        if largest <arr[j]:
            largest = arr[j]
            j+=1

print(largest)





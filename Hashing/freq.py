arr = [2, 3, 2, 3, 5]
n = 5  # Range is 1 to 5
new_arr = []

# Brute force: Check each number from 1 to n
for num in range(1, n + 1):  # Iterate through 1 to n
    count = 0
    # Check every element in arr to see if it matches num
    for element in arr:
        if element == num:
            count += 1
    new_arr.append(count)

print(new_arr)
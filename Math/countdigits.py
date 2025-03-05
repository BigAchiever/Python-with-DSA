# Given a positive integer n, count the number of digits in n that divide n evenly (i.e., without leaving a remainder). Return the total number of such digits.

# A digit d of n divides n evenly if the remainder when n is divided by d is 0 (n % d == 0).
# Digits of n should be checked individually. If a digit is 0, it should be ignored because division by 0 is undefined.

n = 20
orignal_n = n 
count = 0
digits = []
while n > 0:

    digit = n % 10  # Get the rightmost digit using modulo
    digits.append(digit)  # Store the digit in the list
    n = n // 10  # Remove the rightmost digit using integer division
for i in digits: 
    if i != 0:
        if(orignal_n % i == 0):
            count +=1
print(count)
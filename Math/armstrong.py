n = 153
orignal_n = n
count = 0
digits = []
sum = 0
while n>0:
    count+=1            #counting the number of digits
    digit = n % 10      #getting the last digit
    digits.append(digit)    # appending in the list
    n = n //10         # removing the last digit

for i in range(len(digits)):
    sum += digits[i] ** count
print(sum)

if(orignal_n == sum):
    print("it's an armstrong number")
else: "Not an armstrong number"
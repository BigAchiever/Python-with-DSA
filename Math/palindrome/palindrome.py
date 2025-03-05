n = 2345
orignal_n  = n
extractdigits = 0
while(n>0):
    digits = n%10
    extractdigits = extractdigits*10 + digits
    n = n//10
# print(extractdigits)

if(extractdigits == orignal_n):
    print("Its a Palindrome")
else: print("Not a palindrome")

    
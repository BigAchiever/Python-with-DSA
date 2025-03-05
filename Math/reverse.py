n = 12345

reversednum = 0
while(n>0):
    digit =  n%10
    reversednum = reversednum*10 + digit
    n = n//10

print(reversednum)
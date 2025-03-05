n1 = 12
n2 = 12

gcd = 1
for i in range(1, min(n1, n2)):
    if (n1%i ==0 and n2%i ==0):
        gcd =  i

print(gcd)

#optimal approach
# To find the GCD of n1 and n2 where n1 > n2:

# Repeatedly subtract the smaller number from the larger number until one of them becomes 0.
# Once one of them becomes 0, the other number is the GCD of the original numbers.
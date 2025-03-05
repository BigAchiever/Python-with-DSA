n = 36
divisors = []
for i in range(1, n+1):
    if n % i == 0:
        divisors.append(i)
        i+=1
print(divisors)


# Optimal approach is using the square root method
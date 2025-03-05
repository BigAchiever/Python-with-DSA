def lcm(num1, num2):
    max_num = max(num1, num2)
    while True: #until condition is satisfied loop runs
        if(max_num % num1 == 0 and max_num % num2 == 0):
           return max_num
        else: 
            max_num +=  1
    
n1 = 1
n2 = 1
result = lcm(n1, n2)
print(result)
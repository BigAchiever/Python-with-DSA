def fibonacci(n):
    if(n == 0):
        return 1
    
    return n * fibonacci(n-1)


if __name__ == "__main__":
    print(fibonacci(5))

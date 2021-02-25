def fibonacci(n):
    n1 = 0
    n2 = 1
    count = 0
    if n <= 0:
        print("Please enter a positive integer greater than 0")
        return "Invalid Input"
    elif n == 1:
        print("Fibonacci sequence upto",n,":")
        print(n1)
        return n1
    else:
        print("Fibonacci sequence: ")
        while count < n:
            print(n1)
            nth = n1 + n2
            n1 = n2
            n2 = nth
            count += 1
        factorial(n2-n1)
        return n2-n1

def factorial(n):
    x = 1
    for i in range(1, n+1):
        x = x*i
    print("The factorial of",n,"is: ",end="")
    print(x)

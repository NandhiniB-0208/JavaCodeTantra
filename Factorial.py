def recur_factorial(n):
    if n == 0:
        return 1
    else:
        return n * recur_factorial(n-1)

n = int(input())
if n < 0:
    print("Enter a positive number")
else:
    print(recur_factorial(n))
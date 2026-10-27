def computeGCD(x, y):
    while y:
        x, y = y, x % y
    return x
#write your code here..

a = int(input("x: "))
b = int(input("y: "))
print (computeGCD(a, b))

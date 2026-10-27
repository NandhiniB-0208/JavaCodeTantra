str = input("str:")
n = len(str)
mid = n // 2
if n % 2 == 0:
    print("first half str of even length:", str[:mid])
else:
    print("second half str of odd length:", str[mid+1:])

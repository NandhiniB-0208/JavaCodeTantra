data = input("data: ")
list1 = list(map(int, data.split(',')))
squares = []
original_sum = sum(list1)
for num in list1:
    squares.append(num ** 2)
sum_of_squares = sum(squares)
print("list:", list1)
print("sum:", original_sum)
print("squares:", squares)
print("sum of squares:", sum_of_squares)

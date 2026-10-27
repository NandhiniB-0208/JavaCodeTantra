r = int(input("rows: "))
c = int(input("columns: "))
matrix = []
print("row wise elements:")
for i in range(r):
    li = list(map(int, input().split()))
    matrix.append(li)
print("original matrix:", matrix)
transpose = []

for i in range(c):
    tr_row = []
    for j in range(r):
        tr_row.append(matrix[j][i])
    transpose.append(tr_row)

#print the transposed matrix
print("Transposed matrix:", transpose)

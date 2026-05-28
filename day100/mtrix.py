#1 Create and print this matrix:
'''mat=[]
rows=int(input("Enter rows: "))
columns=int(input("Enter columns:"))
for i in range(rows):
    row=[]
    for j in range(columns):
        val=int(input("enter element:"))
        row.append(val)
    mat.append(row)
print(mat)

#2. Access Elements
matrix = [
    [2, 4, 6],
    [1, 3, 5],
    [7, 8, 9]
]
print(matrix[0][1])#4
print(matrix[1][2])#5
print(matrix[2][1])#8

#3 Sum of All Elements
matrix = [
    [1, 2],
    [3, 4]
]
total=0
for kr in matrix:
    for ele in kr:
        total+=ele
print(total)

#4 Row Sum
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
for i in range(len(matrix)):
    total=0
    for ele in matrix[i]:
        total+=ele
    print("Row", i + 1, "sum =", total)'''
    
#5 Column Sum
matrix=[
 [1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]
]  
columns=len(matrix[0])
for i in range(columns):
    col_sum=0
    for  row  in matrix[i]:
        col_sum+=row[i]
    print("column",i+1,"sum =",col_sum)
    

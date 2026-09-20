# Matrices

a =[
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]

rows = len(a)
cols = len(a[0])
sumCol = 0

sumDiag=0
for i in range(0,rows):
    for j in range(0,cols):
        if i==j:
            sumDiag = sumDiag + a[i][j]            
print("Sum of Diagonals:",sumDiag)


for i in range (0,rows):
    sumRow = 0
    for j in range(0,cols):
        sumRow = sumRow + a[i][j]
    print("Sum of",i+1,"Rows:",sumRow)

for i in range (0,rows):
    sumCol = 0
    for j in range(0,cols):
        sumCol = sumCol + a[j][i]
    print("Sum of",i+1,"Col:",sumCol)


##secondary diag
'''
a =[
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]

rows = len(a)
cols = len(a[0])

sumDiagp =0
for i in range(0,rows):
    for j in range(0,cols):
        if i==j:
            sumDiagp = sumDiagp + a[i][j]            
print("Sum of Primary Diagonals:",sumDiagp)

sumDiags = 0
for i in range(0,rows):
    for j in range (0,cols):
        if ((i + j)== (rows - 1)):
            sumDiags = sumDiags + a[i][j]
print("Sum of Secondary Diagonals:",sumDiags)
'''

#addition of two matrices
'''
a = []
n = int(input("Enter N for N x N matrix: "))
for i in range (n):
    row = []
    for j in range (n):
        row.append(int(input("Enter the element at position ("+str(i+1)+")("+str(j+1)+":)")))
    a.append(row)
    
print("Matrices A:")
for row in a:
    print(row)

    
b = []
int(input("Enter N for N x N matrix: "))
for i in range (n):
    row = []
    for j in range (n):
        row.append(int(input("Enter the element at position ("+str(i+1)+")("+str(j+1)+":)")))
    b.append(row)
print()
print("Matrices B:")
for row in b:
    print(row)


##result = [[0 for _ in range(n)] for _ in range(n)  ]
result = []
for i in range(n):
    row = []
    for j in range(n):        
        row.append(0)
    result.append(row)

print()

for i in range (n):
    for j in range(n):
        result[i][j] = a[i][j] + b[i][j]

print("Result:")

for row in result:
    print(row)
'''

#Multiplication of matrices

a = []
n = int(input("Enter N for N x N matrix: "))
for i in range (n):
    row = []
    for j in range (n):
        row.append(int(input("Enter the element at position ("+str(i+1)+")("+str(j+1)+":)")))
    a.append(row)
    
print("Matrices A:")
for row in a:
    print(row)

b = []
n = int(input("Enter N for N x N matrix: "))
for i in range (n):
    row = []
    for j in range (n):
        row.append(int(input("Enter the element at position ("+str(i+1)+")("+str(j+1)+":)")))
    b.append(row)
print()
print("Matrices B:")
for row in b:
    print(row)

result = []
for i in range(n):
    row = []
    for j in range(n):
        row.append(0)
    result.append(row)
print()
for i in range(len(a)):
    for j in range(len(b[0])):
        for k in range(len(b)):
            result[i][j] += a[i][k] * b[k][j]

print("Result:")
for row in result:
    print(row)

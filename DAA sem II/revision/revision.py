
"""greedy coin"""
# def greedy(n):
#     count = 0
#     denomination = [1,2,5,10]

#     for i in range(len(denomination)-1,-1,-1):
#         count += n//denomination[i]
#         n = n%denomination[i]
#     return count
    
# print(greedy(80))

"""LCS"""

# def lcs(s1, s2, m, n):   

#     if m==0 or n==0:
#         return 0

#     if s1[m-1] == s2[n-1]:
#         return 1 + lcs(s1,s2,m-1,n-1)
#     else:
#         return max(lcs(s1,s2,m,n-1),lcs(s1,s2,m-1,n))
    

# s1 = "TAABISH"
# s2 = "AASH"

# m = len(s1)
# n = len(s2)
# print(lcs(s1,s2,m,n))

'''fact'''
# def fact(n):
#     if n==0:
#         return 0
#     elif n==1 or n==2:
#         return n
#     else:
#         return n*fact(n-1)

# print(fact(5))
'''iterative'''
# n = 5
# fact = 1
# for i in range(1,n+1):
#     fact = fact * i

# print(fact)

'''fibo'''
# def fibo(n):
#     a,b=0,1
#     print("fibo of",n,"series")
#     for i in range(n):
#         print(a,end=" ")
#         a,b = b,a+b


# fibo(5)

'''recusive'''
# def recur(n):
#     if n<2:
#         return n
#     else:
#         return recur(n-1) + recur(n-2)
# print(recur(5))

'''tower of hanoi recursive'''
# def do(n,src,des,aux):
#     global i
    
#     if n==1:
#         i+=1
#         print(f"{i}: Move disk 1 from {src} to {des}")
#         return
#     do(n-1,src,aux,des)

#     i+=1
#     print(f"{i}: Move disk {n} from {src} to {des}")
#     do(n-1,aux,des,src)

# n = 3
# src='A'
# aux='B'
# des='C'
# i = 0
# print(f"total moves to be required {2**n-1}")
# do(n,src,des,aux)

'''brute force'''
# def rape(pattern, text):
#     m = len(pattern)
#     n = len(text)
#     x = 1
#     for i in range(n-m+1):
#         j=0
#         while j<m and text[i+j] == pattern[j]:
#             j=j+1
#         if j==m:
#             print("Text is raped and pattern is found at pos",i+1)
#             x=-1
        
#     if x==1:
#         print("Pattern not found text has been raped for nothing")

# text1=input("Enter any string: ")
# pattern=input("Enter pattern from your string:")
# print("Example 1:")
# rape(pattern,text1)

'''max min'''
# def getMinMax(arr):
#     n = len(arr)
#     res_min = arr[0]
#     res_max = arr[0]
#     for i in arr[1: ]:
#         res_min = min(res_min,i)
#         res_max = max(res_max,i)
#     return res_min,res_max

# arr = [1,5,78,965652,21,56,14754,13123132,0]
# print(getMinMax(arr))

'''recursive'''
# arr = [1,5,78,965652,21,56,14754,13123132,0]
# n = len(arr)
# def do(arr,n):
#     if n==1:
#         return arr[0]
#     return min(arr[n-1],do(arr,n-1)), max(arr[n-1],do(arr,n-1))
# print(do(arr,n))    

'''bubble sort'''
# def bubbleSort(arr,n):
#     for i in range(n-1):
#         for j in range(n-(i+1)):
#             if arr[j]>arr[j+1]:
#                 arr[j],arr[j+1] = arr[j+1],arr[j]
#     print(arr)

# arr = [1,5,78,965652,21,56,14754,13123132,0]
# print("Og array",arr)
# print("Sorted array",end=" ")
# bubbleSort(arr,len(arr))

'''selection sort'''
# arr = [1,5,78,965652,21,56,14754,13123132,0]
# print("Og array",arr)

# def selectSort(arr,n):
#     for i in range(n):
#         mini = i
#         for j in range(i+1,n):
#             if arr[mini]>arr[j]:
#                 mini = j
#         arr[i],arr[mini] = arr[mini],arr[i]
#         return arr

# print("Sorted Array",selectSort(arr,len(arr)))

'''insertion sort'''
# def insertSort(arr,n):
#     for i in range(1,n):
#         value=arr[i]
#         j = i-1
#         while j>=0 and value < arr[j]:
#             arr[j+1] = arr[j]
#             j=j-1
#             arr[j+1] = value
#     return arr
# print("Sorted array",insertSort(arr,len(arr)))

'''operations on matrices'''
a = []
n = int(input("Enter N for NxN matix: "))

print("Enter the elements in matix A")
for i in range(n):
    row=[]
    for j in range(n):
        row.append(int(input(f"enter the element for {i+1},{j+1} pos: ")))
    a.append(row)

b = []
print("Enter the elements in matix B")
for i in range(n):
    row=[]
    for j in range(n):
        row.append(int(input(f"enter the element for {i+1},{j+1} pos: ")))
    b.append(row)

row = len(a)
col = len(a[0])
sumCol = 0
sumRow = 0
sumDiagp = 0
sumDiags = 0
for i in range(row):
    for j in range(col):
        sumRow += a[i][j]
        sumCol += a[j][i]
        if (i==j):
            sumDiagp += a[i][j]
        if(i+j) == (row-1):
            sumDiags += a[i][j]
    print("Sum of rows:",sumRow)
    print("Sum of Cols:",sumCol)

print("All the operations performed on a:\n",sumRow,sumCol,sumDiagp,sumDiags)

print("Now performing multiplication and division")

#SUM OF ELEMENTS IN AN ARRAY
'''a=[1,2,3,4]
s=0
for i in range(0,len(a)):
    s=s+a[i]
print("Sum of array is",str(s))'''

#SUM OF ELEMENTS IN AN ARRAY (INPUT FROM USER)
'''n=int(input('Enter length of array:'))
print('Enter',n,'elements')
s=0
a=[]
for i in range(n):
    ele=int(input())
    a.append(ele)
print('The elements of array are',a)
for i in range(0,len(a)):
    s=s+a[i]
print('Sum of elements of array is',str(s))'''

#SEARCHING AN ELEMENT IN ARRAY
'''n=int(input('Enter element to be searched:'))'''
"a=[1,2,5,8,4,6]"
'''for i in range(0,len(a)):
    if n==a[i]:
        print('Element found at',i)
        break;
else:
    print('Element not found.')'''

#MIN MAX
'''def minmaxposition(A,n):
    minposition=A.index(min(A))
    maxposition=A.index(max(A))
    print('The minimum is at position:',minposition + 1)
    print('The maximum is at position:',maxposition + 1)
A=[]
n=int(input('Enter length of array:'))
print('Enter',n,'elements')
for i in range(n):
    ele=int(input())
    A.append(ele)
minmaxposition(A,n)'''

#COUNT EVEN OR ODD:
'''def counteo():
    ce=0
    co=0
    for i in range(n):
        if(A[i]%2==0):
            ce += 1
        else:
            co += 1
    print('There are',ce,'even numbers.')
    print('There are',co,'odd numbers.')
A=[]
n=int(input('Enter length of array:'))
print('Enter',n,'elements')
for i in range(n):
    ele=int(input())
    A.append(ele)
counteo()'''

##2-D ARRAYS
#DISPLAY MATRICE
'''rows=int(input('Enter number of rows:'))
cols=int(input('Enter number of columns:'))
A=[]
for i in range(rows):
    row = []
    for j in range(cols):
        element = int(input(f"Enter element at position ({i},{j}): "))
        row.append(element)
    A.append(row)
print("\n2D Array (Matrix):")
for r in A:
    print(r)'''

#SUM OF ROWS
'''a = [
       [1,2,3],
       [4,5,6],
       [7,8,9]
     ];

rows = len(a);
cols = len(a[0]);

for i in range(0,rows):
    sumRow=0;
    for j in range(0,cols):
        sumRow = sumRow + a[i][j];
    print("Sum of "+str(i+1)+" row:"+str(sumRow));'''

#SUM OF COLUMNS
'''a = [
       [1,2,3],
       [4,5,6],
       [7,8,9]
     ];

rows = len(a);
cols = len(a[0]);
print("The matrix is:")
for r in a:
    print(r)
for i in range(0,rows):
    sumCols=0;
    for j in range(0,cols):
        sumCols = sumCols + a[j][i];
    print("Sum of "+str(i+1)+" column:"+str(sumCols));'''

#SUM OF DIAGONALS:
'''a = [
       [1,2,3],
       [4,5,6],
       [7,8,9]
     ];
rows = len(a);
cols = len(a[0]);
print("The matrix is:")
for r in a:
    print(r)
sumDiag=0
secondary=0
for i in range(0,rows):
    for j in range(0,cols):
        if(i==j):
            sumDiag = sumDiag + a[i][j]
        if((i + j) == (rows-1)):
            secondary += a[i][j]
print(sumDiag)
print(secondary)'''

#ADDITION OF TWO MATRICES:
'''A = []
n=int(input("Enter N for NxN matrix:"))
print('Enter elements for matrix A.')
for i in range(n):
    row=[]
    for j in range(n):
        row.append(int(input(f"Enter element at position [i+1],[j+1]")))
    A.append(row)
print('\nMatrix A:')
for row in A:
    print(row)

#B Matrix

B = []
n=int(input("Enter N for NxN matrix:"))
print('Enter elements for matrix A.')
for i in range(n):
    row=[]
    for j in range(n):
        row.append(int(input(f"Enter element at position (i+1),(j+1)")))
    B.append(row)
print('\nMatrix B:')
for row in B:
    print(row)

#Resultant matrix

result = [[0 for _ in range(n)] for _ in range(n)]

# Addition of matrices A + B
for i in range(n):
    for j in range(n):
        result[i][j] = A[i][j] + B[i][j]

print("\nResultant Matrix (A + B):")
for row in result:
    print(row)'''

#MULTIPLICATION OF TWO MATRICES:
'''A = [
       [1,2,3],
       [4,5,6],
       [7,8,9]
     ];
print('\nMatrix A:')
for r in A:
    print(r)
#B Matrix

B = [
       [1,2,3,8],
       [4,5,6,4],
       [7,8,9,3]
     ];
print('\nMatrix B:')
for r in B:
    print(r)


#Resultant matrix

result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]

for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            result[i][j] += A[i][k] * B[k][j]

print("\nResultant Matrix (A × B):")
for r in result:
    print(r)
'''

#PRACT 3: Various operations on list based stack
'''
list=[]
print("List before appending:",list)
n=int(input("Enter the length of the list:"))
for i in range(n):
    k=int(input(f"Enter element at position {i}:"))
    list.append(k)
print("List after appending:",list)
print("Element popped from stack is",list.pop())
print("List after popping the element:",list)
list.append('A')
list.append('B')
print("List after appending characters:",list)
top=list[-1]
print("Peek:",top)
isEmpty=not bool(list)
print("is empty:",isEmpty)
print("size of stack:",len(list))
'''
#PRACT 4.1: Program to demonstrate Linear Search on an array

'''def linearSearch(array,n,k):
    for i in range(n):
        if(array[i]==k):
            return i
    return -1
array=[]
n=int(input("Enter the length of array:"))
print("Enter",n,"elements:")
for i in range(n):
    a=int(input(f"Enter element at position {i}:"))
    array.append(a)
k=int(input("Enter the element you want to search:"))
result=linearSearch(array,n,k)
if result==-1:
    print("Item not found")
else:
    print(f"Item found at position {i}")
'''

#PRACT 4.1: Program to demonstrate Linear Search on an array

'''def binarySearch(array,n,k,beg,end):
    while beg<=end:
        mid=beg+end//2
        if array[mid]==k:
            return mid
        elif array[mid]>k:
            end = mid-1
        else: 
            beg = mid+1
    return -1
array=[]
n=int(input("Enter the length of array:"))
print("Enter",n,"elements:")
for i in range(n):
    a=int(input(f"Enter element at position {i}:"))
    array.append(a)
k=int(input("Enter the element you want to search:"))
result=binarySearch(array,n,k,0,len(array)-1)
if result==-1:
    print("Item not found")
else:
    print("Item found at position:",result)
'''

#PRACT 5.1: Write a program to demonstrate Bubble Sort:
'''def bubble_sort():
    for i in range(0,len(arr)-1):
        for j in range(0,len(arr)-(i+1)):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
arr=[]
n=int(input("Enter length of array:"))
print("Enter",n,"elements:")
for i in range(n):
    arr.append(int(input(f"Enter element at position {i}: ")))
print("Array before sorting:\n",arr)
print("Array after applying bubble sort:\n",bubble_sort())
'''

#PRACT 5.2: Write a program to demonstrate Selection Sort:
'''def selection_sort():
    for i in range(n):
        mini = i
        for j in range(i+1,n):
            if arr[j]<arr[mini]:
                mini = j
        arr[i],arr[mini]=arr[mini],arr[i]
    return arr
arr=[]
n=int(input("Enter length of array:"))
print("Enter",n,"elements:")
for i in range(n):
    arr.append(int(input(f"Enter element at position {i}: ")))
print("Array before sorting:\n",arr)
print("Array after applying selection sort:\n",selection_sort())
'''

#PRACT 5.3: Write a program to demonstrate Insertion Sort:
'''def insertion_sort():
    for i in range(1,n):
        value=arr[i]
        j = i-1
        while j>=0 and value<arr[j]:
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=value
    return arr
arr=[]
n=int(input("Enter length of array:"))
print("Enter",n,"elements:")
for i in range(n):
    arr.append(int(input(f"Enter element at position {i}: ")))
print("Array before sorting:\n",arr)
print("Array after applying insertion sort:\n",insertion_sort())
'''

#PRACT 6: SELECT THE Nth MIN/MAX element in a list:
'''def get_min():
    res=arr[0]
    for i in arr[1:]:
        res=min(res,i)
    return res
def get_max():
    res=arr[0]
    for i in arr[1:]:
        res=max(res,i)
    return res
arr=[9,4,5,32,534,21,543,42,53,31,53,12,7]
print("Minimum:",get_min())
print("Maximum:",get_max())
'''
#PRACT 7: PROGRAM TO FIND POSITION OF PATTERN FROM TEXT {BRUTE FORCE METHOD}
'''
def search_pattern(pattern,text):
    x=1
    m=len(pattern)
    n=len(text)
    for i in range(n-m+1):
        j=0
        while j<m and text[i+j]==pattern[j]:
            j=j+1
        if j==m:
            print(f"Pattern found at index {i}")
            x=-1
    if x==1:
        print("Invalid")
if __name__=="__main__":
    text1=input("Enter any string: ")
    pattern=input("Enter pattern from your string:")
    print("Example 1:")
    search_pattern(pattern,text1)

'''

#PRACT 8.1: PROGRAM TO DEMONSTRATE FACTORIAL OF A NUMBER:
'''
def fact(n):
    if n==1 or n==0:
        return 1
    else:
        return n*fact(n-1) 
# print(fact(5))

if __name__ == "__main__":
    n = int(input("Enter a number to find factorial: "))
    print(fact(n))
'''

#PRACT 8.2: PROGRAM TO DEMONSTRATE FIBONACCI SERIES OF A NUMBER:
'''
def fib(n):
    if n<0:
        print("Invalid")

    elif n==0:
        return 0

    elif n==1 or n==2:
        return 1
    
    else:
        return fib(n-1) + fib(n-2)
a = int(input("Etner the range of firbonacci: "))
print("fibonacci series" ,fib(a))
'''
#PRACT 8.2: PROGRAM TO DEMONSTRATE TOWER OF HANOI:
'''
n = int(input("Enter the number of disks: "))
src = 'A'
aux = 'B'
des = 'C'
i=0

def move_disks(n,src,des,aux):     //sda
    global i
    if n==1:
        i+=1
        print(f"{i}: Move disk 1 from {src} to {des}")
        return
    move_disks(n-1,src,aux,des)         //sad

    i+=1
    print(f"{i}: Move disk {n} from {src} to {des}")
    move_disks(n-1,aux,des,src)     //ads

    
move_disks(n,src,des,aux)
'''

#PRACT 9: PROGRAM TO DEMONSTRATE COIN CHANGE PROBLEM {GREEDY ALGORITHM}
'''
def findMin(n):
    count = 0
    denomination = [1,2,5,10]

    #Traverse through all denomination
    for i in range(len(denomination) -1, -1, -1):
        #Find Denominations
        count += n//denomination[i]
        n = n%denomination[i]
    return count 
if __name__ == '__main__':
    n=25
    print(findMin(n))
'''

#PRACT 10: PROGRAM TO DEMONSTRATE LONGEST COMMON SUBSEQUENCE USING DYNAMIC PROGRAMMING:
'''
def lcsRec(s1, s2, m, n):
    sub = ""
    # Base case: If either string is empty, the length of LCS is 0
    if m == 0 or n == 0:
        return 0

    # If the last characters of both substrings match
    elif s1[m - 1] == s2[n - 1]:

        # Include this character in LCS and recur for remaining substrings
        # sub += s1[m-1]
        # print(sub)
        return 1 + lcsRec(s1, s2, m - 1, n - 1)

    else:
        # If the last characters do not match
        # Recur for two cases:
        # 1. Exclude the last character of S1 
        # 2. Exclude the last character of S2 
        # Take the maximum of these two recursive calls
        return max(lcsRec(s1, s2, m, n - 1), lcsRec(s1, s2, m - 1, n))
        


if __name__ == "__main__":
    s1 = "TAABISH"
    s2 = "SHAAD"
    m = len(s1) 
    n = len(s2)
    print(lcsRec(s1, s2, m, n))
'''
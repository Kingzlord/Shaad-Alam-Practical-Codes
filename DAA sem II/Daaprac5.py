##Prgram to sort elements in list
##bubble sort
'''
def bubbleSort(arr):
    for i in range(len(arr)- 1):
        for j in range(len(arr)- (i + 1)):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr

##User defined list
a = []
n = int(input("Enter the length of the array: "))
for i in range(n):
    print(f"Enter the element in the pos- {i +1}",end=' ')
    a.append(int(input()))
    
print("Unsorted Array:",a)
print("Sorted Array:",bubbleSort(a))
# print(a)
'''
'''
##Selection sorting:
def selectionSort(arr):
    for i in range(n):
        mini = i
        for j in range(i+1, n):
            if arr[j] < arr[mini]:
                mini = j
        arr[i], arr[mini] = arr[mini], arr[i]
    return arr

a = []
n = int(input("Enter the length of the array: "))
for i in range(n):
    print("Enter the element in the pos- ",i +1,end=' ')
    a.append(int(input()))
print("Og list:",a)
print("Sorted list:",selectionSort(a))


'''
# insertion sort
a = []
n = int(input("Enter the length of the array: "))
for i in range(n):
    print("Enter the element in the pos- ",i +1,end=' ')
    a.append(int(input()))

def insertion_sort(arr):
    for i in range(1,n):
        value=arr[i]
        j = i-1
        while j>=0 and value<arr[j]:
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=value #insert this shit
    return arr  

print("OG arr",a)
print("Sorted arr",insertion_sort(a))

##Example 2 (not to be written in fair journal)
'''
def bubbleSort(arr):
    for i in range(0,len(arr)):
        for j in range(i+1,len(arr)):
            if arr[j] < arr[i]:
                arr[j]
    return arr

a = []
n = int(input("Enter the length of the array: "))
for i in range(n):
    print("Enter the element in the pos- ",i +1,end=' ')
    a.append(int(input()))
    
arr_sort = bubbleSort(a)
print(arr_sort)
'''








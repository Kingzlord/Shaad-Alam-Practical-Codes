#Bubble Sort

def bubble_sort(lst):
    for i in range(0,len(lst)-1):
        for j in range(0,len(lst)-(i+1)):
            if(lst[j]>lst[j+1]):
                temp=lst[j]
                lst[j]=lst[j+1]
                lst[j+1]=temp
    return lst
# print("The unsorted list is: \n",lst)

#Selection Sort

def selectionsort(arr):
    for i in range(n):
        mini=i
        for j in range(i+1,n):
            if arr[j]<arr[mini]:
                mini=j
        arr[i],arr[mini]=arr[mini],arr[i]
    return arr

#Insertion Sort
def insertionsort(arr):
    for i in range(1,n):
        value = arr[i]
        j=i-1
        while j>=0 and value < arr[j]:
            arr[j+1] = arr[j]
            j = j-1
            arr[j+1] = value
    return arr
arr=[]
n=int(input("Enter the length of the array: "))
print("Enter ",n,"elements of the array below.")
for i in range(n):
    arr.append(int(input(f"enter element at pos: {i+1}->")))
print("Enter which sorting technique you wanna choose:\n1: for Bubble" \
"\n2: for Selection sort\n3: for Insertion sort",end="-> ")
c = int(input())
print("Original array: ",arr)
if c==1:
    print("The sorted list is: \n",bubble_sort(arr))
elif c==2:
    print("Sorted array: ",selectionsort(arr))
else:
    print("Sorted array: ",insertionsort(arr))



    

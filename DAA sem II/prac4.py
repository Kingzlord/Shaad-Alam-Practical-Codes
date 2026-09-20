#Linear search:
'''
def LinearSearch(arr,n,k):
    for i in range(0,n):
        if (arr[i]==k):
            return i
    return -1

arr = []
n = int(input("Enter the size of array: "))
for i in range(n):
    print("Enter the element in pos",i+1,end='- ')
    arr.append(int(input()))

k = int(input("Enter the element to search: "))

result = LinearSearch(arr,n,k)
if result != -1:
    print("The element is found at pos:",result+1)
else:
    print("The element is not found")

print("O(n)")

#Binary search:
'''
def binarysearch(arr,k,low,high):
    while low<=high:
        mid =low +(high-low)// 2
        if arr[mid]==k:
            return mid
        elif (arr[mid] < k):
            low = mid + 1
        else:
            high = mid - 1
    return -1

n = int(input("size array: " ))
arr = []
for i in range(n):
    print("Enter the elements in position",i+1,end=" - ")
    arr.append(int(input()))
arr.sort()
print("Sorted Array",arr)
k = int(input("Enter the element to search: " ))
       
        
print("Sorted Array",arr)
result = binarysearch(arr,k,0,len(arr)-1)
if result != -1:
    print("Element is found at pos",result + 1)
else:
    print("Element is not found")


arr=[1,23,2,42,3425,31,67,0]
arr.sort()
# print("Minimum:",arr[0])
# print("Maximum:",arr[-1])



#Linear Search iterative
'''
def get_min(arr):
    res = arr[0]
    for i in arr[1:]:
        res = min(res,i)
    return res
def get_max(arr):
    res = arr[0]
    for i in arr[1:]:
        res = max(res,i)
    return res
arr = [1,423,6,46,34,23,13,53,4]
print("Minimum: ",get_min(arr))
print("Maximum: ",get_max(arr))
'''

#Linear Search recursive
'''
def getMin(arr,n):
    if n==1:
        return arr[0]
    return min(arr[n-1],getMin(arr,n-1))
def getMax(arr,n):
    if n==1:
        return arr[0]
    return max(arr[n-1],getMax(arr,n-1))
arr = [1,423,6,46,34,23,13,53,4]
n=len(arr)
print("Minimum: ",getMin(arr,n))
print("Maximum: ",getMax(arr,n))
'''
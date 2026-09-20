#Change of coin Greedy Algorithm(Iterative)

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



#RECURSIVE
'''def getMin(n: int, denomination: list[int], i: int) -> int:
    #Base Case: if amount becomes 0 or i<0
    if(n==0 or i<0):
        return 0
    return n//denomination[i] +getMin(n%denomination[i],denomination,i-1)

def findMin(n: int) -> int:
    denomination = [1,2,5,10]
    return getMin(n, denomination, len(denomination)-1)

if __name__ == '__main__':
    n=39
    print(findMin(n))
'''
# A Naive recursive implementation of LCS problem

# Returns length of LCS for s1[0..m-1], s2[0..n-1]
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

# def lcs(s1,s2):
#     m = len(s1)
#     n = len(s2)
#     return lcsRec(s1,s2,m,n)
'''
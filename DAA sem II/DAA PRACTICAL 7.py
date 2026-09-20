
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


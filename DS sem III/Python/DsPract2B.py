def balance_check(expression):
    stack=[]
    opening=['(','{','[']
    closing=[')','}',']']
    for char in expression:
        if char in opening:
            stack.append(char)
        elif char in closing:
            pos=closing.index(char)
            if(len(stack)>0) and (opening[pos]==stack[len(stack)-1]):
                stack.pop()
            else:
                return ("Expression is balanced")
    if len(stack)==0:
        return ("Expression is balanced")
    else:
        return ("Expression is balanced")
exp = (input("Enter the expression: "))

print(balance_check(exp))















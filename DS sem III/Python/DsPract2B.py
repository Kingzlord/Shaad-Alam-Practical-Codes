def balance_check(expression):
    stack=[]
    opening=['(','{','[']
    closing=[')','}',']']
    for char in expressio n:
        if char in opening:
            stack.append(char)
        elif char in closing:
            pos=closing.index(char)
            if(len(stack)>0) and (opening[pos]==stack[len(stack)-1]):
                stack.pop()
            else:
                return False
    if len(stack)==0:
        return True
    else:
        return False
print(balance_check('[{()}]'))
print(balance_check('[{(})]'))
















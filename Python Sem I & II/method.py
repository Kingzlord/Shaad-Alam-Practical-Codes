def overload(x=None,y=None,z=None):
    if x==None and y==None and z==None:
        print("No operation is performed")
    elif x!=None and y!=None and z==None:
        c = x + y
        print("Addition of two numbers is:", c)
    elif x!=None and y!=None and z!=None:
        d = x + y + z
        print("Addition of three numbers is:", d)
    else:
        print("Invalid")
overload(None,None,None)
overload(2,3)
overload(4,5)
overload(2,5,7)
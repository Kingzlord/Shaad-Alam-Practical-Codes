#Stacking
list=[]

list.append('A')
list.append('B')
list.append('C')
list.append('D')
print("Stack after pushing:",list)
print("Peek:",list[-1])
print("Popping:",list.pop())
print("Stack after popping",list)
print("Ëmptying the stack:")

for i in range(len(list)):
    list.pop()

isEmpty = not bool(list)
print("Is stack empty",isEmpty)
print("Size of stack:",len(list))

class node:
    def __init__(self,data):
        self.data = data
        self.next = None

def insert(head, data):
    new_node = node(data)
    new_node.data = data
    new_node.next = head

    return new_node

def lprint(head):
    current = head
    while current:
        print((current.data),end=" ->\t")
        current = current.next
        
    print("-1")

def check(head):
    if head is None:  
        return -1
    else:
        return 1

def checkbra(head, bra):
    cur = head
    if bra == cur.data:
        cur = delete(cur, bra)
        return cur, ""
    else:
        return head,bra

def delete(head, cdata):
    current = head
    if current.data == cdata:
        temp = current.data
        current = current.next
        print(temp," is removed")
    return current
        

head = None
# print("Enter a prompt", end="")
prompt = "{(a}b+)}"
print(prompt)
openb = ["(","{","["]
closeb = [")","}","]"]
count = 1
t = ""

for i in prompt:
    print(i)
    if i in openb:
        head = insert(head,i)
        print("inserted")
        print(head)
    elif i in closeb:
        temp = []
        if i==")":
            temp = openb[0]
        elif i=="}":
            temp = openb[1]
        elif i=="]":
            temp = openb[2]          
        head,t = checkbra(head, temp)
        if t == "":
            continue
        else:
            t = i
    else:
        continue
        
count = check(head)
if count == -1:
    lprint(head)
    print("Balanced")
else:
    print("Unbalanced, ",t, "is not closed")

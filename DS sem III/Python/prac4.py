##WAP to implement singly linked list with its operation
""" 
* Definition of Single Linked list - rule side
* Operations - rule side
* Algorithm for traverasal o flinked list- blang page
* Code- rule side
*Output - blank page
"""
class node:
    def __init__(self, data):
        self.data = data
        self.next = None
         

def insert(head,data):
    new_node= node(data)
    new_node.next = head
    print(data)
    return new_node

def traverse(head):
    current = head
    while current:
##            Print the current node's data following by an arrow and space
        print((current.data) ,"->", end="")
        current = current.next

    print("none")

def insert_at_end(head, data):
    new_node = node(data)
    if head is None:
        print("Head cannot be NONE")
        return
    current = head
    while current.next:
        current = current.next
    current.next = new_node
    return head
    

def insert_at_beginning(head,data):
    if head is None:
        print("No head given to insert")
    new_node = node(data)
    current = head
    new_node.next = current
    head = new_node
    return head

def insert_after_specific_node(head,gdata, data):
    current = head
    while current:     
        if current.data == gdata:
            new_node = node(data)
            new_node.next = current.next
            current.next = new_node
            return head
        else:
            current = current.next

##CREATING NEW LINKED            
print("Enter the no. of nodes in link")
n = int(input(""))
head  = None
for i in range(n):
    print("Enter the data inside node: ", i+1,end=". ")
    nd = int(input(""))
    head = insert(head, nd)

##PRINTING THE LIST
traverse(head)
print("\n")

##INSERTING AFTER SPECIFIC NODE
gdata = int(input("Enter the node after which you want to insert: "))
data = int(input("Enter the new data: "))

head = insert_after_specific_node(head, gdata ,data)
traverse(head)
print("\n")

##INSERTING AT BEGINNING
data = int(input("Enter the new data to insert at the beginning: "))

head = insert_at_beginning(head, data)
traverse(head)
print("\n")

##INSERTING AT END
data = int(input("Enter the new data to insert at end: "))

head = insert_at_end(head , data)
traverse(head)
print("\n")

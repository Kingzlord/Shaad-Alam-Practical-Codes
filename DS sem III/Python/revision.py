# Linked List Practical 04
RED = "\033[91m"
RESET = "\033[0m"

"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def insert(head, data):
    print("Enter the type of insert: ",end="")
    c = int(input(""))
    if c == 1:
        new_node = Node(data)
        new_node.next = head
        print(data, " added to the beginning of linked list")
        return new_node
    elif c==2:
        new_node = Node(data)
        current = head
        while current.next:
            current.next
        current.next = new_node
        new_node.next = None
        print(data, " added to the end of linked list")
        return head

    elif c == 3:
        gdata = int(input("Enter the Node after which you want to add: "))
        current = head
        while current:
            if current.data == gdata:
                new_node = Node(data)
                new_node.next = current.next
                current.next = new_node
                print(data," added after", gdata)
                return head
            current = current.next
        print(f"{RED}{gdata} doesn't exist{RESET}")

    else:
        print(f"{RED}Wrong Choice!! start again {RESET}")
        head = insert(head,data=data)

def traverse(head):
    current = head
    while current:
        print(f"{current.data}->",end="")
        current = current.next
    print("none",end="")

def remove_node(head, gnode):
    current = head
    previous = None
    while current:
        if current.data == gnode:
            previous.next = current.next
            current.next = None
            print(gnode,"removed from the linked list")
            return head 

        previous = current
        current = current.next



head = None
head = insert(head,data=6)
head = insert(head,data=5)
head = insert(head,data=4)
head = remove_node(head,5)
traverse(head)
"""

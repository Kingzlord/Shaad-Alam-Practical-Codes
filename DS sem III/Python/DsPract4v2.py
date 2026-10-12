#This is a short code a lot of things are removed

class node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beg(self,data):
        newnode = node(data)

        newnode.next = self.head
        self.head = newnode

    def insert_at_end(self,data):
        newnode = node(data)

        if self.head == None:
            self.head = newnode
            return

        curent = self.head
        while curent.next:
            curent = curent.next
        curent.next = newnode
        
    def insert_at_specific_node(self,data,pos):
        newnode = node(data)
        curent = self.head

        if pos == 1:
            newnode.next = self.head
            self.head = newnode
                        
        for i in range( pos - 2):
            curent = curent.next

        newnode.next = curent.next
        curent.next = newnode


    def delete_at_beg( self ):
        self.head = self.head.next

    def delete_at_end(self):
        curent = self.head


        
        
        while curent.next:
            curent = curent.next
        curent.next = None

    def delete_at_pos(self,pos):
        curent = self.head

        if pos == 1:
            self.head = self.head.next
        
        for i in range(pos-2):
            curent = curent.next

        curent.next = curent.next.next

    def search(self, data):
        curent = self.head

        pos = 1
        while curent.next:
            if curent.data == data:
                print("Node found at",pos)
                return
            
            pos += 1

            curent = curent.next

        print("Node not found")


    def rev(self):
        prev = None
        curent = self.head

        while curent:
            nextnode = curent.next
            curent.next = prev
            prev = curent
            curent = nextnode

        self.head = prev

        print("Linked List REV")


    def display(self):
        curent = self.head

        print("Linked List ",end="")
        while curent:
            print(curent.data,end=" -> ")
            curent = curent.next

        print()



print("Enter initial length of LL",end="")
l = LinkedList()
n = int(input(": "))
for i in range(n):
    data = int(input("Enter data to insert: "))
    l.insert_at_end(data)
l.insert_at_beg(6)
l.display()
l.insert_at_beg(10)
l.display()
l.insert_at_specific_node(15,4)
l.display()
l.delete_at_beg()
l.display()
l.search(6)
l.rev()
l.display()
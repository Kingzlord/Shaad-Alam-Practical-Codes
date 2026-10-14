'''                                     Queue ki mkc
class Linked:
    def __init__(self):
        self.head = None
        self.ll = []
        self.next = None

    def insert_at_beg(self,data):
        self.ll.insert(0,data)

    def insert_at_end(self,data):
        self.ll.append(data)

    def insert_at_spe_pos(self,pos,data):
        self.ll.insert(pos,data)

    def delete_at_begining(self):
        self.ll.pop(0)

    def delete_at_end(self):
        self.ll.pop()

    def delete_after_sep_pos(self,pos):
        self.ll.pop(pos-1)

    def search(self,key):
        try:
            print("Key found at ",self.ll.index(key)+1)
        
        except:
            print(key," does not exist in Linked List")

    def rev(self):
        self.ll.reverse()
        self.display()


    def display(self):
        for i in self.ll:
            print(i ,end="->")
        print("Null")
l = Linked()
l.insert_at_beg(5)
l.insert_at_beg(3)
l.insert_at_end(67)
l.insert_at_end(78)
l.display()
pos = int(input("Enter pos after which to insert Node: "))
l.insert_at_spe_pos(pos,100)
l.display()
l.delete_after_sep_pos(3)
l.display()
l.delete_at_begining()
l.display()
l.delete_at_end()
l.display()
l.search(5)
l.search(100)
l.rev()
'''


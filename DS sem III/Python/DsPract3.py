#wap to implement queue with insertion,deletion and traversal operation.
class Queue():
    def __init__(self,l):
        self.l=l
        self.q=[None]*l
        self.head=self.tail=-1
#Insert an element into the Queue
    def enqueue(self,data):
        if(self.tail==self.l-1):
            print("The queue is full\n")
        elif(self.head==-1):
            self.head=0
            self.tail=0
            self.q[self.tail]=data
        else:
            self.tail=self.tail+1
            self.q[self.tail]=data
    def dequeue(self):
        if(self.head==-1):
            print("The queue is empty \n")
        elif(self.head==self.tail):
            temp=self.q[self.head]
            self.head=-1
            self.tail=-1
            return temp
        else:
            temp=self.q[self.head]
            self.head=self.head+1
            return temp
    def printQueue(self):
        if(self.head==-1):
            print("No element in the queue")
        else:
            for i in range(self.head,self.tail+1):
                print(self.q[i],end=" ")
            print()
obj=Queue(5)
obj.enqueue(1)
obj.enqueue(2)
obj.enqueue(3)
obj.enqueue(4)
obj.enqueue(5)
obj.enqueue(5)
print("initial Queue:")
obj.printQueue()
obj.dequeue()
print("After removing an element from the queue")
obj.printQueue()








            
            
            

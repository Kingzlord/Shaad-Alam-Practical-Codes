#wap to implement queue with insertion,deletion and traversal operation.
class Queue():
    def __init__(self,k):
        self.k=k
        self.q=[None]*k
        self.h=self.t=-1
#Insert an element into the Queue
    def enqueue(self,data):
        if(self.t==self.k-1):
            print("The queue is full\n")
        elif(self.h==-1):
            self.h=0
            self.t=0
            self.q[self.t]=data
        else:
            self.t=self.t+1
            self.q[self.t]=data
    def dequeue(self):
        if(self.h==-1):
            print("The queue is empty \n")
        elif(self.h==self.t):
            temp=self.q[self.h]
            self.h=-1
            self.t=-1
            return temp
        else:
            temp=self.q[self.h]
            self.h=self.h+1
            return temp
    def printQueue(self):
        if(self.h==-1):
            print("No element in the queue")
        else:
            for i in range(self.h,self.t+1):
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








            
            
            

#wap to implement queue with insertion,deletion and traversal operation.
class Queue():
    def __init__(s,k):
        s.k=k
        s.q=[None]*k
        s.h=s.t=-1
#Insert an element into the Queue
    def enqueue(s,data):
        if(s.t==s.k-1):
            print("The queue is full\n")
        elif(s.h==-1):
            s.h=0
            s.t=0
            s.q[s.t]=data
        else:
            s.t=s.t+1
            s.q[s.t]=data
    def dequeue(s):
        if(s.h==-1):
            print("The queue is empty \n")
        elif(s.h==s.t):
            temp=s.q[s.h]
            s.h=-1
            s.t=-1
            return temp
        else:
            temp=s.q[s.h]
            s.h=s.h+1
            return temp
    def printQueue(s):
        if(s.h==-1):
            print("No element in the queue")
        else:
            for i in range(s.h,s.t+1):
                print(s.q[i],end=" ")
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








            
            
            

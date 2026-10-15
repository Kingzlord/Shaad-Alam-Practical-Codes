class Queue:
    def __init__(self,n):
        self.q = []
        self.n = n
    def Enqueue(self,item):
        if len(self.q) == self.n:
            print("Queue is full")
        else:
            self.q.append(item)
    def Dequeue(self):
        if len(self.q)==0:
            return "Queue is empty.. try enqueing"
        return self.q.pop(0)
    def printQueue(self):
        for i in self.q:
            print(i,end=" ")
        print()
n = int(input("Enter size: "))
q = Queue(n)
for i in range(n):
    q.Enqueue(int(input("Enter data: ")))
q.printQueue()
print("Dequeued: ",q.Dequeue())
q.printQueue()
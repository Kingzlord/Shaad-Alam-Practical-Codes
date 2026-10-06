#WAP for ADT:
from abc import ABC, abstractmethod 
class StackADT(ABC):
    @abstractmethod
    def push(self,item):
        pass
    @abstractmethod
    def pop(self):
        pass
    @abstractmethod
    def peek(self):
        pass
    @abstractmethod
    def isEmpty(self):
        pass
    @abstractmethod
    def size(self):
        pass

class Stack(StackADT):
    def __init__(self):
        self._items=[]
    def push(self,item):
        self._items.append(item)
    def pop(self):
        if self.isEmpty():
            raise IndexError("Can't pop from empty stack.")
        return self._items.pop()
    def peek(self):
        if self.isEmpty():
            raise IndexError("Can't peek from empty stack.")
        return self._items[-1]
    def size(self):
        return len(self._items)
    def isEmpty(self):
        return len(self._items)==0

if __name__=="__main__":
    stack=Stack()
print("Pushing 1, 2, 3, 4, 5, 6, 7 to stack.")
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.push(6)
stack.push(7)
print("Top element is:",stack.peek())
print("Stack size:",stack.size())
print("Popped:",stack.pop())
print("Now top element is:",stack.peek())
print("Is stack empty?",stack.isEmpty())

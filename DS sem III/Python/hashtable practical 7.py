class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self,capacity):
        self.capacity = capacity
        self.size = 0
        self.table = [None] * capacity

    def _hash(self,key):
        return hash(key) % self.capacity

    def insert(self,key,value):
        index = self._hash(key)

        if self.table[index] == Node(key,value):
            self.size += 1
        
        else:
            current = self.table[index]
            while current:
                if current.key == key:
                    current.value = value
                    return
                current = current.next
            new_node = Node(key, value)
            new_node.next = self.table[index]
            self.table[index] = new_node
            self.size += 1

    def search(self, key):
        index = self._hash(key)

        current = self.table[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        raise KeyError(key)

    # def remove(self, key):
    #     index = self._hash(key)

    def remove(self, key):
            index = self._hash(key)

            previous = None
            current = self.table[index]

            while current:
                if current.key == key:
                    if previous:
                        previous.next = current.next
                    else:
                        self.table[index] = current.next
                    self.size -= 1
                    return
                previous = current
                current = current.next

            raise KeyError(key)


    def len(self):
        return self.size

    def __contains__(self, key):
            try:
                self.search(key)
                return True
            except KeyError:
                print("No node found in",key)
                return False 
            

n = int(input("Enter the number of nodes you want to add: "))
ht = HashTable(n)
for i in range(1,n+1):
    print(i, end=" ")
    temp = input("Enter the content: ")
    key = input("Enter the Key: ")
    ht.insert(temp, key)


#Checking if the hashtable contains a key
s = input("Enter the node to check if it exists in the table: ")
print(s in ht) #True
# print("Not apple" in ht) #False


s2 = input("Enter the node to search the key: ")
#get the value for a key
print(ht.search(s2)) #2


s3 = input("Enter the node remove from the Hash Table: ")
ht.remove(s3)
print(ht.size) #4
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        current = self.head

        print("Linked List:", end=" ")

        while current:
            print(current.data, end=" -> ")
            current = current.next

        print("None")

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = new_node

    def insert_at_position(self, data, position):
        if position <= 0:
            print("Invalid position")
            return

        new_node = Node(data)

        if position == 1:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head

        for i in range(position - 2):
            if not current:
                print("Position out of range")
                return

            current = current.next

        if not current:
            print("Position out of range")
            return

        new_node.next = current.next
        current.next = new_node

    def delete_at_beginning(self):
        if not self.head:
            print("List is empty")
            return

        self.head = self.head.next

    def delete_at_end(self):
        if not self.head:
            print("List is empty")
            return

        if not self.head.next:
            self.head = None
            return

        current = self.head

        while current.next.next:
            current = current.next

        current.next = None

    def delete_at_position(self, position):
        if position <= 0:
            print("Invalid position")
            return

        if not self.head:
            print("List is empty")
            return

        if position == 1:
            self.head = self.head.next
            return

        current = self.head

        for i in range(position - 2):
            if not current.next:
                print("Position out of range")
                return

            current = current.next

        if not current.next:
            print("Position out of range")
            return

        current.next = current.next.next

    def search(self, value):
        current = self.head
        position = 1

        while current:
            if current.data == value:
                print(
                    f"Element {value} found at position {position}"
                )
                return

            current = current.next
            position += 1

        print(f"Element {value} not found in the list")

    def reverse(self):
        prev = None
        current = self.head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev
        print("Linked list reversed")

    def traverse(self):
        current = self.head
        elements = []

        while current:
            elements.append(current.data)
            current = current.next

        print("Traversal elements:", elements)


# Step 1: Take initial input
n = int(input("Enter the number of elements to create the linked list: "))

linked_list = LinkedList()

for i in range(n):
    value = int(input(f"Enter value for node {i + 1}: "))
    linked_list.insert_at_end(value)

print("\nInitial Linked List:")
linked_list.display()


# Step 2: Menu
while True:
    print("\nMenu:")
    print("1. Insert at Beginning")
    print("2. Insert at End")
    print("3. Insert at Specific Position")
    print("4. Delete at Beginning")
    print("5. Delete at End")
    print("6. Delete at Specific Position")
    print("7. Search Element")
    print("8. Reverse Linked List")
    print("9. Display")
    print("10. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        val = int(input("Enter value to insert: "))
        linked_list.insert_at_beginning(val)

    elif choice == "2":
        val = int(input("Enter value to insert: "))
        linked_list.insert_at_end(val)

    elif choice == "3":
        val = int(input("Enter value to insert: "))
        pos = int(input("Enter position to insert at: "))
        linked_list.insert_at_position(val, pos)

    elif choice == "4":
        linked_list.delete_at_beginning()

    elif choice == "5":
        linked_list.delete_at_end()

    elif choice == "6":
        pos = int(input("Enter position to delete from: "))
        linked_list.delete_at_position(pos)

    elif choice == "7":
        val = int(input("Enter element to search: "))
        linked_list.search(val)

    elif choice == "8":
        linked_list.reverse()

    elif choice == "9":
        linked_list.display()

    elif choice == "10":
        print("Exiting...")
        break

    else:
        print("Invalid option")

    print("\nUpdated Linked List:")
    linked_list.display()
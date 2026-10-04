class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        new_node = Node(key)

        if self.root is None:
            self.root = new_node
            return

        queue = [self.root]

        while queue:
            temp = queue.pop(0)

            if temp.left is None:
                temp.left = new_node
                return
            else:
                queue.append(temp.left)

            if temp.right is None:
                temp.right = new_node
                return
            else:
                queue.append(temp.right)

    def search(self, key):
        if self.root is None:
            return False

        queue = [self.root]

        while queue:
            temp = queue.pop(0)

            if temp.key == key:
                return True

            if temp.left:
                queue.append(temp.left)

            if temp.right:
                queue.append(temp.right)

        return False

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.key, end=" ")
            self.inorder(node.right)

    def preorder(self, node):
        if node:
            print(node.key, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.key, end=" ")

    def delete(self, key):
        if self.root is None:
            return None

        # Find the node to delete
        queue = [self.root]
        node_to_delete = None

        while queue:
            temp = queue.pop(0)

            if temp.key == key:
                node_to_delete = temp
                break

            if temp.left:
                queue.append(temp.left)

            if temp.right:
                queue.append(temp.right)

        # If key is not found
        if node_to_delete is None:
            return None

        # Find the deepest/rightmost node
        queue = [self.root]
        deepest_node = self.root
        parent = None

        while queue:
            temp = queue.pop(0)
            deepest_node = temp

            if temp.left:
                parent = temp
                queue.append(temp.left)

            if temp.right:
                parent = temp
                queue.append(temp.right)

        # Replace the node's key with deepest node's key
        node_to_delete.key = deepest_node.key

        # If the tree has only one node
        if deepest_node == self.root:
            self.root = None

        # Remove deepest node
        elif parent.right == deepest_node:
            parent.right = None
        else:
            parent.left = None


# Main program
bt = BinaryTree()

size = int(input("Enter number of nodes in the Binary Tree: "))

print("Enter elements:")

for i in range(size):
    val = int(input(f"Enter element {i + 1}: "))
    bt.insert(val)


while True:
    print("\n--- Binary Tree Operations ---")
    print("1. Insert")
    print("2. Search")
    print("3. Delete")
    print("4. Inorder Traversal")
    print("5. Preorder Traversal")
    print("6. Postorder Traversal")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        val = int(input("Enter value to insert: "))
        bt.insert(val)
        print(f"Inserted {val} into Binary Tree.")

    elif choice == 2:
        val = int(input("Enter value to search: "))

        if bt.search(val):
            print("Element Found")
        else:
            print("Element Not Found")

    elif choice == 3:
        val = int(input("Enter value to delete: "))

        if bt.search(val):
            bt.delete(val)
            print(f"Deleted {val} if it existed.")
        else:
            print("Element Not Found")

    elif choice == 4:
        print("Inorder Traversal:", end=" ")
        bt.inorder(bt.root)
        print()

    elif choice == 5:
        print("Preorder Traversal:", end=" ")
        bt.preorder(bt.root)
        print()

    elif choice == 6:
        print("Postorder Traversal:", end=" ")
        bt.postorder(bt.root)
        print()

    elif choice == 7:
        print("Exiting Program")
        break

    else:
        print("Invalid choice, please try again!")
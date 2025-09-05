class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next_node = current.next  # Store next node
            current.next = prev       # Reverse current node's pointer
            prev = current            # Move prev to current
            current = next_node       # Move to next node
        self.head = prev  # Update head to the new first node

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

# Example usage
llist = LinkedList()
llist.push(1)
llist.push(2)
llist.push(3)
llist.push(4)

print("Original Linked List:")
llist.print_list()

llist.reverse()
print("Reversed Linked List:")
llist.print_list()

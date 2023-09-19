# Removing duplicates from a two sorted linked list 
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Definition for singly-linked list.
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def deleteDuplicates(self):
        node = self.head
        prev = None
        while node:
            if prev == None:
                prev = node
                node = node.next
            elif prev.data == node.data:
                while node:
                    print(prev.data, node.data)
                    if prev.data == node.data:
                        print("node are same")
                        if node.next == None:
                            prev.next = node.next
                        node = node.next
                    else:
                        prev.next = node
                        break
            else:
                prev = node
                node = node.next
            
        
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

node_list = LinkedList()
node_list.append(1)
node_list.append(1)
node_list.append(1)
node_list.append(1)
node_list.append(2)
node_list.append(2)

# Displaying the linked list
node_list.display()
node_list.deleteDuplicates()
node_list.display()
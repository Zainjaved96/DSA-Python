class Node:
    """
    An object to store the single node of a linked list
    contains data and link to next node
    """
    
    data = None
    next_node = None

    def __init__(self,data):
        self.data = data

    def __repr__(self):
        if self.next_node:
             return f"<Node data:{self.data}, Next Node :  {self.next_node} />"
        else :
            return f"<Node data:{self.data}>"

class LinkedList:
    """
    Singly linked List
    """
    
    def __init__(self):
        self.head = None
    
    def is_empty(self):
        return self.head== None

    def size(self):
        """
        Returns the number of nodes which runs in 
        0(n) linear time because its time will increase as the node
        increases
        """
        
        current = self.head
        count = 0
        while current:
            current = current.next_node
            count += 1
        return count

    def search(self, key)       :

        """
        Search for key in the linkedlist
        returns node if found and nothing if not found 
        it runs in 0(n) linear time
        """
        
        current = self.head
        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return "Key Not found"


    def add(self, data):
        """
        Adding new node to the LinkedList
        Takes 0(1) constant time    
        """
        
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node
    
    def insert(self, data, index):
        """
        Inserting node in a singly linked list 
        Adding a node happens in constant time 
        however finding the place where to store new node
        happens in linear time
        """
        
        if index == 0:
            self.add(data)
        if index > 0:
            new = Node(data)
        
            position = index 
            current = self.head 

            while position > 1:
                current = current.next_node
                position -= 1
            prev_node = current
            next_node = prev_node.next_node

            prev_node.next_node = new
            new.next_node = next_node

    def remove(self, key):
        current = self.head
        previous = None
        found = False

        while current and not found:
            if key == current.data and self.head == current:
                self.head = current.next_node
                found = True
            elif current.data == key:
                found = True
                previous.next_node = current.next_node
            else :
                previous = current
                current = current.next_node

        return current

    def __repr__(self):
        """
        Representing the LinkedList
        """
        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append(f'Head: {current.data}')
            elif current.next_node is None:
                nodes.append(f"Tail : {current.data}")
            else:
                nodes.append(f": {current.data}")
            current = current.next_node
        return " -> ".join(nodes)
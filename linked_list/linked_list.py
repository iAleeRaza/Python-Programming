# Node class to create nodes of linked list
class Node:
    def __init__(self, value):
        self.data = value
        self.next: Node | None = None

        
class LinkedList:
    def __init__(self):
        self.head: Node | None = None
        self.n = 0

    def __len__(self):
        return self.n


    def insert_head(self, value):
    
        #create a new node
        new_node = Node(value)
        #make the connection
        new_node.next = self.head
        #update the head
        self.head = new_node
        #increment in size
        self.n += 1

    #Function to traverse the linked list and return a string representation
    def __str__(self):
        
        result = ''
        if self.head is None:
            return 'Empty Linked List'
        
        current = self.head
        while current != None:
            result = result +str(current.data)+' -> '
            current = current.next
        return result[:-4]
    
    #Function to append a new node at the end of the linked list
    def append(self, value):
        
        new_node = Node(value)
        
        if self.head is None:
            # If the list is empty, set the new node as the head
            self.head = new_node
            self.n += 1
            return
        
        
        current = self.head
        
        while current.next is not None:
            current = current.next
        current.next = new_node
        self.n += 1
    

    #function to insert a new node after an specified node
    def insert_after(self, after, value):

        new_node = Node(value)
        current = self.head

        while current is not None:
            if current.data == after:
                break
            current = current.next
        
        if current is not None:
            new_node.next = current.next
            current.next = new_node
            self.n += 1
        else:
            raise ValueError("Node not found in the linked list")


    #function to delete all the nodes in the linked list
    def clear(self):
        self.head = None
        self.n = 0

    #function to delete the head node
    def delete_head(self):

        if self.head is None:
            raise ValueError("Cannot delete from an empty linked list")
        
        deleted_value = self.head.data
        # If the list is not empty, set the head to the next node
        self.head = self.head.next
        self.n -= 1

        return deleted_value
    
    #function to delete the last node
    def pop(self):

        # If the list is empty, raise an error
        if self.head is None:
            raise ValueError("pop from empty linked list.")
        
        current = self.head
        
        # If there's only one node, delete the head
        if current.next is None:
            return  self.delete_head()
            

        while current.next.next is not None: #type: ignore
            current = current.next  #type: ignore
        
        deleted_value = current.next.data  #type: ignore
        current.next = None #type: ignore
        self.n -= 1

        return deleted_value
    

    #function to delete a node with a specific value

    def remove(self,value):
        if self.head is None:
            raise ValueError("Cannot delete from an empty linked list")
        
        if self.head.data == value:
            self.head = self.head.next
            self.n -= 1
            return
        
        current = self.head

        while current.next is not None:
            if current.next.data == value:
                break
            current = current.next
        
        if current.next is None:
            raise ValueError(f"Node with value {value} not found in the linked list")
        else:
            current.next = current.next.next
            self.n -= 1
    

    def search(self, value):

        current = self.head
        position = 0

        while current is not None:
            if current.data == value:
                return position
            current = current.next
            position += 1
        
        raise ValueError(f"Node with value {value} not found in the linked list")
    

    def __getitem__(self, index):
        if index < 0 or index >= self.n:
            raise IndexError("Index out of bounds")
        
        current = self.head
        position = 0

        while current  is not None:
            if position == index:
                return current.data
            current = current.next
            position += 1

    def __delitem__(self, index):

        current = self.head
        position = 0

        while current is not None:
            if position == index:
                return self.remove(current.data)
            current = current.next
            position += 1
        
        self.n -= 1
        
    
    def replace_max(self, value):
        if self.head is None:
            raise ValueError("Cannot replace max in an empty linked list")

        current = self.head
        max = current

        while current is not None:
            if current.data > max.data:
                max = current
            current = current.next
        
        max.data = value
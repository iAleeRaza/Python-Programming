class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    
    def __init__(self):
        self.top = None
    
    
    def is_empty(self):
        """Check if the stack is empty."""
        return self.top is None
    
    def push(self, data):
    
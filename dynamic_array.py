import ctypes


class MyList():
    def __init__(self):
        self.size = 1
        self.n = 0
        # Have to create an array of Ctype with size  = self.size
        self.A = self.__make_array(self.size)


    def __len__(self):
        return self.n
    

    # Print function to display the contents of the list
    def __str__(self):
        result = ""

        for i in range(self.n):
            result = result + str(self.A[i]) + ", "
        return '[' + result[:-2] + ']' 
    
    
    # Indexing function to access elements
    # arr[index] will return the value at that index

    def __getitem__(self, index):
        if 0 <= index < self.n:
            return self.A[index]
        else:
            raise IndexError("Index out of bounds")

    
    # Function to set the value at a specific index
    def append(self, item):
        if self.n == self.size:
            # If the array is full, double its size
            self.__resize(2 * self.size)
        # if vacant then add the item
        self.A[self.n] = item
        self.n = self.n + 1


    # Function to insert an item at a certain index
    def insert(self, position, item):
        
        if self.size == self.n:
            # If the array is full, double its size
            self.__resize(2 * self.size)
        
        for i in range(self.n, position, -1):
            self.A[i] = self.A[i - 1]
        
        self.A[position] = item
        self.n = self.n + 1


    #Function for deleting an item at a certain index
    def __delitem__ (self, position):
        
        if 0 <= position < self.n:
            
            for i in range (position, self.n -1):
                self.A[i] = self.A[i + 1]
        
        else: 
            raise IndexError("Index out of bounds")
        
        self.n = self.n - 1


    # Function to remove a specific item from the list
    def remove(self, item):
        
        index = self.find(item)

        if index is not None:
            self.__delitem__(index)
        
        else:
            raise ValueError("Item not found in the array")



    # Function to remove the last item from the list
    def pop(self):
        if self.n == 0:
            raise IndexError("Pop from empty list")
        
        # Get the last item
        item = self.A[self.n - 1]
        # Decrease the size of the list
        self.n = self.n - 1

        return item
    
    # Function to delete all the items in the list
    def clear(self):
        """Clear the list."""
        self.n = 0
        self.size = 1


    # Function to find the index of a specific item in the list
    def find(self, item):

        for i in range (self.n):
            if self.A[i] == item:
                return i
        raise ValueError("Item not found in the list")


    # Function to resize the internal array
    def __resize(self, new_size):
        
        # Create a new array with the new size
        B = self.__make_array(new_size)
        self.size = new_size

        # Copy the content from old array to the new array
        for i in range(self.n):
            B[i] = self.A[i]
        
        #Re-Assign the reference to the new array
        self.A = B


    
    # Bubble Sort function to sort the list (ascending or descending)
    def sort(self, reverse=False):

        for i in range(self.n - 1):
            for j in range(self.n-1-i):

                if (not reverse and self.A[j] > self.A[j+1]) or (reverse and self.A[j] < self.A[j+1]):
                    self.A[j], self.A[j+1] = self.A[j+1], self.A[j]

    
    # Function to find the max item in the list
    def max(self):
        if self.n == 0:
            raise ValueError("Max from empty list")
        
        max_item = self.A[0]
        for i in range(1, self.n):
            if self.A[i] > max_item:
                max_item = self.A[i]
        
        return max_item

    # Function to find the min item in the list

    def min(self):
        if self.n == 0:
           raise ValueError("Min from empty list")
        
        min_item = self.A[0]

        for i in range(1, self.n):  # Start from index 1
            if self.A[i] < min_item:
                min_item = self.A[i]

        return min_item
    
    # Function for sum of all the items in the List


    def sum(self):
        if self.n == 0:
            raise ValueError("Sum from empty list")
        
        total = 0

        for i in range(self.n):
            total += self.A[i]

        return total
    

    def extend(self, iteratable):
        for i in iteratable:
            self.append(i)



    def __make_array(self, capacity):
        """Return new array with capacity."""
        return (capacity * ctypes.py_object)()
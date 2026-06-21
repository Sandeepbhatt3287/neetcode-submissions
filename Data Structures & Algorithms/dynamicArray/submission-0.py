class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        # Initialize a fixed-size array with 0s matching the initial capacity
        self.arr = [0] * self.capacity

    def get(self, i: int) -> int:
        # Just return the element at index i
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        # Set the element at index i to n
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        # If the array is full, we must resize it first
        if self.length == self.capacity:
            self.resize()
        
        # Insert at the next available empty position
        self.arr[self.length] = n
        self.length += 1

    def popback(self) -> int:
        # Soft delete: decrement length so the last element is ignored
        if self.length > 0:
            self.length -= 1
            return self.arr[self.length]
        raise IndexError("Cannot pop from an empty array")

    def resize(self) -> None:
        # Double the capacity
        self.capacity = 2 * self.capacity
        # Create a new array with the new capacity
        new_arr = [0] * self.capacity
        
        # Copy elements from the old array to the new array
        for i in range(self.length):
            new_arr[i] = self.arr[i]
            
        self.arr = new_arr

    def getSize(self) -> int:
        # Return the number of elements currently stored
        return self.length
        
    def getCapacity(self) -> int:
        # Return the total available capacity
        return self.capacity
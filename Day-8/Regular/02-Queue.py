class Queue:
    def __init__(self):
        self.queue = []  # List to hold the queue items

    def is_empty(self):
        # Checks if the queue is empty
        return len(self.queue) == 0

    def enqueue(self, item):
        # Adds an item to the end of the queue (FIFO)
        self.queue.append(item)

    def dequeue(self):
        # Removes and returns the item from the front of the queue
        if self.is_empty():
            raise IndexError("dequeue from empty queue")  # Raises error if queue is empty
        return self.queue.pop(0)  # Removes the first item (FIFO)

    def peek(self):
        # Returns the front item without removing it
        if self.is_empty():
            raise IndexError("peek from empty queue")  # Raises error if queue is empty
        return self.queue[0]  # Returns the first item in the queue

    def size(self):
        # Returns the size of the queue
        return len(self.queue)

# Example usage
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print("Peek:", q.peek())  # Output: 10
print("Dequeue:", q.dequeue())  # Output: 10
print("Queue Size:", q.size())  # Output: 2
print("Dequeue:", q.dequeue())  # Output: 20
print("Is queue empty?", q.is_empty())  # Output: False
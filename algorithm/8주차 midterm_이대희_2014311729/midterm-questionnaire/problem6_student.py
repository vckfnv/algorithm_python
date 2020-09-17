class CircularQueue:

    def __init__(self, size):
        self.size = size
        self.queue = [None] * size

        self.front = -1
        self.rear = -1

    def is_empty(self):
        return self.front == -1 and self.rear == -1

    def is_full(self):
        return self.front == (self.rear + 1) % self.size

    def enqueue(self, item):
        # Insert an element at the back of the queue
        """
        Input  >> item
        Output >> None
        """
        if self.is_full():
            print("Cannot Enqueue Full Queue !")
        if self.front == -1:
            self.front = 0
        self.rear = (self.rear+1)%self.size
        self.queue[self.rear] = item

    def dequeue(self):
        # Remove the element at the front of the queue
        """
        Input  >> None
        Output >> None
        """
        if self.is_empty():
            print("Cannot Remove Empty Queue !")
        self.queue[self.front]=None
        self.front = (self.front+1)%self.size
        

    def peek(self):
        if self.is_empty():
            print("No element Empty Queue !")

        else:
            return self.queue[self.front]

    def display(self):
        if self.is_empty():
            print("Empty Queue !")

        else:
            print(self.queue)


def main():
    queue = CircularQueue(6)
    queue.enqueue("Queue")
    queue.enqueue("is")
    queue.enqueue("simple")
    queue.display()  # Expected Result: ['Queue', 'is', 'simple', None, None, None]

    queue.dequeue()
    queue.display()  # Expected Result: [None, None, 'simple', 'Are', 'you', 'sure']


main()

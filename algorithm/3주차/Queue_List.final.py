# -*- coding: utf-8 -*-
"""week3_lab2

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1H_y97uVQe9HXE6s2UzXosIQsBTIC2OXK
"""

class CircularQueue:
    
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    def is_empty(self):
        ## Check if queue is empty
        return True if self.front == self.rear == -1 else False
       
    def is_full(self):
        ## Check if queue is full
        return True if self.front == (self.rear+1)%self.size else False
                
    def enqueue(self, item):
        ## Insert an element at the back of the queue
        if self.is_full():
            print("Cannot Enqueue Full Queue!")
        else:
            if self.is_empty():
                self.front = 0
            self.rear = (self.rear+1)%self.size
            self.queue[self.rear] = item
               
    def dequeue(self):
        ## Remove the element at the front of the queue
        if self.is_empty():
            print("Cannot Remove Empty Queue!")
        elif self.front == self.rear:
            self.queue[self.front] = None
            self.front = -1
            self.rear = -1
        else:
            self.queue[self.front] = None
            self.front = (self.front+1)%self.size
        
    def peek(self):
        ## Retrieve the front element of the queue
        if self.is_empty():
            print("No element Empty Queue!")
        else:
            return self.queue[self.front]
        
    def display(self):
        ## Completed Funtion - DO NOT REMOVE
        ## Display value(s) of the queue
        if self.is_empty():
            print("Empty Queue !")
            
        else:
            print(self.queue)
        
def main():
    queue = CircularQueue(6)
    queue.enqueue("Queue")
    queue.enqueue("is")
    queue.enqueue("simple")
    queue.display() # Expected Result: ['Queue', 'is', 'simple', None, None, None]
    
    queue.enqueue("Are")
    queue.enqueue("you")
    queue.enqueue("sure")
    queue.enqueue("?") # Expected Result: Cannot Enqueue Full Queue !
    queue.display() # Expected Result: ['Queue', 'is', 'simple', 'Are', 'you', 'sure']
    
    queue.dequeue()
    print("function peek():",queue.peek()) # Expected Result: function peek(): is
    queue.dequeue()
    queue.display() # Expected Result: [None, None, 'simple', 'Are', 'you', 'sure']
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    queue.dequeue() # Expected Result: Cannot Remove Empty Queue !
    queue.peek() # Expected Result: No element Empty Queue !
    
main()


# -*- coding: utf-8 -*-
"""week5_lab1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_JO6Rvk2bVblsfbnE3muoH7a3r0spX2m
"""

class MaxHeap:
    
    def __init__(self):
        self.queue = [None]
    
    def insert(self, value):
        ## Insert a new value into heap 
        """
        Input:  value
        Output: None
        """
        i = len(self.queue)
        self.queue.append(value)
        while i>1 :
            pi = int(i//2)
            if self.queue[pi] < self.queue[i]:
                temp = self.queue[pi]
                self.queue[pi] = value
                self.queue[i] = temp
                i = pi
            else:
                break
            
        
    def delete(self):
        ## Delete root node
        """
        Input:  None
        Output: if heap is empty print('Heap is empty')
                return deleted value
        """
        if len(self.queue) == 1:
            print("Heap is empty")
            return
        
        item = self.queue[1]
        self.queue[1] = self.queue[len(self.queue)-1]
        self.queue[len(self.queue)-1]= item
        
        self.queue.pop()
        print(len(self.queue))
        i = 1
        while i <= len(self.queue)-1:

            c = 2*i+1
            if 2*i<= len(self.queue)-1:
                if self.queue[2*i] > self.queue[2*i+1]:
                    c = 2*i
                
                    
            
            if 2*i > len(self.queue)-1:
                break

            self.queue[i], self.queue[c] = self.queue[c], self.queue[i]

            i=c
            
            


            
            # -------------Fill in the blank
            # HINT- left = i*2
            #     - right = i*2 + 1
            

            return item

def main():

    maxheap = MaxHeap()
    
    maxheap.insert(5)
    maxheap.insert(7)
    maxheap.insert(6)
    maxheap.insert(9)
    maxheap.insert(2)
    print(maxheap.queue)
    maxheap.insert(4)
    maxheap.insert(3)
    maxheap.insert(2)
    maxheap.insert(8)
    print(maxheap.queue)
    
    maxheap.delete()
    print(maxheap.queue)
    
main()

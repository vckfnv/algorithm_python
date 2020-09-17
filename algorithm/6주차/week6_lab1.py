# -*- coding: utf-8 -*-
"""week6_lab1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WI9BAeSRrQB071-Tb4EgGJ9j6YXwi7Dr
"""

class Node:
    
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def add(self, item):
        # Add a value in the end of the linked list
        """
        Input:  item
        Output: None
        """
        new_node = Node(item)
        if self.is_empty():
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
        
    def is_empty(self):
        # Check if the linked list is empty
        """
        Input:  value
        Output: return true if the linked list is empty
                return false if the linked list is not empty
        """
        
        return True if not self.head else False
    
    
    def display(self):
        ## Completed Function - Do not remove
        # Display value(s) of the linked list
        values = []

        start_node = self.head
        while start_node:
            values.append(start_node.value)
            start_node = start_node.next

        print(" ", ' -> '.join(map(str,values)))


class ChainedHashTable:

    def __init__(self, size):
        self.table = [None] * size
        self.size = size

    def insert(self, key):
        # Insert a value into the chain hash table
        """
        Input:  item
        Output: None
        """
        
        i = self.hash(key)
        if self.table[i] == None:
            self.table[i] = LinkedList()
        self.table[i].add(key)
        

    def hash(self, key):
        ## Completed Function - Do not remove
        # Hash function
        hash_code = (key*key) % self.size
        return hash_code
    
    def display(self):
        ## Completed Function - Do not remove
        # Display chain hash table
        for i in range(self.size):
            if self.table[i] != None:
                print(i, end='')
                self.table[i].display()
            else:
                print(i)

def main():
    ch_table = ChainedHashTable(10)
    ch_table.insert(7)
    ch_table.insert(48)
    ch_table.insert(1)
    ch_table.insert(73)
    ch_table.insert(100)
    ch_table.insert(90)
    ch_table.insert(45)
    ch_table.insert(36)
    ch_table.insert(77)
    ch_table.display()
    
main()

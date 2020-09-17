class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


    def add_last(self, item):
        # Add a value in the end of the list
        """
        Input >> item: int
        Output >> None
        """
        newnode = Node(item)
        if self.head ==None:
            self.head = newnode
        else:
            curr = self.head
            while curr.next:
                curr= curr.next
            curr.next = newnode


    def concat(self, concatenated_list):
        # Join the given list along the existing axis.
        """
        Input >> concatenated_list: LinkedList
        Output >> None
        """
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = concatenated_list.head

        
    def display(self):
        # Display value(s) of the list
        """
        Input >> None
        Output >> None
        """
        if self.is_empty():
            print("linked list is empty !!")
            
        else:
            values = []

            start_node = self.head
            while start_node is not None:
                values.append(start_node.value)
                start_node = start_node.next

            print("linked list values> ", ' -> '.join(map(str,values)))
            
            
    def get_length(self):
        # Get length of the list
        """
        Input >> None
        Output >> int
        """
        length = 0
        
        start_node = self.head
        while start_node is not None:
            length += 1
            start_node = start_node.next
            
        return length


    def is_empty(self):
        # Check if the list is empty
        """
        Input >> None
        Output >> bool
        """
        return True if not self.head else False


    
def main():

    linked_list1 = LinkedList()
    linked_list1.add_last(3)
    linked_list1.add_last(7) 
    linked_list1.add_last(4) 
    linked_list1.add_last(1) 
    linked_list1.add_last(2) 
    linked_list1.display()
    
    linked_list2 = LinkedList() 
    linked_list2.add_last(2)
    linked_list2.add_last(1) 
    linked_list2.add_last(5) 
    linked_list2.add_last(6) 
    linked_list2.display()
    
    linked_list1.concat(linked_list2)
    linked_list1.display() 
        

main()

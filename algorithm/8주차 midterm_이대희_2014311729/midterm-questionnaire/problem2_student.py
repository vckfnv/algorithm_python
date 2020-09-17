class Stack:
    def __init__(self):
        self.items = []


    def is_empty(self):
        # Check if the stack is empty
        """
        Input >> None
        Output >> bool
        """
        return self.items == []


    def push(self, value):
        # Add an item e to the top of the stack
        """
        Input >> value: int
        Output >> None
        """
        self.items.append(value)

    def pop(self):
        # Remove and return the top item of the stack
        """
        Input >> None
        Output >> value: int
        """
        return self.items.pop()


def palindrome(text):
    # Print whether the given text is palindrome or not
    """
    Input >> text: str
    Output >> None
    """
    i=0
    tex = Stack()
    if len(text)%2 ==1:
        for i in range(len(text)//2):
            tex.push(text[i])
        i = len(text)//2+1
    else:
        for i in range(len(text)//2-1):
            tex.push(text[i])
        i = len(text)//2+1
    
    while not tex.is_empty() and i<len(text):
        
        check = tex.pop()
        if check != text[i]:
            print(text + ' is not a palindrome')
            return
        i += 1
    print(text + ' is a palindrome')
        
    

def main():
    palindrome("hello")
    palindrome("maddsm")
    palindrome("datastructure")
    palindrome("racecar")
    palindrome("6555556")


main()

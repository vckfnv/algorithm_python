class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, node, key):
        # Insert the given key to the BST and return the root node
        """
        Input  >> node: Node, key: int
        Output >> node: Node
        """
        newnode = Node(key)
        if self.root == None:
            self.root = newnode
        else:
            prev = None
            curr = node
            while curr and curr.key != key:
                prev = curr
                curr = curr.left if curr.key>key else curr.right

            if curr == None:
                if key > prev.key:
                    prev.right = newnode
                    
                else:
                    prev.left = newnode
        return self.root
        
    def min_value_node(self):
        # Return the node that has a minimum value
        """
        Input  >> None
        Output >> node: Node
        """
        
        curr = self.root
        while curr.left:
            curr = curr.left
        return curr

    def delete(self, node, key):
        # Delete and return the node with given key
        """
        Input  >> node: Node, key: int
        Output >> Node
        """
        if node == None:
            print('nothing to delete')
        prev = None
        curr = node
        while curr and curr.key != key:
                prev = curr
                curr = curr.left if curr.key>key else curr.right
        if curr is None:
            return self.root
        if curr.right and curr.left:
            if curr is self.root:
                presucc, succ = curr, curr.right
                while succ.left:
                    presucc = succ
                    succ = succ.left
                presucc.left = succ.right
                succ.left = self.root.left
                succ.right = self.root.right
                self.root = succ
                succ = None
            else:
                presucc, succ = curr, curr.right
                while succ.left:
                    presucc = succ
                    succ = succ.left
            
                if presucc == curr:
                    curr.left = presucc.left
                    presucc = succ
                    if key > prev.key:
                        prev.right = succ
                    else:
                        prev.left = succ
                    return curr
                else:
                    presucc.left = succ.right
                    succ.left = curr.left
                    succ.right = curr.right
                    curr = succ
                    if key > prev.key:
                        prev.right = succ
                    else:
                        prev.left = succ
                    return curr
        else:
            if curr.right:
                if key > prev.key:
                    prev.right = curr.right
                else:
                    prev.left = curr.right
            elif curr.left:
                if key > prev.key:
                    prev.right = curr.left
                    
                else:
                    prev.left = curr.left
                
            else:
                if curr is self.root:
                    self.root = None
                else:
                    
                    if key > prev.key:
                        prev.right = None
                    
                    else:
                        prev.left = None
                
                
                



        

    def inorder(self, node):
        # Perform inorder traverse
        """
        Input  >> node: Node
        Output >> None
        """
        if node:
            self.inorder(node.left)
            print(node.key, end=' ')
            self.inorder(node.right)
    


def main():
    bst = BinarySearchTree()
    bst.root = bst.insert(bst.root, 50)
    bst.root = bst.insert(bst.root, 30)
    bst.root = bst.insert(bst.root, 20)
    bst.root = bst.insert(bst.root, 40)
    bst.root = bst.insert(bst.root, 70)
    bst.root = bst.insert(bst.root, 60)
    bst.root = bst.insert(bst.root, 80)
    bst.inorder(bst.root)
    print("\nMin value")
    min_node = bst.min_value_node()
    print(min_node.key)
    print("Delete 50")
    bst.delete(bst.root, 50)
    
    print("Delete 20")
    bst.delete(bst.root, 20)
    print("Delete 40")
    bst.delete(bst.root, 40)
    print("Delete 70")
    bst.delete(bst.root, 70)
    print("Delete 80")
    bst.delete(bst.root, 80)
    #print("Delete 60")
    #bst.delete(bst.root, 60)
    #print("Delete 20")
    bst.inorder(bst.root)
    print("\nDelete 30")
    #bst.delete(bst.root, 30)
    bst.inorder(bst.root)


main()

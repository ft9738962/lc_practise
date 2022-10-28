class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None
        
    def addLeft(self, val) -> None:
        self.left = Node(val)
        
    def addRight(self, val) -> None:
        self.right = Node(val)

def invertTree(node):
    if node == None:
        return
    
    node.left, node.right = node.right, node.left
    
    invertTree(node.left)
    invertTree(node.right)
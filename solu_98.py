class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None
        self.next = None
        
    def addLeft(self, val) -> None:
        self.left = Node(val)
        
    def addRight(self, val) -> None:
        self.right = Node(val)

bst = [] # 空就是没问题，有值就是有问题

def traverse(node):
    if node == None:
        return
    
    if ((node.left != None) and (node.val < node.left.val)) or \
    ((node.right != None) and (node.val > node.right.val)):
        bst.append(False)
        return
    
    traverse(node.left)
    traverse(node.right)
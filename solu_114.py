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

def lastRight(node):
    '''从节点向右得到最下层节点'''
    while node.right != None:
        node = node.right
    return node

def traverse(node):
    if node == None:
        return
    
    traverse(node.left)
    traverse(node.right)
    if (node.left != None)&(node.right != None):
        lastRight(node.left).right = node.right
        node.right, node.left = node.left, None
    elif node.right == None:
        node.right = node.left
        node.left = None
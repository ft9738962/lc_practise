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
        
    def setNext(self, node) -> None:
        self.next = node if node != None else 'NULL'

totLevelNodes = []

def traverse(curLevelNodes, depth):
    # 第一层直接添加到
    if depth == 1:
        totLevelNodes.append(curLevelNodes)
    
    nextLevelNodes = []
    # 遍历当前层，将所有下层节点添加到总清单
    for node in curLevelNodes:
        if (node == None) or (
            (node.left==None) and (node.right==None)):
            return
        if node.left != None:
            nextLevelNodes.append(node.left)
        # else:
        #     nextLevelNodes.append('null')
        if node.right != None:
            nextLevelNodes.append(node.right)
        # else:
        #     nextLevelNodes.append('null')
    
    # 如果下层非空，则递归下层结点
    if len(nextLevelNodes):
        totLevelNodes.append(nextLevelNodes)
        traverse(nextLevelNodes, depth+1)
    
def fillNextCursor(totLevelNodes):
    for levelNodes in totLevelNodes:
        levelNodes[-1].setNext(None)
        num = len(levelNodes)
        for i in range(num-1, 0, -1):
            levelNodes[i-1].setNext(levelNodes[i])
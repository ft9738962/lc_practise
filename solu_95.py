from solu_116 import traverse

class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None
        
    def addLeft(self, val) -> None:
        self.left = Node(val)
        
    def addRight(self, val) -> None:
        self.right = Node(val)

res = []
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
        else:
            nextLevelNodes.append(None)
        if node.right != None:
            nextLevelNodes.append(node.right)
        else:
            nextLevelNodes.append(None)
    
    # 如果下层非空，则递归下层结点
    if len(nextLevelNodes):
        totLevelNodes.append(nextLevelNodes)
        traverse(nextLevelNodes, depth+1)

def parseNodes(totLevelNodes):
    # 解析
    res = []
    for level in totLevelNodes:
        res.extend([x.val if x != None else 'null' for x in level])
    return res

trees = []

def consturct_trees(root, cur_node, nums):
    if len(nums) > 1:
        cur_node.addLeft(Node(nums[0]))
        cur_node.addRight(Node(nums[1]))
        if len(nums)-2 == 0:
            trees.append(root)
            return
        consturct_trees(root, cur_node.left, nums[2:])
        consturct_trees(root, cur_node.right, nums[2:])
        cur_node.left = None
        cur_node.right = None
    
    cur_node.addLeft(Node(nums[0]))
    if len(nums) - 1 == 0:
        trees.append(root)
        return
    consturct_trees(root, cur_node.left, nums[1:])
    cur_node.left = None

    cur_node.addRight(Node(nums[0]))
    if len(nums) - 1 == 0:
        trees.append(root)
        return
    consturct_trees(root, cur_node.right, nums[1:])
    
            
class solution:
    def __init__(self, nums):
        self.nums = nums

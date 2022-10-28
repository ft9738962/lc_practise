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

def traverse(node, depth):
    if len(res) < depth:
        res.append(list())
    
    if node == None:
        res[depth-1].append('null')
        return
    
    else:
        res[depth-1].append(node.val)
        if (node.left == None) & (node.right == None):
            return
        else:
            traverse(node.left, depth + 1)
            traverse(node.right, depth + 1)

trees = []

def consturct_trees(root, cur_node, nums):
    cur_node.addLeft(nums[0])
    if len(nums) - 1 == 0:
        trees.append(traverse(root,1))
        return
    cur_node.addRight(nums[1])
    if len(nums) - 1 == 0:
        trees.append(traverse(root,1))
        return
    
    cur_node.left = None
    cur_node.addRight(nums[0])
    trees.append(traverse(root,1))
    cur_node.right = None
        
    if len(nums) == 2
    
            
class solution:
    def __init__(self, nums):
        self.nums = nums

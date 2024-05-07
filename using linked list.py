class TreeNode:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right = None
    
NewBt= TreeNode("Drinks")
left=TreeNode("Hot")
right=TreeNode("Cold")
NewBt.left=left
NewBt.right=right

def preOrderTraversal(rootnode):
    if rootnode is None:
       return
    print(rootnode.value)
    preOrderTraversal(rootnode.left)
    preOrderTraversal(rootnode.right)

preOrderTraversal(NewBt)




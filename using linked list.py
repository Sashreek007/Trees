class TreeNode:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right = None
    
NewBt= TreeNode("Drinks")
left=TreeNode("Hot")
tea=TreeNode("Tea")
left.left=tea
coffee=TreeNode("Coffee")
left.right=coffee
right=TreeNode("Cold")
NewBt.left=left
NewBt.right=right

def preOrderTraversal(rootnode):
    if  not rootnode:
       return
    print(rootnode.value)
    preOrderTraversal(rootnode.left)
    preOrderTraversal(rootnode.right)

preOrderTraversal(NewBt)

def InOrderTraversal(rootnode):
    if not rootnode :
        return
    InOrderTraversal(rootnode.left)
    print(rootnode.value)
    InOrderTraversal(rootnode.right)

InOrderTraversal(NewBt)

def PostOrderTraversal(rootnode):
    if not rootnode:
        return 
    PostOrderTraversal(rootnode.left)
    PostOrderTraversal(rootnode.right)
    print(rootnode.value)

print(PostOrderTraversal(NewBt))

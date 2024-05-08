from with_linkedlist import Queue
class TreeNode:
    def __init__(self,data):
        self.data=data
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
    print(rootnode.data)
    preOrderTraversal(rootnode.left)
    preOrderTraversal(rootnode.right)

preOrderTraversal(NewBt)

def InOrderTraversal(rootnode):
    if not rootnode :
        return
    InOrderTraversal(rootnode.left)
    print(rootnode.data)
    InOrderTraversal(rootnode.right)

InOrderTraversal(NewBt)

def PostOrderTraversal(rootnode):
    if not rootnode:
        return 
    PostOrderTraversal(rootnode.left)
    PostOrderTraversal(rootnode.right)
    print(rootnode.data)

print(PostOrderTraversal(NewBt))

def LevelOrderTraversal(rootnode):
    if not rootnode:
        return
    else:
        customqueue=Queue()
        customqueue.Enqueue(rootnode)
        while not(customqueue.isEmpty()):
            root= customqueue.dequeue()
            print(root.data)
            if(root.left is not None):
                customqueue.Enqueue(root.left)
            if(root.right is not None):
                customqueue.Enqueue(root.right)
LevelOrderTraversal(NewBt)
        
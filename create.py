class TreeNode:
    def __init__(self,data,children=[]):
        self.data=data
        self.children=children
    
    def __str__(self,level=0):
        ret= " "*level +str(self.data) + "\n"
        for child in self.children:
            ret +=child.__str__(level+1)
        return ret
    
    def addChild(self,TreeNode):
        self.children.append(TreeNode)

tree= TreeNode('Drinks',[])
hot = TreeNode("Hot",[])
Tea=TreeNode('Tea',[])
Coffee=TreeNode('Coffee',[])
cold=TreeNode("Cold",[])
cola=TreeNode('Cola',[])
sprite=TreeNode('sprite',[])

tree.addChild(cold)
tree.addChild(hot)
hot.addChild(Tea)
hot.addChild(Coffee)
cold.addChild(cola)
cold.addChild(sprite)
print(tree)
class BinaryTree:
    def __init__(self,size):
        self.customList= size*[None]
        self.lastUsedIndex=0
        self.maxSize=size
    
    def insert(self,value):
        if self.lastUsedIndex==self.maxSize:
            return "The binary tree is full"
        else:
            self.customList[self.lastUsedIndex+1]=value
            self.lastUsedIndex += 1
            return "The value has been inserted"
    def search(self,target):
        for i in range(len(self.customList)):
            if self.customList[i]== target:
                return "Found"
        return "Not found"

    
    def __str__(self):
        values =(str(x) for x in self.customList) 
        return ' '.join(values)
    
    def preOrderTraversal(self,index):
        if index>self.lastUsedIndex:
            return
        print(self.customList[index])
        self.preOrderTraversal(2*index)
        self.preOrderTraversal(2*index+1)
    
    def InOrderTraversal(self,index):
        if index>self.lastUsedIndex:
            return
        self.preOrderTraversal(2*index)
        print(self.customList[index])
        self.preOrderTraversal(2*index+1)

    def PostOrderTraversal(self,index):
        if index>self.lastUsedIndex:
            return
        self.preOrderTraversal(2*index)
        self.preOrderTraversal(2*index+1)
        print(self.customList[index])

    def levelOrderTraversal(self,index):
        for i in range(index,self.lastUsedIndex+1):
            print(self.customList[i])





newBT= BinaryTree(8)

newBT.insert("Drinks")
newBT.insert("Hot")
newBT.insert("Cold")
newBT.insert("Tea")
newBT.insert("Coffee")
newBT.levelOrderTraversal(1 )




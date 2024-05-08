class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0

class Queue:
    def __init__(self):
        self.LinkedList = LinkedList()

    def isEmpty(self):
        if self.LinkedList.head is None:
            return True
        return False
    
    def Enqueue(self,value):
        new_node=Node(value)
        if self.LinkedList.head is None:
            self.LinkedList.head=new_node
            self.LinkedList.tail=new_node
        else:
            self.LinkedList.tail.next=new_node
            self.LinkedList.tail=new_node
        self.LinkedList.length+=1
    
    def dequeue(self):
        pop=self.LinkedList.head
        self.LinkedList.head=self.LinkedList.head.next
        pop.next=None
        self.LinkedList.length-=1
        return pop.value
    
    def peek(self):
        return self.LinkedList.head.value
    
    def delete(self):
        self.LinkedList.head=None
        self.LinkedList.tail=None
    
    def __str__(self):
        temp=self.LinkedList.head
        result=' '
        while temp is not None:
            result += str(temp.value)
            if temp.next:
                result+='->'
            temp=temp.next
        return result
    
queue=Queue()
    


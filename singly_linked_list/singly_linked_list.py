class ListNode: 
    def __init__(self,value,next=None):
        self.value = value
        self.next = next
    
    def insert(self,value):
        pass

    def delete(self):
        pass


class SingleList:
    def __init_(self,node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0
    

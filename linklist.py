class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class Linklist:
    def __init__(self):
        self.head=None
        self.size=0


    def _Addnode_end(self,data):
        create_node=Node(data)
        if self.head is None:
            self.head=create_node
        else:   
           current=self.head
           while current.next:
               current=current.next
           current.next=create_node
        self.size+=1

    def _Addnode_first(self,data):
        create_node=Node(data)
        create_node.next=self.head
        self.head=create_node
        self.size+=1


    def _Size(self):
        return self.size
    
    def _Remove_end(self):
        if self.head is None:
            print("LINKLIST IS EMPTY")
            self.size=0
            return

        if self.head.next is None:
            self.head=None
            
        else:
            current=self.head
            while current.next.next:
               current=current.next
            current.next=None
        self.size-=1
        
    def _Remove_first(self):
        if self.head is None:
            print("LINKLIST IS EMPTY")     
            self.size=0
            return
        if self.head.next is None:
            self.head=None
        else:
            current=self.head.next
            self.head=None
            self.head=current
        self.size-=1
        
    def _Display(self):
        current=self.head
        while current:
            print(current.value,end=" ---> ")
            current=current.next
        print(None)
        




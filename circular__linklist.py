class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class Circular_linklist:
    def __init__(self):
        self.head=None
        self.size=0

    def _Size(self):
        return self.size
    
    def Inser_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            self.head.next=self.head
        else:
            current=self.head
            while current.next!=self.head:
                current=current.next
            current.next=new_node
            new_node.next=self.head
        self.size+=1

    def Insert_first(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            new_node.next=self.head
        else:
            current=self.head
            while current.next!=self.head:
                current=current.next
            new_node.next=self.head
            self.head=new_node
            current.next=self.head
        self.size+=1


    def Insert_any_index(self,data,index):
        if index < 0 or index >self._Size():
            print("INDEXERROR ")
            return 
        if index==0:
            return self.Insert_first(data)
        if index==self._Size():
            return self.Inser_end(data)
        current=self.head
        create_node=Node(data)
        for _ in range(index-1):
            current=current.next
        create_node.next=current.next
        current.next=create_node
        self.size+=1

        
        
    def Remove_last(self):
        if self.head is None:
            return
        if self.head.next ==self.head:
            self.head=None
        else:
            current=self.head
            while current.next.next!=self.head:
                current=current.next
            current.next=self.head
        self.size-=1

        
    def Remove_first(self):
        if self.head is None:
            return
        if self.head.next==self.head:
            self.head=None
        else:
            current=self.head
            while current.next !=self.head:
                current=current.next
            current.next=self.head.next
            self.head=current
        self.size-=1
    
    def Remove_at_index(self,index):
        if index<0 or index>self._Size()-1:
            print("INDEXERROR ")
            return 
        if index==0:
            return self.Remove_first()
        if index==self._Size()-1:
            return self.Remove_last()
        else:
            current=self.head
            for _ in range(index-1):
                current=current.next
            remove=current.next
            current.next=remove.next
            remove.next=None
            self.size-=1

    def Forward_traveser(self):
        if self.head is None:
            print(" circular linklist is empty !")
            return
        current=self.head
        while True:
            print(current.value,end="---> ")
            current=current.next
            if current==self.head:
                break
        print("head")

link=Circular_linklist()
nums=[10,3,5,78,96]
for num in nums:
    link.Inser_end(num)
link.Forward_traveser()
link.Remove_at_index(2)
link.Forward_traveser()
print(f"circulat linklist size {link._Size()}")
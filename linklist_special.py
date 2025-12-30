from linklist import Linklist,Node
link=Linklist()

def _Addnode_by_index(data,index):
    if index<0 or link.size<index:
        print("INDEX ERROR INDEX OUT OF LINKLIST SIZE")
        return
    if index==0:
        link._Addnode_first(data)
        return
    if index==link._Size():
        link._Addnode_end(data)
        return
    else:
        current=link.head
        create_node=Node(data)
        idx=0
        while idx<index-1:
            current=current.next
            idx+=1
        create_node.next=current.next
        current.next=create_node
        link.size+=1

def _Remove_by_index(index):
    if index<0 or index>=link._Size():
        print("INDEX ERROR THE INDEX OUT OF BOUNDARY")
        return
    if index==0:
        link._Remove_first()   
        return
    if index==link._Size()-1:
        link._Remove_end()
        return
    else:
        current=link.head
        idx=0
        while idx<index-1:
            idx+=1
            current=current.next
        current.next=current.next.next
        link.size-=1


def reverse_travaser():
    current=link.head
    prev=None
    while current:
        current_next=current.next
        current.next=prev
        prev=current
        current=current_next
    link.head=prev
    return link.head


def search_by_index(index):
    if index<0 or index>link._Size()-1:
        print("INDEXERROR INDEX OUT OF BOUNDARY!")
        return
    else:
        current=link.head
        idx=0
        while idx<index:
           current=current.next
           idx+=1
        print(current.value)

def search_by_value(data):
    current=link.head
    index=0
    while current and current.value!=data:
        index+=1
        current=current.next
    return index if index<link._Size() else "data not found"


      
nums=[10,12]
link=Linklist()
for i in range(len(nums)):
   link._Addnode_end(nums[i])


link._Display()
search_by_index(2)
link._Display()
print(search_by_value(132))

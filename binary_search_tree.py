class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if  self.root is None:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, current, value):
        if value < current.value:
            if current.left:
                self._insert(current.left, value)
            else:
                current.left = Node(value)
        else:
            if current.right:
                self._insert(current.right, value)
            else:
                current.right = Node(value)

    def Height(self):
        return self._height(self.root)
    def _height(self,node):
        if node is None:
            return -1
        return max(self._height(node.left),self._height(node.right))+1
    

    def search_value(self,value):
            return self._search_value(self.root,value)
    def _search_value(self,node,value):
        if node is None:
            return False
        if node.value==value:
            return True
        if value<node.value:
            return self._search_value(node.left,value)
        else:
            return self._search_value(node.right,value)
        
        
    def Label_traverse(self):
        if self.root is None:
            return 
        q=[self.root]
        while q:
           node=q.pop(0)
           print(node.value,end=" --> ")
           if node.left:
               q.append(node.left)
           if node.right:
               q.append(node.right)


    def inorder(self):
        self._inorder(self.root)
    def _inorder(self,node):
        if node:
            self._inorder(node.left)
            print(node.value, end=" ")
            self._inorder(node.right)



# Example usage
bst = BinaryTree()
for val in [41, 21, 74, 98, 47, 58, 2]:
    bst.insert(val)

print("Inorder traversal:")
bst.inorder()

print(f"max height of the tree : {bst.Height()}")
bst.insert(600)
bst.Label_traverse()
# print(bst.search_value(58))
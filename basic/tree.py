class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

class tree:
    def __init__(self):
        self.root=None
    
    def isempty(self):
        return self.root==None
    
    def add(self,val):
        if self.root==None:
            self.root=Node(val)
        else:
            self._add(self.root,val)
    
    def _add(self,node,val):
        if val<node.val:
            if node.left==None:
                node.left=Node(val)
            else:
                self._add(node.left,val)
        else:
            if node.right==None:
                node.right=Node(val)
            else:
                self._add(node.right,val)

    def delete(self):
        self.root=None
    
    def print(self):
        if self.root==None:
            print('this tree is empty')
        else:
            self._print(self.root,0)
    
    def _print(self,node,level):
        if node:
            self._print(node.left,level+1)
            print('\t'*level,node.val)
            self._print(node.right,level+1)

t=tree()
t.add(15)
t.add(10)
t.add(8)
t.add(18)
t.add(20)
t.add(6)
t.add(5)
t.add(11)
t.add(13)
t.add(8)
t.add(6)
t.add(9)

t.print()

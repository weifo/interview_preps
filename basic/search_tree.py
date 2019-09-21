class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
        self.level=None
    
    def __str__(self):
        return str(self.val)

class search_tree:
    def __init__(self):
        self.root=None

    def add(self,val):
        if self.root==None:
            self.root=None(val)

        else:
            cur=self.root
            while 1:
                if val<cur.val:

                    if cur.left:
                        cur=cur.left
                    else:
                        cur.left=Node(val)
                        break
                elif val>cur.val:

                    if cur.right:
                        cur=cur.right
                    else:
                        cur.right=Node(val)
                        break

                else:
                    break

    def bft(self):
        self.root.level=0
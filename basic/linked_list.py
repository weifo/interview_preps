class LinkedListNode:
    def __init__(self,val):
        self.val=val
        self.next=None

def reverse(head_of_list):
    current=head_of_list
    previous=None

    while current:
        next=current.next
        current.next=previous
        previous=current
        current=next
    return previous
class DoublyNode:  # Definition for doubly-linked list , it has a pointer to the next node and a pointer to the previous node
    def __init__(self, val=0, next=None, prev=None): #init means initialize, it is a constructor for the class DoublyNode, self is the instance of the class, val is the value of the node, next is the pointer to the next node in the linked list, prev is the pointer to the previous node in the linked list
        #vali is equalt to zero here because we want to initialize the value of the node to zero, next is equal to None because we want to initialize the pointer to the next node to None, prev is equal to None because we want to initialize the pointer to the previous node to None
        self.val = val
        self.next = next
        self.prev = prev

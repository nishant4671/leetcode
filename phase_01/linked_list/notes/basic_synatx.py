class ListNode: # Definition for singly-linked
    def __init__(self, val=0, next=None): #init means initialize, it is a constructor for the class ListNode
        #val is the value of the node, next is the pointer to the next node in the linked list
        #none is the default value for next, which means if we don't provide a value for next, it will be None
        self.val = val #assign the value of the node to the variable val
        self.next = next #assign the pointer to the next node to the variable next

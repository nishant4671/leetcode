# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        # Initialize two pointers:
        # 'prev' will point to the previous node in the reversed list.
        # Initially, it's None because the new head (original tail) will point to None.
        prev = None
        
        # 'curr' will point to the current node being processed.
        # Initially, it's the head of the original list.
        curr = head
        
        # Iterate through the list until 'curr' becomes None (end of list)
        while curr:
            # Step 1: Store the next node in a temporary variable.
            # This is crucial because we are about to change curr.next,
            # and we need to retain the reference to the rest of the original list.
            next_temp = curr.next
            
            # Step 2: Reverse the current node's pointer.
            # Make 'curr' point to 'prev'. This is the core of the reversal.
            curr.next = prev
            
            # Step 3: Move 'prev' one step forward.
            # 'prev' now becomes the current node, as it's correctly linked.
            prev = curr
            
            # Step 4: Move 'curr' one step forward.
            # 'curr' moves to the next node in the original list (which was stored in next_temp).
            curr = next_temp
            
        # After the loop finishes, 'curr' is None, meaning we've processed all nodes.
        # 'prev' will be pointing to the last node of the original list,
        # which is now the new head of the reversed list.
        return prev
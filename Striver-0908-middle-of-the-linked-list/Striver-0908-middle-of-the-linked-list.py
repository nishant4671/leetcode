# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        slow = head
        fast = head
        
        # Iterate until fast pointer reaches the end of the list
        # or the node just before the end.
        # If fast is None, it means the list had an even number of nodes.
        # If fast.next is None, it means the list had an odd number of nodes.
        while fast and fast.next:
            slow = slow.next        # slow moves one step
            fast = fast.next.next   # fast moves two steps
            
        return slow # When the loop finishes, slow pointer is at the middle node
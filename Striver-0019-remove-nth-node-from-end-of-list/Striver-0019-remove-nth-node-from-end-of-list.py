# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        # Create a dummy node to simplify edge cases, especially when the head itself needs to be removed.
        # The dummy node points to the original head.
        dummy = ListNode(0)
        dummy.next = head

        # Initialize two pointers, 'slow' and 'fast', both starting at the dummy node.
        slow = dummy
        fast = dummy

        # Move the 'fast' pointer 'n' steps ahead.
        # This establishes a gap of 'n' nodes between 'slow' and 'fast'.
        # Since 1 <= n <= sz, 'fast' is guaranteed to stay within or at the end of the original list.
        for _ in range(n):
            fast = fast.next
        
        # Now, move both 'slow' and 'fast' pointers one step at a time
        # until the 'fast' pointer reaches the end of the list (i.e., fast.next is None).
        # When fast.next is None, 'fast' is at the last node of the list.
        # Because 'fast' initially started 'n' steps ahead of 'slow',
        # 'slow' will now be positioned exactly one node before the n-th node from the end.
        while fast.next is not None:
            slow = slow.next
            fast = fast.next
        
        # At this point, 'slow.next' is the n-th node from the end that needs to be removed.
        # Bypass this node by making 'slow.next' point to 'slow.next.next'.
        slow.next = slow.next.next
        
        # The new head of the list is dummy.next.
        # If the original head was removed, dummy.next will correctly point to the second node (or None if the list became empty).
        return dummy.next
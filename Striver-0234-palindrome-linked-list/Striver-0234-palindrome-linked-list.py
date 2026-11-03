# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: 'ListNode | None') -> bool:
        if not head or not head.next:
            return True

        # Find middle while reversing first half
        prev = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next

            # reverse the node pointed by slow
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt

        # After loop:
        # prev -> head of reversed first half
        # slow -> start of second half (or middle node if odd length)

        # If the length is odd, skip the middle node
        if fast:  # fast is not None means odd number of nodes
            slow = slow.next

        # Compare reversed first half with second half
        p1, p2 = prev, slow
        while p1 and p2:
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next

        return True
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from typing import Optional

class Solution:
    def hasCycle(self, head: Optional['ListNode']) -> bool:
        """
        Detects a cycle in a singly linked list using Floyd's Tortoise and Hare algorithm.
        Time Complexity: O(N) where N is the number of nodes.
        Space Complexity: O(1).
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next          # move by 1
            fast = fast.next.next     # move by 2
            if slow is fast:
                return True
        return False
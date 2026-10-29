# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # The problem specifies that we are given the node to be deleted,
        # but not access to the head of the list or the previous node.
        # It's also guaranteed that the given node is not the tail (last node).

        # This allows us to use a common trick for this specific problem:
        # We can effectively "delete" the current node by overwriting its value
        # with the value of its successor, and then bypassing its successor.

        # Step 1: Copy the value from the next node into the current node.
        # This makes the current node logically take on the identity of its successor.
        node.val = node.next.val

        # Step 2: Link the current node to the node after its successor.
        # This effectively removes the original successor node from the list,
        # as it is no longer reachable from the current node.
        node.next = node.next.next

        # No return statement is needed as the function modifies the list in-place.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode | None) -> ListNode | None:
        # Handle edge cases: empty list or list with only one node
        if not head or not head.next:
            return head

        # Initialize pointers for the odd and even lists
        odd = head                  # `odd` points to the current tail of the odd-indexed list
        even_head = head.next       # `even_head` stores the head of the even-indexed list for later connection
        even = even_head            # `even` points to the current tail of the even-indexed list

        # Iterate through the list, re-linking nodes
        # The loop continues as long as there are at least two more nodes to process:
        # an even node and the next odd node after it.
        while even and even.next:
            # Connect the current odd node to the next odd node (which is `even.next`)
            odd.next = even.next
            odd = odd.next  # Move `odd` pointer forward to the new tail of the odd list

            # Connect the current even node to the next even node (which is `odd.next` after the above step)
            even.next = odd.next
            even = even.next  # Move `even` pointer forward to the new tail of the even list
        
        # After the loop, `odd` is the tail of the odd-indexed list.
        # Connect the tail of the odd list to the head of the even list.
        odd.next = even_head
        
        # The original head remains the head of the reordered list.
        return head
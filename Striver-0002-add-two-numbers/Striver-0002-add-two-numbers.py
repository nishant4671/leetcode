# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        # Create a dummy head node to simplify the creation of the result list.
        # This allows us to always append to current.next without special handling
        # for the very first node.
        dummy_head = ListNode(0)
        
        # 'current' pointer will traverse the new result list.
        current = dummy_head
        
        # 'carry' will store any carry-over from digit additions.
        carry = 0

        # Loop continues as long as there are digits in either list or a carry remains.
        while l1 is not None or l2 is not None or carry != 0:
            # Get the value from l1, or 0 if l1 is exhausted.
            val1 = l1.val if l1 is not None else 0
            # Get the value from l2, or 0 if l2 is exhausted.
            val2 = l2.val if l2 is not None else 0

            # Calculate the sum of current digits and the carry.
            total_sum = val1 + val2 + carry
            
            # The new carry is the quotient of the total_sum divided by 10.
            carry = total_sum // 10
            
            # The digit for the current node is the remainder of the total_sum divided by 10.
            digit = total_sum % 10

            # Create a new node with the calculated digit and append it to the result list.
            current.next = ListNode(digit)
            
            # Move the 'current' pointer to the newly added node.
            current = current.next

            # Move l1 to its next node if it exists.
            if l1 is not None:
                l1 = l1.next
            
            # Move l2 to its next node if it exists.
            if l2 is not None:
                l2 = l2.next
        
        # The actual result list starts from the node after the dummy head.
        return dummy_head.next
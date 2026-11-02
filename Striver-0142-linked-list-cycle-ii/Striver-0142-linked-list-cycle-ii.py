# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Handle edge cases: empty list or list with a single node (no cycle possible)
        if not head or not head.next:
            return None

        slow = head
        fast = head

        # Phase 1: Detect if a cycle exists using Floyd's Tortoise and Hare algorithm
        # The loop continues as long as fast and fast.next are not None.
        # If either becomes None, it means the end of the list is reached, and no cycle exists.
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break # Cycle detected, exit the loop
        else:
            # This 'else' block is executed if the 'while' loop completes normally
            # (i.e., without hitting a 'break' statement). This means 'fast' or 'fast.next'
            # became None, indicating no cycle in the list.
            return None

        # Phase 2: Find the starting node of the cycle
        # If the loop above broke, it means 'slow' and 'fast' met, confirming a cycle.
        # Now, initialize one pointer (ptr1) at the head and another (ptr2) at the meeting point.
        # Move both pointers one step at a time; they will meet at the start of the cycle.
        ptr1 = head
        ptr2 = slow # 'slow' (and 'fast') is currently at the meeting point

        while ptr1 != ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        
        # When ptr1 and ptr2 meet, they are at the starting node of the cycle.
        return ptr1
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode | None) -> ListNode | None:
        if not head or not head.next:
            return head

        # Calculate the length of the list
        n = 0
        curr = head
        while curr:
            n += 1
            curr = curr.next

        # Dummy node to handle the head of the merged list easily
        dummy = ListNode(0)
        dummy.next = head

        # sub_list_size: current length of sublists to be merged
        # Starts at 1, then 2, 4, 8, ... up to n
        sub_list_size = 1
        while sub_list_size < n:
            # `curr` points to the head of the unsorted portion of the list
            # `tail` points to the last node of the already sorted portion (or dummy)
            curr = dummy.next
            tail = dummy

            # Iterate through the list, merging sublists of `sub_list_size`
            while curr:
                # Get the first sublist (head1)
                head1 = curr
                # `_split_list` splits the list starting from `head1`
                # It returns the head of the second part of length `sub_list_size`
                # and breaks the link between the two parts.
                head2 = self._split_list(head1, sub_list_size)
                
                # Get the second sublist (head2)
                # This call to _split_list sets `next_sublist_start` to the head of the
                # remaining part of the list after `head2` (which is also of `sub_list_size` length)
                next_sublist_start = self._split_list(head2, sub_list_size)

                # Merge the two sublists (head1 and head2)
                # `merged_head` is the head of the merged list
                # `merged_tail` is the tail of the merged list
                merged_head, merged_tail = self._merge_and_get_tail(head1, head2)
                
                # Attach the newly merged list to the overall sorted list
                tail.next = merged_head
                # Update `tail` to the end of the newly attached merged list
                tail = merged_tail
                
                # Move `curr` to the start of the next pair of sublists to be merged
                curr = next_sublist_start
            
            # Double the sublist size for the next pass
            sub_list_size *= 2
        
        return dummy.next

    def _split_list(self, head: ListNode | None, count: int) -> ListNode | None:
        """
        Splits the list starting from `head` into two parts.
        The first part will contain `count` nodes (or fewer if the list is shorter).
        The link between the first part and the second part is broken.
        Returns the head of the second part.
        """
        if not head:
            return None
        
        # Traverse `count - 1` steps to reach the end of the first sublist
        # If the list runs out before `count` nodes, `head` will point to the last node
        for _ in range(count - 1):
            if not head.next:
                break
            head = head.next
        
        # `head` is now the last node of the first sublist
        # `second_half_head` is the node immediately after it, which starts the second sublist
        second_half_head = head.next
        head.next = None # Break the link to separate the two sublists
        return second_half_head

    def _merge_and_get_tail(self, l1: ListNode | None, l2: ListNode | None) -> tuple[ListNode | None, ListNode | None]:
        """
        Merges two sorted linked lists l1 and l2 into a single sorted list.
        Returns the head and the tail of the merged list.
        """
        dummy = ListNode(0)
        current = dummy # `current` pointer to build the merged list

        while l1 and l2:
            if l1.val <= l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        
        # Attach any remaining nodes from l1 or l2
        if l1:
            current.next = l1
        elif l2:
            current.next = l2
        
        # Find the actual tail of the merged list
        # `current` is at the end of the part built by the while loop
        # It needs to advance to the very end if remaining nodes were attached
        while current.next:
            current = current.next
            
        return dummy.next, current # Return the head and the tail of the merged list
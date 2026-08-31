# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        # A critical point requires a previous and a next node.
        # This means the list must have at least 3 nodes to have any potential critical points.
        # If head, head.next, head.next.next are not all present, return [-1, -1].
        # According to constraints, the number of nodes is in range [2, 10^5].
        # So, if head.next.next is None, it means there are only 2 nodes, which cannot form critical points.
        if not head or not head.next or not head.next.next:
            return [-1, -1]

        prev_node = head
        curr_node = head.next
        
        # position_index starts from 1 because head is at index 0,
        # and curr_node is initially head.next (index 1).
        position_index = 1 
        
        first_critical_pos = -1
        last_critical_pos = -1
        min_distance = float('inf')

        # Iterate through the list. curr_node will represent the potential critical point.
        # The loop continues as long as curr_node has a next_node (curr_node.next is not None).
        # This ensures that prev_node, curr_node, and next_node are always valid for comparison.
        # curr_node iterates from head.next (index 1) up to the second-to-last node.
        while curr_node.next:
            next_node = curr_node.next
            
            # Check if curr_node is a local maxima or local minima
            is_local_maxima = (prev_node.val < curr_node.val and curr_node.val > next_node.val)
            is_local_minima = (prev_node.val > curr_node.val and curr_node.val < next_node.val)

            if is_local_maxima or is_local_minima:
                if first_critical_pos == -1:
                    # This is the first critical point found
                    first_critical_pos = position_index
                else:
                    # Update minimum distance between current critical point and the last one found
                    min_distance = min(min_distance, position_index - last_critical_pos)
                
                # Update the position of the last critical point found
                last_critical_pos = position_index
            
            # Move pointers to the next nodes
            prev_node = curr_node
            curr_node = next_node
            position_index += 1
        
        # After iterating through the entire list, check results.
        # If fewer than two critical points were found, first_critical_pos will still be -1
        # or it will be equal to last_critical_pos (meaning only one was found).
        if first_critical_pos == -1 or first_critical_pos == last_critical_pos:
            return [-1, -1]
        
        # Calculate maximum distance, which is between the first and last critical points found.
        max_distance = last_critical_pos - first_critical_pos
        
        return [min_distance, max_distance]
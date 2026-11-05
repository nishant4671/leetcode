# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        """
        Finds the node at which two singly linked lists intersect using a two-pointer approach.
        
        This method achieves O(m + n) time complexity and O(1) space complexity.
        
        The core idea is to make both pointers traverse the same total distance.
        Let listA have a unique part of length L_A and listB have a unique part of length L_B.
        Let the common part after intersection have length L_C.
        
        Total length of listA = m = L_A + L_C
        Total length of listB = n = L_B + L_C
        
        Initialize two pointers, ptrA starting at headA and ptrB starting at headB.
        
        When ptrA reaches the end of listA, it is redirected to headB.
        When ptrB reaches the end of listB, it is redirected to headA.
        
        Path traversed by ptrA: (L_A steps in listA) -> (L_C steps in common part) -> (L_B steps in listB's unique part)
                                -> (L_C steps in common part)
        Total distance for ptrA until meeting: L_A + L_C + L_B.
        
        Path traversed by ptrB: (L_B steps in listB) -> (L_C steps in common part) -> (L_A steps in listA's unique part)
                                -> (L_C steps in common part)
        Total distance for ptrB until meeting: L_B + L_C + L_A.
        
        Since both pointers traverse the same total distance (L_A + L_B + L_C),
        they are guaranteed to meet at the intersection node if one exists.
        If there is no intersection (L_C = 0), they will both reach None simultaneously
        after traversing L_A + L_B steps and the loop will terminate, returning None.
        """
        
        ptrA = headA
        ptrB = headB
        
        # Loop until pointers meet or both become None
        while ptrA != ptrB:
            # If ptrA is not None, move to the next node.
            # If ptrA is None (end of current path), redirect it to headB.
            ptrA = ptrA.next if ptrA else headB
            
            # If ptrB is not None, move to the next node.
            # If ptrB is None (end of current path), redirect it to headA.
            ptrB = ptrB.next if ptrB else headA
            
        # At this point, ptrA (and ptrB) will be:
        # 1. The intersection node, if an intersection exists.
        # 2. None, if no intersection exists.
        return ptrA
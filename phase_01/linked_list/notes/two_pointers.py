# 🔹 Two Pointers (Slow & Fast)
# Fast moves 2 steps, slow moves 1 step. Used for:

# Finding middle node (when fast reaches end, slow is middle).

# Detecting cycles (if fast meets slow, cycle exists).

# Finding k-th node from end (fast moves k steps ahead, then both move together).



# Two pointers in linked list has 3 main patterns:

# Same speed (normal traversal)

# Gap technique (remove nth from end)

# Fast & slow (cycle / middle)


# floyd's algothim 
# 1️⃣ Fast & Slow Pointer (Floyd’s Algorithm)

# Used for:

# Detect cycle

# Find middle

# Find cycle start


# basic template for cycle detection 


def hasCycle(head):
    slow = head
    fast = head
    #theroy of this code is that if there is a cycle in the liked list then the fast pointer will eventualyy meet the slow pointer and if there is no cycle then the fast pointer will reach the end of the linked list
    while fast and fast.next: #here we are checking if the fast pointer is not None and if the next pointer of the fast pointer is not None, because if the fast pointer is None then we have reached the end of the linked list and if the next pointer of the fast pointer is None then we have also reached the end of the linked list
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast: #here we are checking if the slow pointer is equal to the fast pointer, if they are equal then it means that there is a cycle in the linked list and we can return True
            return True
    
    return False




# 🔹 2️⃣ Find Middle of Linked List

# Same idea, different goal.




def findMiddle(head):
    slow = head        
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow

#when the loop ends the slow will be a t the middle and the fast willl ne at the end of the list 




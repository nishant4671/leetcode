# 🔹 Reversing a Linked List
# Iterative: maintain prev, curr, nextTemp.

# Recursive: reverse rest, then adjust.





# Core Idea (3-Pointer Method)

# You need:

# prev

# current

# next_node

# We reverse the arrow direction one by one.


def reverseList(head): # we define a function called reverseList that takes the head of the linked list as an argument
    prev = None # we initialize the prev pointer to None because the previous node of the head node is None
    current = head # we initialize the current pointer to the head of the linked list because we want to start reversing from the head node
    
    while current:# we keep reversing the linked list until we reach the end of the linked list (when current becomes None)
        next_node = current.next   # 1. Save next
        current.next = prev        # 2. Reverse link
        prev = current             # 3. Move prev forward
        current = next_node        # 4. Move current forward
    
    return prev # at the end of the while loop, prev will be pointing to the new head of the reversed linked list, so we return prev


# 🔥 This Line Is The Heart
# current.next = prev


# That’s the actual reversal.

# Everything else is pointer movement.
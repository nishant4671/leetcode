# 🔥 2️⃣ DELETE Operations

# We’ll cover:

# Delete head

# Delete at position

# Delete by value

# A) Delete Head
# Logic:

# Move head forward

def delete_head(head):
    if not head:
        return None
    return head.next







# B) Delete at Position
# Logic:

# If pos = 0 → delete head

# Go to node before target

# Skip the target



def delete_at_position(head, pos):
    if not head:
        return None
    
    if pos == 0:
        return head.next
    
    current = head
    
    for _ in range(pos - 1):
        if not current.next:
            return head
        current = current.next
    
    if current.next:
        current.next = current.next.next
    
    return head






# C) Delete by Value
# Logic:

# If head matches → remove head

# Traverse until next node matches

# Skip it




def delete_by_value(head, val):
    if not head:
        return None
    
    if head.val == val:
        return head.next
    
    current = head
    
    while current.next:
        if current.next.val == val:
            current.next = current.next.next
            break
        current = current.next
    
    return head










# # 1️⃣ INSERT Operations

# # We’ll cover:

# # Insert at beginning

# # Insert at end

# # Insert at position


# ✅ A) Insert at Beginning (Head Insertion)
# Logic:

# New node → points to old head

# Move head to new node



def insert_at_beginning(head, val):
    new_node = ListNode(val)
    new_node.next = head
    head = new_node
    return head



# ✅ B) Insert at End
# Logic:

# Traverse to last node

# Last node.next = new node

def insert_at_end(head, val):
    new_node = ListNode(val)
    
    if not head:
        return new_node
    
    current = head
    while current.next:
        current = current.next
    
    current.next = new_node
    return head



# C) Insert at Position (Index Based)

# Insert at position pos (0-based)

# Logic:

# If pos = 0 → same as head insertion

# Traverse to node before position

# Adjust pointers carefully


def insert_at_position(head, val, pos):
    if pos == 0:
        return insert_at_beginning(head, val)
    
    new_node = ListNode(val)
    current = head
    
    for _ in range(pos - 1):
        if not current:
            return head  # position invalid
        current = current.next
    
    new_node.next = current.next
    current.next = new_node
    
    return head











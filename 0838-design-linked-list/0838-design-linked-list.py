class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        
        current = self.head
        for _ in range(index):
            current = current.next
        return current.val

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        if self.tail is None: # If list was empty, new node is also the tail
            self.tail = new_node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        if self.head is None: # If list is empty, equivalent to addAtHead
            self.addAtHead(val)
            return
        
        new_node = Node(val)
        self.tail.next = new_node
        self.tail = new_node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        
        if index == 0:
            self.addAtHead(val)
            return
        
        if index == self.size:
            self.addAtTail(val)
            return
            
        # Traverse to the node *before* the index-th node (i.e., at index - 1)
        current = self.head
        for _ in range(index - 1):
            current = current.next
        
        new_node = Node(val)
        new_node.next = current.next
        current.next = new_node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        
        if index == 0:
            self.head = self.head.next
            if self.head is None: # If list becomes empty after deleting head
                self.tail = None
            self.size -= 1
            return
            
        # Traverse to the node *before* the index-th node (i.e., at index - 1)
        current = self.head
        for _ in range(index - 1):
            current = current.next
        
        # current is now the node before the one to be deleted
        node_to_delete = current.next
        current.next = node_to_delete.next
        
        if node_to_delete == self.tail: # If the tail was deleted, update tail to current
            self.tail = current
        
        self.size -= 1
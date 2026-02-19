node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)

node1.next = node2
node2.next = node3

head = node1

#this here is the code for creating a linked list with three nodes. We create three nodes with values 1, 2, and 3, and we link them together by setting the next pointer of each node to the next node in the linked list. Finally, we set the head of the linked list to the first node (node1).
#Note that we can also create a linked list using a loop, but for simplicity, we are creating the linked list manually here.

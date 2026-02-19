current = head # we start with the head of the linked list  , here head refer to the forst node of the linked list 
while current: # we keep moving to the next node until we reach the end of the linked list (when current becomes None)
    print(current.val)
    current = current.next # thus we move to the next node in the linked list


#this here is the code for traversing a linked list. We start with the head of the linked list and we keep moving to the next node until we reach the end of the linked list (when current becomes None). In each iteration, we print the value of the current node.
#Note that we are using a while loop to traverse the linked list. We could also use a for loop, but a while loop is more common for traversing linked lists because we don't know the length of the linked list in advance.

'''Write a Python program to reverse a singly linked list using iteration and display the reversed linked list.'''

# Node structure of the linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:

    # Function to reverse the linked list
    def reverseList(self, head):

        # Initialize previous and current pointers
        prev = None
        curr = head

        # Traverse the linked list
        while curr is not None:

            # Store the next node
            nextNode = curr.next

            # Reverse the current node's link
            curr.next = prev

            # Move prev and curr one step forward
            prev = curr
            curr = nextNode

        # Return the new head
        return prev


# Create linked list: 1 -> 2 -> 3 -> 4 -> 5
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

# Create object
obj = Solution()

# Reverse the linked list
head = obj.reverseList(head)

# Print the reversed linked list
print("Reversed Linked List:")

while head is not None:
    print(head.data, end=" ")
    head = head.next
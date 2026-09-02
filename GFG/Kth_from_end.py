'''Write a program to find the Kth node from the end of a singly linked list using the two-pointer approach'''

# Node structure of the linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:

    # Function to find Kth node from the end
    def kthFromEnd(self, head, k):

        # Initialize two pointers
        first = head
        second = head

        # Move first pointer k positions ahead
        for i in range(k):
            if first is None:
                return -1
            first = first.next

        # Move both pointers until first reaches the end
        while first is not None:
            first = first.next
            second = second.next

        # Second pointer is now at Kth node from end
        return second.data


# Create linked list: 10 -> 20 -> 30 -> 40 -> 50
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)

# Take k as input
k = int(input("Enter k: "))

# Create object
obj = Solution()

# Find and print Kth node from the end
result = obj.kthFromEnd(head, k)

print("Kth node from end:", result)
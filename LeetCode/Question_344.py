'''Write a Python program to reverse an array of characters in-place using O(1) extra space.'''

class Solution(object):

    def reverseString(self, s):

        # Initialize two pointers
        left = 0
        right = len(s) - 1

        # Swap characters from both ends
        while left < right:

            s[left], s[right] = s[right], s[left]

            # Move pointers towards the center
            left += 1
            right -= 1
'''Given an integer array nums, write a Python program to determine whether any value appears at least twice in the array. Return True if a duplicate exists; otherwise, return False.'''

class Solution(object):

    def containsDuplicate(self, nums):

        # Create a set to store unique elements
        seen = set()

        # Traverse the array
        for num in nums:

            # If element is already present, duplicate exists
            if num in seen:
                return True

            # Add element to the set
            seen.add(num)

        # No duplicate found
        return False
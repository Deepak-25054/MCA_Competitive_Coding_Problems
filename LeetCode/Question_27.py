''' Given an integer array nums and an integer val, write a Python program to remove all occurrences of val from the array in-place and return the number of elements that are not equal to val.'''

class Solution(object):

    def removeElement(self, nums, val):

        # Pointer to place elements that are not equal to val
        k = 0

        # Traverse the array
        for i in range(len(nums)):

            # If current element is not equal to val
            if nums[i] != val:

                # Move it to position k
                nums[k] = nums[i]
                k += 1

        # Return number of remaining elements
        return k
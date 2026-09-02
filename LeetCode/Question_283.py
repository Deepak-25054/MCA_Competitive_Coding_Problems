'''Given an integer array nums, write a Python program to move all 0s to the end of the array while maintaining the relative order of the non-zero elements. The operation must be performed in-place without making a copy of the array.'''

class Solution(object):

    def moveZeroes(self, nums):

        # Position for the next non-zero element
        k = 0

        # Traverse the array
        for i in range(len(nums)):

            # If the element is non-zero
            if nums[i] != 0:

                # Swap non-zero element to position k
                nums[k], nums[i] = nums[i], nums[k]

                k += 1
''' Given a sorted integer array nums, remove the duplicates in-place so that each unique element appears only once. Return the number k of unique elements.'''

class Solution(object):
    def removeDuplicates(self, nums):

        # If array is empty
        if len(nums) == 0:
            return 0

        # Pointer for placing unique elements
        k = 1

        # Traverse the array
        for i in range(1, len(nums)):

            # If current element is different
            # from the previous unique element
            if nums[i] != nums[k - 1]:

                nums[k] = nums[i]
                k += 1

        return k
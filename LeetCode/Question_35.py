'''Given a sorted array of distinct integers and a target value, write a Python program to find the index of the target. If the target is not present, return the index where it should be inserted to maintain the sorted order. Use binary search with O(log n) time complexity.'''

class Solution(object):

    def searchInsert(self, nums, target):

        left = 0
        right = len(nums) - 1

        # Apply binary search
        while left <= right:

            mid = (left + right) // 2

            # Target found
            if nums[mid] == target:
                return mid

            # Search right half
            elif nums[mid] < target:
                left = mid + 1

            # Search left half
            else:
                right = mid - 1

        # Left is the correct insertion position
        return left
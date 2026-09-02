'''Given a rotated sorted array of distinct integers and a target value, write a Python program to find the index of the target using binary search. Return -1 if the target is not present. The algorithm must run in O(log n) time.'''

class Solution(object):

    def search(self, nums, target):

        left = 0
        right = len(nums) - 1

        while left <= right:

            # Find the middle element
            mid = (left + right) // 2

            # Target found
            if nums[mid] == target:
                return mid

            # Check if left half is sorted
            if nums[left] <= nums[mid]:

                # Target lies in the left sorted half
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            # Otherwise, right half is sorted
            else:

                # Target lies in the right sorted half
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        # Target not found
        return -1

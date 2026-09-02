'''Given an integer array nums and an integer k, find the contiguous subarray of length k that has the maximum average value and return the maximum average.'''

class Solution(object):

    def findMaxAverage(self, nums, k):

        # Find the sum of the first k elements
        window_sum = sum(nums[:k])

        # Store the maximum sum
        max_sum = window_sum

        # Slide the window through the array
        for i in range(k, len(nums)):

            # Remove the first element and add the new element
            window_sum += nums[i] - nums[i - k]

            # Update maximum sum
            max_sum = max(max_sum, window_sum)

        # Return maximum average
        return max_sum / k
'''Given an array nums of size n, find the majority element. The majority element is the element that appears more than n/2 times. The majority element is guaranteed to exist. Solve the problem in O(n) time and O(1) extra space.'''

class Solution(object):

    def majorityElement(self, nums):

        count = 0
        candidate = None

        # Find the majority candidate
        for num in nums:

            # Choose a new candidate when count becomes 0
            if count == 0:
                candidate = num

            # Increase count for same element
            if num == candidate:
                count += 1

            # Decrease count for different element
            else:
                count -= 1

        return candidate
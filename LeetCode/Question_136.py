'''
Question:
Given a non-empty integer array nums where every element appears twice
except for one element, find the element that appears only once.
The solution must have O(n) time complexity and O(1) extra space.
'''

class Solution(object):

    def singleNumber(self, nums):

        # Initialize result
        ans = 0

        # XOR all elements
        for num in nums:
            ans = ans ^ num

        # Return the single number
        return ans
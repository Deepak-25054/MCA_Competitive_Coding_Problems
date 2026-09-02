'''Given an array nums containing n distinct numbers in the range [0, n], write a Python program to find and return the only number that is missing from the array.'''

class Solution(object):

    def missingNumber(self, nums):

        # Start with n
        n = len(nums)
        result = n

        # Use XOR to find the missing number
        for i in range(n):
            result = result ^ i ^ nums[i]

        return result
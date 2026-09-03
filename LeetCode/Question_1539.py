'''
Question:
Given a sorted array arr of strictly increasing positive integers and
an integer k, find the kth positive integer that is missing from the array.
'''

class Solution(object):

    def findKthPositive(self, arr, k):

        # Start checking from 1
        num = 1

        # Continue until k missing numbers are found
        while k > 0:

            # Check if the number is missing
            if num not in arr:
                k -= 1

            # Move to the next positive number
            num += 1

        # Return the kth missing positive number
        return num - 1
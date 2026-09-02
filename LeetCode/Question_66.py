''' Write a Python program to add one to a large integer represented as an array of digits and return the updated array of digits.'''

class Solution(object):

    def plusOne(self, digits):

        # Traverse the array from the last digit
        for i in range(len(digits) - 1, -1, -1):

            # If digit is less than 9, add 1 and return
            if digits[i] < 9:
                digits[i] += 1
                return digits

            # If digit is 9, make it 0 and continue
            digits[i] = 0

        # If all digits were 9, add 1 at the beginning
        return [1] + digits
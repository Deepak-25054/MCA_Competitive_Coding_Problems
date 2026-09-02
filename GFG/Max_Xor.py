''' Write a Python program using a class to find the maximum XOR value among all subarrays of size k in a given array.'''

class Solution:
    def maxSubarrayXOR(self, arr, k):
        # code here
        
       class Solution:
        def maxSubarrayXOR(self, arr, k):
           xor = 0
           ans = 0

           for i in range(len(arr)):
               xor ^= arr[i]
               if i >= k - 1:
                   ans = max(ans, xor)
                   xor^= arr[i - k + 1]

           return ans
arr = list(map(int, input("Enter array elements: ").split()))
k = int(input("Enter k: "))

obj = Solution()

print("Maximum XOR:", obj.maxSubarrayXOR(arr, k))
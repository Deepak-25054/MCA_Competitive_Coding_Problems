'''Given two sorted integer arrays nums1 and nums2, merge them into a single sorted array. The merged array must be stored in nums1 in-place.'''

class Solution(object):

    def merge(self, nums1, m, nums2, n):

        # Start from the last elements of both arrays
        i = m - 1
        j = n - 1

        # Position where we place the largest element
        k = m + n - 1

        # Compare elements from the end
        while i >= 0 and j >= 0:

            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1

            k -= 1

        # Copy remaining elements of nums2
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
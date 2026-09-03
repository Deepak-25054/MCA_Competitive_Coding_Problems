'''Given an integer array height where height[i] represents the height of a vertical line, find two lines that together with the x-axis form a container that can hold the maximum amount of water. Return the maximum area of water the container can store.'''

class Solution(object):

    def maxArea(self, height):

        # Initialize two pointers
        left = 0
        right = len(height) - 1

        # Store maximum area
        max_water = 0

        # Move pointers towards each other
        while left < right:

            # Calculate width
            width = right - left

            # Container height is the smaller line
            h = min(height[left], height[right])

            # Calculate current area
            area = width * h

            # Update maximum area
            max_water = max(max_water, area)

            # Move the pointer with smaller height
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_water
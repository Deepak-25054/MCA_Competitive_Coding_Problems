'''Given the coordinates of two axis-aligned rectangles in a 2D plane, write a Python program to find the total area covered by the two rectangles.'''

class Solution(object):

    def computeArea(self, ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):

        # Calculate the area of first rectangle
        area1 = (ax2 - ax1) * (ay2 - ay1)

        # Calculate the area of second rectangle
        area2 = (bx2 - bx1) * (by2 - by1)

        # Find the overlapping boundaries
        left = max(ax1, bx1)
        right = min(ax2, bx2)
        bottom = max(ay1, by1)
        top = min(ay2, by2)

        # Initially, there is no overlap
        overlap = 0

        # Check whether the rectangles overlap
        if right > left and top > bottom:
            overlap = (right - left) * (top - bottom)

        # Total area = both areas - overlapping area
        return area1 + area2 - overlap
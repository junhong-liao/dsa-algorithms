'''
approach:
    two pointers, left and right
    move the smaller pointer, as it is the bottleneck
    this is because area is calculated as base * height, where height = min(left, right)

'''

import math

# optimal approach
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right, max_area = 0, len(height) - 1, 0
        while left < right:
            base = right - left
            area = base * min(height[left], height[right])
            max_area = max(max_area, area)
            if height[left] <= height[right]: left += 1
            else: right -= 1
        return max_area

# minimized 
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right, max_area = 0, len(height) - 1, 0
        while left < right:
            max_area = max((right-left)*min(height[left],height[right]),max_area)
            if height[left] <= height[right]: left += 1
            else: right -= 1
        return max_area
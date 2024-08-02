import math

class Solution:
    def maxArea(self, height: list[int]) -> int:
        start, end = 0, len(height) - 1
        max_area = -math.inf
        while start < end:
            # INCORRECT: current_area = (end - start + 1) * min(height[start], height[end])
            # incorrect because the width holds water inside, not counting the walls as volume
            # correct approach is end - start
            current_area = (end - start) * min(height[start], height[end])
            max_area = max(current_area, max_area)
            if height[start] > height[end]: 
                end -= 1
            elif height[start] < height[end]:
                start += 1
            else:
                if height[start + 1] > height[end - 1]:
                    start += 1
                else:
                    end -= 1
        return max_area
class Solution:
    # def trap(self, height: List[int]) -> int:
    #     if len(height) < 3:
    #         return 0
    #     start, end = 0, 1
    #     max_height = height[start]
    #     total_sum, current_sum = 0, 0
    #     while end < len(height) - 1:
    #         if height[end] >= max_height:
    #             max_height = height[end]
    #             total_sum += current_sum
    #             current_sum = 0
    #             # increment start and end
    #             start = end
    #             end += 1
    #         else:
    #             # this only works if height[end] >= max_height
    #             current_sum += height[start] - height[end] # height in b * h for adding new area   
    #             end += 1
    #     return total_sum
  
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        start, end = 0, 1
        max_height = height[start]
        total_sum, current_sum = 0, 0
        while end < len(height) - 1:
            if height[end] >= max_height:
                max_height = height[end]
                total_sum += current_sum
                current_sum = 0
                # increment start and end
                start = end
                end += 1
            else:
                # this only works if height[end] >= max_height
                current_sum += height[start] - height[end] # height in b * h for adding new area   
                end += 1
        return total_sum
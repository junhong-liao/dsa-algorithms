from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low, high = 0, len(matrix) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if self.search(matrix[mid], target): return True
            if matrix[mid][0] > target:
                high = mid - 1
            elif matrix[mid][len(matrix[mid]) - 1] < target:
                low = mid + 1
            else: return False
        return False
    
    def search(self, nums: List[int], target: int) -> bool:
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else: return True
            return False

matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]]
target = 40
s = Solution()
print(s.searchMatrix(matrix, target))

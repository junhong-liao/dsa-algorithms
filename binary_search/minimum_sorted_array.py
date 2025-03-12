import math
from typing import List

# remember to draw this one out. visuals are incredibly helpful here.

# class Solution:
#     def findMin(self, nums: List[int]) -> int:
#         left, right = 0, len(nums) - 1
#         res = math.inf
#         while left <= right:
#             mid = left + (right - left) // 2
#             res = min(res, nums[mid])
#             if nums[right] > nums[left]:
#                 res = min(res, nums[left])
#                 right = mid - 1
#             elif nums[mid] > nums[left]: 
#                 left = mid + 1
#             else: 
#                 right = mid - 1
#         return res

# final solution
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            if nums[left] <= nums[right]:
                return nums[left]
            mid = left + (right - left) // 2
            if nums[mid] < nums[left]: # we know the pivot must be in the left side
                right = mid # but the minimum could be mid. our check happens above.
            else: # nums[mid] >= nums[left], we have to check the right side
                left = mid + 1 #

# minimized
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            if nums[left] <= nums[right]:
                return nums[left]
            mid = left + (right - left) // 2
            if nums[mid] < nums[left]: right = mid
            else: left = mid + 1

s = Solution()
nums=[3,4,5,6,1,2]
print(s.findMin(nums))
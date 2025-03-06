from typing import List

# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         res = set()
#         nums.sort()
#         for i in range(len(nums) - 2):
#             left, right = i + 1, len(nums) - 1
#             while left < right:
#                 three_sum = nums[i] + nums[left] + nums[right]
#                 # a, b, c = nums[i], nums[left], nums[right]
#                 if three_sum > 0: 
#                     right -= 1
#                 elif three_sum < 0: 
#                     left += 1
#                 else:
#                     res.add((nums[i], nums[left], nums[right]))
#                     left += 1
#         return [list(x) for x in res]

# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         res, nums = list(), sorted(nums)
#         for i in range(len(nums) - 2):
#             left, right = i + 1, len(nums) - 1
#             if i > 0 and nums[i] == nums[i - 1]:
#                 continue
#             while left < right:
#                 candidate = nums[i] + nums[left] + nums[right]
#                 if candidate > 0:
#                     right -= 1
#                 elif candidate < 0:
#                     left += 1
#                 else:
#                     res.append([nums[i], nums[left], nums[right]])
#                     left, right = left + 1, right - 1
#                     while left < right and nums[left] == nums[left - 1]:
#                         left += 1
#         return res

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res, nums = list(), sorted(nums)
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            if i > 0 and nums[i] == nums[i - 1]: continue
            while left < right:
                candidate = nums[i] + nums[left] + nums[right]
                if candidate > 0: right -= 1
                elif candidate < 0: left += 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    left, right = left + 1, right - 1
                    # 
                    while left < right and nums[left] == nums[left - 1]: left += 1
        return res

nums=[-1,-1,-1,0,1,2,-1,-4]
s = Solution()
print(s.threeSum(nums))
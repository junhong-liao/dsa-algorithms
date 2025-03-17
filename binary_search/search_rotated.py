from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[left] < nums[right]: return left
            elif nums[mid] < nums[left]: # search leftwards
                right = mid
            else: left = mid + 1 # current mid is not the biggest, start again from mid + 1
        return -1

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target: return mid
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]: # mid is a part of the left sorted subarray
                    right = mid - 1
                else: left = mid + 1
            else: # mid is a part of the right sorted subarray
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else: right = mid - 1
        return -1
    
s = Solution()
nums = [4,5,6,7,0,1,2]
target = 0
print(s.search(nums, target))
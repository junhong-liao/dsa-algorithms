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

# more straightforward solution by cases
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target: return mid
            if nums[mid] >= nums[left]:
                if nums[mid] > target >= nums[left]:
                    right = mid - 1
                else:
                    left = mid + 1
            else: 
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
    
s = Solution()
nums = [4,5,6,7,0,1,2]
target = 0
print(s.search(nums, target))
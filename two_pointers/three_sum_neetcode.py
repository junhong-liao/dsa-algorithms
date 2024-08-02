class Solution:
    def threeSum(self, nums: list[int]) -> list[int]:
        result = []
        nums.sort()
        for i, num in enumerate(nums):
            # avoid duplicates
            if i > 0 and num == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                sum = num + nums[left] + nums[right]
                if sum > 0:
                    right -= 1
                elif sum < 0:
                    left += 1
                else:
                    result.append([num, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return result
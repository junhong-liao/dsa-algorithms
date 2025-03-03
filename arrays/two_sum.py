from typing import List

def twoSum(self, nums: List[int], target: int) -> List[int]:
    mem = {}
    for i, n in enumerate(nums):
        if target - n in mem: 
            return [mem[target - n], i]
        mem[n] = i

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mem = dict()
        for i in range(len(nums)):
            if (target - nums[i]) in mem:
                return sorted([i, mem[target - nums[i]]])
            mem[nums[i]] = i
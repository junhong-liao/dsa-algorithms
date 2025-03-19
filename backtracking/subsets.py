from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            current = res[:] # shallow copy > .copy()
            for candidate in current:
                res.append(candidate + [num])
        return res
        
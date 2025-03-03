from typing import List
import collections

# with collections.Counter()
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mem = collections.Counter(nums)
        return [x[0] for x in sorted(mem.items(), key=lambda x : x[1], reverse=True)[:k]]
    
# no Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mem = dict()
        for num in nums:
            if num not in mem: 
                mem[num] = 0
            mem[num] += 1
        return sorted(mem.keys(), key=lambda x: mem[x], reverse=True)[:k]
        
from typing import List

def hasDuplicate(nums: List[int]) -> bool:
    mem = {}
    for n in nums:
        mem[n] = mem.get(n, 0) + 1
        if mem[n] > 1: return False
    return True
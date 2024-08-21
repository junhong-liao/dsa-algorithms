from typing import List
from collections import defaultdict

def groupAnagrams(strs: List[str]) -> List[List[str]]:
    mem = defaultdict(list)
    for s in strs:
        count = [0] * 26
        for c in s: count[ord(c) - ord('a')] += 1
        mem[tuple(count)].append(s)
    return mem.values()
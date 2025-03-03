from typing import List
from collections import defaultdict

def groupAnagrams(strs: List[str]) -> List[List[str]]:
    mem = defaultdict(list)
    for s in strs:
        count = [0] * 26
        for c in s: count[ord(c) - ord('a')] += 1
        mem[tuple(count)].append(s)
    return mem.values()



'''
Group anagrams together into sublists

anagram: string containing exact same chars as another wrt ordering

approach:

since we have only lowercase english letters, we can use 26-length arrays



'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mem = dict()
        for s in strs:
            arr = tuple(self.charCount(s))
            if arr not in mem:
                mem[arr] = list()
            mem[arr].append(s)
        
        res = list()
        for key in mem:
            res.append(mem[key])
        return res

    def charCount(self, s: str) -> List[int]:
        res = [0] * 26
        for ch in s:
            res[ord('a') - ord(ch)] += 1
        return res



    
        
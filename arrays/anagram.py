def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t): return False
    sMap, tMap = dict(), dict()
    for i in range(len(s)):
        sMap[s[i]] = sMap.get(s[i], 0) + 1
        tMap[t[i]] = tMap.get(t[i], 0) + 1
    return sMap == tMap

import collections

def isAnagramOptimized(s: str, t: str) -> bool:
    return collections.Counter(s) == collections.Counter(t)
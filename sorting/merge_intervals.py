'''
Given an array of intervals where intervals[i] = [starti, endi], 
merge all overlapping intervals, and return an array of the 
non-overlapping intervals that cover all the intervals in the input.
'''
from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        res = [intervals[0]]
        for i in intervals[1:]:
            # if the current interval start is prior to the ending of the first interval, merge
            if i[0] <= res[-1][1]: 
                res[-1][1] = max(res[-1][1], i[1])
            # else, new interval group
            else: 
                res.append(i)
        return res
    
# minimized
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        res = [intervals[0]]
        for interval in intervals[1:]:
            if interval[0] <= res[-1][1]: res[-1][1] = max(res[-1][1], interval[1])
            else: res.append(interval)
        return res
            
        

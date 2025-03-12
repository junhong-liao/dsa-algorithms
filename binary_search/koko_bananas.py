import math
from typing import List

class Solution:
	def minEatingSpeed(self, piles: List[int], h: int) -> int:
		low, high = 1, max(piles) # REMEMBER TO START AT 1, avoid divison by zero
		res = math.inf
		while low <= high:
			k = low + (high - low) // 2
			hours = sum([math.ceil(pile / k) for pile in piles])

            # if total time (hours) exceeds h, need to increase eating rate, because eating rate increase = total time decrease
			# here, we went a little too low
			if hours > h: low = k + 1

            # if total time is under or equal to h, we can try decreasing the eating rate, because eating rate decrease = total time decrease.
			else:
				res = min(res, k)
				high = k - 1
		return res
	
piles=[3,6,7,11]
h=8
s = Solution()
print(s.minEatingSpeed(piles, h))
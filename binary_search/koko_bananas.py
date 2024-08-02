class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int: 
        max_pile = 0
        for p in piles:
            max_pile = max(p, max_pile)

        if len(piles) == 1:
            return -(-p//h)

        candidates = [x for x in range(1, max_pile + 1)] # cant divide by zero. also, recall range stops 1 before

        # binary search:
        low, high = 0, len(candidates) - 1
        while low <= high:
            mid = low + (high - low) // 2
            c = candidates[mid]
            c_hours = self.check_candidate_helper(c, piles)
            if c_hours == h:
                return c
            if c_hours > h: # need to eat faster
                low = mid + 1
            if c_hours < h: # can eat slower
                high = mid - 1

    # maybe should have written it all out via example instead of only logic
    def check_candidate_helper(self, k: int, piles: List[int]) -> int:
        sum = 0
        for p in piles:
            sum += -(-p//k) # ceil equivalent, // makes negatives bigger
        return sum
    
# s = Solution()
# piles = [3,6,7,11]
# h = 8
# # piles = [30,11,23,4,20]
# # h = 6
# print(s.minEatingSpeed(piles, h))

# above is my best shot. below is neetcode's sln.

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        while l <= r:
            k = (l + r) // 2

            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p) / k)
            if totalTime <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        return res

class Solution:
    # original
    # 'while check and pop' method prior to appending
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res, fleets = list(), sorted(zip(position, speed), key=lambda x:x[0])
        for p, s in fleets:
            t = (target - p)/s
            while res and t >= res[-1][1]: 
                res.pop()
            res.append((p, t))
        return len(res)

    # minimized
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res = list()
        for p, s in sorted(zip(position, speed), key=lambda x:x[0]):
            t = (target - p)/s
            while res and t >= res[-1][1]: res.pop()
            res.append((p, t))
        return len(res)
from collections import defaultdict

class TimeMap:
    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((value, timestamp))
    
    def get(self, key: str, timestamp: int) -> str:
        res = ""
        arr = self.store[key]
        low, high = 0, len(arr) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if arr[mid][1] <= timestamp: # if valid result, we need to look if theres a closer match
                res = arr[mid][0]
                low = mid + 1
            else: # else, we are indexing (mid) timestamps that are too high, look leftward
                high = mid - 1
        return res

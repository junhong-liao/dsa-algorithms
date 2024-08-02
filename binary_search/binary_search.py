class Solution:
    def search(self, nums: list[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        while low < high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid
            else:
                low = mid
        return -1
    
def main():
    arr = [-1,0,3,5,9,12]
    target = 9
    s = Solution()
    res = s.search(arr, target)
    print(res)

main()
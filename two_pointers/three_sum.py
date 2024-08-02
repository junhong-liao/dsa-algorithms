class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = set()
        nums.sort()
        print(nums)
        for i in range(len(nums)):
            print(str(i) + " iteration of outer loop")
            # print(len(nums))
            start = 0
            end = len(nums) - 1
            while(start < end):
                print("start: " + str(start))
                print("end: " + str(end))
                if start == i:
                    start += 1
                    continue
                if end == i:
                    end -= 1
                    continue
                sum = nums[i] + nums[start] + nums[end]
                if sum == 0:
                    print("sum found, adding to set")
                    r = sorted([nums[i], nums[start], nums[end]])
                    result.add(tuple(r))
                    continue # have to do something diff
                if sum < 0:
                    print("sum is " + str(sum) + " moving start fwd")
                    start += 1
                if sum > 0:
                    print("sum is " + str(sum) + " moving end back")
                    end -=1
        return result
        
def main():
    nums = [-1,0,1,2,-1,-4]
    s = Solution()
    print(s.threeSum(nums))

main()


'''
Given:
* nums: list[int]

Return:
* output: list[int], product of all elements of nums, except nums[i]

Approach:

Input: nums = [1,2,4,6]
Output: [48,24,12,8]

[2*4*6, 1*4*6, 1*2*6, 1*2*4]
[product before, number, product after]

pre-product: [1, 1, 2, 8]
post-product: [1, 6, 24, 48] -> reversed: [48, 24, 6, 1]

'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre, post = list(), list()
        x = 1
        for i in range(len(nums)):
            pre.append(x)
            x *= nums[i]
        x = 1
        for i in range(len(nums) - 1, -1, -1):
            post.append(x)
            x *= nums[i]
        return [pre[i] * post[::-1][i] for i in range(len(nums))]
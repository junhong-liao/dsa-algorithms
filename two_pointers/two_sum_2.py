'''
Given:
* numbers: list[int], sorted in ascending order
* target: int

Returns: indices of two numbers such that they add up to a given target number, and index1 < index2

Approach:
* since sorted, two pointers can be used to traverse and find the result in linear time and constant space.
* if start + end > target: end -= 1. else start += 1

'''
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] > target: right -= 1
            elif numbers[left] + numbers[right] < target: left += 1
            else: return [left + 1, right + 1] # the question indicated that it was one indexed


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start, end = 1, len(numbers)
        while start < end:
            if numbers[start] + numbers[end] > target: end -= 1
            elif numbers[start] + numbers[end] < target: start += 1
            else: return [start, end] # the question indicated that it was one indexed
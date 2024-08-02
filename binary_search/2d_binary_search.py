class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> int:
        low, high, mid = 0, len(matrix) - 1, 0
        while low <= high:
            mid = low + (high - low) // 2
            if matrix[mid][0] > target:
                high = mid - 1
            elif matrix[mid][-1] < target:
                low = mid + 1
            else:
                print(f"matrix row: {mid}")
                return Solution.search(Solution, matrix[mid], target)
        return False
        
    def search(self, arr: list[int], target: int) -> int:
        low, high = 0, len(arr) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if arr[mid] > target:
                high = mid - 1
            elif arr[mid] < target:
                low = mid + 1
            else:
                print(f"row index: {mid}")
                return True
        return False

def main():
    s = Solution()
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 3
    print(s.searchMatrix(matrix, target))

main()
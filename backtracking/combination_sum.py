class Solution():
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = list()
        def backtrack(start, target, comb):
            if target == 0:
                res.append(list(comb))
                return
            for i in range(start, len(candidates)):
                if target < candidates[i]: continue
                comb.append(candidates[i])
                backtrack(i, target - candidates[i], comb)
                comb.pop()
        backtrack(0, target, list())
        return res

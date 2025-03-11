from typing import List
import time

def generateParenthesis(n: int) -> List[str]:
    res = set()
    def backtrack(o, c, candidate, n) -> str:
        if c == n:
            res.add(candidate)   
        if o < n:
            backtrack(o + 1, c, candidate + "(", n)
        if c < o:
            backtrack(o, c + 1, candidate + ")", n)

    backtrack(0, 0, "", n)
    return list(res)

n = 6
tests = [x for x in range(n)]
for i, test in enumerate(tests):
    result = generateParenthesis(test)
    print(f"result {i}: {result}")
    time.sleep(2)
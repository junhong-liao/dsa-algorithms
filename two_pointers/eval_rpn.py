'''
Use a set to check if a token is a member of operands
For each token, if it is an operand, pop the last two values, apply the operator, and append the result.
Else, just append the number as an integer. If you convert to int here, you can skip having to convert it after you pop the values.
Lesson: if you can clean the data when you input the data, do so
'''


from typing import List
import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = set(["*", "-", "+", "/"])
        res = list()
        for t in tokens:
            if t in operands:
                b, a = res.pop(), res.pop()
                if t == '+': res.append(a + b)
                elif t == '-': res.append(a - b)
                elif t == '*': res.append(a * b)
                else: res.append(int(a / b))
            else: res.append(int(t))
        return res[0]
    
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = {'+' : operator.add, '-' : operator.sub, 
                    '*' : operator.mul, '/' : operator.truediv}
        result = list()
        for token in tokens:
            if token in operands:
                b, a = result.pop(), result.pop()
                result.append(int(operands[token](a, b)))
            else: result.append(int(token))
        return result[0]
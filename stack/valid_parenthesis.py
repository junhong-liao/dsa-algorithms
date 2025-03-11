'''
Approach:

store the characters in a stack, one by one.
the stack validates the current string at each step

case 1: empty stack
case 2: closing bracket with mismatching open bracket
case 3: closing bracket with no open brackets
case 4: open brackets
'''

class Solution:
    def isValid(self, s: str) -> bool:
        if not s: return True
        parenthesis_map = {']':'[', '}':'{', ')':'('}
        stack = list()
        for ch in s:
            if ch not in parenthesis_map.keys(): stack.append(ch)
            else:
                if stack and parenthesis_map[ch] == stack[-1]: stack.pop()
                else: return False
        return not stack
    

class Solution:
    def isValid(self, s: str) -> bool:
        mapping, stack = {')': '(', '}': '{', ']': '['}, []
        for c in s:
            if c in mapping:
                if not stack or stack.pop() != mapping[c]:
                    return False
            else: 
                stack.append(c)
        return not stack
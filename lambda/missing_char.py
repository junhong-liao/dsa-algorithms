'''
Function: missing_char
Given: s: str, n: int
Returns:
    s with nth char removed
'''

missing_char = lambda s, n: s[:n] + s[n + 1:]
print(missing_char("hello", 3))
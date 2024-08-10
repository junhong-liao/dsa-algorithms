'''
Prompt: 
    Given a string, we'll say that the front is the first 3 chars of the string. 
    If the string length is less than 3, the front is whatever is there. 
    Return a new string which is 3 copies of the front.

Given: 
    s: str

Returns:
    new string s.t. str = front 3 chars, three times
'''


front3 = lambda s: s[:3] * 3
s = "hello"
print(front3(s))
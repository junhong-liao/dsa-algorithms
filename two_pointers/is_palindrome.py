# initial
class Solution:
    def isPalindrome(self, s: str) -> bool:
        sanitize = [ch.lower() for ch in s if ch.isalnum()]
        sanitize = ''.join(sanitize)
        return sanitize == sanitize[::-1]
    
# optimized
class Solution:
    def isPalindrome(self, s: str) -> bool:
        sanitize = [ch.lower() for ch in s if ch.isalnum()]
        return sanitize == sanitize[::-1]

# two pointers

class Solution:
    def isPalindrome(self, s: str) -> bool:
        start, end = 0, len(s) - 1
        while start < end:
            while not start.isalnum():
                start += 1
            while not end.isalnum():
                end -= 1
            if start.lower() != end.lower(): return False
        return True

# two pointers, concise

class Solution:
    def isPalindrome(self, s: str) -> bool:
        start, end = 0, len(s) - 1
        while start < end:
            while not s[start].isalnum(): start += 1
            while not s[end].isalnum(): end -= 1
            if s[start].lower() != s[end].lower(): return False
            start, end = start + 1, end - 1
        return True

    



'''

Task 1: Encode list of strings to a single string
Task 2: Decode encoded string into a list of strings

Approach:
    Input: ["neet","code","love","you"]

    neet = length of 4 -> #4neet
    encoding: #4neet#4code#4love#3you

    decoding:
        see #, look for number (length)
        slice [i + 2: i + 2 + length + 1], add to result
        i += (2 + length)
        continue while len(str) > 3
'''

class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += "#" + str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = list()
        i = 0
        while i < len(s):
            if s[i] == "#":
                i += 1
                length = ""
                while s[i] != "#":
                    length += s[i]
                    i += 1
                length = int(length)
                i += 1
                res.append(s[i : i + length])
                i += length
        return res
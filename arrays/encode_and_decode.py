'''
encode: formula: # + length + # + string

decode:
* get first #
* extract length
* extract string, add to result
'''

class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs: res += "#" + str(len(s)) + "#" + s
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


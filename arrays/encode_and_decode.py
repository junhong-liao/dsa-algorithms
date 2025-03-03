'''
encode: formula: # + length + # + string

decode:
* get first #
* extract length
* extract string, add to result
'''

# initial
class Solution:
    def encode(self, strs: List[str]) -> str:
        # this results in o(n^2) time
        # res += "#" + str(len(s)) + "#" + s
        return "".join(f"#{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        res, i = list(), 0
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

# optimal
class Solution:
    def encode(self, strs: List[str]) -> str:
        return ''.join(f"{len(s)}:{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        res, i = list(), 0
        while i < len(s):
            j = s.find(":", i) # index of next instance of colon delimiter
            length = int(s[i:j])
            i = j + 1
            res.append(s[i : i + length])
            i += length
        return res

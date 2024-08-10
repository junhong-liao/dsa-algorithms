'''
function: front_back
given: 
    s: str
returns:
    string s.t. characters at 0 and -1 are exchanged
'''

front_back = lambda s: s if not s or len(s) < 2 else s[-1] + s[1:-1] + s[0]
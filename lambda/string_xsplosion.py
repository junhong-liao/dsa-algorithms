string_xsplosion = lambda s: "".join([s[:i+1] for i in range(len(s))])
print(string_xsplosion("hello"))
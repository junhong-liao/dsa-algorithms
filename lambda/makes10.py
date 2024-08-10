makes10 = lambda a, b: True if (a == 10 or b == 10) or (a + b == 10) else False

'''
TESTS
'''

a, b = -5, 9
print(makes10(a, b))
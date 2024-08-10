'''
function: pos_neg
given: a: int, b: int
returns: 
    True if one is positive and one is negative, unless negative: bool = True

approach:
    if the negative flag is True, then we want to return if both are negative
    else we return if not (both are < 0)
    
'''

# def pos_neg(a, b, negative):
#   if negative: return (a < 0 and b < 0)
#   else:
#     return not (a < 0 and b < 0) and (a < 0 or b < 0)
    
pos_neg = lambda a, b, negative: a < 0 and b < 0 if negative else not (a < 0 and b < 0) and (a < 0 or b < 0)

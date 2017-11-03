# -*- coding: utf-8 -*-
"""
list_comprehension.py
    Daniel Thomas
    October 30, 2017
"""

def C_to_F(T_C):
    return (9/5)* T_C + 32


squares = []
for x in range(10):
    squares.append(x**2)

squares2 = [x**2 for x in range(10)]
squares_d = {x:x**2 for x in range(10) if x%2 == 0}
squares_t = [str(x) for x in range(10)]
print(';'.join(squares_t))
extra = [x*y for x in range(10) for y in range(10,20) if x%2==0]
extra = [x*y for (x,y) in (range(10), range(10,20)) if x%2==0]
print(extra)


words = 'to be or not to be, that is the question'.split()
print('_'.join(words))

T_C = [34, 30, 28, 35, 39, 32]
T_Ca = np.array(T_C)
#print(C_to_F(T_C))
print(type(C_to_F(T_Ca)))
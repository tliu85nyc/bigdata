# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


S = 'The Manhattan campus of Fordham Gabelli Business School is located near the Lincoln Center'
S2 = S.lower().replace(' ', '').strip()
d = {}
for i in S2:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
lst = []
for x,y in d.items():
    lst.append((x,y))
print("x=",tuple(lst))

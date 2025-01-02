# 30분
from itertools import product

tc = int(input())
op = [' ', '+', '-']
for i in range(tc):
    n = int(input())
    if i > 0:
        print()
    for case in product(op, repeat=n-1):
        exp = []
        for i in range(1, n):
            exp.append(str(i))
            exp.append(case[i-1])
        exp.append(str(n))
        
        ans = ''.join(exp)
        expStr = ans.replace(" ", "")
        if eval(expStr) == 0:
            print(ans)
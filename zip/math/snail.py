#22.10.02
#달팽이는 올라가고 싶다
#class2/실버5
#공식

# 내 풀이
A, B, V = map(int, input().split())

s = (V-A)//(A-B)+1
b = (V-1)//(A-B)+1

for i in range(s, b+1):
  if i*(A-B) + B >= V:
    print(i)
    break

# 다른 풀이(a*k-b*(k-1) >= v)
A, B, V = map(int, input().split())
d = (V-B)/(A-B)
print(int(d) if int(d) == d else int(d)+1)
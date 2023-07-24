#피보나치 수7
#dp

import sys
n = int(input())
a, b = 0, 1

for _ in range(2, n+1):
    tmp =  a
    a = b
    b += tmp
    b = b % 1000000007

print(b)
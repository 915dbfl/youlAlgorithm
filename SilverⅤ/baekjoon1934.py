#21.08.23
import sys
def gcd(a, b):
  return gcd(b, a%b) if b else a 

def lcm(a, b):
  return a*b // gcd(a,b)

num = int(sys.stdin.readline().rstrip())
nums = []
for i in range(num):
  nums.append(list(map(int, sys.stdin.readline().rstrip().split())))
for x, y in nums:
  print(lcm(x,y))
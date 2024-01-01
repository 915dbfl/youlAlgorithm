# 22.09.23
# 팰린드롬수
# class2_1

import sys

while 1:
  word = sys.stdin.readline().rstrip()

  if word == "0":
    break
  
  if word == word[::-1]:
    print("yes")
  else:
    print("no")
#22.10.10
#리모컨
#class3/골드5
#그리디

def getPosNum(i):
  global lst, answer, n
  lst.sort(key = lambda x: abs(int(answer + x + n[i:])- int(n)))
  print(i, int(answer + lst[0] + n[i:]))
  return str(lst[0])

n = input()
l = len(n)
m = int(input())
answer = ""

if m == 0:
  print(l)
else:
  lst = list(set([str(i) for i in range(10)]) - set(list(input().split())))
  print(lst)
  lst.append("")

  if n == "100":
    print(0)
  else:
    for i in range(l+1):
      answer += getPosNum(i)
    print(answer)
    print(len(answer)+abs(int(n)-int(answer)))
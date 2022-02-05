#21.08.18
num = int(input())
cors =[]
for i in range(num):
  cors.append(list(map(int, input().split())))
cors = sorted(cors, key= lambda i : (i[0], i[1]))
for x, y in cors:
  print(x, y)

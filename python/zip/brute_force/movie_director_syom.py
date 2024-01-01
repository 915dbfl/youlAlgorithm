# 22.09.23
# 영화감독 숌
# 브루트포스 알고리즘
# class2_1

N = int(input())
answer = 666

if N == 1:
  print(answer)
else:
  cnt = 1
  while cnt < N:
    answer += 1
    if "666" in str(answer):
      cnt += 1

  print(answer)
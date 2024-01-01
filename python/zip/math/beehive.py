#22.09.26
#벌집
#class2/브론즈2
#계차수열/규칙

N = int(input())

if N == 1:
  print(1)
else:
  ans = 2
  n = 7

  while N > n:
    n = n + 6*ans
    ans += 1

  print(ans)

# 지나는 방의 개수가 바뀌는 수들은 다음과 같다.
# 1, 7, 19, 37, 61...
# 이 수열의 계차는 6의 배수 만큼 증가하게 된다.
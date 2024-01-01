#22.10.14
#팩토리얼 0의 개수
#class3/실버5
#수학

def factorial(n):
  answer = 1
  for i in range(2, n+1):
    answer *= i
  return answer

N = int(input())
tmp = factorial(N)

if tmp % 10 == 0:
  cnt = 0
  for i in str(tmp)[::-1]:
    if i == "0":
      cnt += 1
    else:
      print(cnt)
      break
else:
  print(0)

# 알고리즘 최적화: N!을 소인수분해했을 때 5의 지수 값
N = int(input())
cnt = 0

while N>= 5:
  cnt += N//5
  N //= 5

print(cnt)
# N//5는 1-N 사이 5의 배수의 개수
# 25와 같은 제곱수의 경우, 이미 5의 배수의 개수에서 한 번 더해줬으므로 5의 개수를 두 번 더하지 않는다.
# 125도 마찬가지로 앞의 5, 25 배수에서 한 번씩 더해줬으므로 5의 개수를 세 번 더하지 않는다.
# 풀이: https://velog.io/@ledcost/%EB%B0%B1%EC%A4%80-1676-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%ED%8C%A9%ED%86%A0%EB%A6%AC%EC%96%BC-0%EC%9D%98-%EA%B0%9C%EC%88%98-%EC%8B%A4%EB%B2%844-%EC%A0%95%EC%88%98%EB%A1%A0
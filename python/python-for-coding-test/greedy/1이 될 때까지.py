# 최대한 많이 빼기 - 그리디

n, k = map(int, input().split())

time = 0
while n > 1:
    time += 1
    if n % k == 0:
        n //= k
    else:
        n -= 1 # n -= (n % k)

print(time)

# n이 100억 이상의 큰 수가 되는 경우
# 1씩 뺄 경우 시간 초과가 발생할 수 있다.
# n의 배수가 되도록 한 번에 빼는 방식을 활용한다.

# 예시 답안
n, k = map(int, input().split())
result = 0

while True:
    # n이 k로 나누어 떨어지는 수가 될 때까지 1씩 빼기
    target = (n//k) * k
    result += (n - target)
    n = target

    if n < k:
        break

    n //= k
    result += 1

result += (n - 1)
print(result)
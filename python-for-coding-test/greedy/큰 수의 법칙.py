n, m, k = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort(reverse = True)

time = 0 # 총 더해진 횟수
result = 0 
while time < m:
    if m - time >= k+1: # 가장 큰 수가 더해지는 횟수보다 많이 남았을 경우
        result += nums[0] * k + nums[1]
        time += k+1
    else: # 남은 횟수 만큼만 가장 큰 수를 더함
        result += nums[0] * (m-time)
        time = m
print(result)

# m의 크기가 10억 이상처럼 커질 경우
# 반복되는 수열을 파악해 result를 구하자
n, m, k = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort(reverse = True)

result = 0
result += (m//(k+1)) * (nums[0]*k + nums[1])
result += (m%(k+1)) * (nums[0])

print(result)
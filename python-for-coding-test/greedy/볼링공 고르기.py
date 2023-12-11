n, m = map(int, (input().split()))
balls = list(map(int, input().split()))
balls.sort()

result = 0
cnt = 1 # 같은 숫자 count
for i in range(n-1):
    if balls[i] != balls[i+1]: # 같은 무게의 공 중 가장 마지막 공인 경우
        result += (n - i - 1) * cnt
        cnt = 1
    else:
        cnt += 1
    
print(result)

# 볼링공 무게가 i일 때
# 해당 무게 볼링공 개수 * 해당 무게 이상 볼링공 개수

n, m = map(int, input().split())
data = list(map(int, input().split()))

# 1부터 10까지의 무게를 담을 수 있는 리스트
array = [0]*11
for i in data:
    array[i] += 1 # 각 무게에 해당하는 볼링공의 개수 카운트

result = 0
# 1부터 m까지의 각 무게에 대하여 처리
for i in range(1, m+1):
    n -= array[i] # 무게가 i인 볼링공의 개수 제외, a가 선택할 수 있는 경우
    result += array[i] * n # b가 선택할 수 있는 경우 곱하기

print(result)
#소가 정보섬에 올라온 이유

#시간초과 
n, q = map(int, input().split())
q = list(map(int, input().split()))
change = list(map(int, input().split()))
dp = [0] * (n)

def getS():
    for i in range(n):
        first = q[i]
        second = q[(i+1)%n]
        third = q[(i+2)%n]
        forth = q[(i+3)%n]

        dp[i] = first * second * third * forth

getS()

for i in change:
    dp[i-4] *= -1
    dp[i-3] *= -1
    dp[i-2] *= -1
    dp[i-1] *= -1
    print(sum(dp))

#dp
n, q = map(int, input().split())
q = list(map(int, input().split()))
change = list(map(int, input().split()))
dp = [0] * (n)
answer = 0

# dp 미리 계산
def getS():
    global answer
    for i in range(n):
        first = q[i]
        second = q[i-1]
        third = q[i-2]
        forth = q[i-3]

        dp[i] = first * second * third * forth
        answer += dp[i]

getS()

for i in change:
    dp[(i-1)%n] = -dp[(i-1)%n]
    answer += dp[(i-1)%n] * 2

    dp[i%n] = -dp[i%n]
    answer += dp[i%n] * 2
    
    dp[(i+1)%n] = -dp[(i+1)%n]
    answer += dp[(i+1)%n] * 2

    dp[(i+2)%n] = -dp[(i+2)%n]
    answer += dp[(i+2)%n] * 2
    
    print(answer)
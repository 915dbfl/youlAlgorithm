# dp
# 핵심: 부분합이 d 이하인 것들 -> 2개를 뽑는 조합의 수 합
import sys

c = int(input())
for _ in range(c):
    d, n = map(int, sys.stdin.readline().split())
    nums = list(map(int, sys.stdin.readline().split()))

    # sum_dp[i]: i번째 인덱스까지의 숫자 합
    sum_dp = [0] * (n+1)
    dic = dict()

    # dp값 계산 및 저장
    for i in range(1, n+1):
        sum_dp[i] = (sum_dp[i-1] + nums[i-1]) % d
        if sum_dp[i] not in dic.keys():
            dic[sum_dp[i]] = 1
        else:
            dic[sum_dp[i]] += 1

    answer = 0
    for k in dic.keys():
        if k == 0:
            answer += dic[k]
            if dic[k] > 1:
                answer += dic[k] * (dic[k]-1) // 2
        else:
            if dic[k] > 1:
                answer += dic[k] * (dic[k]-1) // 2
    print(answer)

# 누적합⭐️
import sys

c = int(sys.stdin.readline())
for _ in range(c):
    d, n = map(int, sys.stdin.readline().split())
    arr = list(map(lambda x: int(x) % d, sys.stdin.readline().split()))
    cnt = 0

    mod = [0] * d
    s = 0

    for num in arr:
        s = (s + num) % d
        # 같은 나머지와 하나씩 매칭되면 d로 나누어 떨어지는 부분 수열에 해당
        # 나중에 2개를 뽑는 연산을 하는 대신 경우의 수를 그때그때 더해준다.
        cnt += mod[s]
        mod[s] += 1

    
    # 나머지가 0인 경우는 그 자체로 부분 수열이므로 추가로 더해주기
    cnt += mod[0]
    print(cnt)
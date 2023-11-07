# 팩토리얼 0의 개수

# dp를 이용한 팩토리얼 -> 시간 초과
m = int(input())
cur = 2
result = 1

def checkZero(number):
    count = 0
    while 1:
        if number % 10 == 0:
            number //= 10
            count += 1
        else:
            return count

while 1:
    cnt = checkZero(result)
    if cnt == m:
        print(cur-1)
        exit(0)
    elif cnt > m:
        print("-1")
        exit(0)
    else:
        result *= cur
        cur += 1

# 시간 초과 -> 5씩 증가하며 dp를 구해서 시간초과가 난 것 같다.
    # m의 최대 <= 100,000,000이므로 5씩 증가하며 확인한다면 반복문이 최대 20,000,000 만큼 돌아야 한다.
# 2와 5의 개수로 0의 개수 구하기
# 가설: 2는 무조건 5보다 개수가 많다. 따라서 곱해지는 5의 개수가 0의 개수가 된다.
m = int(input())

cur = 5
sum = 1

def checkFive(number):
    answer = 0
    while number % 5 == 0:
        answer += 1
        number //= 5

    return answer

while 1:
    if sum == m:
        print(cur)
        exit(0)
    elif sum >= m:
        print(-1)
        exit(0)
    else:
        cur += 5
        sum += checkFive(cur)

# 5의 배수가 몇 개 있는지를 구하는 방법
# 125의 경우
# 5*1, 5*2, 5*3, ... 5*22, 5*23, 5*24, 5*25로 표현 가능(25) -> 125를 5로 나눈 몫
# 여기서 5에 곱해진 1, 2, 3, ..., 22, 23, 24, 25는
# 5*1, 5*2, 5*3, 5*4, 5*5로 표현 가능(5) -> 25를 5로 나눈 몫
# 여기서 다시 5에 곱해진 1, 2, 3, 4, 5는
# 1,2,3,4,5로 표현 가능(1) -> 5를 5로 나눈 몫
# 따라서 125!에는 총 5가 25+5+1 = 31개 존재하게 됨

# 제한 시간이 매우 짧으므로 가장 작은 n을 구하기 위해서 이분 탐색을 활용함

def count_zero(n):
    cnt = 0
    while n >= 5:
        cnt += n//5
        n //= 5
    return cnt

m = int(input())
lower = 1
upper = m * 5 # 0의 개수가 즉 5의 개수이므로 m*5를 하면 구하고자 하는 0의 개수보다 m+1개 존재하는 경우
result = 100000000

while lower <= upper:
    mid = (lower + upper) // 2
    cnt = count_zero(mid)

    if cnt < m:
        lower = mid + 1
    elif cnt >= m:
        if cnt == m:
            result = mid
        upper = mid - 1

if result == 100000000:
    print(-1)
else:
    print(result)
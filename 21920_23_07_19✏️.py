# 서로소 평균

# 유클리드 호제법
# 숫자 a, b가 있을 때, a를 b로 나눈 나머지와 b의 최대공약수는 a와 b의 최대공약수와 같다.

n = int(input())
lst = list(map(int, input().split()))
target = int(input())

def get_gcd(a, b):
    if b > a:
        a, b = b, a
    if b == 0:
        return a
    return get_gcd(b, a%b)

result = []
for num in lst:
    # 두 수의 최대공약수가 1일 경우 서로소로 판단
    if get_gcd(num, target) == 1:
        result.append(num)

print(sum(result)/len(result))

# 절대/상대 오차는 10-6까지 허용한다.
# -> 출력값과 정답의 차이가  10^(-6), 즉 0.000001 이하여야 한다는 뜻입니다.
# -> 따라서 //가 아니라 /를 사용해야 한다.
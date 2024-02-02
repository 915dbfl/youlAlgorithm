# 지수에 대해 1ogN 복잡도로 계산하는 재귀함수
def f(x, y):
    if y == 1:
        return x
    elif y % 2 == 0:
        a = f(x, y/2)
        return a * a % 1000000007
    else:
        b = f(x, (y-1)/2)
        return b * b * x % 1000000007

k, p, n = list(map(int, input().split()))
n = 10*n
result = f(p, n)
result *= k
print(result % 1000000007)
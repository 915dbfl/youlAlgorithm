# 누적합
import sys
input = sys.stdin.readline

n, k, q, m = map(int, input().split())

studentDp = [False] * (n+3)
studentK = set(map(int, input().split()))
studentQ = list(map(int, input().split()))

for std in studentQ:
    # 졸고 있는 학생일 경우
    if std in studentK: continue

    # 배수에게 전달
    for idx in range(std, n+3, std):
        if idx not in studentK:
            studentDp[idx] = True

studentDp[0] = 0 if studentDp[0] else 1

for i in range(1, n+3):
    if not studentDp[i]:
        studentDp[i] = studentDp[i-1] + 1
    else:
        studentDp[i] = studentDp[i-1]

for _ in range(m):
    s, e = map(int, input().split())
    print(studentDp[e] - studentDp[s-1])
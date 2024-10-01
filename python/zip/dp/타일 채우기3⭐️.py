answer = [0, 2, 7]
n = int(input())
if n < 3:
    print(answer[n])
else:
    cross = 1
    a, b, c = answer
    for _ in range(3, n+1):
        newC = (2*cross + 3*b + 2*c) % 1000000007
        a, b, c = b, c, newC
        cross += a
        cross %= 1000000007

    print(c)
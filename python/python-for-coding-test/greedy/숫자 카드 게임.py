n, m = map(int, input().split())
lst = []
min_lst = []

for _ in range(n):
    row = list(map(int, input().split()))
    min_lst.append(min(row))

print(max(min_lst))
# 40분

import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())
dic = {}
child = defaultdict(list)

for _ in range(n+m):
    p, f, c = input().rstrip().split()
    # 폴더인 경우
    if c == "1":
        if p not in dic:
            dic[p] = [[f], []]
        else:
            dic[p][0].append(f)
    # 파일인 경우
    else:
        if p not in dic:
            dic[p] = [[], [f]] # [폴더, 파일]
        else:
            dic[p][1].append(f)

def process(query):
    global type, cnt
    if query in dic:
        type = type | set(dic[query][1])
        cnt += len(dic[query][1])
        for child in dic[query][0]:
            process(child)

q = int(input())
for _ in range(q):
    query = list(input().rstrip().split("/"))[-1]
    type, cnt = set(), 0
    process(query)
    print(len(type), cnt)

# 다른 풀이
from collections import defaultdict
import sys

sys.setrecursionlimit(1_000_000)
input = lambda: sys.stdin.readline().rstrip()
N, M = map(int, input().split())

tree = defaultdict(list)
for _ in range(N+M):
    P, F, C = input().split()
    tree[P].append([F, C])

def dfs(d):
    s, cnt = set(), 0
    for f, c in tree[d]:
        if c == "1":
            result = dfs(f)
            s |= result[0]
            cnt += result[1]
        else:
            s.add(f)
            cnt += 1

    tree_detail[d] = s, cnt
    return s, cnt


tree_detail = {}
dfs("main")

for _ in range(int(input())):
    q = input().split("/")[-1]
    result = tree_detail[q]
    print(len(result[0]), result[1])
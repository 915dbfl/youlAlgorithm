# 문제 추천 시스템 version 1

# 이진 탐색: 시간초과
# 탐색해 값을 추가할 index를 찾는 데에는 n/2의 시간이 걸린다.
# 탐색한 idex에 값을 넣고 하나의 리스트로 만드는 과정에서 시간 복잡도가 10**9까지 증가한다.
import sys

def binary_search(p, l):
    global quizs
    start = 0
    end = len(quizs) -1

    while start <= end:
        mid = (start + end) // 2

        if quizs[mid][0] > l: # 레벨 비교
            end = mid-1
        elif quizs[mid][0] == l:
            if int(quizs[mid][1]) >= int(p): # 문제번호 비교
                end = mid-1
            else:
                start = mid+1
        else:
            start = mid+1

    quizs = quizs[:start] + [(l, p)] + quizs[start:]

n = int(sys.stdin.readline())
quizs = []
for _ in range(n):
    p, l = sys.stdin.readline().split()
    quizs.append((int(l), p))
quizs.sort()

m = int(sys.stdin.readline())
solved_list = set()
for _ in range(m):
    cmds = sys.stdin.readline().split()

    if cmds[0] == "recommend":
        if cmds[1] == "1": # 가장 어려운 문제
            print(quizs[-1][1])
        else:
            print(quizs[0][1])

    elif cmds[0] == "add":
        binary_search(cmds[1], int(cmds[2]))
        
    elif cmds[0] == "solved":
        rm_quiz = []
        for l, p in quizs:
            if cmds[1] != p:
                rm_quiz.append((l, p))

        quizs = rm_quiz

# 우선 순위 큐
# heapq
# heapq에 정렬된 순서: [[1, 1000], [2, 1001], [78, 19998], [37, 2667], [55, 2042]]
# 여기서 트리 형태이므로 무조건 이전 값이 다음 값보다 크다고 가정할 수 없다.
# heappop - 힙 내에서 가장 작은 원소 값을 pop한다.
# recommend에서 제일 처음값을 사용할 수 있는 이유는 heapq는 최대값이 보장되기 때문이다.
from collections import defaultdict
import sys
from heapq import heappush, heappop

n = int(input())
max_heap = []
min_heap = []
in_list = defaultdict(bool)
for _ in range(n):
    p, l = map(int, sys.stdin.readline().split())
    heappush(max_heap, [-l, -p])
    heappush(min_heap, [-l, -p])
    in_list[p] = True

m = int(input())
for _ in range(m):
    command = sys.stdin.readline().split()

    if command[0] == "recommend":
        if command[1] == "1":
            while not in_list[-max_heap[0][1]]:
                heappop(max_heap)
            print(-max_heap[0][1])
        else:
            while not in_list[min_heap[0][1]]:
                heappop(min_heap)
            print(min_heap[0][1])


    elif command[0] == "solved":
        in_list[int(command[1])] = False

    else:
        p = int(command[1])
        l = int(command[2])

        while not in_list[-max_heap[0][1]]:
            heappop(max_heap)
        while not in_list[min_heap[0][1]]:
            heappop(min_heap)
        in_list[p] = True
        heappush(max_heap, [-l, -p])
        heappush(min_heap, [l, p])


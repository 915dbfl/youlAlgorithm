# 오답

import sys
from heapq import heappop, heappush
input = sys.stdin.readline

n, m = map(int, input().split())
table = [list(map(int, list(input().rstrip()))) for _ in range(n)]
k = int(input())

def switch(col_index):
    for i in range(n):
        table[i][col_index] = (table[i][col_index] + 1) % 2

def check_row_trun_on():
    turn_on = 0
    for i in range(n):
        if sum(table[i]) == m:
            turn_on += 1
    return turn_on

if m > k:
    hq = []

    col_table = list(zip(*table))
    for i in range(m):
        heappush(hq, (sum(col_table[i]), i))
    
    for _ in range(k):
        col_sum, col_index = heappop(hq)
        switch(col_index)

    turn_on = check_row_trun_on()
    print(turn_on)
else:
    # 모든 열이 1이 많도록 세팅
    col_table = list(zip(*table))
    min_sum = n
    min_index = []
    for i in range(m):
        col_sum = sum(col_table[i])
        if col_sum < n - col_sum:
            col_sum = n - col_sum
            switch(i)
            k -= 1
        if min_sum >= col_sum:
            min_index.append(i)
    
    # 추가 switch
    k = k % 2
    if k == 0:
        print(check_row_trun_on())
    else:
        max_turn_on = 0
        for col_index in min_index:
            tmp_turn_on = 0
            switch(col_index)

            tmp_turn_on = check_row_trun_on()
            if max_turn_on < tmp_turn_on:
                max_turn_on = tmp_turn_on

            switch(col_index)
        print(max_turn_on)
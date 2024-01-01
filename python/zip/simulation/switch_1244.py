#23.02.18
#스위치 켜고 끄기
#알고리즘 스터디: 시뮬레이션
#실버4
#예외사항을 꼼꼼히 살펴볼 것

import sys
input = sys.stdin.readline

def Boy(n):
    cur = n
    while cur <= switch_n:
        states[cur-1] = abs(states[cur-1]-1)
        cur += n

    # 다른 풀이
    # for i in range(n, switch_n+1, n):


def Girl(n):
    states[n] = abs(states[n]-1)
    cnt = 1

    while 1:
        if 0<= n-cnt and n+cnt < switch_n:
            if states[n-cnt] == states[n+cnt]:
                states[n-cnt] = abs(states[n-cnt]-1)
                states[n+cnt] = abs(states[n+cnt]-1)
                cnt+=1
            else:
                break
        else:
            break


switch_n = int(input())
states = list(map(int, input().split()))

student_n = int(input())

for i in range(student_n):
    g, n = map(int, input().split())
    
    if g == 1: # 남자
        Boy(n)

    else: # 여자
        Girl(n-1)

for i in range(switch_n):
    print(states[i], end = " ")
    if (i+1) % 20 == 0:
        print("")
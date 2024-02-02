# HSAT 5회 기출
import sys
input = sys.stdin.readline

def ranking(base):
    # 추후 인덱스를 기준으로 정렬하기 위해 인덱스와 함께 저장
    with_idx = []
    for idx, v in enumerate(base):
        with_idx.append([idx, v, 0])

    # 점수를 기준으로 정렬
    with_idx.sort(key = lambda x: x[1], reverse = True)

    # 랭킹 저장
    rank, cnt = 1, 1
    with_idx[0][2] = 1
    for i in range(1, n):
        if with_idx[i-1][1] == with_idx[i][1]:
            cnt += 1

        else:
            rank += cnt
            cnt = 1
            
        with_idx[i][2] = rank

    # 인덱스로 재정렬
    with_idx.sort()
    for i in range(n):
        if i == n-1:
            print(with_idx[i][2])
        else:
            print(with_idx[i][2], end = " ")
            
n = int(input())
first = list(map(int, input().split()))
second = list(map(int, input().split()))
third = list(map(int, input().split()))
final = [first[i] + second[i] + third[i] for i in range(n)]

ranking(first)
ranking(second)
ranking(third)
ranking(final)
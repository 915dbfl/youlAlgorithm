"""
[풀이과정]
- [-m+1, -m+1] ~ [n, n]까지 모든 홈이 차는지 확인
- rotate 진행
- 위의 과정 반복
"""

def rotate_right(key):
    return list(map(list, zip(*key[::-1])))

def check_fit_hole(key, lock, x, y):
    m = len(key)
    n = len(lock)
    fit = 0
    for i in range(m):
        for j in range(m):
            if 0 <= x+i < n and 0 <= y+j < n: # 범위 확인
                if key[i][j] != lock[x+i][y+j]: # 자물쇠와 열쇠가 맞는 경우
                    if key[i][j] == 1 and lock[x+i][y+j] == 0:
                        fit += 1
                else: # 맞지 않는 경우
                    return -1
    return fit

def solution(key, lock):
    m = len(key)
    n = len(lock)
    
    hole = n * n
    for row in lock:
        hole -= sum(row)
        
    for _ in range(4):
        key = rotate_right(key)
        for i in range(-m+1, n):
            for j in range(-m+1, n):
                if hole == check_fit_hole(key, lock, i, j):
                    return True
    return False
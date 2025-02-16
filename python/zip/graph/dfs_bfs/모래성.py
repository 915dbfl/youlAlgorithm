"""
주요 정보
1. 8방향 중 모래성이 쌓여있지 않은 부분의 개수 <= 모래성의 튼튼함
2. 모래성의 모양이 더이상 변하지 않는 순간

풀이 과정
1. 각 격자의 상태 저장
2. 사라지는 격자 큐에 저장
3. 큐에서 사라지는 부분 pop -> 8방향 격자 상태 -1
    - 사라진다면 큐에 저장
4. 큐가 empty일 경우 정답
"""

from collections import deque

def wave():
    global dq
    answer = 0
    while dq:
        answer += 1
        remove = set()
        while dq:
            cx, cy = dq.popleft()

            for i in range(8):
                nx = cx + dx[i]
                ny = cy + dy[i]

                if 0<=nx<h and 0<=ny<w and strength[nx][ny] != '.':
                    # 이미 제거되지 않은 부분이라면
                    if sand_state[nx][ny] < int(strength[nx][ny]):
                        sand_state[nx][ny] += 1
                        # 제거되는지 확인
                        if sand_state[nx][ny] >= int(strength[nx][ny]):
                            remove.add((nx, ny))
        dq = deque(remove)
    return answer

h, w = map(int, input().split())
strength = [list(input().rstrip()) for _ in range(h)]
sand_state = [[0] * w for _ in range(h)]

dq = deque()

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

for i in range(h):
    for j in range(w):
        if strength[i][j] == '.':
            dq.append((i, j))

print(wave() - 1)
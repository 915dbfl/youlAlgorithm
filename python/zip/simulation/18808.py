import sys
input = sys.stdin.readline

def rotate_by_90(sticker):
    return list(zip(*sticker[::-1]))

def stick(sx, sy, sticker):
    global answer
    r, c = len(sticker), len(sticker[0])
    for x in range(r):
        for y in range(c):
            if sticker[x][y] == 1:
                answer += 1
                computer[sx+x][sy+y] = 1

def is_stickable(sticker, r, c):
    if n-r+1 <= 0 or m-c+1 <= 0: # 컴퓨터 영역보다 스티커 크기가 더 큰 경우
        return False
    
    for i in range(n-r+1):
        for j in range(m-c+1):
            # i, j를 스티커 왼쪽 기준이라고 했을 때 해당 스티커를 붙일 수 있는지 확인
            isPossible = True # 해당 스티커를 붙일 수 있는지를 나타내는 플래그
    
            for x in range(r):
                if not isPossible:
                    break
                
                for y in range(c):
                    if sticker[x][y] == 1 and computer[i+x][j+y] == 1: # 이미 다른 스티커가 붙여진 공간이라면
                        isPossible = False # 플래그 False로 지정
                        break
            else: # 반복문을 다 돈 경우
                if isPossible: # 스티커를 붙일 수 있는 경우
                    stick(i, j, sticker)
                    return True
    return False

n, m, k = map(int, input().split())
computer = [[0 for _ in range(m)] for _ in range(n)]

answer = 0

for _ in range(k):
    r, c = map(int, input().split())
    sticker = []
    for _ in range(r):
        sticker.append(list(map(int, input().split())))

    for _ in range(4):
        if is_stickable(sticker, len(sticker), len(sticker[0])):
            break
        sticker = list(zip(*sticker[::-1]))
    
print(answer)
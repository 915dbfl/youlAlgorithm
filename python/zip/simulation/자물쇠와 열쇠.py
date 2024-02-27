# 주의해야 할 점
# 1. 처음부터 lock에 빈 공간이 없다면 key 모양과 상관없이 true이다.
# 2. key는 lock보다 왼쪽부터 시작할 수 있다.

def rotate_by_90(key):
    return list(zip(*key[::-1]))

def checkLock(lock):
    check = 0
    for i in range(len(lock)):
        check += sum(lock[i])
        
    return check == len(lock) * len(lock[0])

def checkMatch(sx, sy, lock, key):
    # 임시 자물쇠를 만든다.
    tmpLock = [[0 for _ in range(len(lock[0]))] for _ in range(len(lock))]
    for i in range(len(lock)):
        for j in range(len(lock[0])):
            tmpLock[i][j] = lock[i][j]
            
    # key를 모두 돌며 lock을 채운다.
    for i in range(len(key)):
        for j in range(len(key[0])):
            # 자물쇠 범위 내에 있는지 확인
            if 0<=sx+i<len(lock) and 0<=sy+j<len(lock[0]):
                # key로 채워야 하는 부분
                if tmpLock[sx+i][sy+j] == 0:
                    # key로 채울 수 있는 경우
                    if key[i][j] == 1:
                        tmpLock[sx+i][sy+j] = 1
                    else:
                        # 채워야 하는 부분이 다 채워지지 않는 경우이므로 match false!
                        return False
                # 자물쇠에 돌기가 있는 부분
                else:
                    # 열쇠의 돌기와 자물쇠의 돌기가 만나게 되므로 match false!
                    if key[i][j] == 1:
                        return False
                
    # 자물쇠는 모두 맞는 상황, 나머지 빈 곳이 있는지 확인!
    return checkLock(tmpLock)
                
def solution(key, lock):
    lr, lc = len(lock), len(lock[0])
    kr, kc = len(key), len(key[0])
    
    # 열쇠를 채우기 전에 자물쇠에 빈 곳이 없는지 확인
    if checkLock(lock):
        return True
    
    # 모든 영역을 돌며 열쇠와 자물쇠 match 확인
    for i in range(4):
        for r in range(-kr+1, lr):
            for c in range(-kc+1, lc):
                if checkMatch(r, c, lock, key):
                        return True
        key = rotate_by_90(key)
                
    else:
        return False
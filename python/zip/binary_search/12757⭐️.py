# dict 사용
import sys
input = sys.stdin.readline

# m * k -> 100,000 * 10,000 (최악의 상황)
def findKey(key):

    p1, p2 = key, key
    answer = []

    for _ in range(k):
        p1 -= 1
        p2 += 1
        p1_exist = p1 in dic.keys() 
        p2_exist = p2 in dic.keys()
        
        if p1_exist or p2_exist: # 가장 근접한 Key를 찾은 경우
            if p1_exist:
                answer.append(p1)
            if p2_exist:
                answer.append(p2)
            break
    return answer

n, m, k = map(int, input().split())

dic = dict()
for _ in range(n):
    key, val = map(int, input().split())
    dic[key] = val

for _ in range(m):
    ords = list(map(int, input().split()))

    if ords[0] == 1:
        dic[ords[1]] = ords[2]
    elif ords[0] == 2:
        keys = findKey(ords[1])
        if len(keys) == 1:
            dic[keys[0]] = ords[2]
    else:
        keys = findKey(ords[1])
        
        if len(keys) <= 0:
            print("-1", end = "\n")
        elif len(keys) > 1:
            print("?", end = "\n")
        else:
            print(dic[keys[0]], end = "\n")

# 이분 탐색을 이용한 풀이
import sys
import bisect
 
input=sys.stdin.readline
 
n,m,k=map(int,input().split())
 
# 이진탐색으로 key들을 저장할 리스트
keys=[]
 
# 정확한 key와 value를 저장하기 위한 dict()
dic=dict()
 
# 이진탐색으로 키를 삽입함(순서대로 넣기위함)
def putkey(key):
    bisect.insort(keys,key)
    return
 
# k범위 안의 키가 있는지 찾는 것
def findkey(key):
    idx=0
    val=dic.get(key,-1)
    leng=len(keys)
    if val != -1:
        return key
    else:
        key_idx=bisect.bisect(keys,key)
        # 입력한 key가 들어갈 예상될 곳이 첫 번째 인덱스일 때
        if key_idx==0:
            if abs(keys[0]-key)<=k:
                return keys[0]
        # 입력한 key가 들어갈 예상될 곳이 마지막 인덱스일 때
        elif key_idx==leng:
            if abs(keys[key_idx-1]-key)<=k:
                return keys[key_idx-1]
        else:
            # 답이 ?가 나와야함
            if keys[key_idx]-key==key-keys[key_idx-1]:
                return -2
            # 답 1개(왼쪽 키가 조건에 맞음)
            if keys[key_idx]-key>key-keys[key_idx-1]:
                if key-keys[key_idx-1]<=k:
                    return keys[key_idx-1]
            # 답 1개(오른쪽 키가 조건에 맞음)
            if keys[key_idx]-key<key-keys[key_idx-1]:
                if keys[key_idx]-key<=k:
                    return keys[key_idx]
 
    # 답이 1이 나와야함
    return -1
 
 
for i in range(n):
    key,val=map(int,input().split())
    dic[key]=val
    putkey(key)
 
for i in range(m):
    arr=list(map(int,input().split()))
    if arr[0]==1:
        # 값들을 저장한다
        # 여기는 정확한 키 밸류값
        dic[arr[1]]=arr[2]
        # 정확한 키를 저장
        putkey(arr[1])
    if arr[0]==2:
        tmpkey=findkey(arr[1])
        if tmpkey==-1 or tmpkey==-2:
            continue
        else:
            dic[tmpkey]=arr[2]
    if arr[0]==3:
        tmpkey=findkey(arr[1])
        if tmpkey==-1:
            print(-1)
        elif tmpkey==-2:
            print("?")
        else:
            print(dic[tmpkey])
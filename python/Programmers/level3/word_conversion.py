#22.07.17
#단어 변환

# dfs: 내 풀이(정규식 사용): 시간 복잡도 측면에서 안 좋음.
# 방문한 단어를 재방문하지 않도록 구현했어야 했음.
import re

def getRegex(begin):
    global size
    result = []
    for i in range(size):
        str = begin[:i]
        end = begin[i+1:] if i != size-1 else ""
        result.append("%s[a-z]%s" %(str, end))
    return '|'.join(result)

def getAnswer(begin, target, word, stack):
    global answer
    if len(stack) == l or (len(answer) != 0 and min(answer) <= len(stack)):
        return
    if begin == target:
        return answer.add(len(stack))
    else:
        regex = getRegex(begin)
        for i in re.findall(regex, word):
            if i not in stack: # 방문했던 노드를 재방문하지 않도록 해야 함!
                getAnswer(i, target, word, stack + [i])
    

def solution(begin, target, words):
    global answer, l, size
    l = len(words)
    size = len(words[0])
    answer = set()
    word = " ".join(words)
    getAnswer(begin, target, word, [])
    return min(answer) if len(answer) != 0 else 0


# bfs: zip 사용한 풀이
from collections import deque

def get_adjacent(current, words):
    for word in words:
        count = 0
        for c, w in zip(current, word):
            if c != w:
                count += 1
                
        if count == 1:
            yield word # return과 달리 결과값을 나눠서 얻게 된다.

def solution(begin, target, words):
    dic = {begin: 0}
    queue = deque([begin])
    
    while queue:
        if target in dic:
            break
        current = queue.popleft()
        for word in get_adjacent(current, words):
            if word not in dic:
                dic[word] = dic[current]+1
                queue.append(word)
                
    return dic.get(target, 0) # dictionary.get(값, default값)

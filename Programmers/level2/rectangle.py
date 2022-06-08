#22.06.08
#멀쩡한 사각형

#시간초과 풀이1
import math
def solution(w,h):
    answer = 0
    for i in range(1, w+1):
        answer += math.trunc((-h/w)*i+h)*2
    return answer

# 시간초과 풀이2
import math
def solution(w,h):
    answer = 0
    for i in range(1, w+1):
        tmp = math.trunc(-h/w*i+h)
        answer += tmp + math.trunc((-h/w)*(w-i+1)+h)
        if tmp == -h/w*i+h:
            return w//i*answer
    return answer*2

# 내 풀이
import math
def solution(w,h):
    answer = 0
    n, m = min(w, h), max(w, h)
    gcd = math.gcd(w, h)
    for i in range(1, n//gcd+1):
        answer += math.trunc(-m*i/n+m) + math.trunc(-m*(n-i+1)/n+m)
    return answer*gcd
    
# best 풀이
import math
def solution(w,h):
    return w*h - (w+h-math.gcd(w,h))
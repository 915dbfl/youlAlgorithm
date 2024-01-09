# 브루트 포스 알고리즘
import sys
from collections import defaultdict
from itertools import combinations
n, k = map(int, sys.stdin.readline().split())

base = set(["a", "n", "t", "i", "c"])
dic = defaultdict(set)
related_word_cnt = defaultdict(int)

words = []
answer = 0
# 단어 받아오기
for i in range(n):
    words.append(set(list(sys.stdin.readline().rstrip())))

# 남극 모든 단어는 "anta", "tica"를 포함하므로
if k < 5: 
    print(0)
elif k >= 26:
    print(n)
else:
    k -= 5 # base 제외
    result = 0
    no_base = set(["b", "d", "e", "f", "g", "h", "j", "k", "l", "m", "o", "p", "q", "r", "s", "u", "v", "w", "x", "y", "z"])
    for case in combinations(no_base, k):
        case = set(case)
        base |= case
        tmp_result = 0
        for w in words:
            if len(w - base) <= 0:
                tmp_result += 1
        result = max(result, tmp_result)
        base -= case

    print(result)

# 비트 마스킹 개념 도입⭐️
import sys
from itertools import combinations

input = sys.stdin.readline

def word2bit(word):
    bit = 0
    for char in word:
        bit = bit | (1 << ord(char) - ord('a'))
    return bit

N, K = map(int, input().split())
words = [input().rstrip() for _ in range(N)]
bits = list(map(word2bit, words))
base_bit = word2bit('antic')

if K < 5:
    print(0)
else:
    alphabet = [1 << i for i in range(26) if not (base_bit & 1 << i)]
    answer = 0
    for combination in combinations(alphabet, K-5):
        know_bit = sum(combination) | base_bit
        count = 0
        for bit in bits:
            if bit & know_bit == bit:
                count += 1
        answer = max(answer, count)
    print(answer)
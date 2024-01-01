#2022.03.06
#문자열 압축

# 내 풀이
def solution(s):
  min = len(s)
  for i in range(1, len(s)//2+1):
    key = ""
    cnt = 1
    answer = ""
    for j in range(0, len(s), i):
       # 제일 처음 시작
      if key == "":
        key = s[j: j+i]
      else:
        # 같은 문자일 경우
        if key == s[j:j+i]:
          cnt += 1
        # 다른 문자일 경우
        else:
          # 이전 문자 추가
          if cnt > 1: answer += str(cnt)
          answer += key
          cnt = 1
          key = s[j: j+i]
                  
      if cnt > 1: answer += str(cnt)
      answer += key
      
      if len(answer) < min:
        min = len(answer)
      
  return min


# best 풀이
def compress(text, tok_len):
  #길이가 tok_len인 단어들로 text를 나눔
  words = [text[i: i+tok_len] for i in range(0, len(text), tok_len)]
  lst = []
  cur_word = words[0]
  cur_cnt = 1
  #앞 요소와 뒷 요소를 비교함
  for a, b in zip(words, words[1:] + ['']):
    if a == b:
      cur_cnt += 1
    else:
      lst.append([cur_word, cur_cnt])
      cur_word = b
      cur_cnt = 1
  return sum(len(word) + (len(str(cnt)) if cnt > 1 else 0) for word, cnt in lst)

def solution(text):
  return min(compress(text, tok_len) for tok_len in list(range(1, len(text)//2 + 1)) + [len(text)])
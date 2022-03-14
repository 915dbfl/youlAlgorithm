#2022.03.14
#짝지어 제거하기

def solution(s):
  tmp = [s[0]]
  for i in range(1, len(s)):
    if len(tmp) == 0 or tmp[-1] != s[i]:
      tmp.append(s[i])
    else:
      tmp.pop()

  if len(tmp) == 0:
    return 1
  else:
    return 0
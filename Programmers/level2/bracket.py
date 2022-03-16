# 2022.03.16
# 괄호 변환

#내 풀이
def checkRight(s):
  while "()" in s:
    s = s.replace("()", "")
  if len(s) == 0:
    return True
  else:
    return False

def getUV(s):
  dic = {"(" : 0, ")": 0}
  for i in range(len(s)):
    dic[s[i]] += 1
    if dic["("] == dic[")"]:
      return i

def getReverse(s):
  new = ""
  for i in s:
    if i == ")":
      new += "("
    else:
      new += ")"
  return new

def newString(s):
  if s == "":
    return ""
  key = getUV(s)
  u = s[:key+1]
  v = s[key+1:]
  if checkRight(u):
    return u + newString(v)
  else:
    u = u[1:len(u)-1]
    newU = getReverse(u)
    newV = newString(v)
    return "(" + newV + ")" + newU


def solution(p):
  answer = ''
  if checkRight(p):
    return p
  else:
    return newString(p)

#best 풀이
def solution(s):
  if s == "": return s
  c = 0; r = True
  for i in range(len(s)):
    if s[i] == "(": c-= 1
    else: c += 1
    if c > 0: False
    if c == 0:
      if r:
        return s[:i+1] + solution(s[i+1:])
      else:
        return "(" + solution(s[i+1:]) + ")" + "".join(list(map(lambda x: "(" if x == ")" else ")"), s[1:i]))

# "구분자".join(리스트) -> 구분자를 중심으로 리스트 요소들을 합쳐 하나의 문자열로 반환함.
#22.12.08
#LCS
#class4/골드5

#dp: 시간초과
str1 = input()
str2 = input()

if len(str1) < len(str2):
  s = str1
  m = str2
else:
  s = str2
  m = str1

dp = [0]*len(m)

for i in range(len(s)):
  for j in range(len(m)-1, -1, -1):
    if s[i] == m[j]:
      try:
        dp[j] = max(dp[0:j])+1
      except:
        dp[j] = 1

print(max(dp))

#dp: 리팩토링
str1 = input()
str2 = input()

if str1 == str2:
  print(len(str1))
else:
  if len(str1) < len(str2):
    s = str1
    m = str2
  else:
    s = str2
    m = str1

  dp = [0]*len(m)

  for i in range(len(s)):
    for j in range(len(m)-1, -1, -1):
      if s[i] == m[j]:
        try:
          dp[j] = max(dp[0:j])+1
        except:
          dp[j] = 1
      
  print(max(dp))
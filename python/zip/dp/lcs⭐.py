#22.12.08
#LCS
#class4/골드5

#dp: 시간초과
str1 = input()
str2 = input()

dp = [0]*len(str1)

for i in range(len(str2)):
  for j in range(len(dp)-1, -1, -1):
    if str2[i] == str1[j]:
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

# dp: 리팩토링2
str1 = input()
str2 = input()
matrix = [[0]*(len(str2)+1) for _ in range(len(str1)+1)]

for i in range(1, len(str1)+1):
  for j in range(1, len(str2)+1):
    if str1[i-1] == str2[j-1]:
      matrix[i][j] = matrix[i-1][j-1] + 1
    else:
      matrix[i][j] = max(matrix[i][j-1], matrix[i-1][j])

print(matrix[-1][-1])

# dp: 리팩토링3
str1 = input()
str2 = input()

if str1 == str2:
  print(len(str1))
else:
  dp = [0]*len(str1)

  for i in range(len(str2)):
    v_max = 0
    for j in range(len(str1)):
      if dp[j] > v_max:
        v_max = dp[j]
      elif str1[j] == str2[i]:
        dp[j] = v_max + 1
    print(dp)
  
  print(max(dp))
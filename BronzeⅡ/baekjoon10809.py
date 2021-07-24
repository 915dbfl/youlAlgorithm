#21.07.23
word = input()
lst = ["-1" for i in range(26)]
count = 0
for i in word:
  #ord, chr 정리하기
  if lst[ord(i) - 97] == "-1":
    lst[ord(i) - 97] = str(count)
  count += 1
#.join 함수 정리하기
print(" ".join(lst))
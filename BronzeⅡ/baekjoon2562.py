#2021.07.22
lst = []
# 리트스에 9개의 숫자 저장
for i in range(9):
  lst.append(int(input()))

print(max(lst))
print(lst.index(max(lst)) + 1)
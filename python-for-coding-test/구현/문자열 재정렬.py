# facebook 인터뷰
# 기출 문제

s = input()
strs = []
sum_value = 0

for i in s:
    if i.isdecimal():
        sum_value += int(i)
    else:
        strs.append(i)
strs.sort()

if sum_value > 0:
    strs.append(str(sum_value))

print("".join(strs))
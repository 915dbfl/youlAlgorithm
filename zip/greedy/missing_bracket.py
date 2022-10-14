#22.10.14
#잃어버린 괄호
#class3/실버2
#그리디

#내 풀이
import re

equation = input()
result = re.findall('[0-9]+|[+-]', equation)

for i in range(len(result)):
  if result[i].isdigit():
    result[i] = str(int(result[i]))

equation = "".join(result)
equation = equation.replace("-", ")-(")

print(eval("("+equation+")"))

# best 풀이
lst = input().split('-')
answer = 0

for i in lst[0].split('+'):
  answer += int(i)

for i in lst[1:]:
  for j in i.split('+'):
    answer -= int(j)

print(answer)
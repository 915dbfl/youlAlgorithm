#21.08.15
num = list(map(int, input()))
num = list(map(str,sorted(num, reverse=True)))
print(''.join(num))
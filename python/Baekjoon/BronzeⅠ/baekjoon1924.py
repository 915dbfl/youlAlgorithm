#2021.08.03
days = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
month = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
sum = 0
mon, day = map(int, input().split())
for i in range(1, mon):
  sum += month[i - 1]
print(days[(sum + day) %7])
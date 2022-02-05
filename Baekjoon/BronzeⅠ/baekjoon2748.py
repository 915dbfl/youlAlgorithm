#21.08.04
num = int(input())

# 0부터 num까지 피보나치 수열을 저장하기 위해서 길이가 num + 1인 리스트 생성
# 0으로 초기화 
lst = [0] * (num + 1)
lst[1] = 1

# for문을 돌려 앞 두 수를 더한 값을 i번째에 저장
for i in range(2, num + 1):
  lst[i] = lst[i - 2] + lst[i - 1]

# n번째를 값인 리스트 마지막 값을 출력
print(lst[-1])
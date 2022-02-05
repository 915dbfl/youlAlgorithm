# #21.08.19
N, M = map(int, input().split())
chess = []
for i in range(N):
    chess.append(input())
repair = []

for i in range(N-7):
  for j in range(M-7):
    firstW = 0
    firstB = 0

    for k in range(i,i+8):
      for l in range(j,j + 8):

        # 짝수, 홀수 번째 정사각형은 각각 같은 색을 갖게 됨.
        if (k + l) % 2 == 0:
          # 짝수는 첫 시작과 동일한 색을 갖음.
          if chess[k][l] == 'W':
            # 첫 시작이 W라는 것이므로 B로 시작할 경우, 다시 색칠해야 하는 정사각형에 해당됨.
            firstB += 1
          else:
            firstW +=1

        else:
          # 홀수의 경우, 첫 시작과 다른 색을 갖음.
          if chess[k][l] == 'B':
            # 홀수의 색이 B라는 것은 짝수 번째의 색은 W라는 것! 첫 시작이 B일 경우, 다시 칠해야 하는 정사각형에 해당됨.
            firstB += 1
          else:
            firstW += 1

    # 첫 시작이 B, W인 모든 경우 중 최적해를 구하는 것이므로 firstW, firstB 모두 리스트에 넣음.
    repair.append(firstW)
    repair.append(firstB)

print(min(repair))
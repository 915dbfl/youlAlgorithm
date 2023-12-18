# 삽입 정렬
# O(n^2)
# 특정 데이터를 적절한 위치에 삽입한다.
# 특정 데이터가 적절한 위치에 들어가기 이전에, 그 앞까지의 데이터는 이미 정렬되어 있다고 가정한다.

# 핵심: 현재 리스트의 데이터가 거의 정렬되어 있는 상태라면 매우 빠르게 동작한다. (퀵 정렬보다도!)

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
	for j in range(i, 0, -1):
		if array[j] < array[j-1]:
			array[j], array[j-1] = array[j-1], array[j]
		else: # 자기보다 작은 데이터를 만나면 그 위치에서 멈춤
			break
print(array)